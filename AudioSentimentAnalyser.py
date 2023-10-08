import Audio
from AudioSentiment import AudioSentiment
from Emotion import Emotion
from keras.models import load_model
import librosa
import numpy as np
import time

class AudioSentimentAnalyser:
    def __init__(self):
        self.model = None
        self.last_call_time = 0
        self.emotion = Emotion.NEUTRAL
        pass
    
    # Load model from file.
    def load_model(self, model_path: str) -> None:
        self.model = load_model(model_path)
    
    # Get features from audio sample in the same shape as the model input.
    def get_features(self, audio: Audio) -> list:
        mfccs = np.mean(librosa.feature.mfcc(y=audio.audio_array, 
                                             sr=audio.rate, 
                                             n_mfcc=40).T, axis=0)
        x = np.expand_dims(mfccs, axis=1)
        x = np.expand_dims(x, axis=0)
        return x
    
    # Analyse sentiment of audio sample. Restrict to 1 call per second.
    def analyse(self, audio: Audio) -> AudioSentiment:
        if time.time() - self.last_call_time < 1:
            return AudioSentiment(self.emotion, [])
        if self.model is None:
            raise Exception("Model not loaded. Please call load_model() first.")
        if audio.get_seconds() != 3:
            raise Exception("Audio sample must be exactly 3 seconds long.")
        pred = self.model.predict(self.get_features(audio))
        self.emotion = Emotion(np.argmax(pred))
        self.last_call_time = time.time()
        return AudioSentiment(self.emotion, [])