import urllib.request
import json
import urllib.request

url = "http://api.giphy.com/v1/gifs/translate"
APIKey = "zDMbCp38AEv2LPL8oH83XY9a6V8M28jO"
q = "fat+cat"

with urllib.request.urlopen("http://api.giphy.com/v1/gifs/translate?api_key=" + APIKey + "&s=" + q) as addr:
    s = addr.read()

data = json.loads(s)
gifurl = json.dumps(data, sort_keys=True, indent=4)
#print (json.dumps(data, sort_keys=True, indent=4))

flag = 0
valid = False
gifaddr = ""

for i in gifurl:
    if (flag == 0) and (i == 'u'):
        flag = 1
    elif (flag == 1) and (i == 'r'):
        flag = 2
    elif (flag == 2) and (i == 'l'):
        flag = 3
    elif (flag == 3):
        if i == ' ':
            valid = True
        elif i == ',':
            break
        
        if valid:
            gifaddr += i
    else:
        flag = 0

print(gifaddr)