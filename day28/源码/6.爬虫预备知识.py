from urllib.request import urlopen, Request
url = 'https://movie.douban.com/top250?start=%s&filter='
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
ret = Request(url, headers=headers)
res = urlopen(ret)
aa = res.read().decode('utf-8')
print(aa)