from pytube import YouTube
import pytube.exceptions

# where to save
SAVE_PATH = "C:/Users/User/Downloads"

# link of the video to be downloaded
links = open('links_file.txt', 'r')

for link in links:
    try:
        # object creation using YouTube
        yt = YouTube(link)

        # Get all streams and filter for mp4 files
        mp4_streams = yt.streams.filter(progressive=True,
                                        file_extension='mp4')

        for stream in mp4_streams:
            print('The number of stream ia .. ', stream)

        # get the video with the highest resolution
        d_video = mp4_streams[-1]

        # downloading the video
        d_video.download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')

    except Exception as e:
        print("Encounter Error |  " + format(e))

