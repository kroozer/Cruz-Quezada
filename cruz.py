import time
print("See how long you can hold your breath")
# Ask to Begin
start = input("Press when you are ready ; are you holding your breath? (y/n): ")
if start == "y":
    timeLoop = True

# Variables to keep track and display
Sec = 0
Min = 0
# Begin Process
timeLoop = start
while timeLoop:
    Sec += 1
    print(str(Min) + " Mins " + str(Sec) + " Sec ")
    time.sleep(1)
    if Sec == 60:
        Sec = 0
        Min += 1
        print(str(Min) + " Minute")
    if Sec == 5:
      print("...")
    if Sec == 10:
      print("Piece of Cake")
    if Sec == 15:
      print("Bronze V")
    if Sec == 20:
      print("Getting There")
    if Sec == 25:
      print("Alpha in Training")
    if Sec == 30:
      print("Tyler1")
    if Sec == 35:
      print("GOD")
    if Sec == 40:
      print("IMMORTAL")
    if Sec == 45:
      print("CHALLENGER")
    if Sec == 53:
      print("FAKER")
    if Sec ==60:
      print("I dont know what to tell you, your on your own")
# Program will cancel when user presses X button