import pyttsx3

friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice',voices[1].id)
friend.say("czy,how are you?")
friend.runAndWait()
