import Audio
class AudioHandler: # for now this is useless
    def __init__(self, audio_driver):
        self.audio_driver = audio_driver
        audio_driver.open_stream_callback(None)
        pass

    def listen(self) -> Audio:
        return self.audio_driver.listen_for_n_seconds(5)

    def is_active(self) -> bool:
        return self.audio_driver.stream.is_active()
    
    def close(self) -> None:
        self.audio_driver.close_stream()