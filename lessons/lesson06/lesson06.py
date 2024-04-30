# # list
# l = list()
# print(type(l), l)
# l = list("gasvdjhasvjgd")
# print(type(l), l)
# l = list((1,2,"str", 1.5, None))
# print(type(l), l)
# # l = list(12) #TypeError: 'int' object is not iterable
# l = list(range(15))
# print(type(l), l)
# # l = list(range(1000))
# # print(l.__sizeof__())
# # r = range(1000)
# # print(r.__sizeof__())
# # i = r.__iter__()
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# # print(next(i))
# l = list({15})
# print(type(l), l)

# l = []
# print(type(l), l)
# l = ["bsdjkgkdf"]
# print(type(l), l)
# l = ["bsdjkgkdf", 1, None, [12, 15], (15,55)]
# print(type(l), l)
# print(l[0][2])
# print(l[1:8:2])
# print(l[::-1])
# print([1,2,3] + [19,8,7])
# # print([1,2,3] + 1)#TypeError: can only concatenate list (not "int") to list
# # print([1,2,3] + (1,2,3))#TypeError: can only concatenate list (not "tuple") to list
# print([1,2,3]*5)
# print([0]*20)
# l = [1, 2, 3, 19, 8, 7, [99, 88]]
# print(l)
# l[5] = 155
# print(l)
# # l[55] = 155 #IndexError: list assignment index out of range

# print(19 in l)
# print(99 in l)
# print([99, 88] in l)

# k = [1, 2, 3, 19, 8, 155, [99, 88]]
# print(id(l), l)
# print(id(k), k)
# print(l == k)
# k = [[99, 88], 1, 2, 3, 19, 8, 155]
# print(id(l), l)
# print(id(k), k)
# print(l == k)
# print(dir(list))
# print(list(method for method in dir(list) if not method.startswith("_")))
# l=[1,2,3]
# print(id(l), l)
# l.append(1)
# print(id(l), l)
# l.append([1,2,3,4,5])
# print(id(l), l)
# # l.extend(15) #TypeError: 'int' object is not iterable
# l.extend([1,2,3,4,5]) 
# print(id(l), l)
# l.clear()
# print(id(l), l)
# l = []
# print(id(l), l)
# k = [1,2,3]
# t = [10,20,30]
# l = ["a", "B", k, t]
# print(k, t, l)
# k.clear()
# t = []
# print(k, t, l)
# ll = l.copy()
# print(id(l), l)
# print(id(ll), ll)
# l[0] = 10
# ll[3][1] = 999
# print(id(l), l)
# print(id(ll), ll)
# from copy import deepcopy

# lll = deepcopy(l)
# l[1] = "SS"
# ll[2].append(999)
# print(id(l), l)
# print(id(ll), ll)
# print(id(lll), lll)
# # del lll
# # print(lll)
# print(l.count(10))
# print(l.count([999]))
# print(l.count([]))
# l.append([999])
# print(l)
# # print(l.index([777]))#ValueError: [777] is not in list
# print(l.index([999]))
# print(l.index([999], l.index([999])+1))

# from random import randint
# l = [randint(0, 10) for i in range(20)]
# print(l)
# s = set(l)
# for i in s:
#     count = l.count(i)
#     index = None
#     print(i)
#     while count:
#         index = l.index(i, 0 if index is None else index+1)
#         print("\t", index)
#         count -=1
# l = [1, 9, 2, 7, 3, 1, 8, 5, 4, 3, 0, 8, 4, 0, 7, 4, 5, 1, 7, 1]
# print(l)
# l.insert(3,"test")
# l.insert(3333,"test")
# l.insert(-5,"SSS")
# l.insert(-55,"SSS")

# print(l)
# p = l.pop()
# print(p, l)
# p = l.pop()
# print(p, l)
# p = l.pop(2)
# print(p, l)
# l.remove(1)
# print( l)
# # l.remove(111) #ValueError: list.remove(x): x not in list
# l.reverse()
# print(l)
# r = reversed(l)
# print(list(r))
# print(l)
# l.sort(key=lambda e: e if type(e) is int else 999)
# print(l)

