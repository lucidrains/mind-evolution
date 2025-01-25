from __future__ import annotations

# constants

Population = list[str]
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

def fitness(
    solution: str
) -> float:
    raise NotImplementedError

def refinement(
    critics: list[Module],
    solution: str
) -> str:
    raise NotImplementedError

def mutation(
    solution: str
) -> str:
    raise NotImplementedError

def tournament_selection(
    population: Population,
    num_tournaments: int
) -> tuple[Populations, ...]:
    raise NotImplementedError

def recombination(
    solutions: list[str]
) -> str:
    raise NotImplementedError

# main class

class MindEvolution():
    def __init__(
        self,
        transformer
    ):
        super().__init__()

    def forward(self, x):
        return x
