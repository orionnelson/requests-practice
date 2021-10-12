import requests
import json
url = "https://api.eleuther.ai/completion"
remove_input = 'true'
temp = 0.8
top = 0.9
headers={
                'Accept-Encoding': "gzip, deflate, br",
                'Host': "api.eleuther.ai",
                'Origin': "https://6b.eleuther.ai/",
                'Content-Type' : "application/json",
                'Accept': "application/json",
                'Referer': "https://6b.eleuther.ai/",
                'Sec-Fetch-Dest' : "empty",
                'Sec-Fetch-Mode' : 'cors',
                'Sec-Fetch-Site' : 'same-site'
    
    }






def request(context):
    response_length = int(len(context) * 2)
    
    response = requests.post(url,allow_redirects=False, json={
                    "context": context,
                    "remove_input": remove_input,
                    "response_length": response_length,
                    "temp": temp,
                    "topP": top
            },headers=headers)
    out =json.loads(response.text.replace(']','').replace('[',''))
    print(out['generated_text'])

while True:
    try:
        context = input('Context :')
        request(context)
    except:
        print("Error Please Try Again")
        pass
