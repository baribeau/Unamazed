#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#                                                                                                      #
#       UU     UU  NN      NN    AAAAAA    MM        MM    AAAAAA    ZZZZZZZZ  EEEEEEE  DDDDD          #
#       UU     UU  NNNN    NN   AA    AA   MMMM    MMMM   AA    AA        ZZ   EE       DD   DD        #
#       UU     UU  NN NN   NN   AA    AA   MM MM  MM MM   AA    AA       ZZ    EE       DD    DD       #
#       UU     UU  NN  NN  NN  AA      AA  MM  MMMM  MM  AA      AA     ZZ     EEEE     DD    DD       #
#       UU     UU  NN   NN NN  AAAAAAAAAA  MM        MM  AAAAAAAAAA    ZZ      EE       DD    DD       #
#        UU   UU   NN    NNNN  AA      AA  MM        MM  AA      AA   ZZ       EE       DD   DD        #
#         UUUUU    NN      NN  AA      AA  MM        MM  AA      AA  ZZZZZZZZ  EEEEEEE  DDDDD          #
#                                                                                                      #
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#  Julia Baribeau  #
#  ICS 3UI         #
#  Mr. Schattman   #
#  June 21, 2017   #
#++++++++++++++++++#
 
from tkinter import *
from math import *
from time import *
from random import *
 
root = Tk()
s = Canvas( root, width=800, height=800, background="white" )
 
