import os, sys

# Parses audio files in folder (directories for player)
def parse_audio(folder_name):
    dir = f'static/audio/songs/{folder_name}'
    source = []
    
    if os.path.exists(dir):
        for files in os.listdir(dir):
                         
            file_dir = f'{dir}/{files}' 
            file, extension = os.path.splitext(file_dir)
            
            #DEBUG
            # print(f'{file} : {extension}')
            
            if extension == ".mp3" or extension == ".flac":
                source.append(file_dir)
                         
    else:
        print('Error: folder doesn\'t exists')
        return False
    
    return source

if __name__ == "__main__":
    # python audio_parser.py folder name 
    # will fetch results
    source = parse_audio(sys.argv[1])
    #DEBUG
    print(f'parsed source: {source}')