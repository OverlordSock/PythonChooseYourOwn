import sys, time
from os import system, name
# Typewriter functionality
def typewriter(game):
  for char in game:
    sys.stdout.write(char)
    sys.stdout.flush()
    if char == "-":
      time.sleep(0)
    else:
      time.sleep(0.05)

# Slower typewriter for wait sequence
def typewriter2(game):
  for char in game:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(1.5)

# Clear terminal
def clear():
  time.sleep(1)
  # For windows
  if name == 'nt':
    _ = system('cls')
  # For mac/linux
  else:
    _ = system('clear')

# Enter to continue
def continueGame():
  while True:
    moveOn = input("Press enter to continue: ")
    if moveOn == "":
      clear()
      break
    else:
      print("\n")
      typewriter("Sorry, invalid input.")
      print("\n")

# Restart game
def restartGame():
  while True:
    tryAgain = input("Would you like to try again? (Y/N): ").upper()
    if tryAgain == "Y":
      print("\n")
      typewriter("The game will now restart.")
      time.sleep(1.5)
      clear()
      main()
    elif tryAgain == "N":
      typewriter("Thanks for playing!")
      time.sleep(1.5)
      exit()
    else:
      typewriter("Sorry, invalid input. Please choose from the given list. (Y/N)")
      print("\n")



#Display inventory function
def displayInventory(data, playerName):
  print("\n")
  typewriter("Contents Of Your Adventurer's Pack:")
  print("\n")
  print("-" * 70)
  print("\n")
  for rec in data:
    print(rec[0])
  print("\n")
  print("-" * 70)
  print("\n")
  while True:
    inspectInv = input(f"Should {playerName} inspect the contents further? (Y/N): ").upper()
    if inspectInv == "Y":
      print("\n")
      while True:
        matched = False
        inspectItem = input(f"What item should {playerName} inspect? (Type item as shown or DONE to stop inspecting): ").upper()
        for item in data:
          if item[0].upper() == inspectItem:
            print("\n")
            print(item[1])
            print("\n")
            matched = True
        if inspectItem == "DONE":
          clear()
          break
        if matched == False:
          print("\n")
          typewriter("Item not found, please try again.")
          print("\n")
      break
    elif inspectInv == "N":
      clear()
      break   
    else:
      print("\n")
      typewriter("Sorry, invalid input. Please choose from the given list. (Y/N)")
      print("\n")



#Story beginning function
def storyBegin(records, playerName, pronoun1, pronoun2, pronoun3):
  #Are you ready loop
  print("\n")
  typewriter(f"\n{playerName} is about to embark on a perilous journey.")
  print("\n")
  while True:
    readyAns = input(f"Is {playerName} ready? (Y/N): ").upper()
    if readyAns == "Y":
      typewriter("\nThen let's begin.")
      print("\n")
      clear()
      break
    elif readyAns == "N":
      typewriter(f"\n{playerName} has died of immense cowardice.")
      print("\n")
      restartGame()
    else:
      typewriter("\nSorry, invalid input. Please choose from the given list. (Y/N)")
      print("\n")

  #Story intro
  print("\n")
  typewriter(f"{playerName} awakens in a dim forest clearing, half dead and half buried.")
  print("\n")
  typewriter(f"{pronoun2.capitalize()} memory is cloudy, and the clearing is unfamiliar.")
  print("\n")
  typewriter(f"Strapped to {playerName}'s back is an adventurers pack.")
  print("\n")
    
  #First choice
  while True:
    action = input(f"\nShould {playerName} check the pack, or look around the clearing? (Pack/Clearing): ").upper()
    #Check adventurers pack
    if action == "PACK":
      clear()
      print("\n")
      typewriter(f"\n{playerName} removes the pack and looks inside.")
      displayInventory(records, playerName)
      print("\n")
      continueGame()
      print("\n")
      typewriter(f"{playerName} puts the pack back on, and looks around the clearing.")
      print("\n")
      typewriter("The clearing is clear, save for a few boulders and some animal droppings.")
      print("\n")
      typewriter(f"As {playerName} investigates further, {pronoun1} notices a broken signpost.")
      print("\n")
      typewriter("The signpost reads: 'Old Brittlemoor, 800 paces _____'")
      print("\n")
      typewriter("The sign is damaged, and the direction is unreadable.")
      print("\n")
      continueGame()
      break
    #Look around the clearing
    elif action == "CLEARING":
      clear()
      print("\n")
      typewriter("\nThe clearing is clear, save for a few boulders and some animal droppings.")
      print("\n")
      typewriter(f"As {playerName} investigates further, {pronoun1} notices a broken signpost.")
      print("\n")
      typewriter("The signpost reads: 'Old Brittlemoor, 800 paces _____'")
      print("\n")
      typewriter("The sign is damaged, and the direction is unreadable.")
      print("\n")
      continueGame()
      #Check pack before leaving
      while True:
        packCheck = input(f"Should {playerName} check the adventurers pack before leaving? (Y/N): ").upper()
        if packCheck == "Y":
          clear()
          print("\n")
          typewriter(f"\n{playerName} removes the pack and looks inside.")
          displayInventory(records, playerName)
          print("\n")
          typewriter(f"{playerName} puts the pack back on.")
          print("\n")
          continueGame()
          break
        elif packCheck == "N":
          typewriter(f"\nThe contents of the pack are still a mystery to {playerName}")
          print("\n")
          continueGame()
          break
        else:
          typewriter("\nSorry, invalid input. Please choose from the given list. (Y/N)")
          print("\n")
      break
    else:
      typewriter("\nSorry, invalid input. Please choose from the given list. (Pack/Clearing)")
      print("\n")


