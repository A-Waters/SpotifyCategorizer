import urllib3
import urllib
import requests
import time
import pickle
import os.path
import base64
from selenium import webdriver


class spotifyClient():
    #Spotify URLS
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    REDIR_URL = "https://example.com/callback/"    
    API_URL = "https://accounts.spotify.com/api/token"
    CLIENT_ID = "fb37da23233d4fe581300fa8d7c4b3a0"


    WEBDRIVER = "./Data/chromedriver.exe"
    COOKIES = "./Data/cookies.pk1"



    def authorize(self):


        
        #Surpress Console Output 
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        #start browser
        driver = webdriver.Chrome(executable_path=self.WEBDRIVER, options=options)
        driver.set_window_size(500,1000)

        #load cookies
        if (os.path.exists(self.COOKIES)):
            print("loading cookies")
            cookies = pickle.load(open(self.COOKIES, "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)


        #create url and open url
        scopes = 'user-library-modify user-modify-playback-state playlist-modify-private'
        url =  self.SPOTIFY_AUTH_URL + "?client_id=" + self.CLIENT_ID + '&response_type=token' + '&redirect_uri=' + urllib.parse.quote(self.REDIR_URL.encode("utf-8")) + '&scope=' + urllib.parse.quote(scopes.encode("utf-8"))
        driver.get(url)
        
        #while we not at the url
        while ("access_token" not in driver.current_url):
            pass
        else:       #when we at the url
            parse = urllib.parse.urlparse(driver.current_url)
            access_token = parse.fragment[13:parse.fragment.find("&")]          #get the accesstoken
            pickle.dump(driver.get_cookies(), open(self.COOKIES,"wb"))          #save cookies
            #driver.close()                                                      #close driver
                
        bytearray([])
        print(access_token)
        print(base64.b64encode(access_token.encode()))

        #driver.get(self.API_URL, headers= { 'Authorization': 'Bearer ' + access_token})
        #repsonse = requests.post(self.API_URL, headers= { 'Authorization': 'Bearer ' + access_token})

        #print(repsonse)
        
        '''
        payload = {
            'username': 'xxxx',
            'password': 'xxxx'
        }

        r = requests.Session()

        
        print(url)
        respo = requests.get( 
            url,
            headers={
                'client_id': clientInfo[0]
            }
        )

        print(respo.url)
    
        respo = r.post(respo.url, data=payload)
       
        #print(urllib.parse.urlparse(respo.url))
        print("------------------")

        #print(url)
        #print(request.status)
        '''


if __name__ == "__main__":
    import spotify
    SpoClient = spotify.spotifyClient()
    SpoClient.authorize()