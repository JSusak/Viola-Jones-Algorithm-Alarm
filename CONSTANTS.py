#All constants related to both webcam and phone operations can be found here.

# Change this value to modify the interval at which frames are inspected.
INTERVAL = 30

# Change this variable to modify the universal colour of all shapes in the program. You can also choose to leave it as None, providing random colours.
# Put in the form (g,b,r) otherwise program will crash!
COLOUR = (0, 23, 250)

#OPTIONAL: Change this value if you want to view the algorithm through your Android phone. Requires setup of the 'IP Webcam'
#app by Pavel Khlebovich on the app store. To be honest, I wouldn't bother with this but its there if you want to try :)
#Steps to get this link can be found in the README - it should have the structure "https://abc.def.g.hij:klmn/shot.jpg"
APPURL = None