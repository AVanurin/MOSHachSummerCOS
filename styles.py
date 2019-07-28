from lxml import etree

XSI= """<?xml version="1.0"?>
<Classes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <Class class_id="H1" class_name="Поиск финансирования на проекты технологической направленности по тематике  Цифровые технологии" url="H1"/>
    <Class class_id="H2" class_name="Поиск финансирования на проекты технологической направленности по тематике Медицина" url="H2"/>
    <Class class_id="H3" class_name="Поиск финансирования на проекты технологической направленности по тематике Новые материалы и химические технологии" url="H3"/>
    <Class class_id="H4" class_name="Поиск финансирования на проекты технологической направленности по тематике Новые приборы и интеллектуальные производственные технологии" url="H4"/>
    <Class class_id="H5" class_name="Поиск финансирования на проекты технологической направленности по тематике Биотехнологии"   url="H5"/>
    <Class class_id="H6" class_name="Поиск финансирования на проекты технологической направленности по тематике Энергетика"  url="H6"/>
    <Class class_id="S1" class_name="Поиск финансирования на проекты в области электронных СМИ" url="S1"/>
    <Class class_id="S2" class_name="Поиск финансирования на проекты в области кинематографии" url="S2"/>
    <Class class_id="F1" class_name="Проблема с доначислением налогов ФНС" url="F1"/>
    <Class class_id="M1" class_name="Проблемы с пожаррным надзором" url="M1"/>
</Classes>
"""

def _parse():
    style = etree.XML(XSI)
    result = []

    for Class in style:
        _id = Class.get("class_id")
        _name = Class.get("class_name")
        _url = Class.get("url")
        result.append({"id": _id, "name": _name, "url": _url})
    return result

def make_results(datas):
    r = []
    classes = _parse()

    for data in datas:
        for c in classes:
            if c["id"] == data["elementID"]:
                r.append({
                    "id": c["id"],
                    "name": c["name"],
                    "chance": str(round(float(data["probability"]), 2)),
                    "url": c["url"]
                })
                break
    return r