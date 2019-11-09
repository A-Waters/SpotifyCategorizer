#import pyaudio
import numpy as np
import spotify
import json


if __name__ == "__main__":
    SpoClient = spotify.spotifyClient()
    SpoClient.authorize()
    


    usertracks = "/v1/me/tracks"
    audio_analisys = "/v1/audio-analysis/"#ID

    tempQuery = {"limit": "5"}
    result = SpoClient.getData(usertracks, tempQuery)

    for i in result["items"]:
        print(i["track"]["id"])



    

    data = SpoClient.getData(audio_analisys+"7LJzs1Kr8kW3d6cFTCueNV")
    
    for segment in data["segments"]:
        for DataType in segment:
            #print(segment[DataType])
            print("%s { %s }" % (DataType, segment[DataType]))
        print("--------------------------")
    



    '''with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    print("test")'''

 	