# Called at beginning of game 
def setInitialValues():
    global rPressed, colour1,colour2,colour3, curLayer, \
           xMouse, yMouse, player, curSq, exSq, aBoxes,bBoxes, ladderImage, \
           holeImage, clockDisplay, startTime, gameTime, minutes, seconds
           
    # Defining each colour depending on the palette chosen 
    if palette == "salt&pepper":
        colour1 = "white"
        colour2 = "black"
        colour3 = "red"
        holeImage = PhotoImage(file="hole-black.gif") 
        ladderImage = PhotoImage(file="ladder-white.gif")
        
    elif palette == "citrus":
        colour1 = "#F7E92F"
        colour2 = "#7DB300"
        colour3 = "#FF8800"
        holeImage = PhotoImage(file="hole-lime.gif") 
        ladderImage = PhotoImage(file="ladder-yellow.gif")
        
    elif palette == "plum":
        colour1 = "#C5AEE8"
        colour2 = "#A12D2D"
        colour3 = "#A757ED"
        holeImage = PhotoImage(file="hole-maroon.gif") 
        ladderImage = PhotoImage(file="ladder-violet.gif")
        
    elif palette == "water":
        colour1 = "#84C7D9"
        colour2 = "#224478"
        colour3 = "white"
        holeImage = PhotoImage(file="hole-navy.gif") 
        ladderImage = PhotoImage(file="ladder-turq.gif")
        
    else:
        colour1 = "#B87B53"
        colour2 = "#005400"
        colour3 = "#87E27F"
        holeImage = PhotoImage(file="hole-drkgreen.gif") 
        ladderImage = PhotoImage(file="ladder-brown.gif")
 
    rPressed = False
    
    startTime = time()
    gameTime = 0
    minutes = 0
    seconds = 0
    clockDisplay = s.create_text(100,50, text = "00:00", font = "Courier 20", fill = colour2)
 
 
    # This is how the game knows where the maze walls are. Each array corresponds to a square in a 10x10 grid, where the last element (and
    #  the number in the aray name) is the location of the box——the first digit is the row, the second digit is the column. The first 4 elements
    #  define if there is a wall on the north, east, south, or west side of that particular box, respectively. The 5th element defines whether or
    #  not the character can switch layers (hole/ladder). These values were entered by hand.
 
    # For the layer above, that the player starts on:
    a00 = [1, 0, 0, 1, 0, 0]
    a01 = [1, 1, 0, 0, 0, 1]
    a02 = [1, 0, 0, 1, 0, 2]
    a03 = [1, 0, 1, 0, 0, 3]
    a04 = [1, 1, 0, 0, 0, 4]
    a05 = [1, 0, 0, 1, 0, 5]
    a06 = [1, 1, 1, 0, 1, 6]
    a07 = [1, 0, 0, 1, 0, 7]
    a08 = [1, 0, 1, 0, 0, 8]
    a09 = [1, 1, 1, 0, 0, 9]
    a10 = [0, 1, 0, 1, 0, 10]
    a11 = [0, 1, 0, 1, 0, 11]
    a12 = [0, 1, 0, 1, 0, 12]
    a13 = [1, 0, 0, 1, 0, 13]
    a14 = [0, 1, 1, 0, 0, 14]
    a15 = [0, 0, 1, 1, 0, 15]
    a16 = [1, 1, 0, 0, 0, 16]
    a17 = [0, 0, 1, 1, 0, 17]
    a18 = [1, 1, 0, 0, 0, 18]
    a19 = [1, 1, 0, 1, 0, 19]
    a20 = [0, 1, 0, 1, 0, 20]
    a21 = [0, 1, 1, 1, 0, 21]
    a22 = [0, 1, 0, 1, 0, 22]
    a23 = [0, 0, 1, 1, 0, 23]
    a24 = [1, 1, 0, 0, 0, 24]
    a25 = [1, 0, 1, 1, 0, 25]
    a26 = [0, 0, 1, 0, 0, 26]
    a27 = [1, 1, 0, 0, 0, 27]
    a28 = [0, 1, 0, 1, 0, 28]
    a29 = [0, 1, 0, 1, 0, 29]
    a30 = [0, 0, 1, 1, 0, 30]
    a31 = [1, 0, 1, 0, 0, 31]
    a32 = [0, 1, 1, 0, 0, 32]
    a33 = [1, 0, 0, 1, 0, 33]
    a34 = [0, 1, 1, 0, 0, 34]
    a35 = [1, 0, 0, 1, 0, 35]
    a36 = [1, 0, 0, 0, 0, 36]
    a37 = [0, 1, 1, 0, 0, 37]
    a38 = [0, 1, 1, 1, 1, 38]
    a39 = [0, 1, 0, 1, 0, 39]
    a40 = [1, 0, 0, 1, 0, 40]
    a41 = [1, 0, 1, 0, 0, 41]
    a42 = [1, 1, 0, 0, 0, 42]
    a43 = [0, 0, 1, 1, 0, 43]
    a44 = [1, 1, 1, 0, 1, 44]
    a45 = [0, 1, 1, 1, 0, 45]
    a46 = [0, 0, 1, 1, 0, 46]
    a47 = [1, 0, 1, 0, 0, 47]
    a48 = [1, 1, 0, 0, 0, 48]
    a49 = [0, 1, 0, 1, 0, 49]
    a50 = [0, 1, 1, 1, 1, 50]
    a51 = [1, 1, 0, 1, 1, 51]
    a52 = [0, 1, 0, 1, 0, 52]
    a53 = [1, 0, 0, 1, 0, 53]
    a54 = [1, 1, 0, 0, 0, 54]
    a55 = [1, 0, 0, 1, 0, 55]
    a56 = [1, 0, 0, 0, 0, 56]
    a57 = [1, 1, 1, 0, 0, 57]
    a58 = [0, 0, 0, 1, 0, 58]
    a59 = [0, 1, 1, 0, 0, 59]
    a60 = [1, 1, 0, 1, 0, 60]
    a61 = [0, 1, 0, 1, 0, 61]
    a62 = [0, 0, 1, 1, 0, 62]
    a63 = [0, 1, 1, 0, 0, 63]
    a64 = [0, 0, 1, 1, 0, 64]
    a65 = [0, 1, 1, 0, 0, 65]
    a66 = [0, 0, 1, 1, 0, 66]
    a67 = [1, 0, 0, 0, 0, 67]
    a68 = [0, 1, 1, 0, 0, 68]
    a69 = [1, 1, 0, 1, 0, 69]
    a70 = [0, 0, 1, 1, 0, 70]
    a71 = [0, 1, 0, 0, 0, 71]
    a72 = [1, 0, 0, 1, 0, 72]
    a73 = [1, 0, 1, 0, 0, 73]
    a74 = [1, 0, 1, 0, 0, 74]
    a75 = [1, 0, 0, 0, 0, 75]
    a76 = [1, 1, 1, 0, 0, 76]
    a77 = [0, 0, 1, 1, 0, 77]
    a78 = [1, 0, 1, 0, 0, 78]
    a79 = [0, 1, 0, 0, 0, 79]
    a80 = [1, 1, 0, 1, 0, 80]
    a81 = [0, 0, 1, 1, 0, 81]
    a82 = [0, 1, 1, 0, 0, 82]
    a83 = [1, 0, 0, 1, 0, 83]
    a84 = [1, 1, 0, 0, 0, 84]
    a85 = [0, 0, 0, 1, 0, 85]
    a86 = [1, 1, 0, 0, 0, 86]
    a87 = [1, 1, 0, 1, 1, 87]
    a88 = [1, 1, 0, 1, 0, 88]
    a89 = [0, 1, 1, 1, 1, 89]
    a90 = [0, 0, 1, 1, 0, 90]
    a91 = [1, 0, 1, 0, 0, 91]
    a92 = [1, 0, 1, 0, 0, 92]
    a93 = [0, 1, 1, 0, 0, 93]
    a94 = [0, 0, 1, 1, 0, 94]
    a95 = [0, 1, 1, 0, 0, 95]
    a96 = [0, 0, 1, 1, 0, 96]
    a97 = [0, 1, 1, 0, 0, 97]
    a98 = [0, 0, 1, 1, 0, 98]
    a99 = [1, 1, 1, 0, 0, 99]
 
    # For the layer below, that the player finishes on:
    b00 = [1, 0, 0, 1, 0, 0]
    b01 = [1, 0, 1, 0, 0, 1]
    b02 = [1, 0, 1, 0, 0, 2]
    b03 = [1, 0, 1, 0, 0, 3]
    b04 = [1, 0, 1, 0, 0, 4]
    b05 = [1, 0, 1, 0, 0, 5]
    b06 = [1, 0, 1, 0, 0, 6]
    b07 = [1, 0, 1, 0, 0, 7]
    b08 = [1, 1, 0, 0, 0, 8]
    b09 = [1, 1, 0, 1, 1, 9]
    b10 = [0, 1, 0, 1, 0, 10]
    b11 = [1, 0, 0, 1, 0, 11]
    b12 = [1, 0, 1, 0, 0, 12]
    b13 = [1, 0, 1, 0, 0, 13]
    b14 = [1, 1, 0, 0, 0, 14]
    b15 = [1, 0, 0, 1, 0, 15]
    b16 = [1, 0, 1, 0, 0, 16]
    b17 = [1, 1, 0, 0, 0, 17]
    b18 = [0, 1, 0, 1, 0, 18]
    b19 = [0, 1, 0, 1, 0, 19]
    b20 = [0, 1, 0, 1, 0, 20]
    b21 = [0, 0, 0, 1, 0, 21]
    b22 = [1, 0, 1, 0, 0, 22]
    b23 = [1, 1, 0, 0, 0, 23]
    b24 = [0, 1, 0, 1, 0, 24]
    b25 = [0, 0, 1, 1, 0, 25]
    b26 = [1, 1, 0, 0, 0, 26]
    b27 = [0, 1, 0, 1, 0, 27]
    b28 = [0, 0, 1, 1, 0, 28]
    b29 = [0, 1, 1, 0, 0, 29]
    b30 = [0, 0, 1, 1, 0, 30]
    b31 = [0, 1, 1, 0, 0, 31]
    b32 = [1, 0, 0, 1, 0, 32]
    b33 = [0, 1, 1, 0, 0, 33]
    b34 = [0, 0, 1, 1, 0, 34]
    b35 = [1, 1, 0, 0, 0, 35]
    b36 = [0, 1, 0, 1, 0, 36]
    b37 = [0, 1, 1, 1, 1, 37]
    b38 = [1, 0, 0, 1, 0, 38]
    b39 = [1, 1, 1, 0, 0, 39]
    b40 = [1, 0, 0, 1, 0, 40]
    b41 = [1, 1, 1, 0, 1, 41]
    b42 = [0, 0, 1, 1, 0, 42]
    b43 = [1, 0, 1, 0, 0, 43]
    b44 = [1, 1, 1, 0, 0, 44]
    b45 = [0, 0, 1, 1, 0, 45]
    b46 = [0, 1, 1, 0, 0, 46]
    b47 = [1, 1, 0, 1, 1, 47]
    b48 = [0, 1, 0, 1, 0, 48]
    b49 = [1, 1, 0, 1, 1, 49]
    b50 = [0, 0, 1, 1, 0, 50]
    b51 = [1, 1, 1, 0, 0, 51]
    b52 = [1, 1, 0, 1, 0, 52]
    b53 = [1, 0, 0, 1, 0, 53]
    b54 = [1, 1, 0, 0, 0, 54]
    b55 = [1, 1, 0, 1, 1, 55]
    b56 = [1, 0, 0, 1, 0, 56]
    b57 = [0, 1, 1, 0, 0, 57]
    b58 = [0, 0, 1, 1, 0, 58]
    b59 = [0, 1, 1, 0, 0, 59]
    b60 = [1, 0, 0, 1, 0, 60]
    b61 = [1, 0, 0, 0, 0, 61]
    b62 = [0, 0, 1, 0, 0, 62]
    b63 = [0, 1, 1, 0, 0, 63]
    b64 = [0, 0, 0, 1, 0, 64]
    b65 = [0, 1, 0, 0, 0, 65]
    b66 = [0, 1, 0, 1, 0, 66]
    b67 = [1, 0, 1, 1, 0, 67]
    b68 = [1, 0, 1, 0, 0, 68]
    b69 = [1, 1, 0, 0, 0, 69]
    b70 = [0, 1, 0, 1, 0, 70]
    b71 = [0, 1, 0, 1, 0, 71]
    b72 = [1, 0, 1, 1, 0, 72]
    b73 = [1, 0, 1, 0, 0, 73]
    b74 = [0, 1, 1, 0, 0, 74]
    b75 = [0, 0, 1, 1, 0, 75]
    b76 = [0, 0, 1, 0, 0, 76]
    b77 = [1, 0, 1, 0, 0, 77]
    b78 = [1, 1, 0, 0, 0, 78]
    b79 = [0, 1, 0, 1, 0, 79]
    b80 = [0, 1, 0, 1, 0, 80]
    b81 = [0, 0, 1, 1, 0, 81]
    b82 = [1, 0, 1, 0, 0, 82]
    b83 = [1, 0, 1, 0, 0, 83]
    b84 = [1, 0, 1, 0, 0, 84]
    b85 = [1, 1, 0, 0, 0, 85]
    b86 = [1, 0, 1, 1, 0, 86]
    b87 = [1, 1, 0, 0, 0, 87]
    b88 = [0, 0, 1, 1, 0, 88]
    b89 = [0, 1, 1, 0, 0, 89]
    b90 = [0, 0, 1, 1, 0, 90]
    b91 = [1, 0, 1, 0, 0, 91]
    b92 = [1, 0, 1, 0, 0, 92]
    b93 = [1, 0, 1, 0, 0, 93]
    b94 = [1, 1, 1, 0, 1, 94]
    b95 = [0, 1, 1, 1, 0, 95]
    b96 = [1, 0, 1, 1, 0, 96]
    b97 = [0, 0, 1, 0, 0, 97]
    b98 = [1, 0, 1, 0, 0, 98]
    b99 = [1, 1, 1, 0, 0, 99]
        
    aBoxes = [a00,a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49,a50,a51,a52,a53,a54,a55,a56,a57,a58,a59,a60,a61,a62,a63,a64,a65,a66,a67,a68,a69,a70,a71,a72,a73,a74,a75,a76,a77,a78,a79,a80,a81,a82,a83,a84,a85,a86,a87,a88,a89,a90,a91,a92,a93,a94,a95,a96,a97,a98,a99]
    bBoxes = [b00,b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,b81,b82,b83,b84,b85,b86,b87,b88,b89,b90,b91,b92,b93,b94,b95,b96,b97,b98,b99]
 
    curLayer = "above"
    curSq = a00 # You can change this to start anywhere in the maze, but make sure to change curLayer to match
    exSq = b99
    player = 0
    
    xMouse = 0
    yMouse = 0


