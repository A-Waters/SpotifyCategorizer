import urllib3
import urllib
import requests



class spotifyClient():
    #Spotify URLS
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    REDIR_URL = "https%3A%2F%2Fexample.com%2Fcallback"    


    def authorize(self, clientInfo):
        url =  self.SPOTIFY_AUTH_URL + "?client_id=" + clientInfo[0] + '&response_type=code' + '&redirect_uri=' + self.REDIR_URL + '&scope=' +  'user-library-modify' + '%20' + 'user-modify-playback-state' + '%20' + 'playlist-modify-private'
        
        r = requests.get( 
            url,
            headers={
            'client_id': clientInfo[0],
            }
        )


        print(url)
        print()
        print(r.url)
        print()
        #print(urllib.parse.urlparse(r.url))
        
        #print(url)
        #print(request.status)