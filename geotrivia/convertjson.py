
import json
import re
with open('geotrivia/output15575 copy.json','r',encoding='utf-8') as j:
    data = json.load(j)

new=[]
for key, value in data.items():
    temp={}
    key=key
    temp["question"] = key
    
    temp["answer"] = value
    new.append(temp)


with open('geotrivia/outputlist2.json', 'w',encoding = 'utf-8') as file:
    file.write("[")
    for item in new :
        file.write(f"{item},")

    file.write("]")