def drawIntroScreen():
    global startButton, saltpepperButton,citrusButton,plumButton,waterButton,dirtButton, \
           palette, saltpepperImage, citrusImage, plumImage, waterImage, dirtImage, titleImage

    s.create_rectangle(0,0,800,800, fill = "white")

    # Getting the image files
    titleImage = PhotoImage(file="title.gif")
    saltpepperImage = PhotoImage(file="saltpepper.gif")
    citrusImage = PhotoImage(file="citrus.gif")
    plumImage = PhotoImage(file="plum.gif")
    waterImage = PhotoImage(file="water.gif")
    dirtImage = PhotoImage(file="dirt.gif")

    # Creating the buttons
    startButton = Button(root, text = "START", font = "Courier 20 bold", command = startButtonPressed, anchor = CENTER)
    startButton.pack()
    startButton.place(x=325,y=600, width=150, height = 70)

    saltpepperButton = Button(root, image=saltpepperImage, command = saltpepperChosen, anchor = CENTER)
    saltpepperButton.pack()
    saltpepperButton.place(x=36,y=400, width=112, height=47)
    s.create_text(92,460, text = "Salt & Pepper", font = "Courier 15")
    
    citrusButton = Button(root, image=citrusImage, command = citrusChosen, anchor = CENTER)
    citrusButton.pack()
    citrusButton.place(x=190,y=400, width=112, height=47)
    s.create_text(246,460, text = "Citrus", font = "Courier 15")

    plumButton = Button(root, image=plumImage, command = plumChosen, anchor = CENTER)
    plumButton.pack()
    plumButton.place(x=344,y=400, width=112, height=47)
    s.create_text(400,460, text = "Plum", font = "Courier 15")

    waterButton = Button(root, image=waterImage, command = waterChosen, anchor = CENTER)
    waterButton.pack()
    waterButton.place(x=494,y=400, width=112, height=47)
    s.create_text(550,460, text = "Water", font = "Courier 15")

    dirtButton = Button(root, image=dirtImage, command = dirtChosen, anchor = CENTER)
    dirtButton.pack()
    dirtButton.place(x=648,y=400, width=112, height=47)
    s.create_text(704,460, text = "Dirt", font = "Courier 15")

    # Creating the title and palette message
    s.create_image(400,170, image = titleImage, anchor = CENTER)
    s.create_text(400,350, text = "Choose a 'tasty' colour palette!", font = "Courier 15", anchor = CENTER)
    
