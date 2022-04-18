from gtts import gTTS							#pip install gtts
from playsound import playsound					#pip install playsound

audio ='sound.mp3'
language = 'ru'															#указываем язык
sp = gTTS(text = "Здесь пишется текст для воспроизведения!!!",			#пишем тескт
		  lang = language,slow=False)

sp.save(audio)
playsound(audio)	  
