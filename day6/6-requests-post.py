import requests,json


url = 'https://cn.bing.com/tlookupv3?isVertical=1&&IG=73F09167E79F4558BD8A913395692ED5&IID=translator.5028.4'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
formdata = {
    'from':'zh-CHS',
    'to':'en',
    'text':'小可爱'
}

r = requests.post(url=url,data=formdata,headers=headers)
print(type(r.text))
# r1= json.loads(r.text)
# print(r1.json())