# Called when the player clicks "start"
def startButtonPressed():
    global gameMode, startButton, saltpepperButton,citrusButton,plumButton,waterButton,dirtButton, ovals

    # Get rid of all the buttons
    startButton.destroy()
    saltpepperButton.destroy()
    citrusButton.destroy()
    plumButton.destroy()
    waterButton.destroy()
    dirtButton.destroy()

##    for o in range(len(ovals)):
##        s.delete(ovals[o])

    # Change gameMode to play and run the game
    gameMode = "play"
    runGame()

# Commands for the palette buttons
def saltpepperChosen():
    global palette
    palette = "salt&pepper"
def citrusChosen():
    global palette
    palette = "citrus"
def plumChosen():
    global palette
    palette = "plum"
def waterChosen():
    global palette
    palette = "water"
def dirtChosen():
    global palette
    palette = "dirt"
 
# Called when game starts, and whenever the player switches layers 
def drawLayer():
    global clockDisplay
    s.delete(clockDisplay)

    # Inverses colours for the bottom layer
    if curLayer == "above":
        s.create_rectangle(0,0,800,800,fill = colour1, outline = colour1)
        s.create_text(400,750, text = "Use the arrow keys to move. Press r to restart.", fill = colour2, font = "Courier 14", anchor = CENTER)
        drawTimer(colour2)
    else:
        s.create_rectangle(0,0,800,800,fill = colour2, outline = colour2)
        s.create_text(400,750, text = "Use the arrow keys to move. Press r to restart.", fill = colour1, font = "Courier 14", anchor = CENTER)
        drawTimer(colour1)
     
    xBox = 100 # Coords of top left corner of the box about to be drawn
    yBox = 100
        
    if curLayer == "above":
                
        for j in range(10): #columns
            for i in range(10): #rows
                k = j*10 + i  # This gets the numerical value of the specific box we need to look at
                if aBoxes[k][4] == 1:
                    s.create_image(xBox+30,yBox+30, image = holeImage, anchor = CENTER)# Draws the holes
                if aBoxes[k][0] == 1:
                    s.create_line(xBox,yBox, xBox+60,yBox, width = 2, fill = colour2) # Draw north wall
                if aBoxes[k][1] == 1:
                    s.create_line(xBox+60,yBox, xBox+60,yBox+60, width = 2, fill = colour2) # Draw east wall
                if aBoxes[k][2] == 1:
                    s.create_line(xBox,yBox+60, xBox+60,yBox+60, width = 2, fill = colour2) # Draw south wall
                if aBoxes[k][3] == 1:
                    s.create_line(xBox,yBox, xBox,yBox+60, width = 2, fill = colour2) #Draw west wall
                xBox += 60 # Go to next column in this row
            xBox = 100 # Starting back at the first column of the row
            yBox += 60 # Go to next row down
 
    else:
        s.create_rectangle(640,640, 700,700, fill = colour3, outline = colour3) # "FINISH" square
        s.create_text(670,670, text = "FINISH", fill = colour2, font = "Courier 10 bold")
                
        for j in range(10):
            for i in range(10):
                k = j*10 + i
                if bBoxes[k][4] == 1:
                    s.create_image(xBox+30,yBox+30, image = ladderImage, anchor = CENTER) # We're on the bottom layer so draw ladders, not holes
                if bBoxes[k][0] == 1:
                    s.create_line(xBox,yBox, xBox+60,yBox, width = 2, fill = colour1)
                if bBoxes[k][1] == 1:
                    s.create_line(xBox+60,yBox, xBox+60,yBox+60, width = 2, fill = colour1)
                if bBoxes[k][2] == 1:
                    s.create_line(xBox,yBox+60, xBox+60,yBox+60, width = 2, fill = colour1)
                if bBoxes[k][3] == 1:
                    s.create_line(xBox,yBox, xBox,yBox+60, width = 2, fill = colour1)
                xBox += 60
            xBox = 100
            yBox += 60     
 
        s.update() # Makes the maze appear
 
