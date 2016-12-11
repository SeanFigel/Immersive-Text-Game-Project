#Final Project: Immersive Text Game
#Group members: Moises, Nicholas, and Sean
#December 1, 2016
#CST 205

# This is the completed adventure game which asks for user input to move east, west, south, or north
def adventure():
  global name, validMoves
  name = askName()
  validMoves = ["north","south","east","west","n","s","e","w"]
  if(name == "exit"):
    showInformation(messages["quit"])
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
  
  # begin game
  showInformation(messages["help"])
  showInformation(messages["intro"])
  while move != "exit":
  
    # check if user asked for help
    if move == "help":
      showInformation(messages["help"])
    
    # closet
    if location == 1:
      printNow(messages["closet"])
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
        location += 1
    
    # bedroomSouth
    elif location == 2:
      printNow(messages["bedroomSouth"])
      move = askMove("ns", "You can move north or south.")
      if move == "n":
        location += 1
      elif move == "s":
        location -= 1
    
    # bedroom
    elif location == 3:
      printNow(messages["bedroom"])
      move = askMove("ns", "You can move north or south.")
      if move == "n":
        location += 1
      elif move == "s":
        location -= 1
    
    # bedroomNorth
    elif location == 4:
      printNow(messages["bedroomNorth"])
      move = askMove("nse","You can move north, south, or east.")
      if move == "n":
        location += 2
      elif move == "s":
        location -= 1
      elif move == "e":
        location += 1
    
    # bathroom
    elif location == 5:
      printNow(messages["bathroom"])
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
        location -= 1
    
    # hallSouth
    elif location == 6:
      printNow(messages["hallSouth"])
      move = askMove("ns","You can move north or south.")
      if move == "n":
        location += 1
      elif move == "s":
        location -= 2
    
    # hallNorth
    elif location == 7:
      printNow(messages["hallNorth"])
      move = askMove("nse", "You can move north, south, or east.")
      if move == "n":
        showInformation("\n~The door is locked.~")
        if key:
          if(askUseKey()):
            showInformation("You place the key in the lock. You struggle a bit...It works, you opened the door!")
            location += 1
      elif move == "s":
        location -= 1
      elif move == "e":
        showInformation("\n~You are walking down the curved stairs~")
        location += 3
    
    # masterBedroom (secret room)
    elif location == 8:
      printNow(messages["masterBedroom"])
      move = askMove("sw", "You can move south or west.")
      if move == "s":
        showInformation("You make sure to lock the door before you leave the room.")
        location -= 1
      elif move == "w":
        location += 1
    
    # balcony
    elif location == 9:
      printNow(messages["balcony"]) # Clue   
      move = askMove("e","You can move east.")
      if move == "e":
        location -= 1
        
    # stairs/foyer
    elif location == 10:
      printNow(messages["foyer"])
      move = askMove("nsew", "You can move north, south, east, or west.")
      if move == "n":
        location += 3
      elif move == "s":
        showInformation("\n~You are walking up the curved stairs~")
        location -= 3
      elif move == "e":
        location += 2
      elif move == "w":
        location += 1
    
    # brokenPots
    elif location == 11:
      complete = true
      showInformation(messages["brokenLose"]) # print loses chased and attacked in the dark
      showInformation(messages["loser"])
      move = "exit"
    
    # archway
    elif location == 12:
      printNow(messages["archway"])
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
        location -= 2
    
    # woodenDoors
    elif location == 13:
      move = "exit"
      complete = true
      if flashlight == true and batteries == true:
        if(askUseFL()):
          showInformation(messages["win"]) # print loses attacked in the dark
          showInformation(messages["winner"])
          continue
      showInformation(messages["lose"]) # print wins by escaping
      showInformation(messages["loser"])
  if complete == false:
    showInformation(messages["quitGame"])

# This function tells the user there is a flashlight and asks if the user will take it
def askFlashlight():
  showInformation("You open the bag and notice a flashlight. You grab it but it has no batteries.")
  while true:
    userInput = requestString("Would you like to take it with you?")
    userInput = userInput.lower()
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
  showInformation("At the bottom of the tub you notice a shiny piece of metal. You walk over. It's a key!")
  while true:
    userInput = requestString("Would you like to pick it up?")
    userInput = userInput.lower()
    if userInput in ["yes", "y"]:
      showInformation("~~You now have a key!~~")
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
  showInformation("Walking around you step on something. Its a couple of batteries lying on the floor.")
  while true:
    userInput = requestString("Would you like to pick them up?")
    userInput = userInput.lower()
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
    if len(userInput) == 0:
      showInformation("That is not an option " + name + ".[If you're having trouble? type: help]")
      continue
    userInput = userInput.lower()
    if userInput in validMoves:
      userInput = userInput[0]
      if userInput in directions:
        return userInput
    if userInput != "help" and userInput != "exit":
      showInformation("That is not an option " + name + ".[If you're having trouble? type: help]")
  return userInput

def askUseKey():
  while true:
    userInput = requestString("Would you like to try using the key?")
    userInput = userInput.lower()
    if userInput in ["yes", "y"]:
      return true
    if userInput in ["no", "n"]:
      return false
    if userInput == "exit":
      return "exit"
    if userInput == "help":
      return "help"
    showInformation("That's not a good answer " + name + ", you can either say yes or no.")

def askUseFL():
  while true:
    userInput = requestString("It is incredibly dark out here, would you like to use your flashlight?")
    userInput = userInput.lower()
    if userInput in ["yes", "y"]:
      return true
    if userInput in ["no", "n"]:
      return false
    if userInput == "exit":
      return "exit"
    if userInput == "help":
      return "help"
    showInformation("That's not a good answer " + name + ", you can either say yes or no.")

def askName():
  while true:
    tempInput = requestString("Please enter your name:")
    userInput = tempInput.lower()
    if userInput == "":
      showInformation("Name must be at least one character.")
    elif userInput == "exit":
      return "exit"
    elif userInput == "help":
      showInformation(messages["help"])
    else:
      return tempInput 
    
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
    + "You find yourself in a small bedroom. "\
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
    + "You can see some light coming out from under the door in front of you (north). "\
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
  
  dict = {"name":name, "closet":closet, "bedroomSouth":bedroomSouth, "bedroom":bedroom, "bedroomNorth":bedroomNorth, "bathroom":bathroom,
    "hallSouth":hallSouth, "hallNorth":hallNorth, "masterBedroom":masterBedroom, "balcony":balcony, "foyer":foyer, "brokenLose":brokenLose,
    "archway":archway, "lose":lose, "win":win, "intro":intro, "help":help, "quitGame":quitGame, "loser":loser, "winner":winner}
  return dict

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
def flashLight(originalPic):
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