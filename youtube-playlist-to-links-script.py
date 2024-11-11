from pytube import Playlist

playlist_url = "https/www.youtube.com/playlist?list=PLT0FbUlqszacT_OjsY0V0hwpdV055PIf9&si=YpVKEPEdqoly4Sgx"

playlist = Playlist(playlist_url)

# Получить ссылки на все видео в плейлисте
video_links = playlist.video_urls

# Вывести ссылки
for link in video_links:
    print(link)
