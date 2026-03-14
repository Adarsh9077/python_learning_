import pyjokes
import pyttsx3



joke = pyjokes.get_joke()
engine = pyttsx3.init()

print(joke+ joke)
engine.say("I'm a Software Engineer and and "+ joke +"nice!")
engine.runAndWait()