import random
import numpy as np
import Common

class Node:
    def __init__(self, Ntype = Common.NODES[Common.NODES.index("Data")]):
        self.errorChecking(Ntype)
        self.weights = []
        self.type = Ntype
        self.ending_node = True
        if self.type == Common.NODES[Common.NODES.index("Filter")]:
            self.filter = np.random.uniform(low=-7, high=7, size=(3,3,3))
        elif self.type == Common.NODES[Common.NODES.index("Data")]:
            self.weights = np.random.rand(0)
            self.value = random.randrange(-1,1)
        else:
            raise ValueError("Invalid Node Type", self.type)
        
    def connect(self, Node):
        pass

    def errorChecking(self, Ntype):
        if not isinstance(Ntype, str):
            raise Exception("Node type is not a string")