# Clearing Directions choices
def storyDirections(records, playerName, pronoun1, pronoun2, pronoun3):
  continueGame()
  print("\n")
  typewriter(f"{playerName} must pick a direction to head in.")
  print("\n")
  typewriter("Forward towards the signpost, Left towards an opening in the trees, or Right towards a distant hill.")
  print("\n")
  while True:
    direction = input(f"What direction will {playerName} choose? (Forward/Left/Right): ").upper()
    if direction == "FORWARD":
      clear()
      forestForward(records, playerName, pronoun1, pronoun2, pronoun3)
      break
    elif direction == "LEFT":
      clear()
      forestLeft(records, playerName, pronoun1, pronoun2, pronoun3)
      break
    elif direction == "RIGHT":
      clear()
      forestRight(records, playerName, pronoun1, pronoun2, pronoun3)
      break
    elif direction == "BACKWARD":
      clear()
      print("\n")
      typewriter(f"\n{playerName} turns around and heads back into the clearing.")
      print("\n")
      typewriter("The clearing is still clear.")
      print("\n")
      typewriter("Better wait a while just to make sure.")
      print("\n")
      typewriter2("...")
      print("\n")
      typewriter2("...")
      print("\n")
      typewriter2("...")
      print("\n")
      typewriter("Yep, still clear.")
      print("\n")
      typewriter(f"{playerName} turns around again.")
      print("\n")
      continueGame()
    else:
      typewriter("Sorry, invalid input. Please choose from the given list. (Forward/Left/Right)")
      print("\n")
  # End of direction functions
  clear()
  print("\n")
  typewriter(f"{playerName} sees the beginnings of a cobbled path stretching out ahead of {pronoun3}.")
  print("\n")
  typewriter("This path should provide guidance on the trail to Old Brittlemoor.")
  print("\n")
  continueGame()


     
#Clearing directions functions

#Forward path function
#Towards signpost
def forestForward(records, playerName, pronoun1, pronoun2, pronoun3):
  print("\n")
  typewriter(f"{playerName} heads in the direction of the signpost.")
  print("\n")
  typewriter("The path is very well made. The creator was surely well funded.")
  print("\n")
  typewriter("After a while, the path becomes blocked by a toll booth.")
  print("\n")
  # Toll booth choice
  while True:
    toll = input(f"Should {playerName} use something from the adventurer's pack or go around the toll barrier? (Pack/Around): ").upper()
    #Pack option
    if toll == "PACK":
      clear()
      print("\n")
      displayInventory(records, playerName)
      while True:
        print("\n")
        item = input(f"What item should {playerName} use? (Type item exactly): ").upper()
        if item == "LINT":
          print("\n")
          typewriter("This lint could probably destroy the barrier, but it currently isn't feeling up to it.")
          print("\n")
        elif item == "LOOSE CHANGE":
          print("\n")
          typewriter("Loose Change has been removed from the adventurers pack.")
          print("\n")
          typewriter(f"{playerName} approaches the barrier, loose change in hand.")
          print("\n")
          typewriter("The barrier appears to be susceptible to bribery.")
          print("\n")
          typewriter(f"{playerName} successfully bribes the barrier into allowing {pronoun3} passage.")
          print("\n")
          records.remove("Loose Change")
          continueGame()
          break
        elif item == "PET ROCK":
          print("\n")
          typewriter(f"{playerName} holds {pronoun2} beloved Pet Rock up to the toll barrier.")
          print("\n")
          typewriter("For a moment, nothing happens.")
          print("\n")
          typewriter("Then, the Pet Rock begins to whisper eldritch secrets to the barrier.")
          print("\n")
          typewriter(f"{playerName} is not surprised, as this is fairly standard Pet Rock behaviour.")
          print("\n")
          typewriter("Fearing for it's life, the barrier opens.")
          print("\n")
          typewriter(f"{playerName} has successfully intimidated the barrier into allowing {pronoun3} passage.")
          print("\n")
          continueGame()
          break
        else:
          print("\n")
          typewriter("Item not recognised, please try again.")
      break
    #Around option ending
    elif toll == "AROUND":
      time.sleep(1)
      clear()
      print("\n")
      typewriter(f"{playerName} walks around the barrier, stopping for a moment to consider how easy this was.")
      print("\n")
      typewriter("Surely any logical person would just walk around an unattended toll booth.")
      print("\n")
      typewriter("But if it was that obvious, surely the toll booth owner would have installed security measures to prevent this?")
      print("\n")
      typewriter(f"As {playerName} ponders, the toll booth barrier curls up and strikes {pronoun3} firmly in the back of the head.")
      print("\n")
      typewriter(f"{playerName} has died of complications related to toll evasion.")
      print("\n")
      restartGame()
    else:
      print("\n")
      typewriter("Sorry, invalid input. Please pick from the given list. (Pack/Around)")



