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

# refinement through critical conversation

class RefinementCriticalConversation():
    def __init__(
        self,
        author,
        critic
    ):
        self.author = author
        self.critic = critic

    def __call__(self):
        raise NotImplementedError

# main class

class MindEvolution():
    """
    hyperparameters from section 3.2 of Mind Evolution paper
    """

    def __init__(
        self,
        transformer,
        *,
        generations = 10,   # the maximum number of generations to search for a solution
        islands = 4,        # independent populations to evolve
        conversations = 5,  # conversations per island
        turns = 4,          # turns per conversation
        reset_interval = 3, # how frequently to reset islands in generations
        reset = 2,          # islands to reset, lowest mean score islands are chosen
        top = 5,            # starting parents to transfer to islands when reset
        candidates = 15,    # candidate parents to consider when resetting islands with LLM
        parents = 5,        # maximum number of parents a conversation can have
        prob_no_parents = 1. / 6, # probability of conversation having no parents
        emigrate = 5,       # plans to emigrate to the next island after each island
        retries = 5,        # times to try to generate a plan before giving up
        critic_transformer = None
    ):

        self.transformer = transformer

        self.generations = generations
        self.islands = islands
        self.conversations = conversations
        self.turns = turns
        
        self.reset_interval = reset_interval
        self.reset = reset
        self.top = top
        self.candidates = candidates
        
        self.parents = parents
        self.prob_no_parents = prob_no_parents
        self.emigrate = emigrate
        self.retries = retries

        # critical conversation logic - rcc

        self.rcc = RefinementCriticalConversation(
            transformer,
            default(critic_transformers, transformer)
        )

    def __call__(
        self,
        x
    ):
        return x
