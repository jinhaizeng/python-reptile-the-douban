# 本文件用于测试如何输出字符串中的指定内容
import re
str = "海绵宝宝:25"
cname = re.findall(r"(.+?)[\：\:]",str)
str1 = "".join(cname)
print(str1)

