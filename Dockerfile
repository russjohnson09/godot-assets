# https://hub.docker.com/r/linuxserver/ffmpeg

# RUN apt-get -y update
# RUN apt-get -y upgrade
# RUN apt-get install -y ffmpeg

# FROM linuxserver/ffmpeg:version-8.1-cli

# FROM linuxserver/ffmpeg:version-8.1-cli
FROM ubuntu:22.04

RUN apt-get update && apt-get install ffmpeg libvorbis-dev -y
# sudo apt build-dep libvorbis


COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# copy uv

WORKDIR /data

COPY . .


RUN uv sync


#ffmpeg -i assets/stormfront_punched_maeve.mkv assets/test.mp4
#ffmpeg -i assets/stormfront_punched_maeve.mkv assets/test.ogv


# docker build . -t ffmpeg:test
# docker images
# docker run -it exec  ffmpeg:test

# TODO youtube download + ffmpeg for a full video editor
CMD ["tail", "-f", "/dev/null"]