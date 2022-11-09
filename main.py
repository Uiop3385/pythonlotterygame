from random import *
from time import *
from uuid import *
import os
import hashlib
import base64
import codecs
def dayStart(currentDay, generated):
  global debugMode
  global dayIDstorage
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
  print("4 - End this game")
  if debugMode == False:
    print("5 - Save Game", end = "\n\n")
  if debugMode == True:
    print("\n")
    display = uuid1()
    print("Day ID :", display, end = "\n\n")
    dayIDstorage.append(display)
  choice = int(input("Choice : "))
  if choice == 1:
    print("\n\n\n")
    if generated == False:
      lotteryChoice(currentDay, False)
    else:
      lotteryChoice(currentDay, True)
  elif choice == 2:
    print("\n\n\n")
    workChoice()
  elif choice == 3:
    print("\n\n\n")
    dayStart(currentDay, False)
  elif choice == 4:
    print("\n\n\n")
    endGame(False, currentDay)
  elif debugMode == False and choice == 5:
    print("\n\n\n")
    if generated == False:
      dataSave(currentDay, False)
    else:
      dataSave(currentDay, True)
  else:
    print("Invalid choice [E-03f]")
    sleep(3)
def lotteryChoice(day, generated):
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
    dayStart(day, True)
  elif choice == "9F" or choice == "7C" or choice == "4B" or choice == "1A" or choice == "00":
    print("\n\n\n")
    if generated == False:
      lotteryPlay(choice, day, False)
    else:
      lotteryPlay(choice, day, True)
  else:
    print("Invalid choice [E-03c]")
    sleep(3)
def workChoice():
  print("wip work")
def lotteryPlay(ID, day, generated):
  if ID == "9F":
    global jackpotNL
    global NLticketPrice
    if generated == False:
      jackpotNL = randint(1000, 2000)
      NLticketPrice = uniform(1, 2)
      NLticketPrice = round(NLticketPrice, 2)
    print("Newbie Lottery selected.", end = "\n\n")
    print("Ticket price :", NLticketPrice, "$M")
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
      lotteryChoice(day, True)
    else:
      print("Invalid choice [E-03d]")
      sleep(3)
def lotteryBuy(ID, day):
  global moners
  if ID == "9F":
    global NLticketPrice
    print("Ticket price :", NLticketPrice, "$M, current balance :", moners, "M$", end = "\n\n")
    purchaseAmount = int(input("How many tickets would you like to buy? "))
    if purchaseAmount > 0:
      price = purchaseAmount * NLticketPrice
      price = round(price)
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
        lotteryPlay("9F", day, True)
    else:
      print("Invalid ticket value [E-08]")
      sleep(3)
def lotteryRoll(ID, ticketAmount, day):
  global moners
  winTotal = 0
  JPcount = 0
  rollCount = 0
  profit = 0
  if ID == "9F":
    global jackpotNL
    global NLticketPrice
    for i in range(ticketAmount):
      rollCount += 1
      roll = randint(1, 500)
      if roll == 1:
        JPcount += 1
        print("Jackpot on roll", rollCount,"/",ticketAmount)
      else:
        print("Nothing won on roll", rollCount,"/",ticketAmount, ", roll landed on", roll)
    winTotal = JPcount * jackpotNL
    profit = winTotal - ticketAmount * NLticketPrice
    print("\n\n")
    print(ticketAmount, "rolls completed! Jackpots won :", JPcount,"for total earnings of", winTotal, "$M, totalling up to a profit of", profit, "M$!")
    sleep(2)
    print("Day completed, returning to menu.")
    sleep(1)
    moners += winTotal
    print("\n\n\n")
    dayStart(day, False)
def endGame(endReached, endDay):
  global dayIDstorage
  global debugMode
  if endReached == False:
    print("Game ended early on day", endDay)
    print("Total moners :", moners, "$M")
    if debugMode == True:
      print("Day IDs :", dayIDstorage)
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
        print("Invalid choice [E-03b]")
        sleep(3)
  else:
    print("You have completed this year!")
    print("Total moners :", moners, "$M")
    if debugMode == True:
      print("Day IDs :", dayIDstorage)
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
        print("Invalid choice [E-03b]")
        sleep(3)
def crybaby(day):
  print("\n\n")
  global surrenderGuarantee
  crybaby = randint(7,30)
  surrender = randint(1,1000)
  if surrenderGuarantee == "Y":
    surrender = 1
  elif surrenderGuarantee == "N":
    surrender = randint(1,1000)
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
    dayStart(day, False)
