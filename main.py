from random import *
def dayStart(currentDay):
  currentDay += 1
  if currentDay > 365 or currentDay > 365.0:
    endGame(True, 365)
  print("It is day", currentDay, "and you have", moners, "$M", end = "\n\n")
  if currentDay == 365 or currentDay == 365.0:
    print("This is your final day!", end = "\n\n")
  elif currentDay == 182 or currentDay == 182.0:
    print("You are halfway through this game!", end = "\n\n")
  elif currentDay == 91 or currentDay == 91.0:
    print("You are a fourth of the way through this game!", end = "\n\n")
  elif currentDay == 273 or currentDay == 273.0:
    print("You are 3/4 of the way through this game!", end = "\n\n")
  print("Would you like to :")
  print("1 - Play the lottery")
  print("2 - Work for $M")
  print("3 - Skip day")
  print("4 - End this game", end = "\n\n")
  choice = int(input("Choice : "))
  if choice == 1:
    print("\n\n\n")
    lotteryChoice()
  elif choice == 2:
    print("\n\n\n")
    workChoice()
  elif choice == 3:
    print("\n\n\n")
    dayStart(currentDay)
  elif choice == 4:
    print("\n\n\n")
    endGame(False, currentDay)
def lotteryChoice():
  print("wip lottery")
def workChoice():
  print("wip work")
def endGame(endReached, endDay):
  if endReached == False:
    print("Game ended early on day", endDay)
    print("Total moners :", moners, "$M")
    print("Would you like to play again?", end = "\n\n")
    print("1 - Yes")
    print("2 - No", end = "\n\n")
    choice = int(input("Choice : "))
    if choice == 1:
      print("\n\n\n")
      init()
    elif choice == 2:
      quit()
    else:
      while choice != 1 or choice != 2:
        print("Invalid choice [E-03b]")
        choice = int(input("Choice : "))
  else:
    print("You have completed this year!")
    print("Total moners :", moners, "$M")
    print("Would you like to play again?", end = "\n\n")
    print("1 - Yes")
    print("2 - No", end = "\n\n")
    choice = int(input("Choice : "))
    if choice == 1:
      print("\n\n\n")
      init()
    elif choice == 2:
      quit()
    else:
      while choice != 1 or choice != 2:
        print("Invalid choice [E-03b]")
        choice = int(input("Choice : "))
def init():
  global moners
  moners = randint(100,250)
  print("Welcome! You have a starting budget of", moners, "$M.", end = "\n\n")
  print("Would you like to :")
  print("1 - Start Game")
  print("2 - Learn to play", end = "\n\n")
  choice = int(input("Choice : "))
  if choice == 1:
    print("\n\n\n")
    dayStart(0)
  elif choice == 2:
    print("\n\n\n")
    #write tutorial here
  elif choice == 69:
    print("\n\n\n")
    print("Debug mode enabled")
    startingDay = float(input("Enter a custom starting day : "))
    while startingDay > 365:
      print("Invalid date [E-01]")
      startingDay = float(input("Enter a custom starting day : "))
    while startingDay < 1:
      print("Invalid date [E-04]")
      startingDay = float(input("Enter a custom starting day : "))
    while startingDay.is_integer() == False:
      print("Invalid date [E-07]")
      startingDay = float(input("Enter a custom starting day : "))
      int(startingDay)
    startingDay += -1
    moners = float(input("Overwrite your moners to : "))
    while moners > 999999999999999:
      print("Overflow limit reached [E-02]")
      moners = float(input("Overwrite your moners to : "))
    while moners < 0:
      print("Invalid value [E-05]")
      moners = float(input("Overwrite your moners to : "))
    while moners.is_integer() == False:
      print("Invalid value [E-06]")
      moners = float(input("Overwrite your moners to : "))
    int(moners)
    print("\n\n\n")
    dayStart(startingDay)
  else:
    print("\n\n\n")
    while choice != 1 or choice != 2 or choice != 69:
      print("Invalid choice [E-03a]")
      choice = int(input("Choice : "))
init()