import speech_recognition as sr
import webbrowser
sr.Microphone(device_index=1)
r=sr.Recognizer()
r.energy_threshold=20000
with sr.Microphone()as source:
    print("what you want to search:")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        url="https://www.google.co.in/search?q="
        search_url=url+text
        webbrowser.open(search_url)
    except:
        print("cant recognize")