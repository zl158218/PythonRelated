### 1, replace("·","")   将 · 替换成 空格
	 
### 2, contains(@class, '属性值') 
	- 例子：
	1. xpath("//span[contains(@class,'vote-post-up')]")
	2. 取值 response.xpath("//span[contains(@class,'vote-post-up')]").extract()
	3. 变成数组 response.xpath("//span[contains(@class,'vote-post-up')]").extract()[0]

### 3, url 拼接
	from urllib import parse
	url = "https://www.enterdesk.com/bizhi/35262.html"
	href = "/bizhi/35475-211088.html"
	urls = parse.urljoin(href,url)
	print(urls)
	https://www.enterdesk.com/bizhi/35262.html
### 4, scrapy Requests对象
	url(string): 用于请求的URL
	callback(callable):指定一个回调函数，该回调函数以这个request是的response作为第一个参数。如果未指定callback，则默认使用spider的parse()方法。
	meta(dict):指定Request.meta属性的初始值。如果给了该参数，dict将会浅拷贝。(浅拷贝不懂的赶紧回炉)
	headers(dict):request的头信息
	encoding(string):请求的编码， 默认为utf-8

	priority(int):请求的优先级

	dont_filter(boolean):指定该请求是否被 Scheduler过滤。该参数可以是request重复使用（Scheduler默认过滤重复请求）。谨慎使用！！

	errback(callable):处理异常的回调函数。
