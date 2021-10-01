## Edited file from a friend, test from 2019
import time

def countTo2000():
    # Take an input from user to start with 
    n = int(input("Enter a number to start with : "))

    #Check if the number is less than 2000, if true than continue otherwise else statement executes
    if n < 2000:
        #count up to 2000
        while n!=2001:
        #print the number we have at the moment
            print(n)
        #add one to the number
            n += 1

    
    else:
        print("N is already bigger than 2000")
        print("Exiting the program... ")
        time.sleep(3)



#Program start from here
#ask the user to type start or stop to either start or stop the program
runProgram = str(input("Enter START or STOP:"))

#run program if user types "start", countTo2000 function is called otherwise elif executes
if runProgram == "START":
    countTo2000()
elif runProgram == "STOP":
    print("Stopped, did not run program!")
    time.sleep(3)

    


