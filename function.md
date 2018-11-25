### 1, replace("·","")   将 · 替换成 空格
	 
### 2, contains(@class, '属性值') 
	- 例子：
	1. xpath("//span[contains(@class,'vote-post-up')]")
	2. 取值 response.xpath("//span[contains(@class,'vote-post-up')]").extract()
	3. 变成数组 response.xpath("//span[contains(@class,'vote-post-up')]").extract()[0]
