# Returns the corresponding emotion number from 0 to 6. Note that calm and neutral are combined to code 0.
def get_emotion_number(file_path):
    item = file_path.split('/')[-1]
    code = item.split('-')[2]
    if code == '01' or code == '02':
        return 0
    elif code == '03': # Happy
        return 1
    elif code == '04': # Sad
        return 2
    elif code == '05': # Angry
        return 3
    elif code == '06': # Fearful
        return 4
    elif code == '08': # Surprised
        return 5
    elif code == '07': # Disgust Unused
        return 6

# Returns the corresponding emotion in string form. 
def get_emotion_str(n):
    emotions = ['neutral', 'happy', 'sad', 'angry', 'fearful', 'surprised', 'disgust']
    return emotions[n]
    