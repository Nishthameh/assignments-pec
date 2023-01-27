my_str = str(input('Please enter the string:'))

my_str1 = my_str.replace(' ', '')
low1 = my_str1.lower()
lis1 = list(low1)
lis2 = ''.join(lis1)
rev_list = reversed(lis2)
if list(lis2) == list(rev_list):
    print(my_str, 'is a Palindrome.')
else:
    print(my_str, 'is not a Palindrome.')