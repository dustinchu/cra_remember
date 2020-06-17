import json


myDict = {"dict": [{"a": "none", "b": "none", "c": "none"}]}
test = json.dumps(myDict)
myDict["dict"].append(({"a": "aaaa", "b": "aaaa", "c": "aaaa"}))
test = json.dumps(myDict)
print(test)

home_json = []

home = {"home":"","home_body":[]}
home["home"] = "hostname"
a={
    "title":"1111",
    "name":"name"
}
home["home_body"].append(a)
home["home_body"].append(a)
home["home_body"].append(a)
home["home_body"].append(a)
json.dumps(home)

home_json.append(home)
obj= json.dumps(home_json)
print(obj)
