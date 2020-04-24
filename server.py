from flask import Flask, request, render_template
import MySQLdb
import json

import components.request as request

app = Flask(__name__, static_url_path='/static', template_folder='template')

# Application routes determine the functions to call when the user tries to access a particular URL
@app.route('/')
def index():
	spotify = request.SpotifyRequest()
	spotifyArtist = spotify.get_first_artist("TRAPT")
	twitter = request.TwitterRequest()
	twitterArtist = twitter.get_first_user("TRAPT")
	return render_template("index.html",
		title='Butt-Rock Beef : How angry can these dads get?',
		spotifyArtist=spotifyArtist,
		twitterArtist=twitterArtist,
		artistName=spotifyArtist.name)

@app.route('/search/<artist>')
def show_results(artist=None):
	spotify = request.SpotifyRequest()
	spotifyArtist = spotify.get_first_artist(artist)
	twitter = request.TwitterRequest()
	twitterArtist = twitter.get_first_user(artist)

	print("What is it {}".format(spotifyArtist.name), flush=True)

	if spotifyArtist == None or twitterArtist == None:
		print("It's a bad one!", flush=True)
	return render_template("index.html",
		title='Butt-Rock Beef : Custom Search',
		spotifyArtist=spotifyArtist,
		twitterArtist=twitterArtist,
		artistName=artist)

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	return render_template('500.html'), 500
