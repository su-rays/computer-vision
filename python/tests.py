# data = [10, 20, 30, 40, 50]

# while (n := len(data)) > 0:
#     print(n)
#     data.pop()

# print(data)

# from functools import partial

# def sdd(n1, n2, n3, n4):
#     return n1+n2+n3+n4

# res = partial(sdd, 2, 3, 4)
# print(res(6))

def check(*data):
    print(len(*data))

check(input("enter the datas: ").split())