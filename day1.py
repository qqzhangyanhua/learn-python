
# num = 10
# while num > 0:
#     print(num)
#     num -= 1
# else:
#     print("while循环结束")

# 只要是空的就是false，只要不是空的就是true
# print(bool(0))  # False
# print(bool(1))  # True
# print(bool(-1))  # True
# print(bool(0.0))  # False
# print(bool(0.1))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool([]))  # False
# print(bool([1]))  # True
# print(bool(()))  # False
# print(bool((1,)))  # True
# print(bool({}))  # False
# data =[]
# if bool(data):
#     print("不是空的")
# else:
#     print("是空的")

# s1 = "hello"
# s2 = '1111'
# s3 = '''1111'''
# s4 = '   \t\t\t\t\t\n 我的内容   \r\r\t\t\t\n'
# s5 = "hello\r \n world"
# # print(s1[0:2])
# # print(s1[-1])
# # print(s4.strip())
# s6 = s5.replace("\r", "").replace("\n", "").replace(" ", "")
# print(s6)
# list =['a','b','c','d','e','f','g','h','i','j']
# l =''.join(list)

# list2 =["\r","\n"," ","\t" ,'张三','\r','\n','\t','李四']
# s2 = ''.join(list2).replace("\r","").replace("\n","").replace("\t","")
# print(s2)

# name = "张三"
# s = "我叫%sadasdd" % name
# print(s)

# name = "张三"
# s= "我叫{0}，今年{1}岁了".format(name,18)
# print(s)

# name = "张三"
# s = f"我叫{name}，今年{18}岁了"
# print(s)

# list = ["张三", "李四", "王五",{"name":1}]
# print(list[0])
# print(list[3]['name'])


# list =['张三']
# print(list)
# list.append('李四')
# print(list)
# list.remove('张三')
# print(list)
# list.insert(0,'张三123')
# print(list)

# list =['aaaa']
# list2 =['bbbb']
# list.extend(list2)
# print(list)


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{j}*{i}={i*j}",end="\t")
#     print()

# list =['张三','李四','王五']
# for i in list:
#     print(i)

# obj ={
#         "name":"张三",
#         "age":18,
#   }
# print(obj['name'])
# v = obj.get('name33',123)
# print(v)  # 123

