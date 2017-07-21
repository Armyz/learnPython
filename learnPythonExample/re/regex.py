# coding=utf-8

import re

fd_read = open("test.txt", "r")
fd_write = open("test-regex.txt", "w")

read_lines = fd_read.readlines()

# 匹配指定字符
print("以下是固定字符串")
for line in read_lines:
    ret = re.match("itcast", line)
    if ret is not None:
        print(ret.group())

# 找出手机号
print("以下是手机号")
for line in read_lines:
    ret = re.match("([0-9]){11}", line)
    if ret is not None:
        print(ret.group())

print("找出GET请求目录资源")
for line in read_lines:
    ret = re.search("\s/[\w.]*\s", line)
    if ret is not None:
        print(ret.group(0))

# 匹配正确的163/qq/邮箱
print("以下是163/qq邮箱号")
for line in read_lines:
    ret = re.match("\w{4,20}@(163|qq)\.com$", line)
    if ret is not None:
        print(ret.group())

# 匹配正确的html格式字符串  \1表示匹配到的第一个分组中字符串()内的内容为一个分组
# 以‘<’开头‘>’结尾
print("匹配html格式字符串")
for line in read_lines:
    ret = re.match(r"^<([A-Za-z]+)>.*</\1>$", line)
    if ret is not None:
        print(ret.group())

print("匹配<><>*</></>格式字符串,使用分组方法")
for line in read_lines:
    ret = re.match(r"^<(\w+)><(\w+)>.*</\2></\1>$", line)
    if ret is not None:
        print(ret.group())
print ("匹配<><>*</></>格式字符串,使用分组启别名方法")
for line in read_lines:
    ret = re.match(r"^<(?P<name1>\w+)><(?P<name2>\w+)>.*</(?P=name2)></(?P=name1)>$", line)
    if ret is not None:
        print(ret.group())


for line in read_lines:
    regex_return = re.sub(r"</?\w+>|&nbsp;", "", line)
    # print(regex_return)
    fd_write.writelines(regex_return)

fd_write.write("\n\n图片网址搜索：")
for line in read_lines:
    # ?关闭贪婪模式
    regex_return = re.search(r"(https.+?\.jpg)", line)
    # print(regex_return)
    if regex_return is not None:
        print(regex_return.group())
        fd_write.writelines(regex_return.group())

fd_write.write("\n\n网址匹配：\n")
for line in read_lines:
    # ?关闭贪婪模式
    regex_return = re.match(r"(^http.*\.(com|cn)/)", line)
    # print(regex_return)
    if regex_return is not None:
        print(regex_return.group())
        fd_write.writelines(regex_return.group())
        fd_write.write("\n")


