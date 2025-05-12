import requests
import base64

# افتح صورة الوجه بصيغة Base64
with open("fg.jpeg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# أرسل الصورة إلى السيرفر
response = requests.post("http://127.0.0.1:5000/", json={"image": encoded_string})

# اطبع النتيجة
print(response.json())
