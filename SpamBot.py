#Install pyautogui using the command "pip install pyautogui"
import pyautogui,time,random

msg = [
    "Hello ",
    "Add the Messages you want to send in this list"]

time.sleep(10)

count = 100 #Change this value to increase/decrease the number of messages
i = 0

while i!=count:
    #Select the order of the messages you want to send 
    pyautogui.typewrite(msg[0])
    pyautogui.typewrite(msg[1])

    pyautogui.press("Enter")
    i+=1

