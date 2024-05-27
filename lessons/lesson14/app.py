# file = open('data.txt')
# print(file.read())
# file.close()

# file = open('data.txt', "w")
# print(file.readable())
# file.close()

# file = open('data.txt')
# print(file.tell())
# print(file.readable())
# print(file.readline())
# print(file.tell())
# print(file.readlines())
# # print(file.readable())

# print(dir(file))
# file.close()
# import openpyxl

# xl_obj = openpyxl.load_workbook("data2.xlsx")
# sheet = xl_obj.active
# # print(sheet)
# print(sheet.max_column)
# print(sheet.max_row)

# for i in range(1, sheet.max_row+1):
#     for j in range(1, sheet.max_column+1):
#         print(sheet.cell(row=i, column=j).value, end="\t")
#     print()


# for c1, c2, c3 in sheet["A1": "C9"]:
#     print(c1.value, c2.value, c3.value)
from user import User

# file = open('data.txt')
# for row in file:
#     print(row)
# file.close()

USERS = []
with open('data.txt') as file:
    for row in file:
        user = User(*(row.split(",")))
        USERS.append(user)
print(USERS)
with open('data.txt', "a") as file:
    user = User("99", "L", "test@gmail.com","25", "Ukr")
    file.write(user.get_csv_format())



