


def game1():
    import random
    import tkinter as tk
    import pyttsx3
    import speech_recognition as sr
    from tkinter import messagebox

    class WinnerDeclarationWindow:

        def _init_(self, winner):
            self.window = tk.Toplevel()
            self.window.title("Winner Declaration")
            self.winner = winner

            label = tk.Label(self.window, text=f"{self.winner} are the winner!", font=("Helvetica", 16))
            label.pack(pady=20)

            image_path =r"C:\Users\91744\OneDrive\Desktop\img alexa\trophy.gif" if self.winner == "You" else r"C:\Users\91744\OneDrive\Desktop\img alexa\computer.gif"
            trophy_image = tk.PhotoImage(file=image_path)
            trophy_label = tk.Label(self.window, image=trophy_image)
            trophy_label.image = trophy_image  # Retain a reference to the image to prevent garbage collection
            trophy_label.pack()

            ok_button = tk.Button(self.window, text="OK", command=self.close_window)
            ok_button.pack(pady=20)

        def close_window(self):
            self.window.destroy()

    class RockPaperScissorsGame:
        def _init_(self):

            self.app = tk.Tk()
            self.app.title("Rock, Paper, Scissors Game")
            
            self.user_wins = 0

            self.computer_wins = 0
            self.rounds_played = 0

            self.create_gui()

            self.recognizer = sr.Recognizer()

            self.engine = pyttsx3.init()

        def create_gui(self):
            self.result_label = tk.Label(self.app, text="", font=("Helvetica", 16))
            self.result_label.pack(pady=20)

            frame = tk.Frame(self.app)
            frame.pack()


            choices = ["rock", "paper", "scissors"]
            button_colors = {'rock': 'red', 'paper': 'green', 'scissors': 'blue'}

            for choice in choices:

                button = tk.Button(frame, text=choice.capitalize(),
                                   command=lambda ch=choice: self.play_with_user_choice(ch), bg=button_colors[choice])
                button.pack(side=tk.LEFT, padx=10, pady=10)

            voice_button = tk.Button(frame, text="Voice Input", command=self.get_user_voice_input, bg='purple',
                                     fg='white')
            voice_button.pack(side=tk.LEFT, padx=10, pady=10)

        def get_user_voice_input(self):
            with sr.Microphone() as source:
                self.result_label.config(text="Listening...")
                audio = self.recognizer.listen(source)

            try:
                user_choice = self.recognizer.recognize_google(audio).lower()
                if user_choice in ["rock", "paper", "scissors"]:
                    self.play_with_user_choice(user_choice)
                else:
                    self.result_label.config(text="Invalid choice. Please say rock, paper, or scissors.")
            except sr.UnknownValueError:
                self.result_label.config(text="Sorry, I couldn't understand your voice.")
            except sr.RequestError:
                self.result_label.config(text="Sorry, there was an error with the voice recognition service.")

        def play_with_user_choice(self, user_choice):
            if self.rounds_played < 7:
                computer_choice = random.choice(["rock", "paper", "scissors"])
                result = self.determine_winner(user_choice, computer_choice)
                self.update_result_label(user_choice, computer_choice, result)

                self.rounds_played += 1
                if self.rounds_played == 7:
                    self.determine_overall_winner()

        def determine_winner(self, user_choice, computer_choice):
            if user_choice == computer_choice:
                return "It's a tie!"
            elif ((user_choice == "rock" and computer_choice == "scissors") or
                  (user_choice == "scissors" and computer_choice == "paper") or
                  (user_choice == "paper" and computer_choice == "rock")):
                self.user_wins += 1
                return "You win!"
            else:
                self.computer_wins += 1
                return "Computer wins!"

        def update_result_label(self, user_choice, computer_choice, result):
            result_text = f"You chose {user_choice}, Computer chose {computer_choice}. {result}"
            self.result_label.config(text=result_text)

            # Speak the result
            self.speak(result_text)

        def determine_overall_winner(self):
            if self.user_wins > self.computer_wins:
                winner = "You"
            elif self.user_wins < self.computer_wins:
                winner = "Computer"
            else:
                winner = "It's a tie"

            overall_result = f"Game over! {winner} won {max(self.user_wins, self.computer_wins)} rounds."
            self.result_label.config(text=overall_result)

            # Display a pop-up message for the winner
            messagebox.showinfo("Winner Declaration", f"{winner} is the winner!")

            # Open the winner declaration window
            WinnerDeclarationWindow(winner)

        def speak(self, text):
            self.engine.say(text)
            self.engine.runAndWait()

        def run(self):
            self.app.mainloop()

    if __name__ == "__main__":
        game = RockPaperScissorsGame()
        game.run()


from googletrans import Translator
import pyttsx3
import speech_recognition as sr
import os
import pygame
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

engine = pyttsx3.init()
recognizer = sr.Recognizer()
api_key = 'e2f88f2ec9094fe380db862d25d13f05'
print("apps that can be open with me are: google,chrome,notepad,calculator,mail,edge,explorer,control panel,task manager,registry,powershell,settings,whatsapp,insta,facebook,twitter,snapchat,camera")
base_url = 'https://newsapi.org/v2/top-headlines'
news_params = {
    'country': 'in',
    'language': 'en',
    'apiKey': api_key,
}
engine = pyttsx3.init()


# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize pygame for music playback
pygame.mixer.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"An error occurred: {str(e)}")
        return ""