def dataSave(day, generated):
  global debugModeX
  if not os.path.exists("savefiles"):
    print("""No saves folder found. Would you like to create one? By proceeding, you agree for the game to read, write and delete files located in that folder. The folder will be created in the directory the game is running from.""", end = "\n\n")
    print("1 - Yes")
    print("2 - Cancel and return to day", end = "\n\n")
    choice = int(input("Choice : "))
    if choice == 1:
      os.makedirs("savefiles/1/2/3")
      if debugModeX == True:
        print("Created folder at location", os.getcwd())
      create = open("savefiles/1/slot1.uiop", "wb")
      if debugModeX == True:
        print("Created file at location ", os.getcwd(), "/savefiles/1/slot1.uiop", sep = "")
      create.write("Do not modify this file. \n".encode())
      create.close()
      create = open("savefiles/1/slot1c.uiop", "xb")
      if debugModeX == True:
        print("Created file at location ", os.getcwd(), "/savefiles/1/slot1c.uiop", sep = "")
      create.close()
      create = open("savefiles/1/2/slot2.uiop", "wb")
      if debugModeX == True:
        print("Created file at location ", os.getcwd(), "/savefiles/1/2/slot2.uiop", sep = "")
      create.write("Do not modify this file. \n".encode())
      create.close()
      create = open("savefiles/1/2/slot2c.uiop", "xb")
      if debugModeX == True:
        print("Created file at location ", os.getcwd(), "/savefiles/1/2/slot2c.uiop", sep = "")
      create.close()
      create = open("savefiles/1/2/3/slot3.uiop", "wb")
      if debugModeX == True:
        print("Created file at location ", os.getcwd(), "/savefiles/1/2/3/slot3.uiop", sep = "")
      create.write("Do not modify this file. \n".encode())
      create.close()
      create = open("savefiles/1/2/3/slot3c.uiop", "xb")
      if debugModeX == True:
        print("Created file at location ", os.getcwd(), "/savefiles/1/2/3/slot3c.uiop", sep = "")
      create.close()
      sleep(1.5)
      print("\n")
      print("Successfully created folder and slots!")
      sleep(2)
      print("\n\n\n")
      dataSave(day, generated)
    elif choice == 2:
      print("\n\n\n")
      day += -1
      dayStart(day, generated)
    else:
      print("Invalid choice [E-03g]")
      sleep(3)
  else:
    print("Which slot would you like to save this game to?", end = "\n\n")
    if debugModeX == True:
      print("0 - Debug Saving")
    print("1 - Slot 1")
    print("2 - Slot 2")
    print("3 - Slot 3")
    print("4 - Return to day", end = "\n\n")
    choices = (0, 1, 2, 3, 4)
    choice = int(input("Choice : "))
    if choice not in choices:
      print("\n")
      print("Invalid choice [E-03h]")
      sleep(3)
    elif choice == 0 and debugModeX == True:
      print("Debug Saving enabled")
      writeSave(choice, generated, day)
    elif choice == 4:
      print("\n\n\n")
      dayStart(day, generated)
    else:
      print("\n")
      path = os.getcwd()
      if choice == 1:
        path = path + "/savefiles/1/slot1.uiop"
      elif choice == 2:
        path = path + "/savefiles/1/2/slot2.uiop"
      else:
        path = path + "/savefiles/1/2/3/slot3.uiop"
      size = os.path.getsize(path)
      warning = str(input("Beware! All data on slot "+str(choice)+" will be overwritten! Are you sure you wish to proceed? There are currently "+str(size)+" bytes on the file. Enter Yes to proceed or No to cancel : "))
      if warning == "Yes":
        print("\n\n\n")
        writeSave(choice, generated, day)
      else:
        print("Reloading menu...")
        print("\n\n\n")
        dataSave(day, generated)
