# Jaccard distance is the ratio of the intersection of two sets against their union
def jaccard(a,b):
    #given two strings, calculate the jaccard distance between the sets of their characters
    set_a = set(a)
    set_b = set(b)
    return float(len((set_a.intersection(set_b))))/float(len(set_a.union(set_b)))


string1 = "hello world"
string2 = "wello horld"
print jaccard(string1, string2)

string1 = "hello world"
string2 = "foo foobar"
print jaccard(string1, string2)

#the following text is sampled from Collin's http_example.txt in the source_files directory
string1 = '10.16.94.206 - - [18/Sep/2016:05:57:16 -0400] "GET /helpnew/faq/faq_simple_zh_CN.jsp HTTP/1.1" 404 437 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"'
string2 = '10.16.94.206 - - [18/Sep/2016:05:57:16 -0400] "GET /ymail/images/index_r1_c4.jpg HTTP/1.1" 404 433 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36"'
print jaccard(string1, string2)