def open_application(application_name):
    if "chrome" in application_name:
        os.system("start chrome")
    if "google" in application_name:
        os.system("start chrome")
    elif "notepad" in application_name:
        os.system("start notepad")
    elif "calculator" in application_name:
        os.system("start calc")
    elif "mail" in application_name:
        recipient_email = "recipient@example.com"
        subject = "Hello from Python"
        body = "This is the body of the email."
        # Construct the mailto URL
        mailto_url = f"mailto:{recipient_email}?subject={subject}&body={body}"
        # Open the default email client
        os.system(f'start "" "{mailto_url}"')
    elif "edge" in application_name:
        os.system("start microsoft-edge:")
    elif "explorer" in application_name:
        os.system("explorer")
    elif "control panel" in application_name:
        os.system("control")
    elif "task manager" in application_name:
        os.system("taskmgr")
    elif "registry" in application_name:
        os.system("regedit")
    elif "powershell" in application_name:
        os.system("powershell")
    elif "settings" in application_name:
        os.system("start ms-settings:")
    elif "whatsapp" in application_name:
        os.system("start whatsapp://")
    elif "insta" in application_name:
        os.system("start instagram://")
    elif "camera" in application_name:
        os.system("start microsoft.windows.camera:")
    else:
        print(f"I don't know how to open {application_name}.")
def get_current_datetime():
    now = datetime.now()
    current_time = now.strftime("%H:M:S")
    current_date = now.strftime("%Y-%m-d")
    return f"Current date is {current_date} and current time is {current_time}"

def retrieve_and_speak_news():
    response = requests.get(base_url, params=news_params)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']

        if articles:
            news_text = "Here are the latest news headlines for India in English:\n"

            for i, article in enumerate(articles):
                title = article['title']
                # Modify this line to include only the title
                news_text += f"{i + 1}. {title}\n"
            print(news_text)

        else:
            print("No news articles found for India.")
            speak("No news articles found for India.")
    else:
        print(f"Failed to retrieve English news updates for India. Status code: {response.status_code}")
        speak(f"Failed to retrieve English news updates for India. Status code: {response.status_code}")
is_video_playing = False

def capture_voice():
    with sr.Microphone() as source:
        print("Listening for a search query or 'stop' to end the video...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"An error occurred: {str(e)}")
        return ""


def open_youtube():
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search')))
    print("YouTube is ready.")


def main():
    print("Welcome to your assistant!")

    while True:
        command = listen_for_command()

        if "open" in command:
            application_name = command.replace("open", "").strip()
            open_application(application_name)
            print("You said:", command)
            speak(f"You said: {command}")

        elif "play" in command:
            song_request = command.replace("play", "").strip()
            song_directory = {
             "mini mix": r"C:\Users\91744\Downloads\music\MINI MiX - English songs.mp3",
             "believer": r"C:\Users\91744\Downloads\music\Believer(PagalWorld).mp3",
             "miles and more":r"C:\Users\91744\Downloads\music\Miles & More - English Song.mp3",
                # Add more song mappings as needed

            }

            if song_request in song_directory:
                song_path = song_directory[song_request]
                play_song(song_path)
                print(f"Now playing: {song_request}")
                speak(f"Now playing: {song_request}")

        elif "exit" in command:
            print("Goodbye!")
            speak("Goodbye! Have a nice day.")
            break

        elif "date and time" in command:
            current_datetime = get_current_datetime()
            print(current_datetime)
            speak(current_datetime)
        elif "today" in command:
            retrieve_and_speak_news()

        if "youtube" in command:
            open_youtube()
            is_video_playing = True
            while True:
                video_search_query = capture_voice()

                if video_search_query == "stop":
                    print("Stopping YouTube video.")
                    speak("Stopping YouTube video.")
                    is_video_playing = False
                    driver.quit()
                    break
                elif video_search_query:
                    driver.get('https://www.youtube.com/results?search_query={}'.format(video_search_query))
                    try:
                        # Wait for the first video result to become clickable
                        first_video = driver.find_element(By.CSS_SELECTOR, '#video-title')
                        first_video.click()
                        print(f"Video for '{video_search_query}' opened successfully.")

                        # Play the video
                        body = driver.find_element(By.TAG_NAME, 'body')
                        body.send_keys(Keys.SPACE)  # Press the "k" key to play/pause

                        while True:
                            if driver.execute_script(
                                    "return document.getElementById('movie_player').getPlayerState()") == 0:
                                print("Video has ended.")
                                is_video_playing = False
                                break

                            # Ckapture the user's voice during video playback
                            video_command = capture_voice()
                            if video_command == "stop":
                                print("Stopping the video.")
                                body.send_keys("k")  # Press "k" key to pause
                                driver.quit()
                                is_video_playing = False
                                break

                    except Exception as e:
                        print("An error occurred:", str(e))

        elif "translate" in command:
            print("Please provide a sentence for translation.")
            speak("Please provide a sentence for translation.")
            user_sentence = listen_for_command()


            print("Please specify the target language for translation.")
            speak("Please specify the target language for translation.")
            target_language = listen_for_command()



            try:
                translator = Translator()
                translated_sentence = translator.translate(user_sentence, dest=target_language).text
                print(f"Translation to {target_language}: {translated_sentence}")
                speak(f"Translation to {target_language}: {translated_sentence}")
            except ValueError:
                print("Invalid target language. Please provide a valid language code (e.g., 'fr' for French).")
                speak("Invalid target language. Please provide a valid language code.")
        elif "game" in command:
            game1()

        elif "exit" in command:
            print("Goodbye!")
            speak("Goodbye! Have a nice day.")
            break

if __name__ == "__main__":
    main()