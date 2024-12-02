import requests, time
from app.utils.whatsapp_utils import send_message
from flask import current_app, jsonify

def ping(url):
    result = requests.get(url)
    method = result.request.method
    return (result.status_code == 200, method)


def verifyWebsite(url):
    try:
        isOnline, method = ping(url)
        if(isOnline == True):
            return True
        else:
            # Send whatsapp message, the site is not valid
            message = f"[{time.strftime('%D')}, {time.strftime('%H:%M:%S')}] {method} {url} The website is offline"

            send_message(current_app.config["RECIPIENT_WAID"], message)
            
    except:
        print(f"[{time.strftime('%D')}, {time.strftime('%H:%M:%S')}] Couldn't connect to website")

verifyWebsite('www.google.com')