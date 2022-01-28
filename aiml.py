//pip install aiml
# -*- coding: utf-8 -*-
import aiml
import sys
import os
 
 
def get_module_dir(name):
    print("module", sys.modules[name])
    path = getattr(sys.modules[name], '__file__', None)
    print(path)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))
 
#I have a problem with this place. After installing AIML, the solution to not correctly identifying the path
#Is to find aiml in the Python Installation Path D:\Python-3.7.3\Lib\site-packages
#You can find the python path by typing where python in CMD
#And copy the files under botdata directly to the desktop
alice_path = get_module_dir('aiml') + '\\botdata\\alice'

os.chdir(alice_path)  # switch to the working directory of the Corpus

alice = aiml.Kernel()  # create the robot Alice object
alice.learn("startup.xml") 
alice.respond('LOAD ALICE') 
 
while True:
    message = input("Enter your message >> ")
    if("exit" == message):
        exit()
    response = alice.respond(message) # 机器人应答
    print(response)
#Read more:https://blog.csdn.net/qq_40695642/article/details/100109963
