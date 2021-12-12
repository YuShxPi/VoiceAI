import datetime
import wikipedia
import pywhatkit
import pyttsx3
import webbrowser
from playsound import playsound 

# * Initializing the voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")

# * Sets the program voice.
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

exitCommands = {
    "bye jarvis": "Bye Sir! You can call me anytime",
    "hi jarvis": "Hello Sir! What are you upto?",
    "hello jarvis": "Hi Sir! What are you doing?",
    "hello": "Hi Sir! What are you doing?",
    "hi": "Hi Sir! What are you doing?",
    "buy jarvis": "Bye Sir! You can call me anytime",
    "keep quiet": "Sorry Sir",
    "goodbye": "Bye Sir! You can call me anytime",
    "goodbye jarvis": "Bye Sir! Have a great day!",
    "good bye": "Bye Sir! You can call me anytime",
    "good bye jarvis": "Bye Sir! You can call me anytime",
    "sleep": "Ok sir! You can call me anytime",
    "clip": "Ok sir! You can call me anytime",
    "shut up": "Sorry sir, I am leaving now",
    "leave me alone": "Ok sir, Hve a good day"
}

def speak(text):
    print('')
    print(f"{text}")
    print('')
    engine.say(text)
    engine.runAndWait()

# * Searches the user query on google and wikipedia
def owner():
    speak("Piyush Acharya @r3alix01 from Kathmandu, created me as a test project.")

def googleSearch(term):

    query = term.lower()
    query = query.replace("how to", "")
    query = query.replace("what is", "")
    query = query.replace("what do you mean by", "")
    query = query.replace("search", "")
    query = query.replace("search for", "")
    query = query.replace("jarvis", "")
    query = query.replace("how to", "")
    query = query.replace("who is", "")

    mainQuery = str(term)

    try:
        if 'how to' in mainQuery:
            speak("Opening Google..")
            pywhatkit.search(mainQuery)
        else:
            searchResult = wikipedia.summary(mainQuery, sentences=2)
            speak(f"According to the Internet: {searchResult}")

    except Exception:
        pywhatkit.search(mainQuery)


def youtubeSearch(term):
    speak("Opening YouTube..")
    webbrowser.open(f'https://youtube.com/results/?search_query={term}')
    speak("This is what I found for your search")


def alarmGet(term):
    # speak("Give me time in 24 hour format")
    f = open("DataCenter\\alarm.txt", 'r+')
    f.write(term)
    f.seek(0)
    dataInside = f.read()
    mainData = str(dataInside)
    f.close()

    deleteFileData = open("DataCenter\\alarm.txt", "r+")
    deleteFileData.truncate(0)
    deleteFileData.close()

    return mainData.lower()


def alarmRing(timme):

    timeSet = str(timme)
    timeNow = timeSet.replace("jarvis ", "")
    timeNow = timeSet.replace("java ", "")
    timeNow = timeSet.replace("hey ", "")
    timeNow = timeNow.replace("set an alarm for ", "")
    timeNow = timeNow.replace("alarm for ", "")
    timeNow = timeNow.replace("alarm ", "")
    timeNow = timeNow.replace("jarvis alarm set ", "")
    timeNow = timeNow.replace("jarvis set an alarm for  ", "")
    timeNow = timeNow.replace("java set an alarm for  ", "")
    timeNow = timeNow.replace(" and ", ":")
    timeNow = timeNow.replace(" p.m. ", "")
    timeNow = timeNow.replace(" a.m. ", "")

    alarmTime = str(timeNow)
    print(alarmTime)

    while True:
        currTime = datetime.datetime.now().strftime("%H:%M")

        if currTime == alarmTime:
            speak("Wake Up Sir!")
            # playsound.playsound("DataCenter\\alarmSound.mp3")
            playsound("DataCenter\\sounds\\alarmSound.mp3")

        elif currTime > alarmTime:
            speak("Check your Input sir!")
            break

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results