
from yt_dlp import YoutubeDL
import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import pandas as pd
import pathlib
import shutil, errno
# import imageio
import imageio.v2 as imageio


# my own unlisted youtube video
# https://www.youtube.com/watch?v=b9mW9njaN5c

# transform this into a gif

def _images_iris(video: VideoFileClip):


    print(video)
    print(video.duration)

def _make_path_directory(filepath):
    dir_path = os.path.dirname(filepath)
    print(f'make directory if not exists {dir_path}')
    pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True) 


def _download_iris():

    assets_dir = 'assets/hey_iris_png'
    _make_path_directory(f'{assets_dir}/1.png')

    ydl_opts = {'outtmpl': 'assets/hey_iris_full.mp4'}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info("https://www.youtube.com/watch?v=b9mW9njaN5c")
    
    
    original_video = VideoFileClip('assets/hey_iris_full.mp4')

    clipped_video: VideoFileClip = original_video.subclipped('05.00', '08.30')

    clipped_video.write_videofile('assets/hey_iris_clip.mp4')

    # https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
    i = 0

    frames = []
    while True:
        i += 1
        t = round(i / 10, 2)
        if t >= clipped_video.duration:
            break
        frame_path = os.path.join(assets_dir, f'{i}.png')
        frames.append(frame_path)
        clipped_video.save_frame(frame_path, t)

    with imageio.get_writer('assets/hey_iris.gif', mode='I', loop=0) as writer:
        for frame_path in frames:
            image = imageio.imread(frame_path)
            writer.append_data(image)

def main():

    print("populate_assets")
    _download_iris()


#uv run scripts/hey_iris.py 
main()