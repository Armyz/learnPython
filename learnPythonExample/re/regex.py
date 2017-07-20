# coding=utf-8

import re

fd_read = open("test.txt", "r")
fd_write = open("test-regex.txt", "w")

read_lines = fd_read.readlines()

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
