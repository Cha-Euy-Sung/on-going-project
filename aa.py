import json
from pprint import pprint

with open('stu_info.json', 'r+') as f:
    json_data = json.load(f)
    name = "Yookyung"
    print(json_data[name][3]["memo"])
    json_data[name][3]["memo"] = input("input: ")
    f.seek(0)
    f.write(json.dumps(json_data))
    f.truncate()