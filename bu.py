import os
import requests
import threading
import json
import time


def ng_rok():
    os.system("ngrok http 80")


def xampp():
    os.system("C:\\xampp\\xampp_start.exe")


tXampp = threading.Thread(target=xampp)
tXampp.start()

time.sleep(10)

tNgrok = threading.Thread(target=ng_rok)
tNgrok.start()

time.sleep(10)

os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

with open('tunnels.json') as data_file:
    datajson = json.load(data_file)

ngrok = datajson['tunnels'][1]['public_url']

while 1:
    time.sleep(15)
    urlReact = 'http://ffe0b5c1.ngrok.io/inf-sec-java-ser/java/check'
    dataReact = {"url": "" + ngrok + "/inf-sec-php-ser/servicios-php.php", "config": "backup"}

    headers = {'Content-Type': 'application/json'}
    params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}

    try:
        response = requests.post(urlReact, params=params, data=json.dumps(dataReact), headers=headers)
        urlBackUp = response.json()['url']
    except requests.exceptions.RequestException as e:
        print("React Apagado")

    if urlBackUp != "noRoot":

        urlBackUp = urlBackUp.replace("servicios-php.php", "backuper.php")
        dataBackUp = {"url": "" + ngrok + "/inf-sec-php-ser/recibir.php"}

        print("urlBackUp: " + urlBackUp)
        print("urlBackUp: " + str(dataBackUp))

        try:
            response = requests.post(urlBackUp, params=params, data=json.dumps(dataBackUp), headers=headers)
            print(response)
        except requests.exceptions.RequestException as e:
            print("Error Backapeando")

    time.sleep(45)
