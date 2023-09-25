'''
This is a simple demo that utilises the AudioDriver class, plotting the audio
data sourced from the microphone in real time, using the listen_and_do function.
'''
import AudioDriver as AD
import AudioHandler as AH
import matplotlib.pyplot as plt
import numpy as np

# Some constants
CHUNKS = 10         # Number of chunks to plot (reduce for better performance)
CHUNK_SIZE = 1024   # Number of samples per chunk
RATE = 44100        # Sampling rate

def main():
    # Initialize audio driver
    audio_driver = AD.AudioDriver()
    audio_driver.open_stream()
    
    # Set up plot
    plt.ion()
    fig, ax = plt.subplots()
    x = np.arange(0, CHUNK_SIZE * CHUNKS)
    line, = ax.plot(x, np.random.rand(CHUNK_SIZE * CHUNKS))
    ax.set_ylim(-30000, 30000)
    
    # Set up aux function for listen_and_do
    def aux(audio):
        try:
            if (audio.audio_array.size >= CHUNK_SIZE * CHUNKS):
                line.set_ydata(audio.get_n_chunks(CHUNKS))
                fig.canvas.flush_events()
            return True
        except:
            return False

    audio_driver.listen_and_do(1, aux)
    
    # Clean up
    audio_driver.close_stream()
    plt.close(fig)
        
if __name__ == "__main__":
    main()
