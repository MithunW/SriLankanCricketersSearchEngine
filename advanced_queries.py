import json

#cross_filds
def multi_match_agg_cross(query, fields=['"cricketerName"',"paragraph"]):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
	}

	q = json.dumps(q)
	return q


#phrase_filds
def multi_match_agg_phrase(query, fields=['"cricketerName"',"paragraph"]):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"size": 986,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
	}

	q = json.dumps(q)
	return q
