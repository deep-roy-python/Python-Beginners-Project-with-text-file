import os

def organize_file(file_name, extension):
  music = [".mp3",".wav"]
  video = [".mp4", ".mkv"]
  image = [".jpg",".png"]
  if extension in music:
    if "Music" not in os.listdir():
      os.mkdir("Music")
    os.rename(f"{file_name}{extension}", f"Music/{file_name}{extension}")
  elif extension in video:
    if "Video" not in os.listdir():
      os.mkdir("Video")
    os.rename(f"{file_name}{extension}", f"Video/{file_name}{extension}")
  elif extension in image:
    if "Image" not in os.listdir():
      os.mkdir("Image")
    os.rename(f"{file_name}{extension}", f"Image/{file_name}{extension}")

all_files = os.listdir()
for file in all_files:
  index = file.rfind(".")
  if index != -1:
    extension = file[index:]
    file_name = file[0:index]
    organize_file(file_name, extension)