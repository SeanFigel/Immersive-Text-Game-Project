# Adventure Game Updates
# This is the updated adventure game which asks for user input to move east, west, south, or north
def adventure():
  global name, validMoves, sounds
  
  # Room sounds
  sounds = getSoundsDict()
  play(sounds["start"])
  name = askName()
  validMoves = ["north","south","east","west","n","s","e","w"]
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
  
  # default values
  flashlight = false #item
  batteries = false #item
  key = false #item
  location = 3 # bedroom
  
  move = ""
  complete = false
  
  # Begin game
  showInformation(messages["help"])
  play(sounds["intro"])
  showInformation(messages["intro"])
  stopPlaying(sounds["intro"])
  while move != "exit":
  
    # Check if user asked for help
    if move == "help":
      showInformation(messages["help"])
    
    # Closet
    if location == 1:
      play(sounds["closet"])
      showInformation(messages["closet"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["closet"])
      if flashlight == false:
        flashlight = askFlashlight()
        if flashlight == "exit":
          break
        if flashlight == "help":
          flashlight = false
          move = "help"
          continue
      move = askMove("n", "You can move north.")
      if move == "n":
        play(sounds["openClose"])
        location += 1
    
    # Bedroom South
    elif location == 2:
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
      play(sounds["bathroom"])
      showInformation(messages["bathroom"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["bathroom"])
      if key == false:
        key = askKey()
        if key == "exit":
          break
        if key == "help":
          key = false
          move = "help"
          continue
      move = askMove("w", "You can move west.")
      if move == "w":
        play(sounds["openClose"])
        location -= 1
    
    # Hall South
    elif location == 6:
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
      play(sounds["hallNorth"])
      showInformation(messages["hallNorth"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["hallNorth"])
      move = askMove("nse", "You can move north, south, or east.")
      if move == "n":
        play(sounds["lockedDoor"])
        showInformation("\n~The door is locked.~")
        stopPlaying(sounds["lockedDoor"])
        if key:
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
      play(sounds["balcony"])
      showInformation(messages["balcony"]) # Clue
      stopPlaying(sounds["balcony"])
      move = askMove("e","You can move east.")
      if move == "e":
        play(sounds["balconyClose"])
        location -= 1
        
    # Stairs/Foyer
    elif location == 10:
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
        play(sounds["openClose"])
        location += 2
      elif move == "w":
        location += 1
    
    # Broken Pots
    elif location == 11:
      complete = true
      play(sounds["brokenLose"])
      showInformation(messages["brokenLose"]) # print loses chased and attacked in the dark
      showInformation(messages["loser"])
      move = "exit"
    
    # Archway
    elif location == 12:
      play(sounds["archway"])
      showInformation(messages["archway"])
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["archway"])
      if batteries == false:
        batteries = askBatteries()
        if batteries == "exit":
          break
        if batteries == "help":
          batteries = false
          move = "help"
          continue
      move = askMove("w", "You can move west.")
      if move == "w":
        play(sounds["openClose"])
        location -= 2
    
    # Wooden Doors
    elif location == 13:
      move = "exit"
      complete = true
      if flashlight == true and batteries == true:
        if(askUseFL()):
          play(sounds["woodenDoors"])
          showInformation(messages["win"]) # print wins by escaping
          stopPlaying(sounds["openClose"])
          stopPlaying(sounds["woodenDoors"])
          showInformation(messages["winner"])
          continue
      play(sounds["woodenLose"])
      showInformation(messages["lose"]) # print loses attacked in the dark
      stopPlaying(sounds["openClose"])
      stopPlaying(sounds["woodenLose"])
      showInformation(messages["loser"])
  for key, sound in sounds.iteritems():
      try:
        stopPlaying(sound)
      except:
        continue
  if complete == false:
    showInformation(messages["quitGame"])
    
# This function tells the user there is a flashlight and asks if the user will take it
def askFlashlight():
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
      return true
    if userInput in ["no", "n"]:
      return false
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
      return true
    if userInput in ["no", "n"]:
      return false
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
    if userInput != "help" and userInput != "exit":
      showInformation("That is not an option " + name + ".[If you're having trouble? type: help]")
  return userInput

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
    + "A cold wind blows past as you stand out on the balcony. Below you is a unkept and overgrown garden. "\
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
    + "You open the doors and notice it is incredibly dark. "\
    + "So you turn on the flashlight and are able to see a man standing to your right. "\
    + "At this moment the man runs towards you, so you run away. "\
    + "You notice a car with its engine running. You jump inside the car and drive away. "\
    + "Congratulations, %s. You made it out safe!" % name
  quitGame = "\n~~%s has quit the game~~" % name
  loser = "Sorry %s, you lose." % name
  winner = "Congratulations %s, you made it out safe!" % name
  
  dict = {"closet":closet, "bedroomSouth":bedroomSouth, "bedroom":bedroom, "bedroomNorth":bedroomNorth, "bathroom":bathroom,
    "hallSouth":hallSouth, "hallNorth":hallNorth, "masterBedroom":masterBedroom, "balcony":balcony, "foyer":foyer, "brokenLose":brokenLose,
    "archway":archway, "lose":lose, "win":win, "intro":intro, "help":help, "quitGame":quitGame, "loser":loser, "winner":winner}
  return dict

def getSound():
  """ Gets a sound from a file
  
  Returns the sound of the file selected
  """
  return makeSound(pickAFile())
  
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