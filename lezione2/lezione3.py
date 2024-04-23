#4-1. Pizzas: Think of at least three kinds of your favorite pizza.
#Store these pizza names in a list, and then use a for loop to print the name of each pizza.
#• Modify your for loop to print a sentence using the name of the pizza,
#instead of printing just the name of the pizza.
#For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
#• Add a line at the end of your program, outside the for loop, 
#that states how much you like pizza. 
#The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, 
#such as I really love pizza!

favourite_pizza : list = ("diavola", "patate e tartufo", "bufala")

for n in favourite_pizza:

    print(n)

for n in favourite_pizza:

    print(f"mi piace questa pizza: {n}")

print(f"mi piace davvero tanto {favourite_pizza[0]}, anche {favourite_pizza[1]} e per finire anche {favourite_pizza[2]}") 


#4-2. Animals: Think of at least three different animals that have a common characteristic.
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. 
#You could print a sentence, such as Any of these animals would make a great pet!


animals_list : list = ("cat", "fish", "dog")

for n in animals_list:
    
    print(n)

for n in animals_list:

    print(f"{n} sono davvero belli")

    print(f"")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive
print("this loop print all numbers from n to n")
number : int = int(input("inserisci un numero"))

for n in range(1, number +1) :
    print(n)


#4-4. One Million: Make a list of the numbers from one to one million,
#and then use a for loop to print the numbers.
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

#number= list(range(1,1000001))
#for n in number:

# print(n)


#4-5. Summing a Million: Make a list of the numbers from one to one million,
#and then use min() and max() to make sure your list
#actually starts at one and ends at one million. Also, 
#use the sum() function to see how quickly Python can add a million numbers.

number = list(range(1,1000001))
x = min(number)
print(f"questo è il minimo {x}")
y = max(number)
print(f"questo è il massimo {y}")
z = sum(number)
print(z)

#4-6. Odd Numbers: Use the third argument of the range() function to make 
#a list of the odd numbers from 1 to 20. 
#Use a for loop to print each number.

number_list = [number for number in range(1, 20, 2)]
for n in number_list:
    print(n)


#4-7. Threes: Make a list of the multiples of 3, from 3 to 30.
#Use a for loop to print the numbers in your list.

number_list = [number for number in range(3, 31, 3)]
for n in number_list:
    print(n)



#4-8. Cubes: A number raised to the third power is called a cube.
#For example, the cube of 2 is written as 2**3 in Python.
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
#and use a for loop to print out the value of each cube.


#number_list = [number**3 for number in range(1, 10)]

for number in range(1,10):
    number_list.append(number**3)
for n in number_list :
    print(n)

#4-9. Cube Comprehension: 
#Use a list comprehension to generate a list of the first 10 cubes.

number_list = [number**3 for number in range(1, 10)]

for n in number_list :
    print(n)



#4-10. Slices: Using one of the programs you wrote in this chapter,
#add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:.
#Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. 
#Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:.
#Then use a slice to print the last three items in the list.


number_list = list(range(1,30))

print(f"primi tre numeri: {number_list[:3]}\n",
      f"tre elementi al centro della lista sono: {number_list[len(number_list)//2-2]}",
      f"gli ultimi tre elementi sono: {number_list[-3]}\n")

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1.
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#• Add a new pizza to the original list.
#• Add a different pizza to the list friend_pizzas.
#• Prove that you have two separate lists.
#Print the message My favorite pizzas are:,
#and then use a for loop to print the first list. 
#Print the message My friend’s favorite pizzas are:,
#and then use a for loop to print the second list. 
#Make sure each new pizza is stored in the appropriate list.

favorite_pizza : list = ["margherita", "fiori di zucca", "marinara"]

friend_pizza : list = ["margherita", "fiori di zucca", "marinara"]

favorite_pizza.append("cacio e pepe")
print(favorite_pizza)
friend_pizza.append("napoli")
print(friend_pizza)

for n in favorite_pizza :
    print(f"my favorite pizza are: {n}")

for n in friend_pizza :
    print(f"la pizza preferita del mio amico è : {n}")




#4-12. More Loops: All versions of foods.py in this section have avoided using
#for loops when printing, to save space. 
#Choose a version of foods.py, and write two for loops to print each list of foods.





#4-14. PEP 8: Look through the original PEP 8 style guide at
#https://peps.python.org/pep-0008/ You won’t use much of it now, 
#but it might be interesting to skim through it.




#4-15. Code Review:Choose three of the programs you’ve written 
#in this chapter and modify each one to comply with PEP 8.




#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
#describing each test and your prediction for the results of each test. Your code
#should look something like this:
#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')
#• Look closely at your results, and make sure you understand why each line
#evaluates to True or False.
#• Create at least 10 tests. Have at least 5 tests evaluate to True and another
#5 tests evaluate to False.


counter: int = 0
while couter < 10:
    car: str = input("inserisci una macchina")
    
    if car == "fiat" :
        print("is car == 'fiat'? I predict false")
        print(car == "fiat")

    elif car == "bugatti" :
        print("is car == 'bugatti'? I predict true")
        print(car == "bugatti")

    elif car == "audi" :
        print("is car == 'audi'? I predict false")
        print(car == "audi")
    
    else :
        print("non è presente questa macchina")

        counter +=1 
 


#5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
#ate to 10. If you want to try more comparisons, write more tests and add them
#to conditional_tests.py. Have at least one True and one False result for each of
#the following:
#• Tests for equality and inequality with strings
#• Tests using the lower() method
#• Numerical tests involving equality and inequality, greater than and less
#than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
#• Test whether an item is in a list
#• Test whether an item is not in a list

