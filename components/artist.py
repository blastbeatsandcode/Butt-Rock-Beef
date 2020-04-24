class SpotifyArtist:
    """Contains Spotify Artist Data"""

    def __init__(self, external_url=None, followers=None, genres=None, internal_url=None, images=None, id=None, name=None, popularity=None, uri=None):
        self.external_url = external_url
        self.followers = followers
        self.genres = genres
        self.internal_url = internal_url
        self.images = SpotifyArtist.handle_creating_image_list(images)
        self.id = id
        self.name = name
        self.popularity = popularity
        self.uri = uri
        self.formatted_uri = "spotify:artist:" + uri

    @staticmethod
    def handle_creating_image_list(image_json):
        images = []
        for img in image_json:
            images.append(SpotifyArtistImage(width=img["width"], height=img["height"], url=img["url"]))
        return images


    

class SpotifyArtistImage:
    """Contains data for Spotify artist images"""

    def __init__(self, width, height, url):
        self.width = width
        self.height = height
        self.url = url



class TwitterArtist:
    """Contains Twitter Artist Data"""

    def __init__(self, description=None, favorites_count=None, followers=None, twitter_id=None, name=None, handle=None, image=None, verified=None, tweets=None):
        self.description = description
        self.favorites_count = favorites_count
        self.followers = followers
        self.twitter_id = twitter_id
        self.name = name
        self.handle = handle
        self.image = image
        self.verified = verified
        self.tweets = tweets
        self.url = "https://twitter.com/" + handle