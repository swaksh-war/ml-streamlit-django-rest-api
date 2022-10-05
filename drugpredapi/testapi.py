import requests
predict = [x for x in requests.post("http://127.0.0.1:8000/?age=68&gender=0&bp=2&cholesterol=2&salt=27")]
print(predict)