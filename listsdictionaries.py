#simple list operations
print('creating a list')
slang = ['cheerio', 'pip pip', 'smashing', 'yonks', 'knackered']

#adding and printing elements
print(slang[1])
slang.append('cheeky')
print(slang[1:-1])

#remove element
slang.remove('knackered')
del slang[4]
print(slang)


#simple dictionary operations
print('\ncreating a dictionary')
slangdefine = {'cheerio':'goodbye', 'yonks':'ages', 'knackered':'tired'}
print(slang)

#print value using key
print(slangdefine['cheerio'])

#add/update element to dictionary
slangdefine['smashing'] = 'terrific'
print(slangdefine)

#delete element/item
del slangdefine['smashing']
print(slangdefine)

#get item if exists in the dictionary
result = slangdefine.get('bloody')
result is None

if result:
    print(result)
else:
    print('Key doesnt exist')

