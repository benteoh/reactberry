import numpy as np
class Audio:
    def __init__(self, audio_array, chunk_size, rate, format):
        self.audio_array = audio_array
        self.chunk_size = chunk_size
        self.rate = rate
        self.format = format
        pass

    def get_seconds(self) -> float:
        return self.audio_array.size / self.rate
    
    def get_n_seconds(self, n) -> np.array:
        return self.audio_array[-n * self.rate:]
    
    def get_latest_chunk(self) -> np.array:
        return self.audio_array[-self.chunk_size:]