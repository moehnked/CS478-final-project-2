#SECTION:
#Manipulating Delimiters



from string import maketrans

#this python module 'maketrans' essentially accomplishes the same task as the tr command in a function
print('dog cat god'.translate(maketrans('dog', 'bat')))

print('\n')


print '|'.join(filter(bool, 'a||b|c'.split('|')))