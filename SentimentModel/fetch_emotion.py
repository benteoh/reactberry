def get_emotion(file_path):
    item = file_path.split('/')[-1]
    prefix = item[:1]
    code = item[6:-16]
    
    if code =='01' or prefix=='n' or code =='02' : # Including calm
        return 'neutral'
    elif code =='03' or prefix=='h':
        return 'happy'
    elif code =='04' or item[:2]=='sa':
        return 'sad'
    elif code =='05' or prefix =='a':
        return 'angry'
    elif code =='06' or prefix =='f':
        return 'fearful'
    elif code =='07' or  prefix=='d':
        return 'disgusted'
    elif code =='08' or item[:2]=='su':
        return 'surprised'
