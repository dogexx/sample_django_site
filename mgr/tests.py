# from django.test import TestCase

import requests, pprint


def test_list_customer():
    response = requests.get('http://0.0.0.0:8000/api/mgr/customers?action=list_customer')

    pprint.pprint(response.json())

def test_add_customser():
    # 构建添加 客户信息的 消息体，是json格式
    payload = {
        "action":"add_customer",
        "data":{
            "name":"武汉市桥西医院",
            "phonenumber":"13345679934",
            "address":"武汉市桥西医院北路"
        }
    }

    # 发送请求给web服务
    response = requests.post('http://localhost:8000/api/mgr/customers',
                json=payload)

    pprint.pprint(response.json())

    # 构建查看 客户信息的消息体
    response = requests.get('http://localhost:8000/api/mgr/customers?action=list_customer')

    # 发送请求给web服务
    pprint.pprint(response.json())

if __name__ == "__main__":
    test_add_customser()
    # test_list_customer()