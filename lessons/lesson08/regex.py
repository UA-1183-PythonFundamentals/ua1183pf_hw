import re

text = "IT Academy SoftServe"

result_1 = re.match("IT", text)
result_2 = re.match("Soft", text)
print(result_1)
print(result_1.group(0))
print(result_2)

result_1 = re.search("IT", text)
print(result_1)
print(result_1.group(0))

result_1 = re.findall("[abcdef]", text)
print(result_1)


text = "IT Academy SoftServe 27 193 ad133 22"

result_1 = re.findall("\d", text)
print(result_1)
result_1 = re.findall("\d{2}", text)
print(result_1)