import random

s = 'abcdefghijklmnpoqrstuvwxyz1234567890ABCDEFGHIJKLMNPOQSRTUVWXYZ!@#$%^&*()_+'

LengthOfPass = 14
p = ''.join(random.sample(s, LengthOfPass))
print("Your Password is : " + p)
print("Password Length of :" +  str(LengthOfPass))
