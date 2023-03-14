import machine
import neopixel
import utils
import time
import random
from asciiBinary import ASCII_MAP

from textRoller import TextRoller
from ledMatrix import LedMatrix
import utils

from phew import logging, server, connect_to_wifi
from secret import ssid, password
from phew.template import render_template

import _thread 



#---------------Configuration-------------------#
content = 'default message'

def rollingTextThread():
    global content
    matrix = LedMatrix()
    
    matrix.clear()
    while 1:
        rgbTuple = (random.randint(0, 15),random.randint(0, 15),random.randint(0, 15))
        print('message is', content)
        matrix.rollToLeftV2(content, 0, rgbTuple, 3)
        
def webServerRun():
    
    

    print('into server function')
    ip = connect_to_wifi(ssid, password)
    logging.info("server start at {}".format(ip))
    
    @server.route("/", ['POST', 'GET'])
    def index(request):
        print(request.method)
        if request.method == 'POST':
            global content
            
            content = request.form.get("content", None)
            
            print(content)
            
            return "update successful, refresh your page"
#         return render_template("index.html")
        return render_template('index.html')


    @server.catchall()
    def myCatch(request):
        return "no matching page", 404
    
    
    server.run()
        
        

_thread.start_new_thread(rollingTextThread, ())

webServerRun() 



