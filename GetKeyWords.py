# -*- coding: utf-8 -*-

import http.client, urllib
import json

accessKey = '8f206924c68748519003ad6cbe417df8'

uri = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/keyPhrases'

def GetKeyWords (text):
    documents = { 'documents': [{ 'id': '1', 'language': 'en', 'text': text }]}
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = http.client.HTTPSConnection (uri)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse()
    print('Please wait a moment for the results to appear.\n')
    result = response.read()
    print (json.dumps(json.loads(result), indent=4))
    return (json.loads(result))

