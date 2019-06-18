"""
match 对象使用示例
"""

import re

pattern = r'(ab)cd(?P<pig>ef)'
regex = re.compile(pattern)
obj = regex.search('abcdefghi')  # match对象

#  属性变量
print(obj.pos)  #  匹配的目标字符串开始位置
print(obj.endpos)  #  匹配的目标字符串结束位置
print(obj.re)  #  正则表达式
print(obj.string)  #  目标字符串
print(obj.lastgroup)  #  最后一组的名称
print(obj.lastindex)  #  最后一组的序号

#  属性方法
print(obj.span())  #  获取匹配内容在目标字符串中位置
print(obj.start())
print(obj.end())
print(obj.groupdict())  #  获取捕获组字典,组名为键,对应内容为值
print(obj.groups())  #  获取子组对应内容
print(obj.group(1))
print(obj.group(2))
print(obj.group('pig'))  #  获取匹配内容
