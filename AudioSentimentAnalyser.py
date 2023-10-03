import Audio
import AudioSentiment as AS
import Emotion

class AudioSemanticAnalyser:
    def __init__(self):
        pass
    
    def analyse(self, audio: Audio) -> AS.AudioSentiment:
        return AS.AudioSentiment(Emotion.HAPPY, [])