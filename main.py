import requests
import urllib.parse
from datetime import datetime, timedelta
from flask import Flask, redirect, request, jsonify, session
import json

def save_to_json(data):
    with open('spotify_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET KEY'
store_artist = []

CLIENT_ID = 'b0dbe6cff93d4d5eb182253a5f1a7fc2'
CLIENT_SECRET = 'CLIENT_SECRET_KEY'
REDIRECT_URI = 'http://localhost:5000/callback'

AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'

@app.route('/')
def index():
    return "Welcome to my Spotify App <a href='/login'>login with Spotify </a>"

@app.route('/login')
def login():
    scope = 'user-read-private user-read-email user-read-playback-state user-read-recently-played'

    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'show_dialog': True
    }

    auth_url = f"{AUTH_URL}?{urllib.parse.urlencode(params)}"

    return redirect(auth_url)

@app.route('/callback')
def callback():
    if 'error' in request.args:
        return jsonify({"error": request.args['error']})
    
    if 'code' in request.args:
        req_body = {
            'code': request.args['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }

        response = requests.post(TOKEN_URL, data=req_body)
        token_info = response.json()

        session['access_token'] = token_info['access_token']
        session['refresh_token'] = token_info['refresh_token']
        session['expires_at'] = datetime.now().timestamp() + token_info['expires_in']

        return redirect('/player/recently-played')

@app.route('/player/recently-played')    
def get_player():
    if 'access_token' not in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        return redirect('/refresh_token')
    
    headers = {
        'Authorization': f"Bearer {session['access_token']}"
    }

    params = {
        'limit': 5
    }

    response = requests.get(API_BASE_URL + 'me/player/recently-played', headers=headers, params=params)
    player = response.json()

    genres = set()
    for item in player.get('items', []):
        artist = item.get('track', {}).get('artists', [])
        for art in artist:
            artist_id = art.get('id')
            artist_info = requests.get(API_BASE_URL + f'artists/{artist_id}', headers=headers).json()
            genres.update(artist_info.get('genres', []))
    
    with open('recent_genres.txt', 'w') as file:
        for genre in genres:
            file.write(f'{genre}\n')

    save_to_json(player)

    return jsonify(player)
    
@app.route('/refresh-token')
def refresh_token():
    if 'refresh_token' in session:
        return redirect('/login')
    
    if datetime.now().timestamp() > session['expires_at']:
        req_body = {
            'grant_type': 'refresh_token',
            'refresh_token': session['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }

        response = requests.post(TOKEN_URL, data=req_body)
        new_token_info = response.json()

        session['access_token'] = new_token_info['access_token']
        session['expires_at'] = datetime.now().timestamp() + new_token_info['expires_in']

        return redirect('/player/recently-played')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
