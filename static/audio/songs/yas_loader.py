
from os import link
from yas_parser import parse_links

# dir = f'static/audio/songs/'

# yas Example
# yas --id [youtube-video-id|youtube-video-url] -m [--file [./sample.mp3]] 


def load_links():
    links = parse_links()
    link_string = '\n'.join([f"yas --id {y_link.strip()} -m" for y_link in links])    
    print(link_string)


if __name__=="__main__":
    load_links()