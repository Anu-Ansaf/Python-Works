import random

s = 'abcdefghijklmnpoqrstuvwxyz1234567890ABCDEFGHIJKLMNPOQSRTUVWXYZ!@#$%^&*()_+'

LengthOfPass = 10
p = ''.join(random.sample(s, LengthOfPass))
print("Your Password is : " + p)
