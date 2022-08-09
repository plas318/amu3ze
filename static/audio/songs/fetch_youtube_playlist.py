import sys

api = "AIzaSyAC2WJWzYzE-mU5NVpDFTdl_i8_WGJcCkw"

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser


YOUTUBE_READONLY_SCOPE = "https://www.googleapis.com/auth/youtube.readonly"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

#id search
def get_playlist(id):

    y = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=api)
    playlists = y.playlistItems().list(playlistId = id,
                                part="snippet",
                                maxResults=20)
    
    response = playlists.execute()
    for item in response['items']:
        print(f"videoId: {item['snippet']['resourceId']['videoId']}")
        
            
if __name__ == "__main__":
    print(get_playlist(sys.argv[1]))
    
    
''' 
How to use: 
type: python fetch_youtube_playlist.py (substitute with playlist ID)
ex) python fetch_youtube_playlist.py PLD998248FDA00F900
Result: console ::stdout
'''
