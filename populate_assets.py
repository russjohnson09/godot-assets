
from yt_dlp import YoutubeDL
import os
from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import pandas as pd
import pathlib
import shutil, errno


IRIS_DEATH = "https://www.youtube.com/watch?v=3IPIPLM8ELY"


_dir = os.path.dirname(__file__)
_assets_dir = os.path.abspath(os.path.join(_dir, 'assets'))

def _get_full_path(downloaded, format = 'mp4', directory = _dir):
    id = downloaded.get('id')
    title = downloaded.get('title')

    filename = f'{title} [{id}].{format}'
    return  os.path.abspath(os.path.join(_dir, filename))


def _parse_iris_audio():

    pass


def _get_timing(file_path):
    df = pd.read_csv(file_path, keep_default_na=False)

    dict_output = df.to_dict(orient="index")

    print(dict_output)
    # tests\test_font.py {0: {'start': 1000, 'text': 'PRESS'}, 1: {'start': 2000, 'text': ''}, 2: {'start': 3000, 'text': 'ZIP'}}
    
    result = []
    for key in list(dict_output.keys()):
        row = dict_output[key]
        result.append(row)

    print(result)
    return result


def _make_path_directory(filepath):
    dir_path = os.path.dirname(filepath)
    print(f'make directory if not exists {dir_path}')
    pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True) 


def _get_mp3_filename(assets_dir, text: str):
    filename = text
    filename = f'{filename}.mp3'
    return os.path.abspath(os.path.join(assets_dir, filename)) 

def _save_mp3_from_timing_array(assets_dir, video: VideoFileClip, timing_array):

    count = 0
    for timing in timing_array:
        count += 1
        print(timing)

        filepath = _get_mp3_filename(assets_dir, f'{count}. {timing.get('text')}')

        clipped_video = video.subclipped(timing.get('start'), timing.get('end'))

        _make_path_directory(filepath)
        clipped_video.audio.write_audiofile(filepath)

def _audio_clips_iris_death(original_video):
    timing_array = _get_timing(os.path.dirname(__file__) + '/iris_death.csv')
    print(timing_array)
    assets_dir = os.path.dirname(__file__) + '/assets/iris_death_audio'
    _save_mp3_from_timing_array(assets_dir, original_video, timing_array)

def _audio_clips_the_boys(original_video):
    timing_array = _get_timing(os.path.dirname(__file__) + '/the_boys.csv')
    assets_dir = os.path.dirname(__file__) + '/assets/the_boys_audio'
    _save_mp3_from_timing_array(assets_dir, original_video, timing_array)

def _images_iris(video: VideoFileClip):
    assets_dir = os.path.dirname(__file__) + '/assets/iris_death_png'
    _make_path_directory(f'{assets_dir}/1.png')

    print(video)
    print(video.duration)

    i = 0
    while True:
        i += 1
        t = round(i / 10, 2)
        if t >= video.duration:
            return
        # print(t)
        # print(os.path.join(assets_dir, f'{t}.png'))

        video.save_frame(os.path.join(assets_dir, f'{t}.png'), t)


def _images_iris_2(video: VideoFileClip):
    assets_dir = os.path.dirname(__file__) + '/assets/iris_2_png'
    _make_path_directory(f'{assets_dir}/1.png')

    i = 0
    while True:
        i += 1
        t = round(i / 10, 2)
        if t >= video.duration:
            return
        # print(t)
        # print(os.path.join(assets_dir, f'{t}.png'))

        video.save_frame(os.path.join(assets_dir, f'{t}.png'), t)


def _images_boys(video: VideoFileClip):
    assets_dir = os.path.dirname(__file__) + '/assets/the_boys_png'
    _make_path_directory(f'{assets_dir}/1.png')

    i = 0
    while True:
        i += 1
        t = round(i / 10, 2)
        if t >= video.duration:
            return
        # print(t)
        # print(os.path.join(assets_dir, f'{t}.png'))

        video.save_frame(os.path.join(assets_dir, f'{t}.png'), t)

