items=[n for n in input('Please enter the list: ').split('-')]
items.sort()
print('-'.join(items))