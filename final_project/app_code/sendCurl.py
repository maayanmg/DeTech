import json
import requests

def send_curl(photo_path):
    headers = {
        'accept': 'application/json',
        # requests won't add a boundary if this header is set when you pass files=
        # 'Content-Type': 'multipart/form-data',
    }

    files = {
        'image_file': open(photo_path, 'rb'),
    }

    response = requests.post('http://localhost:5000/pneumonia/predict', headers=headers, files=files)
    print(response.text)

    jRes = json.loads(response.text)
    print(jRes)
    pneu_chance =  str(jRes['pneumonia_probability'])
    pneu_chance = pneu_chance[1:-1]
    pneu_chance = float(pneu_chance)*100
    pneu_chance = str(pneu_chance)
    pneu_chance = pneu_chance[:4]
    pneu_chance = float(pneu_chance)
    if str(jRes['predicted_class']) == 'normal' and pneu_chance < 50:
        return "normal in " + str(100-pneu_chance) + "%"
    return "pneumonia in " + str(pneu_chance) + "%"

if __name__ == '__main__':
    send_curl(r"D:\Projects\pneumonia-detection\fixtures\pneumonia_1.jpeg")