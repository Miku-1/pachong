import urllib.request


url = 'http://www.renren.com/971784533/profile'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Cookie': 'anonymid=jzapomwn-fblm6b; depovince=SXI; jebecookies=e928b521-1b26-45c2-8a36-b48c9f825d3f|||||; _r01_=1; JSESSIONID=abc0a4WM3S4gr4JLPooYw; ick_login=7d01f46e-7ae8-469b-9c6a-92bdfa1ad547; _de=4833D503D4E50E85C01F3B7AB93A379D; p=8b5db27b2ff3f41aa39472d59fc5a40a3; first_login_flag=1; ln_uact=19992683234; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=8ae9ab83934561abe5a4ebd90df2096d3; societyguester=8ae9ab83934561abe5a4ebd90df2096d3; id=971784533; xnsid=71c535ad; ver=7.0; loginfrom=null; jebe_key=cc492ba7-3d78-4951-b250-f3cc380f242f%7Cb958c3060a3953c3a7a9e0fcf1d3338f%7C1565754317382%7C1%7C1565754317819; jebe_key=cc492ba7-3d78-4951-b250-f3cc380f242f%7Cb958c3060a3953c3a7a9e0fcf1d3338f%7C1565754317382%7C1%7C1565754317823; wp_fold=0',

}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)

with open('renren.html','wb')as f:
    f.write(response.read())