import  requests 
from requests.auth import HTTPBasicAuth

url = "https://api.livechatinc.com/agents/AGENT_EMAIL"

auth=HTTPBasicAuth('USERNAME', 'PASSWORD')
headers= {'X-API-Version': '2'}
data= {"status":"not accepting chats"}

r = requests.put(url, auth=auth, headers=headers, data=data)


