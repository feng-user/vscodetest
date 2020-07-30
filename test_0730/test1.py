from redis import *

sr = StrictRedis(host='192.168.126.135', port=6379, password='')
try:
    result = sr.set('py1', 'gj')
    print(result)
except Exception as e:
    print(e)

# result = sr.delete('py1')
# print(result)

result = sr.set('py1', 'he')

result = sr.get('py1')

result= sr.keys