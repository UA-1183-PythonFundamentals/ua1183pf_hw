# doubled_odds = [n * 2 for n in range(10) if n % 2 == 1]
# print(doubled_odds)
# doubled_odds = {n * 2 for n in range(10) if n % 2 == 1}
# print(doubled_odds)
# doubled_odds = {n:n * 2 for n in range(10) if n % 2 == 1}
# print(doubled_odds)

# doubled_odds = (n * 2 for n in range(10) if n % 2 == 1)
# print(doubled_odds)
# print(next(doubled_odds))
# print(next(doubled_odds))
# print(next(doubled_odds))
# print(next(doubled_odds))
# print(next(doubled_odds))
# # print(next(doubled_odds))

# vec1 = [3, 10, 2, -1]
# vec2 = [-20, 5, 1]
# print(zip(vec1, vec2))
# print(list(zip(vec1, vec2)))
# print(list(zip(vec1, vec2, vec1)))

# m = map(int, "123456")
# print(m)
# print(list(m))


# name_str = "Liubov"


# i = iter(name_str)

# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break

# for i in name_str:
#     name_str +=i
#     print(name_str, i)



# class MyRange:

#     def __init__(self, start, stop=None, step=1):
#         if stop == None:
#             self.start = 0
#             self.stop = start
#         else:
#             self.start = start
#             self.stop = stop
#         self.step = step

#     def __iter__(self):
#         self.current = self.start
#         return self
#     def __next__(self):
#         if self.current <= self.stop:
#             x = self.current
#             self.current += 1
#             return x
#         else:
#             raise StopIteration
        
#     def __repr__(self) -> str:
#         return f"Range({self.start},{self.stop},{self.step})"
    

# r1 = MyRange(10)
# r2 = MyRange(-3,5)
# r3 = MyRange(7,12,2)
# print(r1)
# print(r2)
# print(r3)

# for i in r1:
#     print(i)
# print(">"*10)
# for i in r2:
#     print(i)
# print(">"*10)
# for i in r3:
#     print(i)

# l1 = []
# l2 = []
# for i in range(6):
#     l1 = [x for x in range(10**i)]
#     l2 = (x for x in range(10**i))
#     print(i, l1.__sizeof__())
#     print(i, l2.__sizeof__())

from logers import loger

@loger
def get_numbers(n):
    return list(range(10))

print(get_numbers(5))

print(get_numbers)


# def get_numbers():
#     print("text1")
#     yield 1
#     print("text2")
#     yield 2
#     print("text3")
#     yield 3
#     print("text4")
#     yield 4
#     return "texte"

# g = get_numbers()
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def get_numbers(n):
    number = 0
    while number < n:
        yield number
        number += 1
@loger
def get_all_users(_from, _to):

    sql = f"""
    SELECT * From Users limit {_from}, {_to} ;
    """
    print(sql)

_from, _to = 0, 50
while True:
    if _to > 1000:
        break
    get_all_users(_from,_to)
    _from, _to = _to, _to +50
@loger
def get_all_users():
    _from, _to = 0, 50
    while True:
        if _to > 1000:
            break
        sql = f"""
        SELECT * From Users limit {_from}, {_to};
        """
        yield sql
        _from, _to = _to, _to +50


users = get_all_users()
for s in users:
    print(s)

