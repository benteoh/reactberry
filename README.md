"# reactberry" 

Flow of modules:  
    1) Audio Driver: Pulls bitstream from microphone and convert into Audio Object  
    2) Audio and Sentiment Analyser: Based on real time input, analyse the emotion, mood, loudness, and undertones of the audio.  
    3) Audio to Visual Translator: Based on the semantic analysis, produce an appropriate reaction (colour, pulsations, patterns, brightness, flashes)  
    4) Visual Handler: Based on the reaction which is in some standard format, create the appropriate reaction on the hardware.  

To Do:  
    1) Create model for audio sentiment analysis, and sentiment class  
    2) Create map of emotion to colour/pattern  
    3) Implement visual handler  
    4) Create main program  

Completed:  
    1) Create Audio Driver  
    2) Create Audio Class  
    3) Create Demos for Driver  
    4) Create analyser wrapper for audio driver  

Note on Sentiment Analyser:  
    The model was trained on the RAVDESS dataset provided on the Zenodo platform. Only the audio clips were used (Audio_Song_Actors_01-24 and Audio_Speech_Actors_01-24). More details can be found on https://zenodo.org/record/1188976.  
