# Exercise-6.3
GIS 6345 assignment 6.3

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))

print(is_palindrome('allen))
		    
SyntaxError: EOL while scanning string literal

print(is_palindrome('allen'))
False
print(is_palindeome('madam'))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(is_palindeome('madam'))
NameError: name 'is_palindeome' is not defined
  
print(is_palindrome('madam'))
True
print(is_palindrome('civic'))
True
print(is_palindrome('nana'))
False
print(is_palindrome('ama'))
True
