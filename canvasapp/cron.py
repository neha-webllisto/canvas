#canvasapp/cron.py

import kronos
import random
 
@kronos.register('* * * * *')
def complaining():
    f = open("demofile.txt", "a")
    f.write("Now the file has one more line!")
