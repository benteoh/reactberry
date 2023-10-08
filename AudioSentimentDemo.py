'''
This is a simple demo that utilises the AudioDriver class, plotting the audio
data sourced from the microphone in real time, using a callback. Additionally,
utilise the AudioSentimentAnalyser class to analyse the sentiment of the audio.
'''
from AudioDriver import AudioDriver
from AudioAnalyser import AudioAnalyser
from AudioSentimentAnalyser import AudioSentimentAnalyser
import matplotlib.pyplot as plt
import numpy as np
import time

# Some constants
CHUNKS = 10         # Number of chunks to plot (reduce for better performance)
CHUNK_SIZE = 1024   # Number of samples per chunk

def main():
    print("Loading up model...")
    
    # Initialize audio driver, analyser and sentiment analyser.
    sentiment_analyser = AudioSentimentAnalyser()
    sentiment_analyser.load_model("SentimentModel/Audio_Sentiment_Model.h5")
    audio_analyser = AudioAnalyser(AudioDriver(), sentiment_analyser)
    
    # Set up plot.
    plt.ion()
    fig, ax = plt.subplots()
    plt.title('Real Time Audio Analysis')
    x = np.arange(0, CHUNK_SIZE * CHUNKS)
    line, = ax.plot(x, np.random.rand(CHUNK_SIZE * CHUNKS))
    ax.set_ylim(-30000, 30000)
    text = plt.figtext(0.5, 0.01, 'Emotion: NEUTRAL', ha="center")
    
    # Wait for 3 seconds plus time to initialise model prediction.
    print("Starting in a few seconds...")
    
    time.sleep(3.5)
    audio_analyser.analyse()
    
    print("Started.")

    # Grab snapshots of audio and plot them.
    while (audio_analyser.is_active()):
        try:
            analysis = audio_analyser.analyse()
            if analysis[2] is not None:
                text.set_text('Emotion: ' + analysis[2].emotion.name)
            
            line.set_ydata(audio_analyser.listen().get_n_chunks(CHUNKS))
            fig.canvas.flush_events()
        except Exception:
            print("Exception caught.")
            break
        except:
            break
    
    # Clean up
    audio_analyser.close()
    plt.close(fig)
        
if __name__ == "__main__":
    main()
