import pytube
import validators

def download(fparam):
  yt = pytube.YouTube("" + fparam)
  video = yt.streams.first()
  print(video)
  video.download("./videos")

loop = True
while loop:
  url = input("Ingresa la URL: ")
  if url != "exit":
    validURL = validators.url(url)
    if url.strip() != "" and validURL == True:
      loop = False
      print('Downloading...')
      download(url)
      print('Exiting...')
    else:
      print("Invalid URL, try again...")
  else:
    loop = False
    print("Exiting...")




# help('modules')
# from pytube3 import Youtube 

