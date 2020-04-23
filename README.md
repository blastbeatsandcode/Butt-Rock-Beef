# Butt-Rock Beef
This is a silly project created on a whim because TRAPT (yes, the band that made like one song that a lot of people liked circa 2002-ish) keeps trying to stay relevant by starting "twitter beef". The question is, does this beef correlate to changes in plays on Spotify?

### Setting Up Flask

You will need Python 3 to set up Flask properly. You may also need to install the Python 3 virtual environment package with `sudo apt install python3-venv`.

Set up a python virtual environment and activate it. After that, install Flask itself:

```
python3 -m venv venv
. venv/bin/activate
pip install flask
```

Specify the location of the flask app (the file `server.py`) and export it. To do this, open `~/.bashrc` and add the following to the bottom of the file:

```
export FLASK_APP=path/to/server.py
source ~/.bashrc
```

Replacing `path/to/server.py` to wherever the actual file is. The flask server can now be run with `flask run`.
To run on a public-facing server, run it with `flask run --host=0.0.0.0`


### Prerequisites
You will need to install `MySQLdb` for python if you don't already have it installed. For Ubuntu:

```
sudo apt install python3-mysqldb
```

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

