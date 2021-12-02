import re
# 1.提取python
key = 'javapythonc++c'
a = re.findall('python',key)[0]
print(a)
# 2.提取hello world
key = '<html><h1>hello world<h1></html>'
b = re.findall('<h1>(.*)<h1>',key)[0]
print(b)
# 3.提取170
str = '我喜欢170的女孩'
c = re.findall('\d+',str)[0]
print(c)
# 4.提取hello
# 输出<hTml>hello</HtML>
key = 'lalala<hTml>hello</HtML>hahaha'
d = re.findall('<[hH][Tt][mM][lL]>(.*)</[hH][Tt][mM][lL]>',key)[0]
print(d)
# 5.匹配sas和saas
key = 'saas and sas and saas'
e = re.findall('sa{1,2}s',key)
print(e)