#Left path function
#Towards opening in the trees
def forestLeft(records, playerName, pronoun1, pronoun2, pronoun3):
  print("\n")
  typewriter(f"{playerName} heads for the opening in the trees.")
  print("\n")
  typewriter(f"{pronoun1} walks for a while, shaded by the forest canopy.")
  print("\n")



#Right path function
#Towards distant hill
def forestRight(records, playerName, pronoun1, pronoun2, pronoun3):
  print("\n")
  typewriter(f"{playerName} heads for the hill in the distance.")
  print("\n")
  typewriter(f"The hill looks like it would be a good vantage point, {pronoun1} might be able to spot the town.")
  print("\n")
  typewriter(f"As {playerName} arrives at the base of the hill, {pronoun1} is startled by a loud click underfoot.")
  print("\n")
  typewriter(f"{pronoun2} leg becomes trapped in what looks like a hand crafted snare.")
  print("\n")
  #Free from snare
  while True:
    snare = input(f"Should {playerName} attempt to free {pronoun3}self from the snare? (Y/N): ")
    if snare == "Y":
      typewriter(f"{playerName} reaches down to pry the snare open, trapping both of {pronoun2} hands in the process.")
      print("\n")
      typewriter(f"{playerName} is now completely immobilised, and has no choice but to wait.")
      print("\n")
      handsTrapped = 1
      break
    elif snare == "N":
      typewriter(f"{playerName} decides to wait for whoever set the snare.")
      print("\n")
      handsTrapped = 0
      break
    else:
      typewriter("Sorry, invalid input. Please pick from the given list. (Y/N)")
      print("\n")
  typewriter2(". . .")
  print("\n")
  typewriter(f"Some time later, a rustling in the trees alerts {playerName} to an unknown presence.")

  #Hill goblins arrive


def main():
  #Set up starter inventory
  records = []
  records.append(["Lint", "A small ball of blue lint, most likely from fabric of a similar blue hue."])
  records.append(["Loose Change", "Coins of various shape, size and materials. Probably enough to buy a milkshake."])
  records.append(["Pet Rock", "A beloved companion, stolen from a Necromancer. What dark magic resides within?"])

  print("\n")
  typewriter("Welcome Adventurer!")
  print("\n")
  playerName = input("Please give your character a name: ").capitalize()
  while True:
    gender = input(f"\nWhat is {playerName}'s gender? (Male/Female/Other): ").upper()
    if gender == "MALE":
      pronoun1 = "he"
      pronoun2 = "his"
      pronoun3 = "him"
      playerGender = "Male"
      break
    elif gender == "FEMALE":
      pronoun1 = "she"
      pronoun2 = "her"
      pronoun3 = "her"
      playerGender = "Female"
      break
    elif gender == "OTHER":
      pronoun1 = "they"
      pronoun2 = "their"
      pronoun3 = "them"
      playerGender = "Other"
      break
    else:
      typewriter("Sorry, invalid input. Please pick from the given list. (Male/Female/Other)")
      print("\n")
  typewriter(f"\nCharacter Name: {playerName}")
  print("\n")
  typewriter(f"Character Gender: {playerGender}")
  print("\n")
  while True:
    checkpoint = input("Load a checkpoint? (Y/N): ").upper()
    if checkpoint == "Y":
      while True:
        print("\n")
        checkpointCode = input("Please enter a checkpoint name, or type BACK to cancel: ").upper()
        if checkpointCode == "BACK":
          clear()
          break
        elif checkpointCode == "CLEARING":
          print("\n")
          typewriter("Beginning the story from CHECKPOINT: Clearing.")
          time.sleep(1.5)
          clear()
          storyDirections(records, playerName, pronoun1, pronoun2, pronoun3)
        else:
          print("\n")
          typewriter("Checkpoint not recognised, please try again.")
    elif checkpoint == "N":
      time.sleep(1)
      clear()
      break
    else:
      print("\n")
      typewriter("Sorry, invalid input. Please pick from the given list. (Y/N)")
      print("\n")

  #Story intro
  storyBegin(records, playerName, pronoun1, pronoun2, pronoun3)

  # Move on from clearing
  print("\n")
  typewriter("CHECKPOINT: Clearing (Enter on the checkpoint screen to resume progress)")
  print("\n")
  storyDirections(records, playerName, pronoun1, pronoun2, pronoun3)



main()