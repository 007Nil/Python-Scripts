
import pytube
from pytube import YouTube

video_link = input("Enter link of YouTube Video :")

yt = YouTube(video_link)

videos = yt.streams.all()

i = 1
for stream in videos:
    print(str(i) + " " + str(stream))
    i += 1

stream_number = int(input("Enter Your Video Quality number : "))

video = videos[stream_number - 1]
video.download("/home/nil/")

print("Download Complete")
