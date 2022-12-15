'''
step 1: log into spotify
step 2: grab our lkiekd videos
step 3: create a new playlist
step 4: search for the song
step 5: add song to new spotify playlist
'''

import json
import requests
from secrets import spotify_user_id, spotify_token
class CreatePlaylist:

    def __init__(self):
        self.user_id = spotify_user_id

    #step 1: log into spotify
    def get_youtube_client(self):
        pass
    #step 2: grab our lkiekd videos
    def get_liked_videos(self):
        pass
    #step 3: create a new playlist
    def create_playlist(self):
        request_body = json.dumps({
            "name":"Youtube Liked Vids",
            "description": "All Liked Youtube Videos",
            "public": True
        })

        end_point = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)

        response = requests.post(
            end_point,
            data=request_body,
            headers={
                #"Accept":"application/json",
                "Content-Type":"application/json",
                "Authorization":"bearer {}".format(spotify_token)
            }
        )
        response_json = response.json()
        print(response_json)
        
        #playlist id
        #return response_json["id"]

    #step 4: search for the song
    def get_spotify_uri(self):
        pass
    #step 5: add song to new spotify playlist
    def add_song_to_playlist(self):
        pass

object = CreatePlaylist()
new_response = object.create_playlist()

