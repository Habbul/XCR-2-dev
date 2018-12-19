import ANet
import time
import Thread
import MotionController

def leak(net):
    while(True):
        net.Leak()
        time.sleep(1)

def Processing(net):
    for i in range(4):
        net.AddNeuron(i)
        net.AddNeuron(i)
   


print("ANet demo:")
net = ANet.ANet()
thr = Thread.myThread(1, "leak",1 , Processing, net)
proc = Thread.myThread(2,"leak",2 , leak, net)

proc.start()
thr.start()





"""net.NeuronGroups[1].Neurons[1].Demo()
net.NeuronGroups[0].Neurons[0].Demo()
"""
