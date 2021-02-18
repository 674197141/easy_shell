import requests
import json

def test_req(msg,data):
    url = "http://localhost:8000/msg"
    body = {
        "msg":msg,
        "arg":{
            "a":"a",
        }
    }
    res = requests.post(url,json=body)
    print(res.text)

if __name__ == '__main__':
    test_req("hand_test",{})
    