#tuple

# t = tuple()
# print(type(t), t)
# t = tuple("test")
# print(type(t), t)
# t = ()
# print(type(t), t)
# # t = (1)#<class 'int'> 1
# t = (1,)
# print(type(t), t)
# t = (1,2,3,4,[1,2,3])
# print(type(t), t)
# print(t[2])
# # t[2]=33 #TypeError: 'tuple' object does not support item assignment
# t[4].append(999)
# print(type(t), t)
# print(list(method for method in dir(tuple) if not method.startswith("_")))

# from random import randint
# l = [randint(-99999, 99999) for i in range(30000)]
# t = tuple(l)
# print(type(t), t.__sizeof__())
# print(type(l), l.__sizeof__())


## set

# s = set()
# print(type(s), s)
# s = set("favsdvsacdfsacdgfcsadhgsaghdah")
# print(type(s), s)
# s = {1,2,4,23,3,56,7,3,32,21,3,3,54,5,4,4,4}
# print(type(s), s)
# s = {} #<class 'dict'> {}
# print(type(s), s)

# print(list(method for method in dir(set) if not method.startswith("_")))
# s = {1,2,3,4}
# s.add(55)
# s.add(55)
# s.add(55)
# s.add((1,2,3))
# print(type(s), s)
# print(s.pop(), s)
# s.remove(4)
# print( s)
# s.update({1,2,3,4})
# print( s)


## dict

# d = dict()
# print(type(d), d)
# # d = dict( "svkjdbvjhdf")#ValueError: dictionary update sequence element #0 has length 1; 2 is required
# d = dict([(1,2), ("key", "value")])
# print(type(d), d)
# d = {}
# print(type(d), d)
# d = {
#     "key":"value",
#     "ke2":"value1",
#     99:"value",
# }
# print(type(d), d)

# d["key"] = [1,2,3]
# d[99] = {1:1, 2:"test"}
# print(d)
# from pprint import pprint

# pprint(d, width=2)
# # d[11] #KeyError: 11
# d['oo'] = 99
# pprint(d, width=2)
# from pprint import pprint
# print(list(method for method in dir(dict) if not method.startswith("_")))

# d = {
#     "key":"value",
#     "ke2":"value1",
#     99:"value",
# }
# pprint(d, width=1)

# print(d["ke2"])
# print(d.get("ke2"))
# print(d.get("ke3"))
# print(d.get("ke4", 999))
# # p = d.pop()#TypeError: pop expected at least 1 argument, got 0
# p = d.pop("key")
# print(p)
# pprint(d, width=1)
# d.update({
#     "key44":"value",
#     "ke24":"value1",
#     99:777,
# })
# pprint(d, width=1)
# print(d.keys())
# print(d.values())
# print(d.items())
# print("ke2" in d)
# print("errr" in d)

# for key in d:
#     print(key, d[key])


# a, b = 1, 2

# for e in d.items():
#     print(e)
# for key, value in d.items():
#     print(key, value)


# l = []
# for i in range(10):
#     l.append(i**3)
# print(l)
# l = [i**3 for i in range(10)]
# print(l)
# l = []
# for i in range(10):
#     v = i**3
#     if v%5:
#         l.append(i**3)
# print(l)
# l = [i**3 for i in range(10) if (i**3)%5]
# print(l)
l = []
for i in range(5):
    for j in range(i, 5):
        if (i+j) %2:
            l.append((i,j))
        # else:
        #     print((i,j))
        
print(l)

l = [(i, j) for i in range(5) for j in range(i, 5) if (i+j) %2 ]
print(l)
l = {x for x in "test"}
print(l)
l = {x : x*2 for x in "test"}
print(l)

l = ((i, j) for i in range(5) for j in range(i, 5) if (i+j) %2 )
print(l)
