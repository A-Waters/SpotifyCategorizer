#import pyaudio
import numpy as np
import spotify


if __name__ == "__main__":
    SpoClient = spotify.spotifyClient()
    SpoClient.authorize()
    


    usertracks = "/v1/me/tracks"
    audio_analisys = "/v1/audio-analysis/"#ID

    tempQuery = {"limit": "5"}
    result = SpoClient.getData(usertracks, tempQuery)

    '''for i in result["items"]:
        print(i["track"]["id"])'''

    uhhh = SpoClient.getData(audio_analisys+"7LJzs1Kr8kW3d6cFTCueNV")
    print(uhhh)
 	