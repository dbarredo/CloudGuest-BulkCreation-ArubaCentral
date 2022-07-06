import pandas as pd
import json
import requests

headers1 = {'content-type': 'application/json', 'accept': 'application/json'}
baseurl = " " #BaseURL
tokens = " " #TokenID
portal_id = "" #portal id

central_cli = "/guest/v1/portals"
central_guest_gen = "/guest/v1/portals/"+portal_id+"/visitors?access_token="+tokens
dir = " " #local directory of the file

df = pd.read_csv(r'{dir}.csv')
df.set_index("Number", drop=True, inplace=True)
dictionary = df.to_dict(orient="index")


for i in dictionary:
   GuestAccounts = dictionary[i]
   guest_gen_url = baseurl+central_guest_gen
   guest_account = {"name": str(GuestAccounts['Username']),"company_name": " "\
   ,"user": {"phone": "+6512310000","email":str(GuestAccounts['Email']) },\
   "is_enabled": True,"valid_till_no_limit": False,"valid_till_days": 35,\
   "valid_till_hours": 0,"valid_till_minutes": 0,"notify": False,\
   "notify_to": "email","password": str(GuestAccounts['Password']),"status": True,\
   "created_at": "","expire_at": "1672307969"}
   payload=json.dumps(guest_account)
   http_resp = requests.post(guest_gen_url,payload, headers=headers1)
   print("Account Created for Guest Username: "+ str(GuestAccounts['Username'])+" Password: "+str(GuestAccounts['Password'])+ " " +  "Name :"+ str(GuestAccounts['FirstName']) + " " + str(GuestAccounts['LastName']))
    