def addZero(n): # Only used when drawing the clock, so it looks like 01:08 instead of 1:8
    if n < 10: # So it doesn't give us 04:016 when we want 04:16
        pre = "0"
    else:
        pre = ""
 
    return pre
 
def drawTimer(col): # Gets called every second
    global clockDisplay, minutes, seconds, gameTime
 
    s.delete(clockDisplay) # Deletes the timer from a second ago
    seconds = gameTime # gameTime is how many seconds have passed so far in the game
    if seconds / 60 >= 1: # Every 60 secs, increase the amount of minutes by 1
        minutes += 1
        gameTime = 0
 
    # Calling the addZero function seen above
    sec0 = addZero(seconds) 
    min0 = addZero(minutes)
        
    clockDisplay = s.create_text(400,50, text = min0 + str(round(minutes))+":"+ sec0 + str(round(seconds)), font = "Courier 20", fill = col, anchor = CENTER)
                                        #   preceding 0 + minute value + colon + preceding 0 + seconds value 
    s.update() # Makes the timer appear
    
def playerAtExit(): # During the runGame procedure below, if playerAtExit == True, it stops the game
    if curSq == exSq:
        return True
    else:
        return False
 
# Used to find coordinates of the current square in the 10x10 grid 
def findxyDigit(curSq,digit):  # Digit will be entered as 0 if we want to find the row number, 1 if we want to find the column number
    num = str(curSq[5]) 
    value = int(num[digit])
    return value
 
