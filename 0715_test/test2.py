# 1.
# 熟练使用常用DOS命令行进行操作, cd
# cd 切换路径
# cd..放回上一级
# cd/返回根目录
#
# 2.
# 自己安装Python开发环境并清楚配置环境变量的目的
#
# 3.
# 写一个初级程序
# 打印：大家好，我是XXX
print('大家好，我是xxx')
#
# 4.
# 在控制台打印出古诗如下所示的格式：
# 春眠不觉晓，
# 处处闻啼鸟。
# 夜来风雨声，
# 花落知多少。
#
# 5.
# 控制台打印出如下格式所示的内容
# ** ** ** ** ** ** *
# 欢迎学习Python
# ** ** ** ** ** ** *
#
# 6.
# 进制转换
# a, 将二进制1100和10111
# 分别转成八进制、十进制、十六进制
#
# b, 将下列10进制数转成二进制
# 193, 49, 81, 35
#
# c, 将下列二进制数转成八进制、十进制、十六进制
# 100001001
# 11001101
#
# d, 把八进制27转换成十六进制
#
# 7.
# 自查资料，预习知识点：变量
# 运算符，if语句

# 初级：
#
# 1.判断下面标识符是否合法并说明不合法的原因
# 	@abc.com    不合法，只能由字母数字下划线组成
# 	123ok       不合法，不能以数字开头
# 	_xiaoming   合法
# 	Xiaoming_$  不合法，只能由字母数字下划线组成
# 	interface   合法
# 	sina@163    不合法，只能由字母数字下划线组成


# 2.从控制台输入圆的半径，计算周长和面积, π=3.14
radius = int(input('请输入圆的半径：'))
area = 3.14 * radius**2
perimeter = 2 * 3.14 * radius
print(f'该圆的面积为{area},周长为{perimeter}')

# 3.一辆汽车以40km/h的速度行驶,行驶了45678.9km,求所用的时间
journey = 45678.9
time = journey/40
print(f'汽车所用的时间为{time}小时')



# 4.华氏温度转摄氏温度
# 【提示：将华氏温度转换为摄氏温度(F是华氏温度)  F = 1.8C + 32】
# 1.8C = F - 32  =>c = F/1.8 - 32/1.8
F = int(input('请输入您想转换的华氏温度：'))
C = F/1.8 - 32/1.8
print(f'该华氏温度转换成的摄氏温度为：{C}')


# 5.从控制台输入两个数，输出较大的值
num1 = int(input('请输入第一个数字'))
num2 = int(input('请输入第二个数字'))
if num1 > num2:
    print(f'两个数中较大的数为num1，值为{num1}')
else:
    print(f'两个数中较大的数为num2，值为{num2}')


# 6.模拟玩骰子游戏，根据骰子点数决定什么惩罚【例如：1.跳舞，2.唱歌....】
import random
n = random.randint(1,6)  # 随机取1~6中的某一个整数
if n == 1:
    print('跳舞')
elif n == 2:
    print('唱歌')
elif n == 3:
    print('看电视')
elif n == 4:
    print('散步')
elif n == 5:
    print('逛街')
else:
    print('倒立洗头')

# 中级：
# 1.x 为 0-99 取一个数,y 为 0-199 取一个数,如果 x>y 则输出 x， 如果 x 等于 y 则输出 x+y，否则输出y
x = int(input('请输入一个0-99之间的数'))
y = int(input('请输入一个0-199之间的数'))
if (x < 0 or x > 99) or (y < 0 or y > 199):
    print('输入错误')
else:
    if x > y:
        print(x)
    elif x == y:
        print(x + y)
    else:
        print(y)

# 2.从控制台输入三个数，输出较大的值
num3 = int(input('请输入第一个数字num3'))
num4 = int(input('请输入第二个数字num4'))
num5 = int(input('请输入第三个数字num5'))
if num3 > num4:
    if num3 > num5:
        print(f'最大的数字为num3，值为{num3}')
    else:
        print(f'最大的数字为num5，值为{num5}')
else:
    if num4 > num5:
        print(f'最大的数字为num4，值为{num4}')
    else:
        print(f'最大的数字为num5，值为{num5}')


# 3.从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”
# 该数的每一位的立方和等于自身的值,比如:153=1^3+5^3+3^3
# 	例如：153=1^3+5^3+3^3
# 	n = 153:
# 	个位：n%10
# 	十位：(n//10)%10
# 	百位：n//100
num6 = int(input('请输入一个三位数：'))
the_unit2 = num6 % 10
tens2 = (num6%100)//10
hundreds2 = n // 100
if num6 < 100 or num6 > 999:
    print('输入错误')
else:
    if the_unit2**3 + tens2**3 + hundreds2**3 == num6:
        print('输入的数字是水仙花数')
    else:
        print('输入的数字不是水仙花数')


# 高级：
# 1.从控制台输入一个五位数，如果是回文数就打印“是回文数”，否则打印“不是回文数”
#  回文数: 对称的5位数
# 	例如：11111   12321   12221
num7 = int(input('请输入一个五位数：'))
the_unit1 = num7 % 10
tens1 = (num7 % 100) // 10
# hundreds1 = (num7 % 1000) // 100
kilobit1 = (num7 % 10000) // 1000
myriabit1 = num7 // 10000
if num7 < 10000 or num7 > 99999:
    print('输入错误')
else:
    if the_unit1 == myriabit1 and tens1 == kilobit1:
        print('是回文数')
    else:
        print('不是回文数')



# 预习内容：list、for循环
#









