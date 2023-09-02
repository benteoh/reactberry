class PiAudioHandler:
    def __init__(self): 
        # Some kind of arguments can be passed in the future.
        channel_opened = False
        pass
    
    def listen(self) -> Audio:
        if !channel_opened:
            self.open_channel()
        
        # TODO: Implement listen
    
    def open_channel(self) -> None:
        channel_opened = True
        # TODO: Implement open_channel
        
    def close_channel(self) -> None:
        channel_opened = False
        # TODO: Implement close_channel