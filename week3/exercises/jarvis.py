import pyttsx3
import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)

def Speak(audio):
    print("   ")
    assistant.say(audio)
    print("   ")
    assistant.runAndWait()


    
def takecommand():
    command = sr.recognizer()
    with sr.microphone() as source:
        print("Listening......")
    command.pause_threshold = 1
    audio = command.listen(source)

    try:
        print("Recognizing......")
        query = command.recognize_google(audio,language= 'en-in')
        print(f"You Said : {query}")
        
    except Exception as Error:
        return "None"

        return query.lower()

    query = takecommand()

    if 'hello' in query:
        Speak ("Hello Sir")

    else:
        Speak("no command found")