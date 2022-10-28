from random import *
from time import *
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
    lotteryChoice(currentDay)
  elif choice == 2:
    print("\n\n\n")
    workChoice()
  elif choice == 3:
    print("\n\n\n")
    dayStart(currentDay)
  elif choice == 4:
    print("\n\n\n")
    endGame(False, currentDay)
  else:
    print("Invalid choice [E-03f]")
def lotteryChoice(day):
  print("To choose a lottery, enter it's ID.", end = "\n\n")
  print("Return - FF")
  print("Newbie Lottery - 9F")
  print("Casino Lottery - 7C")
  print("Advanced Lottery - 4B")
  print("Mega Lottery - 1A")
  print("Impossible Lottery - 00", end = "\n\n")
  choice = str(input("Choice : "))
  if choice == "FF":
    print("\n\n\n")
    day += -1
    dayStart(day)
  elif choice == "9F" or choice == "7C" or choice == "4B" or choice == "1A" or choice == "00":
    print("\n\n\n")
    lotteryPlay(choice, day)
  else:
    print("Invalid choice [E-03c]")
def workChoice():
  print("wip work")
def lotteryPlay(ID, day):
  if ID == "9F":
    global jackpotNL
    jackpotNL = randint(1000, 2000)
    print("Newbie Lottery selected.", end = "\n\n")
    print("Ticket price : 1 $M")
    print("Jackpot value :", jackpotNL, "$M")
    print("Ticket limit : 25000 tprd")
    print("Jackpot chance : 0.5%", end = "\n\n")
    print("Would you like to :", end = "\n\n")
    print("1 - Play the Newbie Lottery")
    print("2 - Choose another lottery", end = "\n\n")
    choice = int(input("Choice : "))
    if choice == 1:
      print("\n\n\n")
      lotteryBuy(ID, day)
    elif choice == 2:
      print("\n\n\n")
      lotteryChoice(day)
    else:
      print("Invalid choice [E-03d]")
def lotteryBuy(ID, day):
  global moners
  if ID == "9F":
    print("Ticket price : 1 $M, current balance :", moners, "M$", end = "\n\n")
    purchaseAmount = int(input("How many tickets would you like to buy? "))
    if purchaseAmount > 0:
      price = purchaseAmount * 1
      print("\n\n\n")
      print("This will cost you", price, "$M. Current balance :", moners, "$M. Are you sure you want to continue?", end = "\n\n")
      print("1 - Yes")
      print("2 - No", end = "\n\n")
      choice = int(input("Choice : "))
      if choice == 1:
        if price > moners:
          print("\n")
          print("Not enough $M! Returning to purchase menu...")
          sleep(1)
          print("\n\n\n")
          lotteryBuy("9F", day)
        elif purchaseAmount > 25000:
          crybaby(day)
        else:
          moners += -price
          print("\n\n")
          print("Purchase successful!")
          print("New $M balance :", moners)
          print("Rolls will start shortly...")
          sleep(1)
          print("\n\n\n")
          lotteryRoll("9F", purchaseAmount, day)
      if choice == 2:
        print("\n\n\n")
        lotteryPlay("9F", day)
      else:
        print("Invalid choice [E-03e]")
    else:
      print("Invalid ticket value [E-08]")
def lotteryRoll(ID, ticketAmount, day):
  global moners
  winTotal = 0
  JPcount = 0
  rollCount = 0
  profit = 0
  if ID == "9F":
    global jackpotNL
    for i in range(ticketAmount):
      rollCount += 1
      roll = randint(1, 500)
      if roll == 1:
        JPcount += 1
        print("Jackpot on roll", rollCount,"/",ticketAmount)
      else:
        print("Nothing won on roll", rollCount,"/",ticketAmount, ", roll landed on", roll)
    winTotal = JPcount * jackpotNL
    profit = winTotal - ticketAmount * 1
    print("\n\n")
    print(ticketAmount, "rolls completed! Jackpots won :", JPcount,"for total earnings of", winTotal, "$M, totalling up to a profit of", profit, "M$!")
    sleep(2)
    print("Day completed, returning to menu.")
    sleep(1)
    moners += winTotal
    print("\n\n\n")
    dayStart(day)
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
def crybaby(day):
  print("\n\n")
  global surrenderGuarantee
  crybaby = randint(7,30)
  surrender = randint(1,1000)
  if surrenderGuarantee == True:
    surrender = 1
  if surrender == 1:
    print("""Oops! You bought more than 25000 tickets! You get humiliated on Twitter by the lottery company! You become extremely depressed from all the social pressure and surrender on life.""", end = "\n\n")
    sleep(5)
    print("""Congratulations! You got the ultra-rare easter egg! It's a very slim 0.1% chance of getting it, and you can't spam it like the lottery, so really, congrats! Well... now that you've surrendered, you can't actually play this game any further... I'm just gonna force quit the program so you don't have to, just re-execute it again! Also, I figured, to give you something for your achievement, try and type 69 in the menu you have when you first execute the program. This'll give you access to insane features! Anyways, bye!""")
    sleep(15)
    quit()
  else:
    print("""Oops! You bought more than 25000 tickets! You get humiliated on Twitter by the lottery company! You end up spending the next""", crybaby, "days crying in bed!", end = "\n\n")
    sleep(5)
    for loop in range(crybaby):
      print("You cry another day...")
      sleep(0.25)
      day += 1
    day += 1
    dayDisplay = day + 1
    print("\n\n")
    print("Returning to day menu on day", dayDisplay, end = "\n\n\n\n")
    sleep(0.8)
    dayStart(day)
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
    while moners > 999999999999999999:
      print("Overflow limit reached [E-02]")
      moners = float(input("Overwrite your moners to : "))
    while moners < 0:
      print("Invalid value [E-05]")
      moners = float(input("Overwrite your moners to : "))
    while moners.is_integer() == False:
      print("Invalid value [E-06]")
      moners = float(input("Overwrite your moners to : "))
    int(moners)
    global surrenderGuarantee
    surrenderGuarantee = bool(input("Guarantee surrender? (True or False) : "))
    print("\n\n\n")
    dayStart(startingDay)
  else:
      print("Invalid choice [E-03a]")
init()