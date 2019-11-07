import urllib3
import urllib
import requests



class spotifyClient():
    #Spotify URLS
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    REDIR_URL = "https://www.example.com/callback"    


    def authorize(self, clientInfo):
        payload = {
            'username': 'xxxx',
            'password': 'xxxx'
        }

        r = requests.Session()

        scopes = 'user-library-modify user-modify-playback-state playlist-modify-private'
        
        url =  self.SPOTIFY_AUTH_URL + "?client_id=" + clientInfo[0] + '&response_type=code' + '&redirect_uri=' + urllib.parse.quote(self.REDIR_URL.encode("utf-8")) + '&scope=' + urllib.parse.quote(scopes.encode("utf-8"))
        

        print(url)
        respo = r.get( 
            url,
            headers={
            'client_id': clientInfo[0]
            }
        ).text
    
        #respo = r.post(respo, data=payload).url
       
        #print(urllib.parse.urlparse(respo.url))
        print("------------------")

        #print(url)
        #print(request.status)