def writeSave(slot, generated, day):
  global moners
  if slot == 0:
    print("wip")
  else:
    magic = 'cHJpbnQoIldyaXRpbmcgZGF0YSB0byBzbG90Iiwgc2xvdCwgIi4uLiIpDQppZiBzbG90ID09IDE6DQogIGZpbGVwYXRoID0gInNhdmVmaWxlcy8iK3N0cihzbG90KSsiL3Nsb3QiK3N0cihzbG90KSsiLnVpb3AiDQogIGZpbGVwYXRoQyA9ICJzYXZlZmlsZXMvIitzdHIoc2xvdCkrIi9zbG90IitzdHIoc2xvdCkrImMudWlvcCINCmVsaWYgc2xvdCA9PSAyOg0KICBmaWxlcGF0aCA9ICJzYXZlZmlsZXMvMS8iK3N0cihzbG90KSsiL3Nsb3QiK3N0cihzbG90KSsiLnVpb3AiDQogIGZpbGVwYXRoQyA9ICJzYXZlZmlsZXMvMS8iK3N0cihzbG90KSsiL3Nsb3QiK3N0cihzbG90KSsiYy51aW9wIg0KZWxzZTo'
    love = 'APvNtMzyfMKOuqTttCFNvp2S2MJMcoTImYmRiZv8vX3A0pvumoT90XFfvY3Afo3DvX3A0pvumoT90XFfvYaIco3NvQDbtVTMcoTIjLKEbDlN9VPWmLKMyMzyfMKZiZF8lYlVep3ElXUAfo3DcXlVip2kiqPVep3ElXUAfo3DcXlWwYaIco3NvQDc2LJk1MFN9VT1iozIlpj0XqzSfqJHlVQ0tMTS5QDc2LJk1MFN9VTyhqPu2LJk1MFxAPaMuoUIyZvN9VTyhqPu2LJk1MGVcQDc2LJk1MFN9VTuyrPu2LJk1MFxAPaMuoUIyZvN9VTuyrPu2LJk1MGVcQDcxLKEuVQ0to3OyovuznJkypTS0nPjtVaqvVvxAPzEuqTRhq3WcqTHbVxEiVT5iqPOgo2EcMaxtqTucplOznJkyYvOpovVhMJ5wo2EyXPxcQDcxLKEuYaqlnK'
    god = 'RlKHZhbHVlLmVuY29kZSgpKQ0KZGF0YS53cml0ZSgiXG4iLmVuY29kZSgpKQ0KZGF0YS53cml0ZSh2YWx1ZTIuZW5jb2RlKCkpDQpkYXRhLmNsb3NlKCkNCmRhdGEgPSBvcGVuKGZpbGVwYXRoLCAicmIiKQ0KZGF0YV9yZWFkID0gZGF0YS5yZWFkKCkNCmhhc2hlZF9zdHJpbmcgPSBoYXNobGliLnNoYTI1NihkYXRhX3JlYWQpLmhleGRpZ2VzdCgpDQpkYXRhLmNsb3NlKCkNCmRhdGEgPSBvcGVuKGZpbGVwYXRoQywgIndiIikNCmRhdGEud3JpdGUoaGFzaGVkX3N0cmluZy5lbmNvZGUoKSkNCmRhdGEuY2xvc2UoKQ0KcGF0aCA9IG9zLmdldGN3ZCgpDQppZiBzbG90ID09IDE6DQogIHBhdGggPSBwYXRoI'
    destiny = 'PftVv9mLKMyMzyfMKZiZF9moT90ZF51nJ9jVt0XMJkcMvOmoT90VQ09VQV6QDbtVUOuqTttCFOjLKEbVPftVv9mLKMyMzyfMKZiZF8lY3Afo3DlYaIco3NvQDcyoUAyBt0XVPOjLKEbVQ0tpTS0nPNeVPVip2S2MJMcoTImYmRiZv8mY3Afo3DmYaIco3NvQDcmnKcyVQ0to3ZhpTS0nP5aMKEmnKcyXUOuqTtcQDcjpzyhqPtvH3IwL2Imp2M1oTk5VUqlo3EyVvjtp2y6MFjtVzW5qTImVUEiVUAfo3DvYPOmoT90XD0Xp2kyMKNbZvxAPaOlnJ50XPWFMKE1pz5cozptqT8toJIhqF4hYvVcQDcmoTIypPtjYwp1XD0XpUWcoaDbVykhKT5povVcQDcxLKxtXm0tYGRAPzEurIA0LKW0XTEurFjtM2IhMKWuqTIxXD=='
    joy = '\x72\x6f\x74\x31\x33'
    trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
    eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
def init():
  global debugMode
  debugMode = False
  global debugModeX
  debugModeX = False
  global moners
  moners = randint(100,250)
  print("Welcome! You have a starting budget of", moners, "$M.", end = "\n\n")
  print("Would you like to :")
  print("1 - Start Game")
  print("2 - Learn to play", end = "\n\n")
  choice = int(input("Choice : "))
  if choice == 1:
    print("\n\n\n")
    dayStart(0, False)
  elif choice == 2:
    print("\n\n\n")
    #write tutorial here
  elif choice == 69:
    debugMode = True
    global dayIDstorage
    dayIDstorage = []
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
    while moners > 999999999999999999999999999999:
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
    surrenderGuarantee = str(input("Guarantee surrender? (Y or N) : "))
    if surrenderGuarantee == "X":
      debugMode = False
      # and yes this code is secret and will never be open-sourced to make sure to prevent anyone from accessing Debug Mode X
      magic = 'Y29kZSA9IGludChpbnB1dCgiRW50ZXIgYWNjZXNzIGNvZGUgOiAiKSkNCmNvZGUgPSBvY3QoY29kZSkNCmNvZGUgP'
      love = 'FOmqUVbL29xMFxAPzyzVTAiMTHtCG0tVwOiZGD3AGNjZGHlZFV6QDbtVTqfo2WuoPOxMJW1M01iMTILQDbtVTEyLa'
      god = 'VnTW9kZVggPSBUcnVlDQogIGRlYnVnTW9kZSA9IEZhbHNlDQogIHByaW50KCJEZWJ1ZyBNb2RlIFggRW5hYmxlZCI'
      destiny = 'cQDcyoUAyBt0XVPOjpzyhqPtvFJ5wo3WlMJA0VTAiMTHuVSgSYGNjKFVcQDbtVUAfMJIjXQZcQDbtVUS1nKDbXD=='
      joy = '\x72\x6f\x74\x31\x33'
      trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
      eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
      debugModeX = True
    print("\n\n\n")
    dayStart(startingDay, False)
  else:
      print("Invalid choice [E-03a]")
      sleep(3)
init()