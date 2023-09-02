class AudioHandler:
    def __init__(self, machine_handler):
        self.machine_handler = machine_handler
        machine_handler.open_channel() 

    def listen(self) -> Audio:
        return self.machine_handler.listen()
    