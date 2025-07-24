# print("Welcome to the guess the number game")
# print("im thinking of a number between 1 and 100. can you guess what it is?")
# print("you have 7 attempts to guess correctly")
# # Generate the random number
# secret_number = (random.randint(1, 100))
# #maximum number of guesses
# max_attempts = 7
# attempts = 0
# # start guessing loop
# while True:
#     guess = input("Enter your guess: ").capitalize()
#     guess = int(guess)
# if secret_number == 99:
#     print("Your guess is too low. guess again")
# elif guess > secret_number:
#     print("Your guess is too high. guess again")
# else: 
#     print(f"Congratulations! you guessed the number correctly in {attempts} attempts(s)!")
#     break
# else:
# print(f"Sorry, you have run out of attempts. the correct number was {secret_number}. better luck next time!")
# import random
# print(random.randint(1,20))

# import random python checkpoint
# secret_number = random.randint(1, 100)
# print(secret_number)

# while True:
#     user_number = int(input("Enter the secret number: "))
#     if user_number == secret_number:
#         print("you guess the secret_number right 👌")
#         break
#     elif user_number > secret_number:
#         print("Too high 🤣")
#     else:
#         print("Too low 😒")


#python data structure are four(4):
#1. list, 2. dictionary, 3. Tuple, 4. set
#list is ordered, and changable (mutable)

#my_list = [1, 2, 3, 4, "orange", "pawpaw", 23.0, True, [6,7, [1, 2, 3, 4, 5, 6]]]
#print(my_list)     #ordered list retains its order
#list indexing numbers counts from o t0 10
# print(my_list[3])   #forsingle indexing
# print(my_list [8])
#list slicing is used to select couple of items from the list
# print(my_list [2:5])
#print(my_list [6:9])
#use append is used to add a single items to a list
# my_list.append("Orange")
# my_list.append("mango")

#use insert to add an item at a specified position(index) in a list
#example:my_list = [10,20,30]
#my_list.insert(1, 10) #inserts 15 at index 1
#print(my_list) output:[10,15,20,30]
# my_list.insert(0, "Mango")

# #pop is used to remove and return an item from a data structure at the end of the list
# my_list.pop()
# print(my_list)
# #remove is used to remove an item at the a particular index on the list

# my_dict = {"name": "Brianna", "age": 20, "class": "ss1"}
# print(my_dict ["name"])
# print(["age"])
# print(["class"])

#change previously assigned values in dict


#use key function to get all the keys
# the values

#set is not oredered and unindexed collection on items, it only allows you to store unique 
#items, it doesnt allow duplicates of items
#my_set1 = {"orange", "mango", "pawpaw"}
#my_set2 = {"orange", "apple", "pineapple"}
# print(my_set1.difference(my_set2))
# print(my_set2.difference(my_set1))

#print(my_set2.intersection(my_set1)) #to intersect the items in two variables or items
#print(my_set1.union(my_set2))
#print(my_set2.symmetric_difference(my_set1))

#a tuple is ordered but not changable; oncde a tuple is created, ypu cnt add items to it
#except you go back to reassigned it.
#my_tuple = ("a", "b", "c")

