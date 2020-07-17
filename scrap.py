import requests

from bs4 import BeautifulSoup

url = "https://text-to-speech-demo.ng.bluemix.net/"

page_source = requests.get(url)

soup = BeautifulSoup(page_source.content,"html.parser")

voices = soup.find_all("option")

with open("voice type.txt","w") as file:
    for voice in voices:
        file.write(f"{voice.get('value')} --> {voice.text} \n")



