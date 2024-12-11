import speech_recognition as sr

def main():
    # Create a recognizer instance
    recognizer = sr.Recognizer()
    
    # Use microphone as source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Please speak something...")
        # Listen for audio input
        audio = recognizer.listen(source)
        
        try:
            # Use Google Speech Recognition to convert audio to text
            text = recognizer.recognize_google(audio)
            print("\nYou said:", text)
            
            # Basic text processing
            print("\nBasic text analysis:")
            print("Number of words:", len(text.split()))
            print("Number of characters:", len(text))
            print("All uppercase:", text.upper())
            print("All lowercase:", text.lower())
            
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()