def _download_iris():
    # os.chdir(_assets_dir, 'iris')
    # https://stackoverflow.com/questions/41240726/change-the-output-name-when-download-with-youtube-dl-using-python
    ydl_opts = {'outtmpl': 'assets/iris_death.mp4'}
    with YoutubeDL(ydl_opts) as ydl:
        downloaded = ydl.extract_info(IRIS_DEATH)
        # print("result")
        # print(downloaded.get('id'))
        # print(downloaded.get('title'))
        # fullpath = _get_full_path(downloaded)
        # print(fullpath)
        # os.rename(fullpath, os.path.abspath(os.path.join(_assets_dir, 'iris_death.mp4')))
        # Megaman X4： Iris's Death [3IPIPLM8ELY].mp4
    
    
    original_video = VideoFileClip('assets/iris_death.mp4')
    original_video.audio.write_audiofile('assets/iris_death.mp3')
    _audio_clips_iris_death(original_video)

    _images_iris(original_video)

    # 

def _clip_the_boys():
    original_video: VideoFileClip = VideoFileClip('assets/The Boys S02E08 What I Know 1080p BluRay R10Bit DDP5 1 HEVC-d3g[EZTVx.to].mkv')
    print("clip")
    print(original_video)

    my_file =  pathlib.Path('assets/boys_s02e08.mp3')

    if not my_file.is_file():
        # file does not exist
        original_video.audio.write_audiofile('assets/boys_s02e08.mp3')

    
    _audio_clips_the_boys(original_video)

    video: VideoFileClip = original_video.subclipped('44:02.8', '44:07.2')
    _images_boys(video)

    # audio=False
    # 44:02  - 44:06
    # video.write_videofile('assets/stormfront_punched_maeve.mp4')


    #   File "C:\Users\russj\dev\not-a-fan-of-repliforce\python-scripts\.venv\Lib\site-packages\moviepy\video\VideoClip.py", line 393, in write_videofile
    # ffmpeg_write_video(
    # ~~~~~~~~~~~~~~~~~~^
        # self,

    #  [vost#0:0 @ 0000026a3e8db600] Invalid encoder type 'libvorbis'
    
    # https://stackoverflow.com/questions/37325629/efficient-ogv-video-conversion-in-linux
    # https://stackoverflow.com/questions/25569180/ffmpeg-convert-without-loss-quality
    # https://superuser.com/questions/1096841/how-do-i-convert-mp4-to-ogv-while-still-retaining-the-same-quality-using-ffmpeg
    ffmpeg_params = [
        # "-qscale", "0",
        "-q:v", "2",
        "-q:a", "2"

    ]
    video.write_videofile('assets/stormfront_punched_maeve.ogv', ffmpeg_params = ffmpeg_params)
    # video.write_videofile('assets/stormfront_punched_maeve.mkv')




def copy_dir_or_file(src, dst):
    # https://stackoverflow.com/questions/1994488/copy-file-or-directories-recursively-in-python
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
    except OSError as exc: # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else: raise

def _download_iris_2():
    # https://stackoverflow.com/questions/41240726/change-the-output-name-when-download-with-youtube-dl-using-python
    ydl_opts = {'outtmpl': 'assets/mmx4_all.mp4'}
    with YoutubeDL(ydl_opts) as ydl:
        downloaded = ydl.extract_info("https://www.youtube.com/watch?v=ppKAi63EHRo")
        # print("result")
        # print(downloaded.get('id'))
        # print(downloaded.get('title'))
        # fullpath = _get_full_path(downloaded)
        # print(fullpath)
        # os.rename(fullpath, os.path.abspath(os.path.join(_assets_dir, 'iris_death.mp4')))
        # Megaman X4： Iris's Death [3IPIPLM8ELY].mp4
    
    
    original_video = VideoFileClip('assets/mmx4_all.mp4')
    # original_video.audio.write_audiofile('assets/iris_death.mp3')
    # _audio_clips_iris_death(original_video)

    clipped_video = original_video.subclipped('5:59', '6:02')

    _images_iris_2(clipped_video)
    pass



def main():

    print("populate_assets")
    _download_iris()
    _download_iris_2()
    
    _clip_the_boys()
    # _copy_assets_to_godot()

main()