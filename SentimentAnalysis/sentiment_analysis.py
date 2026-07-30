import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json=input_json, headers=headers)
    
    # Check the status code FIRST before trying to parse the JSON
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
        
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None
        
    # For any other unexpected status codes, set label and score to None
    else:
        label = None
        score = None

    # Return the label and score in a dictionary (Aligned all the way to the left of the function)
    return {'label': label, 'score': score}