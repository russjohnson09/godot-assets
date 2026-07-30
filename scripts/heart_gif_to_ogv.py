
from yt_dlp import YoutubeDL
import os
from moviepy import VideoFileClip
import pathlib
import imageio.v2 as imageio


# my own unlisted youtube video
# https://www.youtube.com/watch?v=b9mW9njaN5c

# transform this into a gif

def _make_path_directory(filepath):
    dir_path = os.path.dirname(filepath)
    print(f'make directory if not exists {dir_path}')
    pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True) 


def _gif_to_png():

    assets_dir = 'assets/wikimedia_commons/Real_Human_Heart_Turntable_gif'
    original_video = VideoFileClip('assets/wikimedia_commons/Real_Human_Heart_Turntable.gif')

    ffmpeg_params = [
        # "-qscale", "0",
        "-q:v", "10",
        # "-q:a", "2"
    ]

    original_video.write_videofile('assets/wikimedia_commons/Real_Human_Heart_Turntable.ogv', ffmpeg_params = ffmpeg_params)

    # print(original_video)

    # counter = 0
    # # https://www.geeksforgeeks.org/python/moviepy-iterating-frames-of-video-file-clip/
    # for frame in original_video.iter_frames():
    #     # print(frame)
    #     counter += 1
    #     print(counter)

def main():

    print("populate_assets")
    _gif_to_png()


#uv run scripts/heart_gif_to_ogv.py 
main()