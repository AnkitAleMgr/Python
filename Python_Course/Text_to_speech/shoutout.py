from gtts import gTTS
from playsound import playsound
import os


def main():
    # input section
    text = ""
    while True:
        # forcing user to put valid input
        text = input("Enter text to convert into speech: ")
        if text == "":
            print("It cannot be emput. Please enter the value again.")
        elif not text.isalnum():
            print("Invalid input please try again.")
        else:
            break

    # logic section 
    tts = gTTS(text= text, lang= "en", slow=False)
    tts.save("output.mp3")
    print("Text has been convented into speech as file named \" output.mp3\"")
    playsound("output.mp3")
    

if __name__ == "__main__":
    main()