#ora possono essere effettuati diversi test perchè il counter viene inserito da tastiera
n: int = int(input("inserisci un numero"))
counter: int = 0
while n>counter:
    car: str = input("inserisci una macchina")
     
     if car == "fiat" :
        print("is car == 'fiat'? I predict false")
        print(car == "fiat")

    elif car == "bugatti" :
        print("is car == 'bugatti'? I predict true")
        print(car == "bugatti")

    elif car == "audi" :
        print("is car == 'audi'? I predict false")
        print(car == "audi")
    
    else :
        print("non è presente questa macchina")

        counter +=1 
    

#5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
#Create a variable called alien_color and assign it a value or 
#'green', 'yellow', or 'red'.
#• Write an if statement to test whether the alien’s color is green.
#If it is, print a message that the player just earned 5 points.
#• Write one version of this program that passes the if test and another that fails. 
#(The version that fails will have no output.)

alien_color: str = input("inserisci colore alieno tra 'yellow, green and red'")

if alien_color == "green":
    print("the player earned 5 points")


#5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3,
#and write an if-else chain.
#• If the alien’s color is green,
#print a statement that the player just earned 5 points for shooting the alien.
#• If the alien’s color isn’t green, 
#print a statement that the player just earned 10 points.
#• Write one version of this program that runs the if block and
#another that runs the else block.

alien_color: str = input("inserisci colore alieno tra 'yellow, green and red'")

if alien_color == "green":
    print("the player earned 5 points for shoting the alien")
else :
    print("the player just earned 10 points")

#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4into an if-elif-else chain.
#• If the alien is green, print a message that the player earned 5 points.
#• If the alien is yellow, print a message that the player earned 10 points.
#• If the alien is red, print a message that the player earned 15 points.
#• Write three versions of this program,
#making sure each message is printed for the appropriate color alien.

alien_color: str = input("inserisci colore alieno tra 'yellow, green and red'")

if alien_color == "green":
    print("the player earned 5 points for shoting the alien")
elif alien_color == "yellow" :
    print("the player just earned 10 points")
else :
    print("the player just earned 15 points")    



#5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. 
#Set a value for the variable age, and then:
#• If the person is less than 2 years old, print a message that the person is a baby.
#• If the person is at least 2 years old but less than 4,
#print a message that the person is a toddler.
#• If the person is at least 4 years old but less than 13,
#print a message that the person is a kid.
#• If the person is at least 13 years old but less than 20,
#print a message that the person is a teenager.
#• If the person is at least 20 years old but less than 65, 
#print a message that the person is an adult.
#• If the person is age 65 or older, print a message that the person is an elder.

n: int = int(input("inserisci l'eta"))

if n<2:
    print("the person is a baby")

elif n<4:
    print("the person is a toddler")

elif n<13:
    print(" the person is a kid")

elif n<20:
    print("the person is a teenager")

elif n<66:
    print("the person is an adult")

else:
    print("the person is an elder")        


#5-7. Favorite Fruit: Make a list of your favorite fruits, 
#and then write a series of independent if statements that check for certain fruits in your list.
#• Make a list of your three favorite fruits and call it favorite_fruits.
#• Write five if statements. Each should check whether a certain kind of fruit is in your list.
#If the fruit is in your list, 
#the if block should print a statement, such as You really like Apples!

favorite_fruits: list= ["apple" , "ananas" , "peach"]
fruit : str = input("inserisci la frutta da controllare")

if favorite_fruits[0]== fruit :
    print(f"such as you i really like {favorite_fruits[0]}")

elif favorite_fruits[1]== fruit :
    print(f" such as yuo i really like{favorite_fruits[1]}")

else :
    print(f"such as yuo i really like {favorite_fruits[2]}")


#5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
#Imagine you are writing code that will print a greeting to each 
#user after they log in to a website. Loop through the list, and print a greeting to each user.
#• If the username is 'admin', print a special greeting, such as Hello admin, 
#would you like to see a status report?
#• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.

username_list : list= ["admin" , "user01" , "user02"]

for n in username_list :

    if n== "admin":
        print(f"hello {n} would you like to see a status report")

    else :
        
        print(f" hello {n}, thank you for logging")

#`5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.

username_list : list= ["admin" , "user01" , "user02"]

if len(username_list)!= 0 :

    print("the list is not empty")

else:
    print("we need to find some users")



#5-10. Checking Usernames: Do the following to create a program 
#that simulates how websites ensure that everyone has a unique username.
#• Make a list of five or more usernames called current_users.
#• Make another list of five usernames called new_users. 
#Make sure one or two of the new usernames are also in the current_users list.
#• Loop through the new_users list to see if each new username has already been used.
#If it has, print a message that the person will need to enter a new username.
#If a username has not been used, print a message saying that the username is available.
#• Make sure your comparison is case insensitive.
#If 'John' has been used, 'JOHN' should not be accepted.
#(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_user : list= ["user01","user02","user03","user04","user05"]
new_user : list= ["user01","user03","user06","user07","user08"]


#N = 10
#for i in range(o,N):
#  new:str = input()
# new_low: str = new.lower()ù
#current_users.append(new)

#new_users_low: list = []
#for user in new_users:
#    new_users_low.append(user.lower())

new_users_low: list = [user.lower() for user in new_users]

for curr_user in current_users:

    if curr_user in new_users_list:
        print("NEED NEW USENAME")
    else:
        print("the username is avaible")




#5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list,
#such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#• Store the numbers 1 through 9 in a list.
#• Loop through the list.
#• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
#Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
#and each result should be on a separate line.

number_list: list= [ i for i in range(1, 10)]

print(number_list)

for i in number_list :
    if i== 1 :
       print(f"{i}st")
    elif i==2 :
       print(f"{2}nd")
    elif i==3 :
        print(f"{3}rd")
    else :
        print(f"{i}th")
        

