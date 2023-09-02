"# reactberry" 

Flow of modules:
    1) Audio Handler and Parser: Pulls bitstream from microphone and convert into waveform format.
    2) Audio Semantic Analyser: Based on real time input, semantically analyse the emotion, mood, loudness, and undertones of the audio.
    3) Audio to Visual Translator: Based on the semantic analysis, produce an appropriate reaction (colour, pulsations, patterns, brightness, flashes)
    4) Visual Handler: Based on the reaction which is in some standard format, create the appropriate reaction on the hardware.

Note on portability:
The Audio Semantic Analyser and the Audio to Visual Translator are very portable and only relies on the standardisation of inputs and outputs. The Audio and Visual Handlers would have to be different for various machines and peripheral set ups. This is good because the bulk of the code would be in the modules 2 and 3. 

Note on Audio Semantics: 
This has to be determined using a model, and the easiest would be to use machine learning. 

Note on real-time pipelining:
This would be one of the most difficult parts, as we have to continuously listen and output. We would have to break the audio streams into digestable chunks and standardise the chunk size. We can vary it to find the most optimal, which results in accurate analysis and also fast response on the visual end. Additionally, we have to consider how the program does it garbage collect, we would not want memory to be filled with audio clips.