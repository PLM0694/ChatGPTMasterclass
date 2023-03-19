import logging
import openai
import azure.functions as func

#sample request
# {"model":"text-davinci-003", "prompt":"give me a slogan for a cookie company", "max_tokens":200, "temperature":0}

secret_key = 'your secret key from openai'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    #give OpenAI our secret_key to authenticate 
    openai.api_key = secret_key

    #get variables from the HTTP request body
    req_body = req.get_json()
    logging.info(type(req_body))

    #call the OpenAI API
    output = openai.Completion.create(
        model= req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
    )

    #format the response
    output_text = output["choices"][0]['text']

    #provide the response
    return func.HttpResponse(output_text, status_code=200)
