#Section:
#Unicode, UTF, and ASCII

#one key difference is that python 3 does not support implicit hexadecimal to integer conversions
#in the book, Collins begins this code segment with an input of 4E09, which is the hex equivalent of 19977
#python 3 interprets that as a float, and a cast to int results in an unsigned int outside of the index range for the unichr function
s = unichr(19977)
print(s)
print(unichr(19977))

#
print(type(s))
#python 3 seems to use utf-8 natively
print(s.encode('utf-8'))

s = u'a'
print s

print (s.encode('utf-8'))

print(ord(s))
