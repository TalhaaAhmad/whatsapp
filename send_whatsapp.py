import pandas as pd
import requests
import json

def send_whatsapp_message(whatsapp, message):
    api_url = 'http://116.203.191.58/api/async_send_image_url'
    img_url = 'https://i.ibb.co/KNXjdVJ/20231206-155642.png'
    api_key = '984d4c593074ad943ac2f9e5810e4d1535ad7b25bfe17e2e'

    payload = {
        "phone_no": "923189477670",
        "key": api_key,
        "url": img_url,
        "message": message
    }

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    city_wise = pd.read_csv("Remaining.csv")
    contacts = city_wise["Mobileno"][1475:1480]
    number = 1475

    for contact in contacts:
        contact = int(contact)
        whatsapp = "92" + str(contact)
        message = """🎓 Tariqjee Allied Health Sciences Peshawar presents Scholarship Seats! 🌟"""

        print(f"{number} : {contact} : {send_whatsapp_message(whatsapp, message)}")
        number += 1