# Finds the current position of the player and draws the red ball on screen
def drawPlayer():
    global player
    if len(str(curSq[5])) < 2: # Have to test for this because python doesn't recognize 03 or 08 etc as two-digit numbers
        yPlayer = 100
    else:
        yPlayer = 100 + 60*findxyDigit(curSq,0)
 
    xPlayer = 100 + 60*findxyDigit(curSq,-1)
 
    player = s.create_oval(xPlayer+10,yPlayer+10,xPlayer+50,yPlayer+50, fill = colour3, outline = colour3) # Draws the ball
 
# Function gets called whenever the mouse is clicked 
def mouseClickHandler(event):
    global xMouse, yMouse
 
    xMouse = event.x
    yMouse = event.y

##    if gameMode == "intro":
##        funStuffIntroScreen()

##def funStuffIntroScreen():
##    global ovals
##    r = randint(2,15)
##    colour = choice(["red","orange","yellow"])
##    ovals = []
##    curOval = s.create_oval(xMouse-r, yMouse-r, xMouse+r, yMouse+r, fill = colour)
##    ovals.append(curOval)
 
# Gets called whenever a key is pressed
def keyDownHandler(event):
    global curSq, rPressed
 
    i = curSq[5]
    if gameMode == "play": 
        if curLayer == "above": # See which set of arrays we're dealing with 
            if event.keysym == "Up":
                if aBoxes[i][0] == 0:
                    i -= 10 
                    
            if event.keysym == "Right":
                if aBoxes[i][1] == 0:
                    i += 1 
                    
            if event.keysym == "Down":
                if aBoxes[i][2] == 0:
                    i += 10
     
            if event.keysym == "Left":
                if aBoxes[i][3] == 0:
                    i -= 1
     
            curSq = aBoxes[i] # Changes the value for curSq depending on which direction we're going (on the top layer)
     
        else:
            if event.keysym == "Up":
                if bBoxes[i][0] == 0:
                    i -= 10
                    
            if event.keysym == "Right":
                if bBoxes[i][1] == 0:
                    i += 1
                    
            if event.keysym == "Down":
                if bBoxes[i][2] == 0:
                    i += 10
     
            if event.keysym == "Left":
                if bBoxes[i][3] == 0:
                    i -= 1           
     
            curSq = bBoxes[i] # Changes the value for curSq depending on which direction we're going (on the bottom layer)
     
     
        if event.keysym == "r" or event.keysym == "R": # Restart
            rPressed = True
            
