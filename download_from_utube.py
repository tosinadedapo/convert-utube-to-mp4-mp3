from pytube import YouTube
from pytube.cli import on_progress  #this module contains the built in
# progress bar.

# where to save
SAVE_PATH = "C:/Users/User/Downloads"

link = 'https://youtu.be/ySA7mSgF54I?si=v5KeU4_or6dWyuh4'
yt = YouTube(link, on_progress_callback=on_progress)
videos = yt.streams.filter(progressive=True, file_extension='mp4')

videos = videos[-1]

videos.download(output_path=SAVE_PATH)

print('Video downloaded successfully!')

