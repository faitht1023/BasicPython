#me attempting to do something
#I ain't gassy

"""
def userInputTest():

    userInput = input("Enter something here: ")

    print("This is what you entered: " + userInput)
    
userInputTest()    
"""
def petrolCalculator():
    
    #getting information about the situation from the user
    sizeOfTank = int(input("Size of tank: "))
    percentFull = int(input("Percent of tank full: "))
    kmLitre = int(input("Km per litre: "))
    distance = int(input("Km to nearest petrol kiosk: "))
    
    #calculating how many litres of fuel are left based on the percentage given
    litresLeft = sizeOfTank * percentFull * 0.01
    
    #calculating how many km the user can drive before empty
    kmLeft = litresLeft * kmLitre
    
    #telling the user how much they can drive before empty
    print("You can drive for another " + kmLeft + " km.")
    
    
    if(kmLeft <= distance):
         print("You're in trouble! You're gonna have to walk a bit.")
        
    elif(kmLeft == distance):
        print("It's your lucky day! You have JUST ENOUGH petrol to make it to the station")
        
    else:
        print("You're good to go for a bit!")
        
def main():
	petrolCalculator()

if _name_ == '_main_':
    main()
