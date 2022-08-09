from flask import Blueprint
from flask import render_template, url_for, request, redirect, session
from static.audio.audio_parser import parse_audio
from flask_login import current_user, login_required
from models import User, Playlist, LikesTable
from app import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    s= session.get('source')
    
    print(f'request get s: {s}')
    if not s:
        s = parse_audio('Recommend')        
    
    
    playlists = Playlist.query.all()
    
        
    if playlists:
        likes = {}
        for p in playlists:
            likes[p.id] = get_likes(p.id)
        
        
        return render_template('amu3ze/index.html', source=s, playlists=playlists, likes=likes)
    return render_template('amu3ze/index.html', source=s)    
    

# Calamansi player function if you give path /hidden you might get interesting results.!

@views.route('<string:folder_name>', methods=['GET', 'POST'])
def generate_list(folder_name):
    # folder_name = request.form.get('folder-name')
    #print(folder_name)
    source = parse_audio(folder_name)
    
    #print(f'before session: {source}')
    session['source'] = source
    
    return redirect(url_for('views.index'))
   


@views.route('/create-playlist', methods=['POST'])
@login_required
def create_playlist():
    if request.method=="POST":
        url = request.form.get('playlist-id')
        name = request.form.get('playlist-name')
        
        
        exist_playlist = Playlist.query.filter_by(url=url).first()
        print(url, name)
        if exist_playlist:
            print('Playlist already exists!')
        else:    
            new_playlist = Playlist(url=url, name=name, user=current_user.id)
            db.session.add(new_playlist)
            db.session.commit()
            
                
        return redirect(url_for('views.index'))



@views.route('/remove-playlist/<int:pid>', methods=['GET', 'POST'])
@login_required
def remove_playlist(pid):
    exist_playlist = Playlist.query.get_or_404(pid)
    if exist_playlist:
        if exist_playlist.creator == current_user:
            db.session.delete(exist_playlist)
            db.session.commit()
                
    return redirect(url_for('views.index'))

@views.route('/like-playlist/<int:pid>', methods=['GET', 'POST'])
@login_required
def like_playlist(pid):
    #Check if you've already have liked the playlist
    already_liked = LikesTable.query.filter_by(playlist_id=pid, user_id =current_user.id).first()
    if already_liked:
        #We're gonna remove the like from the table (unlike)
        db.session.delete(already_liked)
        db.session.commit()
    else: 
        #Create a new_like row and add it to the table
        new_like = LikesTable(user_id=current_user.id, playlist_id = pid)
        db.session.add(new_like)
        db.session.commit()
    return redirect(url_for('views.index'))


def get_likes(pid):
    likes = LikesTable.query.filter_by(playlist_id=pid)
    if likes.all():
        return likes.count()
    else:
        return 0