from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
import advanced_queries
client = Elasticsearch(HOST="http://localhost",PORT=9200)
# INDEX = 'srilankan_cricketers_tokenized'
INDEX =  'lka-cricketer-index'

synbirth_place = ['තැන','ස්ථානය','ප්‍රදේශය', 'උපන්ගම', 'ගම','ප්‍රාන්තය', 'පළාත','රට']
synbirth_date = ['උපන්දිනය','ජන්ම දිනය','උපන්','උපතලද','උපත','මෙලොවට ආ','මෙලොව එළිය දුන්','එළිය දුටු','මෙලොවට','ඉපදුන', 'වන දින']
synFemale = ["ගැහැනු", "ගැහැණු", "ස්ත්‍රී", "ක්‍රීඩිකා", "ක්‍රීඩිකාවන්", "ක්‍රීඩිකාව", "කාන්තාව", "කාන්තාවන්", "කාන්තා"]
synMale = ["පුරුශ","පිරිමි","ක්‍රීඩකයන්","ක්‍රීඩකයා","ක්‍රීඩකයෝ"]
synDead = ["අභාවප්‍රාප්ත", "මළ", "නැසී ගිය", "නැසිගිය", "මැරුනු", "මියගිය"]

synonym_list = [ synbirth_place, synbirth_date, synDead]



def search(search_query):
    processed_query = ""
    tokens = search_query.split()
    processed_tokens = search_query.split()
    search_fields = []
    sort_num = 0
    field_list = ["Birth","Birth","Death"]
    all_fields = ["cricketerName","bio","paragraph", "Gender", "Is", "Birth", "Age", "Star sign","Sports Teams","Death","Profiles"]
    final_fields = []

    for word in tokens:
        print (word)

        if (word in synMale and not("පිරිමි" in word)):
            processed_tokens.remove(word)
            processed_tokens.append("පිරිමි")
        elif(word in synMale and not("පිරිමි" in word)):
            processed_tokens.remove(word)
            search_fields.append("Gender")
        if (word in synFemale and not("ගැහැණු" in word)):
            processed_tokens.remove(word)
            processed_tokens.append("ගැහැණු")
        elif(word in synFemale and not("ගැහැණු" in word)):
            processed_tokens.remove(word)
            search_fields.append("Gender")

        for i in range(0, 3):
            if word in synonym_list[i]:
                print('Adding field', field_list[i], 'for ', word, 'search field list')
                search_fields.append(field_list[i])
                if(i%2==0):
                    search_fields.append(field_list[i+1])
                else:
                    search_fields.append(field_list[i -1])
                processed_tokens.remove(word)

    if (len(processed_tokens)==0):
        processed_query = search_query
    else:
        processed_query = " ".join(processed_tokens)

    ##Boosting
    for field in all_fields:
        if (field in search_fields):
            final_fields.append(field+"^5")
        else:
            final_fields.append(field)
    final_fields = search_fields

    
    if(len(search_fields)==0):
        query_es = advanced_queries.multi_match_agg_cross(processed_query, all_fields)
    elif (len(search_fields) == 2):
        query_es = advanced_queries.multi_match_agg_phrase(processed_query, all_fields)
    else:
        query_es = advanced_queries.multi_match_agg_cross(processed_query, final_fields)


    print("QUERY BODY")
    print(query_es)
    search_result = client.search(index=INDEX, body=query_es)
    return search_result





