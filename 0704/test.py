# 1.计算矩形面积：用户输入矩形的长和宽，计算其面积并输出，结果四舍五入，保留2位小数。
# lenght = float(input('请输入矩形的长：'))
# wide = float(input('请输入矩形的宽：'))
# s = (lenght * wide)
# res = round(s, 2)
# print(res)

# for i in range(100, 201):
#     for j in range(2, i//2+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(f'{j}x{i}={i*j}',end='    ')
#     print()

# year = int(input('请输入年份：'))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f'{year}是闰年')
# else:
#     print(f'{year}不是闰年')

# s = 0
# for i in range(100, 1001):
#     s += i
# print(s)
# for v in {1, 2, 3}:
#     print(v)
# res = map(lambda x:x**2, [1, 2, 3, 4])
# print(res)
# dict1 = {'001’':'zhangsan','002':'lisi','003':'wangwu'}
# print(list(dict1.items()))

# a = [1, 2, ['a', 'b']]  

# b = a  

# a.insert(0, 3)  

# a[-1].append(3)
# print(b) 

# s ='1'
# print(type(s) == str)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(list1 + list2)
# print(list1 * 2)
# list1.append(7)
# print(list1)
# list1.extend([8, 9])
# print(list1)
# list1.insert(0, 10)
# print(list1)
# list1.pop()
# print(list1)
# list1.remove(10)
# print(list1)
# list1[0] = 10
# print(list1)
# print(list1[0])
# for n in list1:
#     pass
# list1[1:4]

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict1.pop('c')
# dict1.keys
# dict1.values
# dict1.get('a')
# dict1.clear

# str1 = 'asdFGH123'
# print(str1.upper())
# print(str1.lower())
# print(str1.swapcase())
# print(str1.isalpha())
# print(str1.isdigit())
# print(str1.isalnum())

# list2 = [1, 2, 3, 4]
# t1 = tuple(list2)

# 1.
# 定义函数实现冒泡排序功能，参数是要排序的列表，返回值是排序后的列表. 如list1=[1,3,5,6,7,9,0,2,4,7,9], 排序后的结果：[0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 9]
# list1=[1,3,5,6,7,9,0,2,4,7,9]
# def my_sort(li):
#     for i in range(len(li)-1):
#         for j in range(len(li)-1-i):
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j]
#     return li
# res = my_sort(list1)
# print(res)

# 2.
# 定义一个函数求偶数的累加和，参数是范围，如参数是n，则表示求1-n的范围内偶数的累加和，结果以返回值形式返出

# def even_sum(end):
#     s = 0
#     for i in range(0, end+1, 2):
#         s += i
#     return s
# res = even_sum(10)
# print(res)

# 3.
# 定义一个函数: 实现产生验证码的功能，参数是产生验证码的个数，验证码要求是大小写字母数字的随机组合.
def generate_verification_code(n):
    list1 = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']



