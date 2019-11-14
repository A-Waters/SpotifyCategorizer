import NodeClass as NC
import Common

class Layer:
    def __init__(self, Ltype = Common.LAYERS[0], nodes = 0, shape = (1,1)):
        self.errorChecking(Ltype, nodes, shape)
        self.type = Ltype
        self.numNodes = nodes
        self.shape = shape
        self.nodes = [NC.Node(Ntype = Common.NODES[Common.LAYERS.index(self.type)])] * nodes
    
    def connect(self,layer):
        if self.type == Common.LAYERS[Common.LAYERS.index("Flatten")]:
            if layer.type == Common.LAYERS[Common.LAYERS.index("Flatten")]:
                raise Exception("No uses for Flatten to Flatten")
            elif layer.type == Common.LAYERS[Common.LAYERS.index("Convolution")]:
                raise Exception("1D Convolution")
            elif layer.type == Common.LAYERS[Common.LAYERS.index("Dense")]:
                for node in self.nodes:
                    for otherNodes in layer.nodes:
                        pass
            
            
    
    def errorChecking(self, Ntype, nodes, shape):
        if not isinstance(Ntype, str):
            raise Exception("Layer type is not a string")
        if nodes < 0:
            raise Exception("Number of nodes must be >= 0")

    

