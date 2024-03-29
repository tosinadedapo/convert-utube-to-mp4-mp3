from pytube import YouTube
from pytube.cli import on_progress  #this module contains the built in
# progress bar.

# where to save
SAVE_PATH = "C:/Users/User/Downloads"

link = 'https://youtu.be/1e9CZfQm2RU?si=3N3o4Yv11iqKD_1g'
yt = YouTube(link, on_progress_callback=on_progress)
videos = yt.streams.filter(progressive=True, file_extension='mp4')

videos = videos[-1]

videos.download(output_path=SAVE_PATH)

print('Video downloaded successfully!')

def on_progress(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz,1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion,2)

    #print(f'Total Size: {totalsz} MB')
    print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')