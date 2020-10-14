import requests

req = requests.get('https://kea.dk/', allow_redirects=True)


print(req.text)
txt = req.text

with open('img.png', 'bw') as f:
    f.write(req.content)