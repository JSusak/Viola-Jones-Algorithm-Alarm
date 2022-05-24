#CODE IS HERE if you want to run a function EXACTLY once throughout the duration of the loop.

#import threading
#import queue
#import winsound
#from cv2 import add
#from time import sleep
from playsound import playsound

#q = queue.Queue()
#def runOnce(f):
        #async def wrapper(*args, **kwargs):
                #if not wrapper.has_run or wrapper.run_again:
                        #wrapper.has_run = True
                        #await asyncio.sleep(3)
                        #return f(*args, **kwargs)

        #wrapper.has_run = False
        #wrapper.run_again = True
        #return wrapper

#Asynchronously play a sound in the resources folder.
def playSound(sound,extension):
        playsound("resources/"+sound+"."+extension,block=False)

