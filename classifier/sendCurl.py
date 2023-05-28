import json
import requests

headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    'image_file': open('D:\\Projects\\pneumonia-detection\\fixtures\\test_normal_1.jpeg', 'rb'),
}

response = requests.post('http://localhost:5000/pneumonia/predict', headers=headers, files=files)
print(response.text)

jRes = json.loads(response.text)
print(jRes)
print(jRes['pneumonia_probability'])