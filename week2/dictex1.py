phonebook_dict = {
    'Alice' : '703-49301834',
    'Bob' : '857-384-1234',
    'Elizabeth' : '484-584-2923'

}

#PROBLEM 1
phoneNumber = phonebook_dict["Elizabeth"]
print phoneNumber

#PROBLEM 2
phonebook_dict["Kareem"] = "938-489-1234"
kareemPhone = phonebook_dict["Kareem"]
print kareemPhone

#CHECK ANSWERS
for key in phonebook_dict:
    print key

#PROBLEM 3
del phonebook_dict["Alice"]
print phonebook_dict

#PROBLEM 4
phonebook_dict["Bob"]= "968-345-2345"
newNumber = phonebook_dict["Bob"]
print newNumber

# PROBLEM 5
values = phonebook_dict.values()
print values
