#Written my AlexWaters
import random
import numpy as np
import NodeClass as NC
import LayerClass as LC
import Common

class TRIP_LOSS_CNN3D:
    def __init__(self):
        self.layers = []

    def addLayer(self, layerType, nodes = 1, inputShape=(0,0,0)):
        self.ErrorChecking(layerType, nodes, inputShape)
        if self.layers == []:
            self.layers.append(LC.Layer(layerType, nodes=nodes, shape=inputShape))
        else:
            newLayer = LC.Layer(layerType, nodes=nodes)
            self.layers.append(newLayer)
            self.layers[len(self.layers)-1].connect(newLayer)
            



    def ErrorChecking(self, layerType, nodes, inputShape):
        if (nodes <= 0):
            raise ValueError("Number of Nodes in layers cant be less than 1")
        if self.layers == [] and 0 in inputShape:
            raise ValueError("Invalid or missing input shape")
        if (layerType not in Common.LAYERS):
            raise ValueError("Invalid Layer Type")

    
    def feedForward(self, ):
        pass

    
if __name__ == "__main__":
    NN = TRIP_LOSS_CNN3D()
    NN.addLayer("Convolution", nodes=5, inputShape=(200,200,1))
    NN.addLayer("Convolution", nodes=5)
    print("working")

