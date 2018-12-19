


class AssocNeuron(object):
    def __init__(self, Id, groupId):
        self.treshhold = 7
        self.Id = Id
        self.sinapces = []
        self.locked = False
        self.chosen = []
        self.groupId = groupId

    def Spiking(self):
        self.chosen.clear()
        for sinaps in range(len(self.sinapces)):
            self.sinapces[sinaps].weight += 1
            if (self.sinapces[sinaps].weight > self.treshhold):
                self.chosen.append(self.sinapces[sinaps])



    def UpdateSinaps(self, neuron):
        for sin in self.sinapces:
            if (sin.n2 is neuron):
                sin.weight += 1
                if (sin.weight > self.treshhold and not self.chosen.__contains__(sin)):
                    self.chosen.append(sin)


    def Leak(self):
        if(self.locked == False):
            for sin in self.sinapces:
                sin.weight -= 1


    def Demo(self):
        print("Neuron " + str(self.Id) + " of group " + str(self.groupId) + " sinapces weights:")
        for i in range(len(self.sinapces)):
            print("Ids: " + str(self.sinapces[i].n1.Id) + " of group " + str(self.sinapces[i].n1.groupId) + " " + str(self.sinapces[i].n2.Id) + " of group " + str(self.sinapces[i].n2.groupId))
            print("weight: " + str(self.sinapces[i].weight))
        for elem in self.chosen:
            print(str(elem.n2.Id) + " " + str(elem.n2.groupId))
