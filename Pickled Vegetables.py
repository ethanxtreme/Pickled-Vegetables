#Pickled Vegetables

import pickle 

def pickle(veggies):
    #dumps veggies into file
    import pickle
    veggieFile = open('veggieFile.txt','wb')
    pickle.dump(veggies,veggieFile)
    veggieFile.close()
    

def stop(veggies):
    #pickle the vegetables and print a goodbye message
    pickle(veggies)
    print("\n-=-=- Goodbye! -=-=-")


def unpickle():
    #uses try/except to check for a veggieFile.txt to load veggies
    import pickle
    veggieFile = open('veggieFile.txt', 'rb')
    try:
        veggies = pickle.load(veggieFile)
        print("Veggies loaded!\n")
    except:
        print("No exisisting veggies found.\nA new veggies file will be created.\n")
        veggies = {}
    veggieFile.close()
    return veggies


def menu():
    #menu print
    print("-=-=- Menu -=-=-")
    print("V. View veggies.")
    print("A. Add new veggie.")
    print("C. Change veggie.")
    print("D. Delete veggie.")
    print("S. Stop.")
    #input validation loop
    while True:
        choice = (input("Enter your choice: "))
        if choice.upper() not in ('V','A','C','D','S'):
            print("Please enter a valid menu option")
        else:
            break
    print("-=-=-=-=-=-=-=-=-=-=-\n")
    return choice


def viewVeg(veggies):
    #prints out veggies
    print("-=-=- Veggie , Price -=-=-")
    for key in veggies:
        print(key,",",veggies[key])


def addVeg(veggies):
    #adds a new vegetable
    key = input("Enter a name for the new vegetable: ")
    if key not in veggies:
        while True:
            try:
                value = float(input("Enter a price for the new vegetable:$"))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                #price was successfully parsed!
                #we're ready to exit the loop.
                break
        veggies[key] = value
    else:
        print("That vegetables already exists!")


def changeVeg(veggies):
    key = input("Enter the name of a vegetable to change:")
    if key in veggies:
        while True:
            try:
                value = float(input("Enter a new price for the new vegetable:$"))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            else:
                #price was successfully parsed!
                #we're ready to exit the loop.
                break
        veggies[key] = value
        print("Price successfully changed!")
    else:
        print("Sorry, that vegetable was not found!")


def deleteVeg(veggies):
    key = input("Enter the name of a vegetable to delete: ")
    if key in veggies:
        del veggies[key]
        print("Vegetable Deleted!")
    else:
       print("Sorry, that vegetable was not found!") 

 
def main():
    
    veggies = unpickle()
    
    choice = 0
    choice = menu()
    choice = choice.upper()
    if choice == "V":
        viewVeg(veggies)
        pickle(veggies)
    elif choice == "A":
        addVeg(veggies)
        pickle(veggies)
    elif choice == "C":
        changeVeg(veggies)
        pickle(veggies)
    elif choice == "D":
        deleteVeg(veggies)
        pickle(veggies)
    elif choice == "S":
        stop(veggies)
        return
    main()

main()

        
