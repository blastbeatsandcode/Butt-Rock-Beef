import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import json
import components.artist as artist_component
import twitter
import os

class TwitterRequest:
    """Used to make Twitter Requests"""

    def __init__(self):
        self.api = twitter.Api(consumer_key=os.getenv('TWITTER_CONSUMER_API_KEY'),
                  consumer_secret=os.getenv('TWITTER_CONSUMER_API_SECRET_KEY'),
                  access_token_key=os.getenv('TWITTER_ACCESS_TOKEN'),
                  access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
        #self.api = twitter.Api()

    def search_for_first_user(self, artistName="TRAPT"):
        user = self.api.GetUsersSearch(term=artistName, count=1)
        return user[0]

    
    def get_first_user(self, artistName="TRAPT"):
        user = self.search_for_first_user(artistName=artistName)

        description = user.description
        favorites_count = user.favourites_count
        followers = user.followers_count
        twitter_id = user.id
        name = user.name
        handle = user.screen_name
        image = user.profile_image_url_https
        verified = user.verified
        tweets = user.status

        return artist_component.TwitterArtist(description=description,
            favorites_count=favorites_count,
            followers=followers,
            twitter_id=twitter_id,
            name=name,
            handle=handle,
            image=image,
            verified=verified,
            tweets=tweets)



class SpotifyRequest:
    """Used to make Spotify requests"""

    def __init__(self):
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    def get_first_artist_id(self, artistName):
        """Returns the ID of the first artist in the search results."""  
        search_result = self.spotify.search(q='artist:' + artistName, type='artist')

        json_list = json.loads(json.dumps(search_result))

        list_of_artists = json_list['artists']['items']
        artist_id = list_of_artists[0]['id']

        return artist_id

    def get_first_artist_uri(self, artistName="TRAPT"):
        """Returns the first search result of the term's artist ID formatted in the spotify:artist:ID format."""
        return "spotify:artist:" + self.get_first_artist_id(artistName)

    def get_first_artist(self, artistName="TRAPT"): 
        search_result = self.spotify.search(q='artist:' + artistName, type='artist')

        json_list = json.loads(json.dumps(search_result))

        artist = json_list['artists']['items'][0]

        external_url = artist['external_urls']['spotify']
        followers = artist['followers']['total']
        genres = artist["genres"]
        internal_url = artist["href"]
        images = artist["images"]
        artist_id = artist["id"]
        name = artist["name"]
        popularity = artist["popularity"]
        uri = artist["uri"]

        return artist_component.SpotifyArtist(external_url=external_url,
            followers=followers,
            genres=genres,
            internal_url=internal_url,
            images=images,
            id=artist_id,
            name=name,
            popularity=popularity,
            uri=uri)