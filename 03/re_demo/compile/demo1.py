import re


content1 = '2018-6-19 20:03'
content2 = '2018-6-20 22:00'
content3 = '2018-6-28 10:30'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)