class VisualHandler:
    def __init__(self, machine_handler):
        self.machine_handler = machine_handler 

    def display(self, reaction: Reaction) -> None:
        self.machine_handler.display(reaction)