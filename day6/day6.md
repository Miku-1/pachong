day06-爬虫6

1、selenium+phantomjs
	selenium是什么？它是一个浏览器的自动化测试工具，其实就是你写一份代码，然后这个代码去操作浏览器执行一些功能。
	安装selenium   pip install selenium
	selenium操作了一个谷歌浏览器驱动，由这个谷歌浏览器的驱动来驱动浏览器做操作
	谷歌浏览器驱动下载地址
		http://chromedriver.storage.googleapis.com/index.html
		http://npm.taobao.org/mirrors/chromedriver/
	谷歌驱动和浏览器版本关系映射表
		http://blog.csdn.net/huilan_same/article/details/51896672
	browser查找节点的方法
		browser.find_element_by_id   根据id查找指定节点
		browser.find_elements_by_class_name   根据class查找指定节点s
		browser.find_elements_by_xpath   根据xpath路径查找指定节点s
		browser.find_elements_by_css_selector  根据选择器查找指定节点s
		browser.find_elements_by_link_text    根据a链接的内容查找指定的a链接s
		browser.find_element_by_link_text
	上面的就是让你熟悉selenium可以操作浏览器，真正我们操作的是phantomjs
	phantomjs是什么？也是一款浏览器，因为这个浏览器没有界面，所以你没有听过和用过。虽然没有界面，但是它是浏览器，就有浏览器的功能，可以将html、css转化为界面，可以执行js代码，程序猿用的就是phantomjs可以执行js的功能。
	抛出问题：如果页面中的内容是动态加载的数据，请问如何抓取？
		动态数据：ajax结合js然后动态的生成标签和内容
	（1）捕获接口，获得json数据，解析json数据即可
	（2）大招，绝招，selenium+phantomjs，一般不要用，主要是因为效率。因为phantomjs是浏览器，它就可以执行js，我们可以获取到执行完js代码之后的页面，然后再去解析即可
	selenium操作phantomjs
		见代码
		拍照片记录走到哪
		browser.save_screenshot('./pic/baidu1.png')
	滚动条滚动到底部

模拟滚动条到底部, 第二个可以写body，也可以写documentElement

​		js = 'document.body.scrollTop=10000'

让phantomjs执行这个代码

​		browser.execute_script(js)
​	获取的执行完js之后的结果
​		browser.page_source
​	selenium不仅可以操作谷歌浏览器、phantomjs、火狐、ie浏览器、欧朋
2、headlesschrome
​	phantomjs已经不再维护，以后要使用无界面的谷歌。
​	headlesschrome是什么？谷歌浏览器的无界面模式
​	from selenium.webdriver.chrome.options import Options
​	chrome_options = Options()
​	chrome_options.add_argument('--headless')
​	chrome_options.add_argument('--disable-gpu')
3、requests
​	是什么？是一个第三方库，功能和urllib是一样的。模拟发送http请求的，requests提供的接口简介、人性化。
​	安装：pip install requests
​	http://docs.python-requests.org/zh_CN/latest/index.html
​	发送get请求
​	定制头部
​		r = requests.get(url=url, params=data, headers=headers)
​	响应对象
​		字符串格式：  r.text
​		字节格式：    r.content
​		状态码：      r.status_code
​		得到请求url： r.url
​		响应头部：   r.headers
​		设置或者获取字符集：    r.encoding
​		如果返回内容为json格式：  r.json()  直接得到python对象
​	发送post请求
​		r = requests.post(url=url, data=formdata, headers=headers)
​	ajax-get-post
​		r.json()
​	代理
​		见代码
​	cookie
​		会话，如何通过代码保存和携带cookie
​		s = requests.Session()
​		后续的请求都使用s.get()   s.post()  即可
​	异常
​		所有的异常都在这个模块中：requests.exceptions
​		ConnectionError ： 就是以前的URLError
​		HTTPError：就是以前的HTTPError
​		Timeout：超时的异常
4、requests实例

https://www.8684.cn	

公交车