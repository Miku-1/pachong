import requests
from requests.exceptions import Timeout

url = 'http://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
try:
    r = requests.get(url=url,headers=headers,timeout=0.1)
    print(r.text)
except Timeout as e:
    print(e)
