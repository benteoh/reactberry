import Audio
import numpy as np
N_SECONDS = 5

class AudioAnalyser: # for now this is useless
    def __init__(self, audio_driver, sentiment_analyser):
        self.audio_driver = audio_driver
        self.sentiment_analyser = sentiment_analyser
        audio_driver.open_stream_callback(None)
        pass

    def listen(self) -> Audio:
        return self.audio_driver.listen_for_n_seconds(N_SECONDS)

    def is_active(self) -> bool:
        return self.audio_driver.stream.is_active()
    
    def close(self) -> None:
        self.audio_driver.close_stream()
        
    # Obtain sound descriptors from audio
    # Using sentiment analyser, obtain sentiment of last 5 seconds.
    def analyse(self):
        audio = self.listen()
        chunk = audio.get_latest_chunk()
        
        # Obtain average volume of last chunk.
        current_volume = np.average(np.abs(chunk))
        
        # Obtain average volume of last 5 seconds.
        average_volume = np.average(np.abs(audio.audio_array))
        
        # Analyse sentiment of audio sample.
        sentiment = self.sentiment_analyser.analyse(audio)
        
        return [current_volume, average_volume, sentiment]
        
        