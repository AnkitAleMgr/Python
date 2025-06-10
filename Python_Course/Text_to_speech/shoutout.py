from gtts import gTTS
import os


def main():
    # input section
    text = ""
    while True:
        # forcing user to put valid input
        text = input("Enter text to convert into speech: ")
        if text == "":
            print("It cannot be empty. Please enter the value again.")
        elif not all(x.isalnum() or x.isspace() for x in text) or not any(x.isalpha() for x in text):
            print("Invalid input please try again.")
        else:
            break


    # logic section 
    tts = gTTS(text= text, lang= "en", slow=False)
    tts.save("output.mp3")
    print("Text has been convented into spe`ech as file named \" output.mp3\"")
    os.system("afplay output.mp3")
    

if __name__ == "__main__":
    main()