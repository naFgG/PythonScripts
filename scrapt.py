"""
在Python中，我们可以使用第三方库来实现爬虫。
比如requests库用于发送HTTP请求，只能爬静态网页。有javascript的网页需要其他库
beautifulsoup4库用于解析HTML代码
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
首先，我们需要获取要爬取的网页的源代码。
这里我们可以使用requests库中的get()函数向网站发送一个GET请求
然后使用.text属性获取请求返回的HTML源代码。
"""
url = 'https://www.example.com/'
header = {'User-Agent': 'xxxxxx'}
response = requests.get(url, header)
response.encoding = response.apparent_encoding
html = response.text

"""
得到网页源代码后，我们需要从中提取出我们需要的信息。
通常情况下，我们需要使用beautifulsoup4库中的BeautifulSoup类来解析HTML代码。
"""
soup = BeautifulSoup(html, 'lxml')

"""
接下来，我们需要找到包含所需信息的HTML标签，并将其提取出来。
比如，假设我们想要从一个网页中提取所有的链接，我们可以使用find_all()方法查找所有的<a>标签，并从中获取href属性。
"""
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

"""
最后，我们需要将提取出来的数据存储到本地文件或数据库中，以便后续使用。
比如，我们可以将数据保存为CSV文件，使用pandas库中的DataFrame类和to_csv()函数实现。
"""
df = pd.DataFrame({'Links': links})
print(df)
# df.to_csv('links.csv', index=False)
