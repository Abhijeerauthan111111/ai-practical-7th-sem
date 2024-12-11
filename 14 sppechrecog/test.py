import speech_recognition as sr

def speech_to_text():
    # Create a recognizer instance
    recognizer = sr.Recognizer()
    
    # Use microphone as source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=2)
        
        print("Please speak something...")
        # Listen for audio input
        audio = recognizer.listen(source)
        
        try:
            # Use Google Speech Recognition to convert audio to text
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    print("Speech Recognition Program")
    print("-------------------------")
    
    # Run the speech recognition
    speech_to_text()