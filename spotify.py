import urllib3
import urllib
import requests
import time
import pickle
import os.path
import base64
import json
from selenium import webdriver


class spotifyClient():
    #Spotify URLS
    SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
    REDIR_URL = "https://example.com/callback/"    
    API_URL = "https://accounts.spotify.com/api/token"
    CLIENT_ID = "fb37da23233d4fe581300fa8d7c4b3a0"
    SPODATA = 'https://api.spotify.com'

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
        scopes = 'playlist-modify-private playlist-read-collaborative user-read-private user-library-modify playlist-modify-public user-library-read playlist-read-private'
        url =  self.SPOTIFY_AUTH_URL + "?client_id=" + self.CLIENT_ID + '&response_type=token' + '&redirect_uri=' + urllib.parse.quote(self.REDIR_URL.encode("utf-8")) + '&scope=' + urllib.parse.quote(scopes.encode("utf-8"))
        
       
        driver.get(url)

        #while we not at the url
        while ("access_token=" not in driver.current_url):
            pass
        else:       #when we at the url
            parse = urllib.parse.urlparse(driver.current_url)
            self.access_token = parse.fragment[13:parse.fragment.find("&")]          #get the accesstoken
            pickle.dump(driver.get_cookies(), open(self.COOKIES,"wb"))          #save cookies
            driver.close()                                                      #close driver
                





    def getData(self, url_ented, inquery = None):
        headers = {'Authorization': 'Bearer %s' % self.access_token }
        response = requests.get(self.SPODATA + url_ented, headers=headers, params=inquery)        #get data from spotify
        return response.json()
    
        
        
                



if __name__ == "__main__":
    import spotify
    SpoClient = spotify.spotifyClient()
    SpoClient.authorize()