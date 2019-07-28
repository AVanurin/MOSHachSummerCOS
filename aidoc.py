import requests
from lxml import etree
from xml.sax.saxutils import escape, unescape
import json

base_ip = "http://81.5.119.111:5000/moshack"


def send_xml(text):
    url = base_ip + "/document_card"
    headers = {
        "Content-Type": "text/xml"
    }
    data = f"""<?xml version="1.0"?><AIDOC-request><Text>{text}</Text></AIDOC-request>"""
    response = requests.post(url, headers=headers, data=data.encode('ascii','xmlcharrefreplace'))
    return _parse(response.content.decode())

def _parse(xml_string):
    root = etree.XML(xml_string)
    classifiers_xml = root[0]

    result = []

    for classifier in classifiers_xml:
        if classifier.tag == "Classifier":
            result.append({
                "class_id": classifier.get('class_id'),
                "elementID": classifier.get('elementID'),
                "probability": classifier.get('probability'),
            })
    return result

def send_json(text):
    url = "http://rtx2080.cos.ru:5007/intents"

    data = json.dumps({
        "context": [text]
    })

    headers = {"Content-Type": "application/json"}

    r = requests.post(url, headers=headers, data=data)
    print(r.content)
    print(r)

send_json('Мой дорогой текст')
