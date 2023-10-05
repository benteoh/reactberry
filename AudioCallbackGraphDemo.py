'''
This is a simple demo that utilises the AudioDriver class, plotting the audio
data sourced from the microphone in real time, using a callback.
'''
from AudioDriver import AudioDriver
from AudioAnalyser import AudioAnalyser
import matplotlib.pyplot as plt
import numpy as np

# Some constants
CHUNKS = 20         # Number of chunks to plot (reduce for better performance)
CHUNK_SIZE = 1024   # Number of samples per chunk

def main():
    # Initialize audio driver and handler
    audio_handler = AudioAnalyser(AudioDriver(), None)
    
    # Set up plot
    plt.ion()
    fig, ax = plt.subplots()
    x = np.arange(0, CHUNK_SIZE * CHUNKS)
    line, = ax.plot(x, np.random.rand(CHUNK_SIZE * CHUNKS))
    ax.set_ylim(-30000, 30000)

    # Grab snapshots of audio and plot them.
    while (audio_handler.is_active()):
        try:
            line.set_ydata(audio_handler.listen().get_n_chunks(CHUNKS))
            fig.canvas.flush_events()
        except:
            break
    
    # Clean up
    audio_handler.close()
    plt.close(fig)
        
if __name__ == "__main__":
    main()
