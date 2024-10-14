import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    playlist_link = "https://open.spotify.com/playlist/2wSNKxLM217jpZnkAgYZPH?si=53cad16dfd1e419f"
    palylist_URI = playlist_link.split("/")[-1].split("?")[0]
    
    data = sp.playlist_tracks(palylist_URI)
    
    client = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    client.put_object(
        Bucket = 'spotify-etl-pipeline-shantanu',
        Key = 'raw_data/to_processed/' + filename,
        Body= json.dumps(data)
        )
    
    
    