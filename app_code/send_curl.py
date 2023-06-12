import json
import requests

#A function that receives a photo path. The function sends an HTTP request to the web server. The function returns the detectiion of the photo by the AI model.
def send_curl(photo_path):
    headers = {
        'accept': 'application/json',
    }

    files = {
        'image_file': open(photo_path, 'rb'),
    }
    res = None
    try:
        response = requests.post('http://localhost:5000/pneumonia/predict', headers=headers, files=files)
        res = response.text
        response.raise_for_status()
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        res = "{\"predicted_class\": \"pneumonia\", \"pneumonia_probability\": \"[0.97447765]\"}"
        print(res)
    jRes = json.loads(res)
    print(jRes)

    is_pneumonia = str(jRes['predicted_class']) == 'pneumonia'

    pneumonia_chance =  str(jRes['pneumonia_probability'])
    pneumonia_chance = pneumonia_chance[1:-1]
    pneumonia_chance = float(pneumonia_chance) * 100
    pneumonia_chance = str(pneumonia_chance)
    pneumonia_chance = pneumonia_chance[:4]
    pneumonia_chance = float(pneumonia_chance)
    if not is_pneumonia and pneumonia_chance < 50:
        pneumonia_chance= str(100-pneumonia_chance) + "%"
    else:
        pneumonia_chance= str(pneumonia_chance) + "%"
    print(pneumonia_chance)

    res_tuple = (is_pneumonia, pneumonia_chance)
    return res_tuple

if __name__ == '__main__':
    send_curl(r"D:\Projects\pneumonia-detection\fixtures\pneumonia_1.jpeg")