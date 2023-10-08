# Flask-amu3ze

Amu3ze is a Simple website for streaming local songs or playlists via youtube api

Simple responsive ui with 2 Players

## Calamansi Player to play local songs:

![image](https://github.com/plas318/Flask-amu3ze/assets/64758800/f4fc5e8c-ef37-4572-a90a-b83811591845)

## Youtube Player API:

![image](https://github.com/plas318/Flask-amu3ze/assets/64758800/3d1a54f3-c693-4fb4-ba0d-6157cbf9bf06)


### Run Local Server
activate virtualenv, move to root folder
<code> python app.py </code>


## Features
Basic Login using 
Youtube Player API
- shuffle option
- autoplay option
- basic buttons
- add playlist, remove playlist
- like playlist (test)


## Stacks
Flask

Sql Alchemy & sqlite

Bootstrap (CSS)

Youtube Player API

Calamansi Js - https://github.com/voerro/calamansi-js

fluent-ffmpeg node module -https://github.com/fluent-ffmpeg/node-fluent-ffmpeg/issues/802

## PowerShell Script
auto launches the local server at startup
<code>
  -noexit -command &{cd "{your_url}\flask-amu3ze";.venv/bin/activate;python app.py;}
</code>

## Misc
This is a simple app made to easily switch playlists and play static files while having this website on the corner of the page

The youtube player api (embedded player) enables to play youtube videos without ads if that is the purpose
