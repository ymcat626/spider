# coding: utf-8

import re


content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\s\w+\s\w', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
