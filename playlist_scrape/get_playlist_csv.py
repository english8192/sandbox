import csv
import os
from googleapiclient.discovery import build

# Replace with your own API key
API_KEY = 'AIzaSyCCjt-vJBwFNiqra7tqtlDvWhv6AIWCvig'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_playlist_videos(playlist_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    
    videos = []
    next_page_token = None

    while True:
        playlist_items_response = youtube.playlistItems().list(
            part='snippet',
            maxResults=50,  # Max value is 50
            playlistId=playlist_id,
            pageToken=next_page_token
        ).execute()

        for item in playlist_items_response['items']:
            video_title = item['snippet']['title']
            video_id = item['snippet']['resourceId']['videoId']
            videos.append({'title': video_title, 'video_id': video_id})
        
        next_page_token = playlist_items_response.get('nextPageToken')

        if not next_page_token:
            break

    return videos

def save_to_csv(videos, filename):
    videos.reverse()
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'video_id'])
        # writer.writeheader()
        writer.writerows(videos)
        
        

if __name__ == '__main__':

    playlist_id = 'PLmesIA4XUr-exqwOf8Cliquf_CJXMrUdF' #input("Enter the YouTube playlist ID: ")
    output_file = 'vgm2.csv'            #input("Enter the output CSV filename: ")

    videos = get_playlist_videos(playlist_id)

    save_to_csv(videos, f"playlist_scrape/{output_file}")

    print(f"Successfully saved {len(videos)} videos to {output_file}")
