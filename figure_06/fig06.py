#SECTION:
#Hamming Distance

def hamming(a,b):
    if len(a) == len(b):
        return sum(map(lambda x:1 if x[0] == x[1] else 0, zip(a,b)))
    else:
        return Exception, "strings of different length"

str1 = "hello world"
str2 = "mellow weld"
print hamming(str1, str2)

# between the two string variables, there are 3, space delimited, strings
# they are 'dog', 'cat', and 'bat'
# the hamming value is then 3
str1 = "dog cat"
str2 = "cat bat"
print hamming(str1, str2)