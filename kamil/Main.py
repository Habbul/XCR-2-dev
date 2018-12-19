import MotionController
import ANet
import time

import buttons_sketch
import Distance
import Thread


print("ANet started")

net = ANet.ANet()

def leak(net):
    while(True):
        net.Leak()
        time.sleep(1)

def Processing(net):
    for i in range(5):
        net.AddNeuron(i)
        net.AddNeuron(i)
   
def pleasure(net):
    buttons_sketch.checkPleasure(net)

def dist(net):
    Distance.checkDistance(net)

def curi(net):
    MotionController.curiosity(MotionController.blocked)


Processing(net)    
buttonsProcessing = Thread.myThread(1, "pleasure",1 , pleasure, net)
leak = Thread.myThread(2,"leak",2 , leak, net)
sonarProcessing = Thread.myThread(3, "pain", 3 , dist, net)
curiosity = Thread.myThread(4, "curi", 4 , curi, net)

leak.start()
buttonsProcessing.start()
sonarProcessing.start()
curiosity.start()
#"""make leak in thread"""



