# Exercise 1 Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
sentence = 'Cualquier tecnología lo suficientemente avanzada es indistinguible de la magia'
number = 314
list = ['lagarto','gecko','salamandra']
boolean = True


# Exercise 2 - Use an index to grab the first 3 letters in your string, store that in a variable.
first_3_letters = sentence[0:3]
#print(first_3_letters)


# Exercise 3 - Use an index to grab the first element from your list.
list[0]
#print(list[0])


# Exercise 4 - Create a new number variable that adds 10 to your original number.
new_number = number + 10
#print(new_number)


# Exercise 5 - Use an index to get the last element in your list.
list[-1]
#print(list[-1])


# Exercise 6 - Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'
names = names.split(',')
#print(names)


# Exercise 7 - Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
first_word = sentence[0:sentence.index(' ')]
rest_of_sentence= sentence[sentence.index(' '):]
new_sentence = first_word.upper() + rest_of_sentence
#print(new_sentence)


# Exercise 8 - Use string interpolation to print out a sentence that contains your number variable.
print(f'My favorite number is: {number}')


# Exercise 9 - Print “hello world”.
print('hello world')
