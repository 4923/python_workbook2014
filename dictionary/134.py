# Exercise 134: Unique Characters
# 대소문자는 구분 하나?

# input
_str = input('Input your message: ').lower()
uniq_str = set(_str)
# output
print(f'characters "{_str}"" has {len(uniq_str)} unique characters.')