from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'lk-cricketer-index'


def createIndex():
    settings = {
        "settings": {
            "index":{
                "number_of_shards": "1",
                "number_of_replicas": "1"
            },
            "analysis" :{
                "analyzer":{
                    "sinhala-analyzer":{
                        "type": "custom",
                        "tokenizer": "icu_tokenizer",
                        "filter":["edge_ngram_custom_filter"]
                    }
                },
                "filter" : {
                    "edge_ngram_custom_filter":{
                        "type": "edge_ngram",
                        "min_gram" : 2,
                        "max_gram" : 50,
                        "side" : "front"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                    "cricketerName": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "bio": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "Is": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "Gender": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "paragraph": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "Birth": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "Age": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Star sign": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Stats": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Family": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Politics": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Education": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Was": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Profiles": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Death": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "Sports Teams": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                }
            }
        }
    


    # index = Index(INDEX,using=client)
    # result = index.create()
    result = client.indices.create(index=INDEX , body =settings)
    print (result)


def read_translated_cricketers():
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file1 = os.path.join(THIS_FOLDER, 'data')
    my_file = os.path.join(my_file1, 'filtered-si-data.json')
    
    with open(my_file,'r',encoding='utf8') as tra_file:
        tra_cricketer = json.loads(tra_file.read())
        results_list = [a for num, a in enumerate(tra_cricketer) if a not in tra_cricketer[num + 1:]]
        return results_list


# def clean_function(song_lyrics):
#     if (song_lyrics):
#         processed_list = []
#         song_lines = song_lyrics.split('\n')
        
#         for place,s_line in enumerate(song_lines):
#             process_line = re.sub('\s+',' ',s_line)
#             punc_process_line = re.sub('[.!?\\-]', '', process_line)
#             processed_list.append(punc_process_line)
        
#         sen_count = len(processed_list)
#         final_processed_list = []
        
#         for place,s_line in enumerate(processed_list):
#             if (s_line=='' or s_line==' '):
#                 if (place!= sen_count-1 and (processed_list[place+1]==' ' or processed_list[place+1]=='')) :
#                     pass
#                 else:
#                     final_processed_list.append(s_line)
#             else:
#                 final_processed_list.append(s_line)
#         final_song_lyrics = '\n'.join(final_processed_list)
#         return final_song_lyrics
#     else:
#         return None

def data_generation(cricketer_array):
    for cricketer in cricketer_array:

        cricketerName = cricketer["cricketerName"]
        bio = cricketer["bio"]
        paragraph = cricketer['paragraph']

        gender = cricketer["Gender"]
        is_ = cricketer["Is"]
        birth = cricketer["Birth"]
        age = cricketer["Age"]
        
        star_sign = cricketer["Star sign"]
        sports_Teams = cricketer["Sports Teams"]
        death = cricketer["Death"]
        profiles = cricketer["Profiles"]
        

        yield {
            "_index": INDEX,
            "_source": {
                "cricketerName": cricketerName,
                "bio": bio,
                "paragraph": paragraph,
                "Gender": gender,
                "Is": is_,
                "Birth": birth,
                "Age": age,
                "Star sign": star_sign,
                "Sports Teams": sports_Teams,
                "Death": death,
                "Profiles": profiles
            },
        }


createIndex()
translated_cricketers = read_translated_cricketers()
helpers.bulk(client,data_generation(translated_cricketers))