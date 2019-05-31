# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:02:47 2019

@author: Faith Tan
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
    print("You can drive for another ", kmLeft, " km.")
    
    
    if(kmLeft <= distance):
         print("You're in trouble! You're gonna have to walk a bit.")
        
    elif(kmLeft == distance):
        print("It's your lucky day! You have JUST ENOUGH petrol to make it to the station")
        
    else:
        print("You're good to go for a bit!")
        
def main():
	petrolCalculator()

if __name__ == '__main__':
    main()