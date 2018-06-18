# coding: utf-8

import re


content = 'Hello 123 4567 World_This is a Regex Demko'
print(len(content))
result = re.match('^Hello\s\d{3}\s\d{4}\s\w{5}', content)
print(result.group())
print(result.span())
