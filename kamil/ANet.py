import Neuron
import Sinaps
import NeuronGroup
import MotionController
class ANet:
    def __init__(self):
        self.NeuronGroups = []
        for elem in range(5):
            ng = NeuronGroup.NeuronGroup(elem)
            self.NeuronGroups.append(ng)

    def AddNeuron(self, numb):
        if(numb < 5):
            n = Neuron.AssocNeuron(len(self.NeuronGroups[numb].Neurons)+1, numb)
            self.NeuronGroups[numb].Neurons.append(n)
            for group in range(len(self.NeuronGroups)):
                if(group != numb):
                    for elem in range(len(self.NeuronGroups[group].Neurons)):
                        new = self.NeuronGroups[group].Neurons[elem]
                        n.sinapces.append(Sinaps.Sinaps(n, new))
                        new.sinapces.append(Sinaps.Sinaps(new, n))
            print("Neuron " + str(n.Id) + " added to group " + str(numb))

    def SpikeProcessing(self, groupId, neuronId):
        spiked = []
        self.NeuronGroups[groupId].Neurons[neuronId].Spiking()
        for group in range(len(self.NeuronGroups)):
            if(group != groupId):
                for elem in range(len(self.NeuronGroups[group].Neurons)):
                    new = self.NeuronGroups[group].Neurons[elem]
                    for sin in range(len(new.sinapces)):
                        if(new.sinapces[sin].n2 is self.NeuronGroups[groupId].Neurons[neuronId]):
                            new.UpdateSinaps(self.NeuronGroups[groupId].Neurons[neuronId])
        if(len(self.NeuronGroups[groupId].Neurons[neuronId].chosen) > 0):
            locked = self.NeuronGroups[groupId].Neurons[neuronId]
            spiked = []
            spiked.append(locked)
            for elem in locked.chosen:
                spiked.append(elem.n2)
                if(len(elem.n2.chosen) > 0):
                    for ch in elem.n2.chosen:
                        if(not spiked.__contains__(ch)):
                            spiked.append(ch.n2)
            for i in range(len(locked.chosen)):
                print("Spike! " + str(locked.chosen[i].n1.Id) + " of group " + str(locked.chosen[i].n1.groupId)
                  + " associated with " + str(locked.chosen[i].n2.Id) + " of group " + str(locked.chosen[i].n2.groupId))
            """methods of decidion maker"""
        MotionController.Process(groupId, neuronId, spiked, MotionController.blocked)


    def Leak(self):
        for group in self.NeuronGroups:
            for elem in group.Neurons:
                elem.Leak()
        


    def AppendDistinct(self, spiked, sinaps):
        for elem in spiked:
            if(elem.n1 is sinaps.n2 and elem.n2 is sinaps.n1):
                continue
            spiked.append(sinaps)
