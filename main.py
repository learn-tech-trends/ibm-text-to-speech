import requests

url = 'https://text-to-speech-demo.ng.bluemix.net/api/v3/synthesize'

params = {
    "text" : "Hello Everyone. Wellcome back to my channel.",
    "voice" : "en-GB_JamesV3Voice",
    "download" : "true",
    "accept" : "audio/mp3",
    }

result = requests.get(url,params=params)

with open("sample1.mp3","wb") as file:
    file.write(result.content)
