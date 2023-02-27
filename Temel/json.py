

import json

data = '{"firstName":"berke","lastName":"yapıcı"}'

y = json.loads(data)

print(y["firstName"])
print(y["lastName"])


customer = {
        "firstName":"berke",
        "email":"berke@gmail.com"
        }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("berke"))
