import json

studentJson ="""{ 
   "class":{ 
      "student":{ 
         "name":"jhon",
         "marks":{ 
            "physics": 70,
            "mathematics": 80
         }
      }
   }
}"""

PATH = r'C:\\development\\repos\\MARC-SIM\\Tests\\message_60_61_data.json'

with open(PATH, "r") as json_file:
        data = json.load(json_file)

data["0x6061"]["COPAATarget"][0]["TargetLatitude"] = 1
print(data)
