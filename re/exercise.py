#  提取出一段文字中所有的日期(2019-05-23)
#  将日期打印出来,打印格式为2019/05/23

import re

s = 'sadf(2019-15-23)dsgdg(2019-15-23)sdaggh(2019-15-23)'
pattern = r'\d{4}-\d{2}-\d{2}'
l = re.findall(pattern,s)
for i in l:
    print(re.sub(r'-','/',i))