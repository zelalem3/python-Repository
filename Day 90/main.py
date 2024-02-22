import requests


response = requests.get("http://api.ispeech.org/api/rest?action=convert &text=something &voice=usenglishfemale\
      &format=mp3\
      &frequency=44100\
      &bitrate=128\
      &speed=1\
      &startpadding=1\
      &endpadding=1\
      &pitch=110\
      &filename=myaudiofile")
print(response)