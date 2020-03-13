import re
print re.search('foo', 'foobar')
print re.search('foo', 'barfoo')

print '\n'
print re.search('foo', 'waffles')

print '\n'
print re.match('foo', 'foobar')
#this line will fail because the characters 'bar' precede the match set 'foo'
print re.match('foo', 'barfoo')

#findall returns an array of matching sets from the search string
#the length of the array is the number of found instances
print '\n'
print re.findall('foo', 'foofoo')

print '\n regular expressions:\n'
#the '.' in the regular expression specifies a match for a single character
# the '+' specifies a match for one ore more characters
print re.findall('foo.+', 'foo foon foobar')
print re.findall('foo.?', 'foo foon foobar')
print re.findall('foo.', 'foo foon foobar')
print re.findall('foo*', 'foo foon foobar')
print re.findall('foo.*', 'foo foon foobar')

# regular expression can specify groups in the search set
# only characters matching the groups will be included in the output
print '\n'
print re.findall('f(o)+', 'foo foooooooo')
print re.findall('f(o)+', 'foo')

# what this expression is doing is looking for the set of characters "To: " in the search string, followed by anything
# the 'anything' is then grouped for the output, so everything that follows a match for 'To: ' will be output
# but the 'To: ' set itself will be omitted
print '\n'
print re.findall('To: (.+)', 'To: Bob Smith <bob@smith.com>')

print '\n'
print re.findall('To: (.+) <', 'To: Bob Smith <bob@smith.com>')
print re.findall('To: (.+) <(.*)>', 'To: Bob Smith <bob@smith.com>')

# logical paramters can be specified in groups to control matching queries
# the | is logical or, so the first line will output 'a' or 'b' characters when a match is found
# the second line uses brackets to specify an instance range
# an 'a' character will only be output when it matches a sequence of at least 2, but no more than 4
print '\n'
print re.findall('T(a|b)', 'To Ta Tb To Tb Ta')
print re.findall('T(a){2,4}','To Ta Taa Taaa')

print '\n'
print re.findall('^f[o]+', 'foo fooo')
print re.findall('f[o]+', 'foo fooo')
print re.findall('f[o]+$', 'foo fooo fo')