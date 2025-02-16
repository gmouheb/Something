import xmltodict
import json
from bs4 import BeautifulSoup

with open('resu.xml', 'r') as f:
    data = f.read()

# Parse XML with BeautifulSoup
Bs_Data = BeautifulSoup(data, 'xml')

# Remove duplicates
noDuplicates = set()
for i in Bs_Data.find_all():
    eleToString = str(i)
    if eleToString in noDuplicates:
        i.extract()
    else:
        noDuplicates.add(eleToString)

# Get the cleaned XML as string
clean_data = str(Bs_Data)

# Convert XML to dict using xmltodict
xml_dict = xmltodict.parse(clean_data)

# Convert dict to JSON
json_data = json.dumps(xml_dict, indent=4)

# Save to file
with open('outputNew.json', 'w') as f:
    f.write(json_data)

print("XML successfully converted to JSON and saved as 'output.json'")

'''


print(noDuplicates)

json_data = json.dumps(noDuplicates,indent=4)

print(json_data)

new_json_output = "data.json"
with open("outputJson.json","w",encoding="utf-8") as json_file:
    json_file.write(json_data)
'''