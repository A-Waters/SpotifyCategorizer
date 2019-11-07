import pyaudio
import numpy as np
import spotify









def getTokens():
    f =  open("clientID.txt")
    ClientInfo = ['null' , 'null']
    ClientInfo[0] = f.readline()
    ClientInfo[0] = ClientInfo[0][0:len(ClientInfo[0])-1]
    ClientInfo[1] = f.readline()

    f.close()
    return ClientInfo


if __name__ == "__main__":
    ClientInfo = getTokens()
    SpoClient = spotify.spotifyClient()
    SpoClient.authorize(ClientInfo)
    
    



