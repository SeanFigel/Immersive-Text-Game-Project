# ---------Change getSoundsDict and getImagesDict file paths---------
def getSoundsDict():
  # Room sounds
  start = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\Long_Note_Three.wav")
  openClose = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\openClose.wav")
  intro = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\intro.wav")
  bedroom = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\bedroom.wav")
  bedroomSouth = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\bedroomSouth.wav")
  bedroomNorth = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\bedroomNorth.wav")
  closet = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\closet.wav")
  closetFoundFL = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\closetFoundFL.wav")
  hallSouth = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\hallSouth.wav")
  hallNorth = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\hallNorth.wav")
  lockedDoor = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\lockedDoor.wav")
  lock = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\lock.wav")
  useKey = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\useKey.wav")
  bathroom = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\bathroom.wav")
  bathroomFoundKey = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\bathroomFoundKey.wav")
  bathroomGotKey = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\bathroomGotKey.wav")
  masterBedroom = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\masterBedroom.wav")
  stairs = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\stairs.wav")
  foyer = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\foyer.wav")
  balcony = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\balcony.wav")
  balconyClose = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\balconyClose.wav")
  archway = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\archway.wav")
  archwayFoundBatteries = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\archwayFoundBatteries.wav")
  brokenLose = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\brokenLose.wav")
  woodenDoors = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\woodenDoors.wav")
  woodenLose = makeSound("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\sounds\\woodenLose.wav")
  dict = {"start":start, "openClose": openClose, "closet":closet, "closetFoundFL":closetFoundFL, "bedroomSouth":bedroomSouth,
    "bedroom":bedroom, "bedroomNorth":bedroomNorth, "bathroom":bathroom, "bathroomFoundKey": bathroomFoundKey,
    "bathroomGotKey": bathroomGotKey, "hallSouth":hallSouth, "hallNorth":hallNorth, "lockedDoor":lockedDoor,"lock":lock,
    "useKey":useKey,"masterBedroom":masterBedroom, "balcony":balcony, "balconyClose":balconyClose, "stairs":stairs,
    "foyer":foyer, "brokenLose":brokenLose, "archway":archway, "archwayFoundBatteries":archwayFoundBatteries, "intro":intro,
    "woodenDoors":woodenDoors, "woodenLose":woodenLose}
  return dict
 
def getImagesDict():
  # Room Images
  bedroom = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\bedroom.jpg")
  bedroomSouth = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\bedroomSouth.jpg")
  bedroomNorth = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\bedroomNorth.jpg")
  closet = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\closet.jpg")
  closetTook = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\closetTook.jpg")
  closetFoundFL = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\closetFoundFL.jpg")
  hallSouth = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\hallSouth.jpg")
  hallNorth = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\hallNorth.jpg")
  bathroom = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\bathroom.jpg")
  bathroomTook = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\bathroomTook.jpg")
  bathroomFoundKey = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\bathroomFoundKey.jpg")
  bathroomFoundKeyTook = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\bathroomFoundKeyTook.jpg")
  masterBedroom = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\masterBedroom.jpg")
  foyer = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\foyer.jpg")
  foyerTook = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\foyerTook.jpg")
  balcony = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\balcony.jpg")
  #archway = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\archway.jpg")
  #archwayFoundBatteries = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\archwayFoundBatteries.jpg")
  #woodenDoors = makePicture("C:\\Users\\Moises\\Desktop\\GitHub\\Immersive-Text-Game-Project\\resources\\images\\woodenDoors.jpg")
  dict = {"bedroom":bedroom, "bedroomSouth":bedroomSouth, "bathroomTook":bathroomTook, "bedroomNorth":bedroomNorth,
    "bathroomFoundKeyTook":bathroomFoundKeyTook, "closet":closet, "closetTook":closetTook, "closetFoundFL":closetFoundFL,
    "hallSouth":hallSouth, "hallNorth":hallNorth, "bathroom":bathroom, "bathroomFoundKey": bathroomFoundKey, "masterBedroom":masterBedroom,
    "foyer":foyer, "foyerTook":foyerTook,"balcony":balcony}
  return dict
  
#-------------------------------------------Game Code-------------------------------------------
# Adventure Game Updates
# This is the updated adventure game which asks for user input to move east, west, south, or north
def adventure():
  global name, validMoves, validActions, sounds, messages, images, inven, blackPic
  # Room sounds
  sounds = getSoundsDict()
  ###play(sounds["start"])
  # Ask name
  name = askName()
  if(name == "exit"):
    i = 0
    for key, sound in sounds.iteritems():
      try:
        stopPlaying(sound)
      except:
        continue
    showInformation("~~You have quit the game.~~")
    return
  # Room messages
  messages = getMessagesDict()
  # Room messages
  images = getImagesDict()
  # Inventory
  inven = {"flashlight": false, "batteries": false, "keyHouse": false, "radio": false, "keyDinner": false}
  # default values
  validMoves = ["north","south","east","west","left","right","n","s","e","w","l","r"]
  validActions = ["hide","jump","crawl","wait","h","j","c","w"]
  blackPic = makeEmptyPicture(getWidth(images["bedroom"]), getHeight(images["bedroom"]), black)
  # Begin first stage
  result = firstStage()
  # Continue to next stage
  if result == "won":
    move = ""
    while move!="exit":
      # Begin next level
      showInformation("[Next Stage]")
      showInformation(messages["startNext"])
      # Ask left/right
      move = askMove("lr", "You can go left or right.")
      if move == "l":
        result = leftStage()
        break
      elif move == "r":
        result = rightStage()
        break
      elif move == "help":
        showInformation(messages["help"])
      elif move in ["i","inventory"]:
        getInventory()
  if result == "quit":
    showInformation(messages["quitGame"])
  # End sounds
  for key, sound in sounds.iteritems():
      try:
        stopPlaying(sound)
      except:
        continue
    
