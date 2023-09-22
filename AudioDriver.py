'''
This is a specialised audio driver for listening and reading audio in real-time.
It is designed to listen to an audio stream and concurrently update an audio
buffer. The audio buffer can be accessed at any time to get the most recent N 
seconds of audio.
'''

import pyaudio
import numpy as np
import Audio

# Constants for audio stream
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
MAX_SECONDS = 10

class AudioDriver:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream_opened = False
        self.using_callback = False
        self.audio_array = np.array([])
        pass

    # Open audio stream
    def open_stream(self) -> None:
        self.stream_opened = True
        self.stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                                      rate=RATE, input=True,
                                      frames_per_buffer=CHUNK_SIZE)
    
    # Open audio stream with callback
    # This allows audio to be read and stored in the background
    def open_stream_callback(self, aux) -> None:
        # Define callback for playback
        def callback(in_data, frame_count, time_info, status):
            # Update audio array
            self.write_chunk(in_data)
                
            if aux is not None:
                aux(self.audio_array)
            return (in_data, pyaudio.paContinue)
        
        self.stream_opened = True
        self.using_callback = True
        self.stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                                      rate=RATE, input=True,
                                      frames_per_buffer=CHUNK_SIZE,
                                      stream_callback=callback)
    
    # Listen to audio and return Audio object
    # This should be used if the stream is opened a callback
    def listen_for_n_seconds(self, n) -> Audio:
        if not self.stream_opened or not self.using_callback:
            print("Error: Stream not opened with callback.")
            return None
        
        return self.get_n_seconds(n)
    
    # Listen to audio and perform some auxiliary function
    # This should be used if the stream is opened without a callback
    def listen_and_do(self, n, aux) -> None:
        while True:
            audio_data = self.stream.read(CHUNK_SIZE)
            self.write_chunk(audio_data)
            aux(self.get_n_seconds(n))    

    # Get most recent N seconds of audio
    def get_n_seconds(self, n) -> Audio:
        arr = self.audio_array
        arr = arr if arr.size < n * RATE else arr[-n * RATE:]

        return Audio.Audio(arr, CHUNK_SIZE, RATE, FORMAT)
    
    def write_chunk(self, data) -> None:
        # Attach data to audio array
        audio_array_extension = np.frombuffer(data, dtype=np.int16) 
        self.audio_array = np.append(self.audio_array, audio_array_extension)
    
        # Limit length of audio array to N seconds
        if self.audio_array.size > MAX_SECONDS * RATE:
            self.audio_array = self.audio_array[-MAX_SECONDS * RATE:]
    
    # Close audio stream
    def close_stream(self) -> None:
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
