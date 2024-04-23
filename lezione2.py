#Edoardo Cianfoni
# 17/04/2024

print("hello world!")


# 2-3. Personal message: Use a variable to represent a person’s name,
# and print a message to that person.
# Your message should be simple, such as,
# “Hello Eric, would you like to learn some Python today?”

name: str = "Mario"

message: str = f"ciao {name}, ti va di imparare un po di python insieme"
print(message)

#2-4. Name cases: Use a variable to represent a person’s name,
#and then print that person’s name in lowercase,
#uppercase, and title case.

name_2: str = "Mario"

uppercase_name = name.upper()
title_name = name_2.title()
lower_name = name_2.lower()
print(uppercase_name)
print(title_name)
print(lower_name)

#2-5. Famous Quote: Find a quote from a famous person you admire.
#Print the quote and the name of its author.
#Your output should look something like the following,
#including the quotation marks:
#Abert Einstein once said,
#“A person who never made a mistake never tried anything new.”

name_3: str = "Daniele De Rossi"
print (f"Una volta {name_3} disse : Alla roma darei due carriere")

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, 
#represent the famous person’s name using a variable called famous_person.
#Then compose your message and represent it with a new variable called message. 
#Print your message.

famous_person: str = "Daniele De Rossi"
message : str = (f" Una volta {famous_person} disse: Alla roma darei 2 carrire")
print (message)

#2-8. File Extensions: Python has a removesuffix()
#method that works exactly like removeprefix().
#Assign the value 'python_notes.txt' to a variable called filename.
#Then use the removesuffix() 
#method to display the filename without the file extension,
#like some file browsers do.

filename: str = 'python_notes.txt'
filename_remove: str = filename.removesuffix(".txt")
print(filename_remove)


#3-1. Names: Store the names of a few of your friends in a list called names.
#Print each person’s name by accessing each element in the list, one at a time.

names : list = ["franco", "ciccio", "beppe", "tullio"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3-2. Greetings: Start with the list you used in Exercise 3-1,
#but instead of just printing each person’s name, print a message to them.
#The text of each message should be the same,
#but each message should be personalized with the person’s name.

names : list = ["franco", "ciccio", "beppe", "tullio"]
print(f"ciao {names[0]} disse")
print(f"ciao {names[1]} disse")
print(f"ciao {names[2]} disse")
print(f"ciao {names[3]} disse")

#3-3. Your Own List: Think of your favorite mode of transportation,
#such as a motorcycle or a car, and make a list that stores several examples.
#Use your list to print a series of statements about these items,
#such as “I would like to own a Honda motorcycle.”

cars : list = ["ferrari", "lamborghini", "bmw", "smart"]
print(f"vorrei avere una {cars[0]}")
print(f"vorrei avere una {cars[1]}")
print(f"vorrei avere una {cars[2]}")
print(f"vorrei avere una {cars[3]}")

#3-4. Guest List: If you could invite anyone, living or deceased,to dinner,
#who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. 
#Then use your list to print a message to each person, inviting them to dinner.

guest_list : list = ["sara", "alessio", "paolo", "elisa"]
print(f"sei invitata a cena {guest_list[0]}")
print(f"sei invitato a cena {guest_list[1]}")
print(f"sei invitato a cena {guest_list[2]}")
print(f"sei invitata a cena {guest_list[3]}")

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
#so you need to send out a new set of invitations.
#You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. 
#Add a print() call at the end of your program,
#stating the name of the guest who can’t make it.
#• Modify your list, 
#replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

guest_list : list = ["sara", "alessio", "paolo"]
print(f"sei invitata a cena {guest_list[0]}")
print(f"sei invitato a cena {guest_list[1]}")
print(f"sei invitato a cena {guest_list[2]}")

print(f"{guest_list[0]} non puoi più venire")

guest_list.remove("sara")
guest_list.insert("sofia")

print(f"sei invitata a cena {guest_list[0]}")
print(f"sei invitato a cena {guest_list[1]}")
print(f"sei invitato a cena {guest_list[2]}")


#3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
#Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
 #• Print a new set of invitation messages, one for each person in your list.

guest_list : list = ["sara", "alessio", "paolo", "giulia", "giulio","marco" ]

print( "abbiamo a disposizione una tavola piu grande")

print(f"sei invitata a cena {guest_list[0]}")
print(f"sei invitato a cena {guest_list[1]}")
print(f"sei invitato a cena {guest_list[2]}")
print(f"sei invitata a cena {guest_list[3]}")

insert(4, giulia)
insert(5,giulio)
append(mario)


#3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
#arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. 
#Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list,
#print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list,
#so you have an empty list. 
#Print your list to make sure you actually have an empty list at the end of your program.

guest_list : list = ["sara", "alessio", "paolo"]
print(f"sei invitata a cena {guest_list[0]}")
print(f"sei invitato a cena {guest_list[1]}")
print(f"sei invitato a cena {guest_list[2]}")
print(f"sei invitato a cena {guest_list[3]}")
print(f"sei invitato a cena {guest_list[4]}")

pop{guest_list[0]}
pop{guest_list[4] }






