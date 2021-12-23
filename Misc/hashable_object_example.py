'''
  Example of hash function for custom object (hashable)
  
  Written by Gabriel Heberle
  Developed by https://zetcode.com/python/hashing/#:~:text=Python%20hash()%20function,the%20__hash__()%20method.

'''

# class User:
#     def __init__(self, name, occupation):
#         self.name = name
#         self.occupation = occupation

# u1 = User('John Doe', 'gardener')
# u2 = User('John Doe', 'gardener')

# print('hash of user 1')
# print(hash(u1))

# print('hash of user 1')
# print(hash(u2))

# if u1==u2:
#     print('same users')
# else:
#     print('different users')

val1 = 'eaf514gtr'
val2 = 'eaf514gtr'

print('hash value for val1')
print(hash(val1))
print('hash value for val2')
print(hash(val2))

print('new hash value for val1')
print(hash(val1)+1)
print('new hash value for val2')
print(hash(val2)-1)