# Gets called when the player completes the maze 
def endGame():
    global playAgainButton, quitButton
    s.create_rectangle(0,0,800,800, fill = colour1, outline = colour1)
    s.create_text(400,350, text = "You win!", font = "Courier 40", fill = colour2)
    sec0 = addZero(seconds) # See "drawTimer" for explanation of these next 3 lines
    min0 = addZero(minutes)
    s.create_text(400,450, text = "Your time was " + min0 + str(round(minutes))+":"+ sec0 + str(round(seconds)), font = "Courier 30", fill = colour2)

    playAgainButton = Button(root, text= "PLAY AGAIN", font = "Courier 20", command = playAgain, anchor = CENTER)
    playAgainButton.pack()
    playAgainButton.place(x=400,y=600, width=200,height=25, anchor = E)

    quitButton = Button(root, text = "QUIT", font = "Courier 20", command = quitGame, anchor = CENTER)
    quitButton.pack()
    quitButton.place(x=400, y=600, width=140, height=25, anchor = W)

def quitGame():
    root.destroy()
    raise SystemExit()

# Called if player clicks "play again"
def playAgain():
    global playAgainButton, quitButton
    playAgainButton.destroy()
    quitButton.destroy()
    intro() # Sends us back to the beginning

# First procedure the code runs
def intro():
    global gameMode, palette

    palette = "salt&pepper" # In case the player doesn't choose a palette, s&p is the default
    gameMode = "intro" # Makes sure nothing changes if the player presses keys before the game starts
    drawIntroScreen()
 
# Runs the game 
def runGame():
    global curLayer, curSq, startTime, gameTime, clockDisplay

    setInitialValues()
    drawLayer()
    
    while playerAtExit() == False and rPressed == False: 
        
        drawPlayer()
        i = curSq[5]
        if curSq[4]==1: # If this square has a hole or a ladder,
            if curLayer == "above":
                curLayer = "below" # switch to the opposite layer
                curSq = bBoxes[i] # Now that we're on the bottom layer, we're dealing with the b arrays
            else:
                curLayer = "above"
                curSq = aBoxes[i]
            drawLayer() # Draw the new layer
 
        curTime = time() # Time function is built in, gives how many seconds it's been since Dec 31, 1969
        deltaTime = curTime - startTime # startTime was defined in setInitialValues()
        if deltaTime >= 1: # If a second has passed,
            gameTime += 1 # increase gameTime by 1 second,
            # update the timer to show the new time,
            if curLayer == "above":
                drawTimer(colour2) 
            else:
                drawTimer(colour1)
            startTime = time() # and start counting until the next second
        else:
            s.update()
            
        s.update() 
        sleep(0.01)
        s.delete(player)
     
            
    if rPressed == False: # Don't show ending screen if the player simply restarted
        endGame() # If playerAtExit == True, the game ends
    else: # If player pressed "r", restart the game
        runGame()
 
root.after(0, intro) # Start the game immediately
s.bind( "<Button-1>", mouseClickHandler) # Call the function mouseClickHandler if the mouse is left-clicked
s.bind( "<Key>", keyDownHandler) # Call the function keyDownHandler if a key is pressed
 
s.pack()
s.focus_set()
root.mainloop()
 
 
 
 
 
 
