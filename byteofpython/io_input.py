def reverse(text):
	return text[::-1]

def is_palindrome(text):
	return text == reverse(text)

something = raw_input("Enter text: ")
new_something = something.translate(None, "[]{}:;/!@#$%^&*()_+-=?.,\'\"")
new_something = new_something.lower()
print '%s'%(new_something)
if is_palindrome(new_something):	# 회문 판별
	print 'Yes, it is a palindrome'
else:
	print 'No, it is not a palindrome'