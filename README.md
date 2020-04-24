# Butt-Rock Beef
This is a silly project created on a whim because TRAPT (yes, the band that made like one song that a lot of people liked circa 2002-ish) keeps trying to stay relevant by starting "twitter beef". The question is, does this beef correlate to changes in plays on Spotify?

### Prerequisites
You will need to install `MySQLdb` for python if you don't already have it installed. For Ubuntu:

```
sudo apt install python3-mysqldb
```

You will also need to set up your developer account with Spotify and register your application using [this guide](https://developer.spotify.com/documentation/web-api/quick-start/). From this, you will get your Client ID and Client Secret. You will need this to make calls to the Spotify API. Once you get the values from your dashboard, set the `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` values in `~/.bashrc`:

```bash
export SPOTIPY_CLIENT_ID=your-id-here
export SPOTIPY_CLIENT_SECRET=your-secret-here
```

You will need to do the same with Twitter using [this guide](https://developer.twitter.com/en/apply-for-access). Then set the following environment variables in `~/.bashrc`:

```bash
export TWITTER_CONSUMER_API_KEY=your-api-key
export TWITTER_CONSUMER_API_SECRET_KEY=your-secret-key
export TWITTER_ACCESS_TOKEN=your-access-token
export TWITTER_ACCESS_TOKEN_SECRET=your-token-secret
```

### Setting Up Flask

You will need Python 3 to set up Flask properly. You may also need to install the Python 3 virtual environment package with `sudo apt install python3-venv`.

Set up a python virtual environment and activate it. After that, install Flask itself as well as httplib2 and spotipy:

```
python3 -m venv venv
. venv/bin/activate
pip install flask
pip install httplib2
pip install spotipy --upgrade
pip install python-twitter
pip install requests_oauthlib
```

Specify the location of the flask app (the file `server.py`) and export it. To do this, open `~/.bashrc` and add the following to the bottom of the file:

```
export FLASK_APP=path/to/server.py
source ~/.bashrc
```

Replacing `path/to/server.py` to wherever the actual file is. The flask server can now be run with `flask run`.
To run on a public-facing server, run it with `flask run --host=0.0.0.0`

### Start Server On Boot
This section outlines how to easily set up the server to run on boot. This is ideal for an instance where you want to run the server on something like a Raspberry Pi. It might also be a good idea to configure a static IP to make it easier to connect to the server.

Create a bash script to actually start the server, replacing `path/to/Butt/Rock/Beef/server.py` with your `server.py` location. NOTE: make sure to run `chmod +x name-of-your-script.sh` to allow for executing it!

```bash
#!/bin/bash

echo "Starting Flask Server . . ."

export FLASK_APP=/path/to/Butt-Rock-Beef/server.py
flask run --host=0.0.0.0


echo "Server Closed."
```

Create a `.service` file inside of `/lib/systemd/system`. It should look something like this, replacing `/path/to/your/flask/script.sh` with the flask script you previously created:

```bash
[Unit]
Description=Flask Server Service

[Service]
ExecStart=/path/to/your/flask/script.sh

[Install]
WantedBy=multi-user.target
```

Run the following commands to start the service and enable it on boot, replacing `your_service_name` with the `.service` file you created earlier.

```bash
sudo systemctl start your_service_name.service
sudo systemctl stop your_service_name.service
sudo systemctl enable your_service_name.service
```

After a reboot, it should start automatically after a few seconds.