def firstStage():
  global inven
  image = blackPic
  # Begin game
  showInformation(messages["help"])
  play(sounds["intro"])
  showInformation(messages["intro"])
  stopPlaying(sounds["intro"])
  move = ""
  flashlightOn = false
  location = 3 # bedroom
  while move != "exit":
    # Check flashlight
    if inven["flashlight"] == true and inven["batteries"] == true:
      flashlightOn = true
    else:
      flashlightOn = false
    # Check if user asked for help
    if move == "help":
      showInformation(messages["help"])
    # Show Inventory
    if move in ["i","inventory"]:
      getInventory()
    # Closet
    if location == 1:
      if inven["flashlight"] == true:
        copyInto(images["closetTook"], image, 0, 0)
        repaint(image)
      else:
        copyInto(images["closet"], image, 0, 0)
        repaint(image)
      play(sounds["closet"])
      showInformation(messages["closet"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["closet"])
      if inven["flashlight"] == false:
        response = askFlashlight(image)
        if response == "true":
          copyInto(images["closetTook"], image, 0, 0)
          repaint(image)
          inven["flashlight"] = true
        elif response == "false":
          inven["flashlight"] = false
        if response == "exit":
          break
        if response == "help":
          inven["flashlight"] = false
          move = "help"
          continue
      move = askMove("n", "You can move north.")
      if move == "n":
        play(sounds["openClose"])
        location += 1
    # Bedroom South
    elif location == 2:
      copyInto(images["bedroomSouth"], image, 0, 0)
      repaint(image)
      play(sounds["bedroomSouth"])
      showInformation(messages["bedroomSouth"])
      stopPlaying(sounds["bedroomSouth"])
      stopPlaying(sounds["openClose"])
      move = askMove("ns", "You can move north or south.")
      if move == "n":
        location += 1
      elif move == "s":
        play(sounds["openClose"])
        location -= 1
    # Bedroom
    elif location == 3:
      copyInto(images["bedroom"], image, 0, 0)
      repaint(image)
      play(sounds["bedroom"])
      showInformation(messages["bedroom"])
      stopPlaying(sounds["bedroom"])
      move = askMove("ns", "You can move north or south.")
      if move == "n":
        location += 1
      elif move == "s":
        location -= 1
    # Bedroom North
    elif location == 4:
      copyInto(images["bedroomNorth"], image, 0, 0)
      repaint(image)
      play(sounds["bedroomNorth"])
      showInformation(messages["bedroomNorth"])
      stopPlaying(sounds["bedroomNorth"])
      stopPlaying(sounds["openClose"])
      move = askMove("nse","You can move north, south, or east.")
      if move == "n":
        play(sounds["openClose"])
        location += 2
      elif move == "s":
        location -= 1
      elif move == "e":
        play(sounds["openClose"])
        location += 1
    # Bathroom
    elif location == 5:
      if inven["keyHouse"] == true:
        if flashlightOn:
          copyInto(flashLightFilter(images["bathroomTook"]), image, 0, 0)
        else:
          copyInto(images["bathroomTook"], image, 0, 0)
        repaint(image)
      else:
        if flashlightOn:
          copyInto(flashLightFilter(images["bathroom"]), image, 0, 0)
        else:
          copyInto(images["bathroom"], image, 0, 0)
        repaint(image)
      play(sounds["bathroom"])
      showInformation(messages["bathroom"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["bathroom"])
      if inven["keyHouse"] == false:
        copyInto(images["bathroomFoundKey"], image, 0, 0)
        repaint(image)
        response = askKey()
        if response == "true":
          copyInto(images["bathroomFoundKeyTook"], image, 0, 0)
          repaint(image)
          inven["keyHouse"] = true
        elif response == "false":
          inven["keyHouse"] = false
        if response == "exit":
          break
        if response == "help":
          inven["keyHouse"] = false
          move = "help"
          continue
      move = askMove("w", "You can move west.")
      if move == "w":
        play(sounds["openClose"])
        location -= 1
    # Hall South
    elif location == 6:
      if flashlightOn:
        copyInto(flashlightFilter(images["hallSouth"]), image, 0, 0)
      else:
        copyInto(images["hallSouth"], image, 0, 0)
      repaint(image)
      play(sounds["hallSouth"])
      showInformation(messages["hallSouth"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["hallSouth"])
      move = askMove("ns","You can move north or south.")
      if move == "n":
        location += 1
      elif move == "s":
        location -= 2
    # Hall North
    elif location == 7:
      if flashlightOn:
        copyInto(flashlightFilter(images["hallNorth"]), image, 0, 0)
      else:
        copyInto(images["hallNorth"], image, 0, 0)
      repaint(image)
      play(sounds["hallNorth"])
      showInformation(messages["hallNorth"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["hallNorth"])
      move = askMove("nse", "You can move north, south, or east.")
      if move == "n":
        play(sounds["lockedDoor"])
        showInformation("\n~The door is locked.~")
        stopPlaying(sounds["lockedDoor"])
        if inven["keyHouse"]==true:
          if(askUseKey()):
            play(sounds["useKey"])
            showInformation("You place the key in the lock. You struggle a bit...It works, you opened the door!")
            stopPlaying(sounds["useKey"])
            location += 1
      elif move == "s":
        location -= 1
      elif move == "e":
        play(sounds["stairs"])
        showInformation("\n~You are walking down the curved stairs~")
        stopPlaying(sounds["stairs"])
        location += 3
    # Master Bedroom (secret room)
    elif location == 8:
      if flashlightOn:
        copyInto(flashlightFilter(images["masterBedroom"]), image, 0, 0)
      else:
        copyInto(images["masterBedroom"], image, 0, 0)
      repaint(image)
      play(sounds["masterBedroom"])
      showInformation(messages["masterBedroom"])
      stopPlaying(sounds["balconyClose"])
      stopPlaying(sounds["masterBedroom"])
      move = askMove("sw", "You can move south or west.")
      if move == "s":
        play(sounds["lock"])
        showInformation("You make sure to lock the door before you leave the room.")
        stopPlaying(sounds["lock"])
        play(sounds["openClose"])
        location -= 1
      elif move == "w":
        location += 1
    # Balcony
    elif location == 9:
      if flashlightOn:
        copyInto(flashlightFilter(images["balcony"]), image, 0, 0)
      else:
        copyInto(images["balcony"], image, 0, 0)
      repaint(image)
      play(sounds["balcony"])
      showInformation(messages["balcony"]) # Clue
      stopPlaying(sounds["balcony"])
      move = askMove("e","You can move east.")
      if move == "e":
        play(sounds["balconyClose"])
        location -= 1
    # Stairs/Foyer
    elif location == 10:
      if inven["batteries"] == true:
        if flashlightOn:
          copyInto(flashlightFilter(images["foyerTook"]), image, 0, 0)
        else:
          copyInto(images["foyerTook"], image, 0, 0)
        repaint(image)
      else:
        if flashlightOn:
          copyInto(flashlightFilter(images["foyer"]), image, 0, 0)
        else:
          copyInto(images["foyer"], image, 0, 0)
        repaint(image)
      play(sounds["foyer"])
      showInformation(messages["foyer"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["foyer"])
      move = askMove("nsew", "You can move north, south, east, or west.")
      if move == "n":
        play(sounds["openClose"])
        location += 3
      elif move == "s":
        play(sounds["stairs"])
        showInformation("\n~You are walking up the curved stairs~")
        stopPlaying(sounds["stairs"])
        location -= 3
      elif move == "e":
        location += 2
      elif move == "w":
        location += 1
    # Broken Pots
    elif location == 11:
      play(sounds["brokenLose"])
      showInformation(messages["brokenLose"]) # print loses chased and attacked in the dark
      stopPlaying(sounds["brokenLose"])
      copyInto(gameOver(image), image, 0, 0)
      repaint(image)
      showInformation(messages["loser"])
      return "lost"
    # Archway
    elif location == 12:
      play(sounds["archway"])
      showInformation(messages["archway"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["archway"])
      if inven["batteries"] == false:
        response = askBatteries()
        if response == "true":
          copyInto(images["foyerTook"], image, 0, 0)
          repaint(image)
          inven["batteries"] = true
        elif response == "false":
          inven["batteries"] = false
        if response == "exit":
          break
        if response == "help":
          inven["batteries"] = false
          move = "help"
          continue
      move = askMove("w", "You can move west.")
      if move == "w":
        location -= 2
    # Wooden Doors
    elif location == 13:
      move = "exit"
      if inven["flashlight"] == true and inven["batteries"] == true:
        if(askUseFL()):
          play(sounds["woodenDoors"])
          showInformation(messages["win"]) # print wins by escaping
          stopPlaying(sounds["openClose"])
          stopPlaying(sounds["woodenDoors"])
          showInformation(messages["winner"])
          return "won"
      play(sounds["woodenLose"])
      showInformation(messages["lose"]) # print loses attacked in the dark
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["woodenLose"])
      copyInto(gameOver(image), image, 0, 0)
      repaint(image)
      showInformation(messages["loser"])
      return "lost"
  return "quit"

#--------------------------------------------------------------------------------------------------------Left Stage
def leftStage():
  showInformation(messages["leftIntro"])
  showInformation(messages["leftIntro2"])
  move = ""
  location = 1 # Diner
  while move != "exit":
    # Check if user asked for help
    if move == "help":
      showInformation(messages["help"])
    # Show Inventory
    if move in ["i","inventory"]:
      getInventory()
    # Back to Car
    if location == 0:
      showInformation(messages["backToCar"])
      copyInto(gameOver(image), image, 0, 0)
      repaint(image)
      showInformation(messages["loser"])
      return "lost"
    # Diner
    elif location == 1:
      showInformation(messages["diner"])
      move = askMove("nsew", "You can move north, south, east, or west.")
      if move == "s":#backToCar
        location -= 1
      elif move == "w":#keyDiner
        location += 1
      elif move == "n":#radio
        location += 2
      elif move == "e":#sideStreet
        showInformation(messages["padlock"])
        location += 3
    # Key Diner
    elif location == 2:
      showInformation(messages["keyDiner"])
      move = askMove("e", "You can move East.")
      if move == "e":#diner
        location -= 1
    # Radio
    elif location == 3:
      showInformation(messages["radio"])
      move = askMove("s", "You can move south.")
      if move == "s":#diner
        location -= 2
    # Side Street
    elif location == 4:
      showInformation(messages["sideStreet"])
      move = askMove("ew", "You can move east or west.")
      if move == "w":#diner
        location -= 3
      elif move == "e":#seePolice
        location += 1
    # See Police
    elif location == 5:
      showInformation(messages["seePolice"])
      showInformation(messages["policeCar"])
      move = askMove("ew", "You can move east or west.")
      if move == "w":#sideStreet
        location -= 1
      elif move == "e":#keypad
        showInformation(messages["keypad"])
        if askCode():
          showInformation(messages["correctCode"])
          location += 1 #policeStation
        else:
          showInformation(messages["wrongCode"])
          showInformation("You start heading back.")
          location += 2 #loseRadio
    # Police Station
    elif location == 6:
      showInformation(messages["policeStation"])
      showInformation(messages["win2"])
      showInformation(messages["winner"])
      return "won"
    # Lose Radio
    elif location == 7:
      showInformation(messages["radioSound"])
      showInformation(messages["loseRadio"])
      copyInto(gameOver(image), image, 0, 0)
      repaint(image)
      showInformation(messages["loser"])
      return "lost"

#--------------------------------------------------------------------------------------------------------Right Stage
def rightStage():
  showInformation(messages["rightIntro"])
  showInformation(messages["rightIntro2"])
  move = ""
  location = 0 # Entryway
  while move != "exit":
    # Check if user asked for help
    if move == "help":
      showInformation(messages["help"])
    # Show Inventory
    if move in ["i","inventory"]:
      getInventory()
    # Entryway
    if location == 0:
      showInformation(messages["entryway"])
      move = askMove("new", "You can move north, east, or west.")
      if move == "w":#bathroomFactory
        location += 1
      elif move == "e":#supplyCloset
        location += 2
      elif move == "n":#factory
        location += 3
    # Factory Bathroom
    elif location == 1:
      showInformation(messages["bathroomFactory"])
      move = askMove("e", "You can move East.")
      if move == "e":#entryway
        location -= 1
    # Supply Closet
    elif location == 2:
      showInformation(messages["supplyCloset"])
      move = askMove("w", "You can move west.")
      if move == "w":#entryway
        location -= 2
    # Factory
    elif location == 3:
      showInformation(messages["factory"])
      move = askMove("ns", "You can move north or south.")
      if move == "s":#entryway
        location -= 3
      elif move == "n":#asklogs
        if askLogs():
          location += 1#logs
        else:
          showInformation("You start walking back inside.")
    # Logs
    elif location == 4:
      showInformation(messages["logs"])
      move = askActions("hj", "You can hide or jump.")
      if move == "j":#jump
        location += 1
      elif move == "h":#hide
        location += 2
    # Jump
    elif location == 5:
      showInformation(messages["jump"])
      copyInto(gameOver(image), image, 0, 0)
      repaint(image)
      showInformation(messages["loser"])
      return "lost"
    # Hide
    elif location == 6:
      showInformation(messages["hide"])
      move = askActions("cw", "You can crawl or wait.")
      if move == "c":#crawl
        showInformation(messages["crawl"])
        showInformation(messages["loser"])
      elif move == "w":#wait
        showInformation(messages["wait"])
        showInformation(messages["loser"])
      return "lost"
      
# This function tells the user there is a flashlight and asks if the user will take it
def askFlashlight(image):
  copyInto(images["closetFoundFL"], image, 0, 0)
  repaint(image)
  play(sounds["closetFoundFL"])
  showInformation("You open the bag and notice a flashlight. You grab it but it has no batteries.")
  stopPlaying(sounds["closetFoundFL"])
  while true:
    userInput = requestString("Would you like to take it with you?")
    try:
      userInput = userInput.lower()
    except:
      userInput = "exit"
    if userInput in ["yes", "y"]:
      showInformation("~~You now have a flashlight!~~")
      return "true"
    if userInput in ["no", "n"]:
      return "false"
    if userInput == "exit":
      return "exit"
    if userInput == "help":
      return "help"
    showInformation("That's not a good answer " + name + ", you can either say yes or no.")

# This function tells the user there is a key and asks if the user will pick it up
def askKey():
  play(sounds["bathroomFoundKey"])
  showInformation("At the bottom of the tub you notice a shiny piece of metal. You walk over. It's a key!")
  stopPlaying(sounds["bathroomFoundKey"])
  while true:
    userInput = requestString("Would you like to get the key?")
    try:
      userInput = userInput.lower()
    except:
      userInput = "exit"
    if userInput in ["yes", "y"]:
      play(sounds["bathroomGotKey"])
      showInformation("~~You now have a key!~~")
      stopPlaying(sounds["bathroomGotKey"])
      return "true"
    if userInput in ["no", "n"]:
      return "false"
    if userInput == "exit":
      return "exit"
    if userInput == "help":
      return "help"
    showInformation("That's not a good answer " + name + ", you can either say yes or no.")

# This function tells the user there are batteries and asks if the user will pick them up
def askBatteries():
  play(sounds["archwayFoundBatteries"])
  showInformation("Walking around you step on something. Its a couple of batteries lying on the floor.")
  stopPlaying(sounds["archwayFoundBatteries"])
  while true:
    userInput = requestString("Would you like to pick them up?")
    try:
      userInput = userInput.lower()
    except:
      userInput = "exit"
    if userInput in ["yes", "y"]:
      showInformation("~~You now have batteries!~~")
      return "true"
    if userInput in ["no", "n"]:
      return "false"
    if userInput == "exit":
      return "exit"
    if userInput == "help":
      return "help"
    showInformation("That's not a good answer " + name + ", you can either say yes or no.")

# This function asks the user if they would like to use the key if they found the key
def askUseKey():
  while true:
    userInput = requestString("Would you like to try using the key?")
    try:
      userInput = userInput.lower()
    except:
      userInput = "exit"
    if userInput in ["yes", "y"]:
      return true
    if userInput in ["no", "n"]:
      return false
    if userInput == "exit":
      return "exit"
    if userInput == "help":
      return "help"
    showInformation("That's not a good answer " + name + ", you can either say yes or no.")

# This function asks the user if they would like to use the flashlight if they found it
def askUseFL():
  while true:
    userInput = requestString("It is incredibly dark out here, would you like to use your flashlight?")
    try:
      userInput = userInput.lower()
    except:
      userInput = "exit"
    if userInput in ["yes", "y"]:
      return true
    if userInput in ["no", "n"]:
      return false
    if userInput == "exit":
      return "exit"
    if userInput == "help":
      return "help"
    showInformation("That's not a good answer " + name + ", you can either say yes or no.")

# Asks the user for the their name.
def askName():
  while true:
    tempInput = requestString("Please enter your name:")
    try:
      userInput = tempInput.lower()
    except:
      userInput = "exit"
    if userInput == "":
      showInformation("Name must be at least one character.")
    elif userInput == "exit":
      return "exit"
    elif userInput == "help":
      showInformation(messages["help"])
    else:
      return tempInput

# Asks the user for keypad code.
def askCode():
  userInput = requestString("Please enter code:")
  try:
      userInput = userInput.lower()
  except:
      return false
  if userInput == "4825":
    return true
  return false

# Asks the user to go to the logs
def askLogs():
  showInformation(messages["outside"])
  while true:
    userInput = requestString("Would you like to go into the logs?")
    try:
      userInput = userInput.lower()
    except:
      userInput = "exit"
    if userInput in ["yes", "y"]:
      return true
    if userInput in ["no", "n"]:
      return false
    if userInput == "exit":
      return "exit"
    if userInput == "help":
      return "help"
    showInformation("That's not a good answer " + name + ", you can either say yes or no.")

# This function asks the user what direction he/she will move.
# The user may also ask for help or exit
def askMove(directions, text):
  userInput = ""
  while(userInput != "exit" and userInput != "help"):
    userInput = requestString(text + " Where do you want to move?")
    try:
      userInput = userInput.lower()
    except:
      userInput = "exit"
    if userInput in validMoves:
      userInput = userInput[0]
      if userInput in directions:
        return userInput
    if userInput in ["i","inventory"]:
      return userInput
    if userInput != "help" and userInput != "exit":
      showInformation("That is not an option " + name + ".[If you're having trouble? type: help]")
  return userInput

# This function asks the user what direction he/she will move.
# The user may also ask for help or exit
def askActions(actions, text):
  userInput = ""
  while(userInput != "exit" and userInput != "help"):
    userInput = requestString(text + " What do you want to do?")
    try:
      userInput = userInput.lower()
    except:
      userInput = "exit"
    if userInput in validActions:
      userInput = userInput[0]
      if userInput in actions:
        return userInput
    if userInput in ["i","inventory"]:
      return userInput
    if userInput != "help" and userInput != "exit":
      showInformation("That is not an option " + name + ".[If you're having trouble? type: help]")
  return userInput
  
# Function to add all the string variables into a directory.  The function returns the directory.
def getMessagesDict():
  # Room messages
  help = "\n***Welcome to the house adventure %s***\n"%name\
    + "The directions that you are allowed to move will be displayed for you once you enter into a room. "\
    + "Directions that you can move in are north, south, east or west by typing the direction that you would like to go. "\
    + "Typing help will display this explanation again. "\
    + "Typing exit will exit the game."
  intro = "\nThere is a loud creak of what sounds like wood which causes you to stir from your sleep. "\
    + "As you open your eyes you realize that you are not in your familiar bedroom, in fact you are not even on your bed. "\
    + "You jerk upwards and attempt to figure out where you are, though the room you seem to be in is dark and it is difficult to see. "\
    + "There is moonlight streaming through the windows to your right, which allows you to see what looks to be a switch on the side of the wall. "\
    + "You flip the switch."
  bedroom = "\n-----Bedroom-----\n"\
    + "You find yourself in a small bed room. "\
    + "There are three doors in the bedroom and a small window. "\
    + "There is a small bed and the room is covered in dust. "
  bedroomSouth = "\n-----Bedroom South-----\n"\
    + "You are now in the back of the room standing next to a small door(south). "\
    + "It looks too small to be another room. "\
    + "Across the room (north) are the two doors."
  bedroomNorth = "\n-----Bedroom North-----\n"\
    + "You feel a small cool breeze coming in from under the door to your north. "\
    + "To the east, you can see another door. "\
    + "Across the room (south) is another small door."
  closet = "\n-----Closet-----\n"\
    + "You open the door in the back of the room and find it to be a closet. "\
    + "Inside the closet are some moth eaten sweaters, one that seems to be the remains of one of those holiday sweaters. "\
    + "On the floor there seems to be a small bag."
  hallSouth = "\n-----Hallway South-----\n"\
    + "You find yourself in a dark hallway. The wooden floor is covered in dust and grim. It is very dark. "\
    + "There is a window halfway down the hall that is letting in a cool breeze. "\
    + "Its also letting in some moonlight which allows you to see a staircase going down. "\
    + "You can also faintly make out another door at the end of the hallway (north) past the stairs. "\
    + "You are standing by the bedroom door(south)."
  hallNorth = "\n-----Hallway North-----\n"\
    + "You are standing next to the open window. You can see some light coming out from under the door in front of you (north). "\
    + "The way down the staircase (east) is hard to see. Looks like the lights are off downstairs. "\
    + "Down the hall to the south is the door to the bedroom." 
  bathroom = "\n-----Bathroom-----\n"\
    + "Opening the door you walk into a very dark room. Faint light coming from the skylight allows you to see in the room. "\
    + "You are able to make out a tub, sink and a toilet. "
  masterBedroom = "\n-----Master Bedroom-----\n"\
    + "You find yourself in a large bedroom. Like everywhere else in the house there is dust everywhere. "\
    + "A large bed sits in the center of the room. Moonlight is illuminating the room. "\
    + "The moonlight is being let in by a set of ornate glass double doors that are to your west."
  foyer = "\n-----Foyer-----\n"\
    + "At the foot of the curving stairs you see a grand entryway with a very dusty chandelier hanging overhead. "\
    + "In front of you (north) is a large set of heavy wooden doors. "\
    + "To your left (west) are pedestals with broken pots lying in pieces around them. "\
    + "To your right (east), a large archway with nothing but darkness beyond it. "\
    + "Behind you (south), are the stairs."
  balcony = "\n-----Balcony-----\n"\
    + "A cold wind blows past as you stand out on the balcony. Below you is an unkept and overgrown garden. "\
    + "Off in the distance you can make out a forest of pine trees. Something else catches your eye. "\
    + "You notice three burly men standing outside the west entrance of the house."
  archway = "\n-----Archway-----\n"\
    + "You start walking in past the archway but it is completely black. "\
    + "You try to go further but the way seems to be blocked off."
  brokenLose = "\n-----West Entrance to the House-----\n"\
    + "You make a loud noise as you accidently step on the broken pieces lying on the ground. "\
    + "Three burly men are alerted and chase after you. "\
    + "You trip and one of the men catches you, attacking you. %s is left lying unconscious on the ground. " % name
  lose = "\n-----Outside to the North-----\n"\
    + "You open the doors and it is too dark to see anything. You hear loud footsteps. "\
    + "Suddenly, you are attacked and now lie unconscious. "\
    + "%s, you have led your character to a bad end." % name
  win = "\n-----Outside to the North-----\n"\
    + "You turn on the flashlight and are able to see a man standing to your right. "\
    + "At this moment the man runs towards you, so you run away. "\
    + "You notice a car with its engine running. You jump inside the car and drive away."
  startNext = "\n-----Driving Car-----\n"\
    +"Driving away from the house you see a fork in the road. You can continue to "\
    +"the right towards the forest or the left towards a lake."
  leftIntro = "Your vehicle breaks through the settling mist sounding the river. Passing through, "\
    +"the only thing visible is the towering packed forestry creeping to the sides of the "\
    +"narrow winding road. confused and shaking you continue the drive through the misting "\
    +"green scenery."
  leftIntro2 = "Suddenly you hear a noise from the engine, panicked you start pressing "\
    +"down harder on the gas paddle. Creeping into your mind is the worst thought possible..."\
    +"avoiding the glaze to the inevitable you see the orange glowing fate of your future...empty. "\
    +"Now that your fate is settling into your mind you keep pursuing on the last fumes of hope "\
    +"which you cling onto. You are able to get down the road a few miles until there is a "\
    +"clearing in the dense woods. the over towing cover from the trees disappear and you can "\
    +"see the clearing mist the sparkling stars above you. This clearing in the woods turned out "\
    +"to be a nestled town for what seems to be made for the working class. Here in this town "\
    +"you see and post office with a town hall adjacent, a steeple from a church so tall it "\
    +"seems to be point the stars above, and most of across from the church is the true hope "\
    +"in your heart...a diner. "\
    +"You pull over the ever fainting car and walk into the diner, hoping to find some"\
    +"answers, or at least a sandwich."
  diner = "\n-----Diner-----\n"\
    +"You press the creaking door open and see the checkered floor below your feet. "\
    +"Feeling overwhelmed by the contrasting colored floor you look straight ahead (north). In front of you "\
    +"is a cold bar top accompanied by a swiveling cushion chair. You look to the left (west) and more "\
    +"chairs and tables. To the right (east) you see an unlabeled door. There is no one to be seen and "\
    +"everything is covered in dust."
    #(north-radio, east-side street, west-key)
    #"You can move north, south, east, or west."
  backToCar = "\n-----Outside of Diner-----\n"\
    +"You leave the diner and head back to the car. You freeze as you see the man from the house, "\
    +"the one who chased you. You quickly turn back but two men grab hold of you and a third knocks you unconscious."
  radio = "\n-----Diner North-----\n"\
    +"Going behind the bar you search through the old items on the shelving. The only thing which "\
    +"appear useful to you is an old red radio."
    #ask player if they want to pick up radio
    #wiping off the dust from the old red radio you notice that the weight seems to be light. Turning the device around you notice that there are no batteries. In desperation you search in vain for replacements, but to no avail. You put the radio away. (south-diner)
    #"You can move south."
  keyDiner = "\n-----Diner West-----\n"\
    +"You start approaching the tables and notice that the plates have been set up for a meal never had. "\
    +"On one plate closest to the you, your flashlight is reflecting back towards you. Walking closer you "\
    +"notice that your light is reflecting off of a key."
    #(east-diner)
    #ask player if they want to pick up the key
    #"You can move east."
  padlock = "\n-----Diner East-----\n"\
    +"Heading towards the door you notice the cold metal framing on the imposing padlocked door. "\
    +"You try to open the door."
    #if player has key ask them if they want to use it
  sideStreet = "\n-----Side Street-----\n"\
    +"You feel the cold brisk air brushing against your face. You are outside on the side street "\
    +"of the diner.\nThe fog has settled back down between the crevices of the buildings. Blanketing you "\
    +"in cold awareness."
    #(west-diner, east-see police)
    #"You can move west or east."
  seePolice = "\n-----Street East-----\n"\
    +"The fog is very thick and it is difficult to see ahead of you as you move down the street. "\
    +"As you move down the street an abandoned police car attracts your attention."
  policeCar = "\n-----Police Car-----\n"\
    +"You walk up to the police car to investigate and notice that the window is broken in the back door "\
    +"windows. Peering into the car you notice a few things on the seat of the car. There seems to be a "\
    +"notepad. "\
    +"You reach and pick up the notepad. Written on the notepad is the number 4825."#Would you like to pick up the notepad?
    #Add notepad to inventory. (you also can search the glove box)
    #Glove Box
    ##+"Looking into the glove box you find something that looks like a gun, but it turns out to be a stun gun. "
    #Would you like to take the stun gun?
    #Continue down the street east (west-side street, east-far street)
  keypad = "\n-----Keypad-----\n"\
    +"You continue to walk forward down the street and up ahead you see what looks to be a police "\
    +"station. You walk up to the door and find that the door is locked with what seems to be a keypad with "\
    +"a red light."
    #Prompt the user for code. Answer is on the notepad.
  wrongCode = "The keypad makes a buzzing noise and falls silent. The light continues to stay red. Seems "\
    +"like the code was incorrect. "
    #(west - see police, north - radio)
  correctCode = "The keypad light turns green and you can hear a faint click as the door opens. "
  policeStation = "\n-----Police Station-----\n"\
    +"Walking into the police station, you quickly close the door behind you and make sure that it locks "\
    +"behind you. Something about the building seems to fill you with ease. This is the first time you have "\
    +"felt completely safe since you first woke up in that house in the forest. An officer asks if you need "\
    +"something and you proceed to tell him what happened. You tell him your name. Turns out your name was "\
    +"all over the news. You had been abducted."
  win2 = "At that moment, a police officer walks in with a man in handcuffs. It is the man who chased you earlier. "\
    +"You tell the officer he was your kidnapper.\nSoon after, a few officers come in with three burly men who "\
    +"were also with your kidnapper. The officer said they were a group of criminals, wanted for robbery. "\
    +"And now, also for second-degree kidnapping."
    #Win
  radioSound = "Traversing through the low visibility there is a low crackling sounds emanating from your body. "\
    +"With panic and tumbling hands, you look around and realize that this sound is from that red radio. The "\
    +"crackling sounds increase and faint shadows can be seen in the fog in front of you."\
    #go to loseRadio
  loseRadio = "The static and crackling sounds are extremely loud and you see three shadows in the fog. They "\
    +"rush towards you and you see it is the three men that you had seen at the house. One of the men jumps "\
    +"forward and tackles you. As you fall your head hits the ground hard and you struggle to stay conscious. "\
    +"The last thing you remember is the men picking you up to take you away."
    #lose
  rightIntro = "Turning the wheel to the right, you drive towards the forest. The tall pine trees line the road "\
    +"as it takes your deeper into the forest. After driving for a while you see that the gas tank is almost "\
    +"empty. In your rush to escape the house and those strange men you did not notice the amount of fuel left "\
    +"in the car. There is a road ahead that leads to a building. You hope it is a gas station."
  rightIntro2 = "The building turns out to be an old lumber mill. There does not seem to be much light coming "\
    +"from the building as you pull up. You get out of the car and walk up to the door. You try to open the door "\
    +"and to your surprise it opens right up."
  entryway ="\n-----Entryway-----\n"\
    +"You walk into the entryway of the factory, there is a reception desk in the center of the room with "\
    +"large doors behind the desk (north). There is also a small door to the right (east) that is tucked away in "\
    +"the corner. To the left (west) is another small door with the word 'Bathroom' written on a sign above it."
    #"You can move north, east, or west."
  factory ="\n-----Factory-----\n"\
    +"You see a large factory floor. You see large saw blades that are rusted and "\
    +"broken. Sawdust and wood chips are everywhere on the floor. You see on the far side (north) of the room a large "\
    +"set of wooden double doors that seem to lead outside."
    #"You can move north or south."
  supplyCloset = "\n-----Supply Closet-----\n"\
    +"You open the door and there is are a few shelves with papers and office supplies stacked on top of "\
    +"them. As you look around for anything useful you see some batteries on the shelf."
    #Would you like to take the batteries?
    #"You can move west."
  bathroomFactory = "\n-----Factory Bathroom-----\n"\
    +"You walk into the bathroom and it is in complete shambles. The mirrors are shattered, the "\
    +"sinks are broken and the stall doors are on the floor. Looking around the room there does not seem to be "\
    +"anything useful."
    #"You can move east."
  outside = "\n-----Outside Factory-----\n"\
    +"Outside there are many large piles of logs stacked. These are creating corridors and looking down "\
    +"across the top of the logs you see what looks to be the headlights of a car."
    #Would you like to go into the logs?
  logs = "\n-----By the Logs-----\n"\
    +"You begin to walk through the logs towards the lights. As you walk through the logs you begin to become "\
    +"lost as every pile of logs looks the same. As you continue to move forward you see a shadow move past your "\
    +"vision and then you hear the sound of wood creaking. Looking behind you, you see the logs beginning to "\
    +"topple over towards you. You begin to run away from the logs but you soon realize that you are not quick "\
    +"enough to outrun the avalanche of logs. Looking forward you see a large boulder up ahead that you could try "\
    +"to hide behind or you can try to jump to the left to avoid the logs."
    #"Would you like to hide or jump?"
  jump = "You quickly jump towards the left and attempt to dive away from the falling logs. As you land on the "\
    +"ground a log slides in front of you. Before you have time to react you crash into the log and fall to the "\
    +"ground. You lay there as logs continue past you and your consciousness fades."
    #lose
  hide = "You decide to hide behind the large boulder. As you reach the boulder you quickly slip around and crouch "\
    +"behind it, while covering your head. You head logs crashing around you and slamming into the boulder, which "\
    +"shifts slightly with each impact. Once the crashing is over you slowly look around and find it difficult to "\
    +"see. The logs have fallen all around you and have trapped you. Looking around you see that there is a small "\
    +"opening that you might be able to crawl through or you could wait to see if anyone notice what had happened. "\
    +"After all that must have created a large noise."
    #(crawl or wait)
    #"You can crawl or wait."
  crawl = "You attempt to crawl through the small opening but as you move forward the logs around you shift "\
    +"slightly and pin you in. You are not completely trapped. As you struggle to wiggle yourself free you see "\
    +"some motion. Looking closer you see it is a man dressed similar to the guy who chased you earlier. He looked "\
    +"down upon you and balls up his hand. He then swings a fist at you and you are knocked unconscious."
    #lose
  wait = "You wait and after some time you hear commotion around your log prison. As you listen you can hear that "\
    +"it sounds like a man talking, definitely not English. It sounds like he is trying to dig you out. As he digs you out, you see that "\
    +"he is dressed similar to the guy who chased you earlier. He swings a fist towards you and you are "\
    +"knocked unconscious."
    #lose

  quitGame = "\n~~%s has quit the game~~" % name
  loser = "Sorry %s, you lose." % name
  winner = "Congratulations %s, you have completed the game!" % name
  
  dict = {"closet":closet, "bedroomSouth":bedroomSouth, "bedroom":bedroom, "bedroomNorth":bedroomNorth, "bathroom":bathroom,
    "hallSouth":hallSouth, "hallNorth":hallNorth, "masterBedroom":masterBedroom, "balcony":balcony, "foyer":foyer, "brokenLose":brokenLose,
    "archway":archway, "lose":lose, "win":win, "intro":intro, "help":help, "quitGame":quitGame, "loser":loser, "winner":winner,
    "startNext":startNext, "leftIntro":leftIntro, "leftIntro2":leftIntro2, "diner":diner, "backToCar":backToCar, "radio":radio,
    "keyDiner":keyDiner, "padlock":padlock, "sideStreet":sideStreet, "seePolice":seePolice, "policeCar":policeCar, "keypad":keypad,
    "wrongCode":wrongCode, "correctCode":correctCode, "policeStation":policeStation, "win2":win2, "radioSound":radioSound,
    "loseRadio":loseRadio, "rightIntro":rightIntro, "rightIntro2":rightIntro2, "entryway":entryway, "factory":factory,
    "supplyCloset":supplyCloset, "bathroomFactory":bathroomFactory, "outside":outside, "logs":logs, "jump":jump,
    "hide":hide, "crawl":crawl, "wait":wait}
  return dict
  
  #------------------------------------------------------------------------------------------------Images
  #----Image Code----
#Darkens all color values in a picture.
def darken(originalPic):
 pic = copy(originalPic)
 pixels = getPixels(pic)
 for p in pixels:
  darkColor = makeDarker(getColor(p))
  setColor(p, darkColor)
 return pic

#Lightens all color values in a circle in the center of an image.
def flashlightFilter(originalPic):
 pic = copy(originalPic)
 circleRadius = min(getHeight(pic), getWidth(pic)) / 2
 for x in range(0, getWidth(pic)):
  for y in range(0, getHeight(pic)):
   #Uses a circle function to detect pixels within a circle of the desired size, then lightens those pixels.
   if (x-(getWidth(pic)/2))**2 + (y-(getHeight(pic)/2))**2 <= (circleRadius-25)**2:
    p = getPixel(pic, x, y)
    lightColor = makeLighter(getColor(p))
    setColor(p, lightColor)
 return pic

#Blurs an image, makes it redder, and adds the text "GAME OVER" to the center.
def gameOver(pic):
 picCopy = copy(pic)
 gameOverPic = moveAndFade(pic, picCopy, 10, factor=4)
 gameOverPic = moreRed(gameOverPic, 50)
 gameOverPic = endText(gameOverPic, "GAME OVER")
 return gameOverPic
 
def moveAndFade(source, target, distance = 0, moveLeft = false, factor=1):
  targetW = getWidth(target)
  targetH = getHeight(target)
  sourceW = getWidth(source)
  sourceH = getHeight(source)
  if(distance > targetW):
    return target    
  xMax = min(distance + sourceW, targetW)
  yMax = min(sourceH, targetH)
  fadeSize = 50
  x = 0
  for destX in range(distance, xMax):
    y = 0
    for destY in range(0, yMax):
      if(moveLeft):
        p = getPixel(source, xMax-x-1, yMax-y-1)
        destPixel = getPixel(target, xMax-destX-1, yMax-destY-1)
      else:
        p = getPixel(source, x, y)
        destPixel = getPixel(target, destX, destY)
      
      if(x<fadeSize*factor):
        # Create a fade in effect
        tempFactor = x-1
        r = (tempFactor*getRed(p)+fadeSize*getRed(destPixel))/(fadeSize+tempFactor)
        g = (tempFactor*getGreen(p)+fadeSize*getGreen(destPixel))/(fadeSize+tempFactor)
        b = (tempFactor*getBlue(p)+fadeSize*getBlue(destPixel))/(fadeSize+tempFactor)
      else:
        # Copy Average, transparent effect
        r = (factor*getRed(p)+getRed(destPixel))/(factor+1)
        g = (factor*getGreen(p)+getGreen(destPixel))/(factor+1)
        b = (factor*getBlue(p)+getBlue(destPixel))/(factor+1)
      setColor(destPixel, makeColor(r,g,b))
      y += 1
    x += 1
  return target

#Makes a copy of a picture
def copy(pic):
  w = getWidth(pic)
  h = getHeight(pic)
  mypic = makeEmptyPicture(w, h)
  for p in getPixels(pic):
    x = getX(p)
    y = getY(p)
    setColor(getPixel(mypic, x, y), getColor(p))
  return mypic

#Increases red value of pixels by n%.
def moreRed(pic, n):
 #Set n to a decimal number appropriate for increase. (100 increased by 75% is 100*1.75)
 n = (100+n) * 0.01
 pixels = getPixels(pic)
 for p in pixels:
  r = getRed(p)
  r = r * n
  #Max value of r is 255
  if r >= 255:
   setRed(p, 255)
  else:
   setRed(p, r)
 return pic

#Adds red "GAME OVER" text to the center of an image.
def endText(pic, string):
 x = (getWidth(pic)/2)-150
 y = (getHeight(pic)/2)-15
 s = makeStyle(sansSerif, italic+bold, 48)
 addTextWithStyle(pic, x, y, string, s, red)
 return pic

def getInventory():
  global inven
  message = "Inventory \n" 
  allFalse = true
  if inven["flashlight"] == true:
    str = "\n A small handheld flashlight. Its light provides some slight comfort within the darkness. \n"
    allFalse = false
    message = message + str
  
  if inven["batteries"] == true:
    str = "\n AA batteries. These seeme to be the correct size for a small flashlight."
    allFalse = false
    message = message + str
  
  if inven["keyHouse"] == true:
    str = "\n \n A small key found in the bathtub. It seems like it might fit a door to a bedroom. \n"
    allFalse = false
    message = message + str
    
  if inven["keyDinner"] == true:
    str = "\n A small key found on a table in the diner. It is very small and seems to be for some type of metal door. \n"
    allFalse = false
    message = message + atr
    
  if inven["radio"] == true:
    str = "\n A small red radio. There does not seems to be a way to open the radio to check the batteries. Oddly enough it still seems to make nosies from time to time. \n"
    allFalse = false
    message = message + str
    
  if allFalse == true:
    str = "\n You do not have anything in your pockets besides lint. \n"
    message = message + str
  showInformation(message)