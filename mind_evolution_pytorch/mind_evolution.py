from __future__ import annotations

import torch
from torch import nn, Tensor
from torch.nn import Module, ModuleList
import torch.nn.functional as F

# constants

Population = list[Tensor]
Islands = list[Population]

# helper functions

def exists(v):
    return v is not None

def default(v, d):
    return v if exists(v) else d

# operators

def init_islands(
    model: Module,
    num_islands = 1
) -> Islands:
    raise NotImplementedError

def migration(
    islands: Islands
) -> Islands:
    raise NotImplementedError

def reset_island(
    islands: Islands
) -> Islands:
    raise NotImplementedError

def refinement(
    critics: list[Module],
    solution: Tensor
) -> Tensor:
    raise NotImplementedError

def mutation(
    solution: Tensor
) -> Tensor:
    raise NotImplementedError

def tournament_selection(
    population: Population,
    num_tournaments: int
) -> tuple[Populations, ...]:
    raise NotImplementedError

def recombination(
    solution1: Tensor,
    solution2: Tensor
) -> Tensor:
    raise NotImplementedError

# main class

class MindEvolution(Module):
    def __init__(
        self,
        transformer: Module
    ):
        super().__init__()

    def forward(self, x):
        return x
