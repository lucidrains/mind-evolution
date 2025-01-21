import torch
from torch import nn
from torch.nn import Module, ModuleList
import torch.nn.functional as F

# helper functions

def exists(v):
    return v is not None

def default(v, d):
    return v if exists(v) else d

# main class

class MindEvolution(Module):
    def __init__(
        self,
        transformer: Module
    ):
        super().__init__()

    def forward(self, x):
        return x
