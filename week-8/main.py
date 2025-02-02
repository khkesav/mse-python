# Factorial

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(4))

# number = [2, 3, 4, 5]
 
# factorials = [1 if n == 0 else (f := 1, [f := f * i for i in range(1, n + 1)], f)[-1] for n in number]
# print(factorials)

keys = ['a', 'b', 'c']
values = [1, 2, 3]
# print( tuple(zip(keys, values)) )
dictionary = { k: v for k, v in zip(keys, values)}
print(dictionary)

dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged_dict = { **dict1, **dict2 }
print(merged_dict)
  