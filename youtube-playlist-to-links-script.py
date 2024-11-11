from pytube import Playlist

playlist_url = "INSERT THE PLAYLIST YOUTUBE URL HERE"

playlist = Playlist(playlist_url)

# Get all the video links from the playlist
video_links = playlist.video_urls

# Display the links
for link in video_links:
    print(link)
