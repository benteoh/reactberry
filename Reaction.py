from enum import Enum

# Preset Reaction Types. If provided, this would override the action 
# but may use the values provided in the reaction.
class Preset(Enum):
    NONE = 1
    SPARKLE = 2

class Reaction:
    def __init__(self, colour_set: list, intensity: float, rate: float, preset: Preset = NONE):
        self.colour_set = colour_set
        self.intensity = intensity
        self.rate = rate
        self.preset = preset
