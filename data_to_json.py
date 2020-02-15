import json

with open('source.txt') as s:
    source = s.read()
    source = source.split('\n')
    print(type(source),source)

source_dict = {'producer' : source[0], 'model' : source[1], 'fuel' : source[2], 'price' : source[3]}

print (source_dict)

with open ('source_to_json.txt', 'w') as f:
    json.dump(source_dict, f)