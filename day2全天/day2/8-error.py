import urllib.request
import urllib.error

# url = 'http://www.maodan.com/'
# try:
#     response = urllib.request.urlopen(url)
# # except Exception as e:
# except urllib.error.URLError as e:
#     print(response.getcode())

url = 'https://blog.csdn.net/csdnnews/article/details/97990644'
try:
    response = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:

    print(response.getcode())