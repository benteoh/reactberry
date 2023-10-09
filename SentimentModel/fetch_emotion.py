# Returns the corresponding emotion number from 0 to 6. Note that calm and neutral are combined to code 0.
def get_emotion_number(file_path):
    item = file_path.split('/')[-1]
    code = item[6:-16]
    if code == '01' or code == '02':
        return 0;
    return int(code) - 2

# Returns the corresponding emotion in string form. 
def get_emotion_str(n):
    emotions = ['neutral', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']
    return emotions[n]
    