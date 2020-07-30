


# url = 'http://api.map.baidu.com/place/v2/search?query=餐饮&region=长沙&output=json&ak=j1rw21ZB3hpsz8XjqVULHTC4vwbytqxC'
import requests
a='http://api.map.baidu.com/place/v2/search?query=餐饮&region=长沙&page_num='
b='&page_size=20&output=json&ak=j1rw21ZB3hpsz8XjqVULHTC4vwbytqxC'
i=1
f=open(r'e:\baidupoi.txt','a')
for p in range(20):
    url=a+str(p)+b
    web=requests.get(url).json()
    for poi in web['results']:
        name=poi['name']
        y=poi['location']['lat']
        x=poi['location']['lng']
        add=poi['address']
        city=poi['city']
        area=poi['area']
        rt=str(i)+','+name+','+str(x)+','+str(y)+','+add+','+city+','+area
        print(rt)
        print(url)
        f.write(rt+'\n')
        i+=1
f.close()
