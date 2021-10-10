Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def first(madam):
	return madam[0]

>>> def last(madam):
	return madam[-1]

>>> def middle(madam):
	return madam[1:-1]

>>> def is_palindrome(madam):
	if len(madam) <= 2 and word[0] == word[-1]:
		print('True')
	elif madam[0] == madam[-1]:
		is_palindrome(word[1:-1])
	else:
		print('False')

		
>>> is_palindrome(madam)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    is_palindrome(madam)
NameError: name 'madam' is not defined
>>> madam = str(raw_input('Is it palindromic?\Y'))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    madam = str(raw_input('Is it palindromic?\Y'))
NameError: name 'raw_input' is not defined
>>> 
================================ RESTART: Shell ================================
>>> from __future__ import print_function, division

>>> def first(word):
	return madam[0]

>>> 
================================ RESTART: Shell ================================
>>> from __future__ import print_function, division
>>> def first(word):
	return word[0]

>>> def last(word):
	return word[-1]

>>> def middle(word):
	return word[1:-1]

>>> def is_palindrome(word):
	if len(word) <= 1:
		return True
	if first(word) != last(word):
		return False
	return is_palindrome(middle(word))

>>> print(is_palindrome('allen))
		    
SyntaxError: EOL while scanning string literal
>>> print(is_palindrome('allen'))
False
>>> print(is_palindeome('madam'))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(is_palindeome('madam'))
NameError: name 'is_palindeome' is not defined
>>> print(is_palindrome('madam'))
True
>>> print(is_palindrome('civic'))
True
>>> print(is_palindrome('nana'))
False
>>> print(is_palindrome('ama'))
True
>>> 