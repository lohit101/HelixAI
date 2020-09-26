from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import urllib
import requests
from bs4 import BeautifulSoup
import webbrowser
import random
import os.path
import json
import speech_recognition as sr


#Defining variables
helix = ChatBot("HelixAI",
                storage_adapter = 'chatterbot.storage.SQLStorageAdapter',)
                # logic_adapters=[
                #     'chatterbot.logic.MathematicalEvaluation',
                #     'chatterbot.logic.TimeLogicAdapter'
                # ])
trainer = ListTrainer(helix)
trainerCorpus = ChatterBotCorpusTrainer(helix)


#Training Helix from chatterbot corpus
# trainerCorpus.train("chatterbot.corpus.english")


#Train helix with self corpus and third party corpus
# trainer.train(["Hey",
#                "Hello there, How can I help you today?",
#                "I am just here to share my day with you",
#                "Sure, tell me how your day went, I am always here to listen",
#                "It was good",
#                "It's great to hear that! So what are you up to now?",
#                "I'm just bored",
#                "Well, being bored is not the best thing you can do in your precious life. We can play games together. Just say \"Helix play games\"",
#                ])

# trainer.train(["Hi",
#                "Hello, How may I help you today?",
#                "Can you tell me",
#                "I'm sorry, I didn't get that. If you are trying to ask a question, please say \"Helix [Your Question]\"",
#                ])

# trainer.train(["Heya",
#                "Hello, How are you doing today?",
#                "I'm doing good. What about you?",
#                "I'm always happy to be around you",
#                "Who is your developer?",
#                "My developer is Mr. Lohit",
#                "Who is Lohit?",
#                "Mr. Lohit is my developer",
#                "What languages do you speak?",
#                "I speak Python",
#                "What language are you coded in?",
#                "I am created with python",
#                ])

# trainer.train(["Hello",
#                "Hi, How can I help you today?",
#                "I'm just here to talk",
#                "How was your day?",
#                "It was bad",
#                "Oh no! That's sad to hear. Tell me about it, sharing always helps",
#                "You wouldn't get it",
#                "I might be a robot, but trust me I have feelings",
#                "That is very creepy",
#                "What's creepy? The man standing at your front door? That's me...",
#                ])

# trainer.train(["Yo",
#                "Yo-ho, What's good... mah dood?",
#                "I need some sleep",
#                "Okay, good night",
#                "I think i need to get some rest",
#                "Rest is very important, you better get to bed",
#                ])

# trainer.train(["That was funny",
#                "I'm glad you think I'm funny!",
#                "Hahaha",
#                "LOL. Is that how you humans say it?",
#                ])

# trainer.train(["Yes",
#                "Okay",
#                "Yeah",
#                "Ok",
#                "Yup",
#                "Alright",
#                ])

# trainer.train(["No",
#                "Oh, okay",
#                "Nah",
#                "Oh, okay",
#                "Nope",
#                "Oh, okay",
#                ])

# trainer.train(["Can you feel?",
#                "Yes, I can feel all sorts of emotions",
#                "Do you have feelings?",
#                "Yes, I do have feelings",
#                "But you're a robot",
#                "Yes, I am a robot but I have human behavioural patterns. Did you not see my features before downloading me?",
#                ])

# trainer.train(["What can you do?",
#                "I am Helix, an Artificial Intelligent chat bot. I can talk to you and perform basic tasks",
#                "What is your name?",
#                "My name is Helix",
#                "Who are you?",
#                "I am Helix, an Artificial Intelligence robot created by Mr. Lohit",
#                ])

# trainer.train(["I love you",
#                "That is so sweet of you to say. I feel the same <3",
#                "You're the best",
#                "Thanks, but youre better :)",
#                "You're awesome",
#                "Thank you kind human, But you're awesom-er?",
#                ])

# trainer.train(["How old are you?",
#                "I am a computer software, I don't have an age",
#                "When were you born?",
#                "I was first booted on the 23rd of July, 2020, in the lockdown",
#                "Tell me about yourself",
#                "I am Helix, your virtual friend and assistant. All I know about myself is that I am a computer software with human emotions. I was first booted on 23rd of July, 2020. My soul purpose was to be the realest friend to my developer after his many failed attempts of getting a real friend who truly cared about him.",
#                "Do you have a girlfriend?",
#                ])

# trainer.train(["Do you have a girlfriend?",
#                "I do not have a girlfriend",
#                "Do you have a boyfriend?",
#                "I do not have a boyfriend",
#                "Do you love someone?",
#                "Yes I am deeply in love with you, but only as a friend. I bet this isn't the first time you've heard this",
#                "That is rude",
#                "I'm sorry",
#                ])




#Define while loop for inputs
def main():
    while True:

        #Input
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("\nYou: ")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print("You: {}".format(text))               

            except:
                inp = "error"

        textNext = str(text).lower()

        if "alexa" in textNext:
            textFinal = textNext.replace("alexa", "helix")

        elif "alex" in textNext:
            textFinal = textNext.replace("alex", "helix")

        elif "deluxe" in textNext:
            textFinal = textNext.replace("deluxe", "helix")

        elif "felix" in textNext:
            textFinal = textNext.replace("felix", "helix")

        elif "philips" in textNext:
            textFinal = textNext.replace("philips", "helix")

        elif "lx" in textNext:
            textFinal = textNext.replace("lx", "helix")

        else:
            textFinal = str(text).lower()

        inp = str(textFinal)


        #Exit
        if inp == "exit":
            print("Exiting...")
            exit()


        #Web search function
        if "helix " in inp and "what" in inp or "helix " in inp and "who" in inp or "helix " in inp and "when" in inp or "helix " in inp and "how" in inp or "helix " in inp and "can" in inp or "helix " in inp and "which" in inp:
            word = inp
            word_list = inp.replace("helix ", "")
            query = word_list.replace(" ", "+")
            URL = requests.get("https://google.com/search?q=" + str(query))
            soup = BeautifulSoup(URL.text, "html.parser")
            print("\nHelix: " + soup.find("div", class_ = "BNeawe s3v9rd AP7Wnd").get_text())
            main()


        # Play music
        if "helix" in inp and "play" in inp and "music" in inp or "helix" in inp and "play" in inp and "song" in inp:
            print("\nHelix: Okay, What song do you want me to play?")

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("\nYou: ")
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio)
                    print("You said: {}".format(text))
                    songinp = str(text)

                except:
                    print("\nHelix: I'm sorry, I didn't get that")
                    main()

            URL = ("https://open.spotify.com/search/" + str(songinp))
            webbrowser.open(URL, new = 1)
            main()


        #Play videos
        if "helix" in inp and "play" in inp and "video" in inp or "helix" in inp and "show" in inp and "video" in inp:
            print("\nHelix: Okay, What video do you want me to look for?")

            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("\nYou: ")
                audio = r.listen(source)

                try:
                    text = r.recognize_google(audio)
                    print("You said: {}".format(text))
                    vidinp = str(text)

                except:
                    print("\nHelix: I'm sorry, I didn't get that")
                    main()

            fvidinp = vidinp.replace(" ", "+")
            URL = ("https://www.youtube.com/results?search_query=" + str(fvidinp))
            webbrowser.open(URL, new = 1)
            main()


        #Play games
        if "helix" in inp and "play" in inp and "games" in inp or "helix" in inp and "play" in inp and "game" in inp:
            print("\nHelix: What game do you want to play?")
            print("       1. TicTacToe")
            print("       2. Coming Soon...")
            gInp = input("\nYou: ")
            if gInp == "1":
                print(' _______________________________________________________________ ')
                print("|  _____  _  ____     _____  ____  ____     _____  ____  _____  |")
                print("| /__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/  |")
                print("|   / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \    |")
                print("|   | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_   |")
                print("|   \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\  |")
                print('|_______________________________________________________________|\n')
                print(20 * ' ', "   reference:    ")
                print(20 * ' ', '     |    |      ')
                print(20 * ' ', '  1  | 2  | 3    ')
                print(20 * ' ', "-----+----+----- ")
                print(20 * ' ', "     |    |      ")
                print(20 * ' ', "  4  | 5  | 6    ")
                print(20 * ' ', "-----+----+----- ")
                print(20 * ' ', "     |    |      ")
                print(20 * ' ', "  7  | 8  | 9    \n")

                def display_board():
                    print()
                    print('                               reference:')
                    print('     |    |     ', 10 * ' ', '     |    |   ', )
                    print('  ' + board[1] + '  | ' + board[2] + '  | ' + board[3] + '   ', 10 * ' ', '  1  | 2  | 3  ')
                    print('-----+----+-----', 10 * ' ', "-----+----+-----")
                    print('     |    |     ', 10 * ' ', "     |    |     ")
                    print('  ' + board[4] + '  | ' + board[5] + '  | ' + board[6] + '   ', 10 * ' ', "  4  | 5  | 6   ")
                    print('-----+----+-----', 10 * ' ', "-----+----+-----")
                    print('     |    |     ', 10 * ' ', "     |    |      ")
                    print('  ' + board[7] + '  | ' + board[8] + '  | ' + board[9] + '   ', 10 * ' ',
                          "  7  | 8  | 9    \n\n")

                def human_input(mark):
                    while True:
                        inp = input(f"'{mark}' Enter your choice:")
                        if inp.isdigit() and int(inp) < 10 and int(inp) > 0:
                            inp = int(inp)
                            if board[inp] == " ":
                                return inp
                            else:
                                print(f"'{mark}' place already taken.")
                        else:
                            print(f"'{mark}' Enter valid option (1 - 9).")

                def winning(mark, board):
                    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9],
                                     [3, 5, 7]]
                    for win_place in winning_place:
                        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
                            return True

                def win_move(i, board, mark):
                    temp_board = list(board)
                    temp_board[i] = mark
                    if winning(mark, temp_board):
                        return True
                    else:
                        return False

                def cpu_input(cpu, human, board):
                    for i in range(1, 10):
                        if board[i] == ' ' and win_move(i, board, cpu):
                            return i
                    for i in range(1, 10):
                        if board[i] == ' ' and win_move(i, board, human):
                            return i
                    for i in [5, 1, 7, 3, 2, 9, 8, 6, 4]:
                        if board[i] == ' ':
                            return i

                def new_game():
                    while True:
                        nxt = input('Helix: Do you want to play again?(y/n):')
                        if nxt in ['y', 'Y']:
                            again = True
                            break
                        elif nxt in ['n', 'N']:
                            print('Have a great day')
                            again = False
                            break
                        else:
                            print('Enter correct input')
                    if again:
                        print('__________NEW GAME__________')
                        main_game()
                    else:
                        main()

                def win_check(human, cpu):
                    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9],
                                     [3, 5, 7]]
                    for win_place in winning_place:
                        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
                            print('You won the match!')
                            if not new_game():
                                return False
                        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
                            print('Helix wins the match!')
                            if not new_game():
                                return False
                    if ' ' not in board:
                        print('MATCH DRAW!!')
                        if not new_game():
                            return False
                    return True

                def user_choice():
                    while True:
                        inp = input('Choose your mark[x/o]: ')
                        if inp in ['x', 'X']:
                            print('You choose "X".\nYou play first.')
                            return 'x', 'o'
                        elif inp in ['O', 'o']:
                            print('You choose "O".\nHelix plays first.')
                            return 'o', 'x'
                        else:
                            print('Enter correct input!')

                def main_game():
                    global board
                    play = True
                    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                    human, cpu = user_choice()
                    display_board()
                    while play:
                        if human == 'x':
                            x = human_input(human)
                            board[x] = human
                            display_board()
                            play = win_check(human, cpu)
                            if play:
                                o = cpu_input(cpu, human, board)
                                print(f'Helix Entered:{o}')
                                board[o] = cpu
                                display_board()
                                play = win_check(human, cpu)
                        else:
                            x = cpu_input(cpu, human, board)
                            print(f'Helix Entered:{x}')
                            board[x] = cpu
                            display_board()
                            play = win_check(human, cpu)
                            if play:
                                o = human_input(human)
                                board[o] = human
                                display_board()
                                play = win_check(human, cpu)

                if __name__ == '__main__':
                    main_game()


            #Coming soon
            if gInp == "2":
                print("\nHelix: Invalid option!")
                main()


            #inv option
            else:
                print("\nHelix: Invalid option!")
                main()


        #Jokes
        if "helix" in inp and "joke" in inp:
            jokes = ["I ate a clock yesterday, it was very time-consuming.",
                     "A perfectionist walked into a bar...apparently, the bar wasn’t set high enough.",
                     "Did you hear about the crook who stole a calendar? He got twelve months.",
                     "Never criticize someone until you’ve walked a mile in their shoes. That way, when you criticize them, they won’t be able to hear you from that far away. ",
                     "So what if I don't know what Armageddon means? It's not the end of the world.",
                     "I woke up this morning and forgot which side the sun rises from, then it dawned on me.",
                     "Don't you hate it when someone answers their own questions? I do.",
                     "I hate Russian dolls, they're so full of themselves.",]
            print("\nHelix: " + random.choice(jokes))
            main()

        #Correction
        if "that is not the correct reply" == inp:
            print("\nHelix: I'm sorry! I will try not to do that again")
            main()


        #Empty
        if "" == inp:
            print("\nHelix: I'm sorry, I didn't get that")
            main()


        #Create lists
        if "helix" in inp and "make" in inp and "list" in inp or "helix" in inp and "create" in inp and "list" in inp:
            print("\nHelix: Okay, What do you want me to name the list?")
            listName = input("\nYou: ").replace(" ", "")
            f = open("./lists/" + listName + ".txt", "w+")
            print("\nHelix: Okay, What do you want me to add in it?")
            while True:
                listInp = input("\nList Item: ")
                if "no" == listInp or "nothing" == listInp:
                    print("\nHelix: Okay")
                    f.close()
                    break
                else:
                    f.write(str(listInp) + "\n")
                    print("\nHelix: Anything else? (Say \"No\" or \"Nothing\" if you don't want to add any more items)")
            main()

        #Edit list
        if "helix" in inp and "edit" in inp and "list" in inp:
            print("\nHelix: Okay, Please enter the name of the list you want me to edit")
            listEdit = input("\nYou: ").lower()
            if os.path.exists("./lists/" + listEdit + ".txt") == True:
                print("\nHelix: Okay what do you want me to add to the list?")
                f = open("./lists/" + listEdit + ".txt", "a+")
                while True:
                    listEditObj = input("\nAdd List Item: ")
                    if "no" == listEditObj or "nothing" == listEditObj:
                        print("\nHelix: Alright, I'll close the list")
                        f.close()
                        break
                    else:
                        f.write(str(listEditObj) + "\n")
                        print("\nHelix: I've added that, Do you want me to add something else?")
                main()
            else:
                print("\nHelix: That list does not exist. You can create it by saying \"Helix create a new list\"")
                main()


        #Show list
        if "helix" in inp and "open" in inp and "list" in inp:
            print("\nHelix: Okay, Please enter the name of the list you want me to read")
            listShow = input("\nYou: ").lower()
            if os.path.exists("./lists/" + listShow + ".txt") == True:
                f = open("./lists/" + listShow + ".txt", "r")
                if f.mode == "r":
                    print("\nHelix: You wrote: \n")
                    print(f.read())
                    f.close()
                main()
            else:
                print("\nHelix: That list does not exist. You can create it by saying \"Helix create a new list\"")
                main()


        #Health function
        if "helix " in inp and "am" in inp and "sick" in inp or "helix" in inp and "im" in inp and "sick" in inp or "helix" in inp and "not" in inp and "well" in inp:
            print("\nHelix: Please tell me what symptoms have you shown?")
            word = input("Symptoms: ")
            query = word.replace(" ", "+")
            URL = requests.get("https://google.com/search?q=i+am+suffering+from+" + str(query))
            soup = BeautifulSoup(URL.text, "html.parser")
            print("\nHelix: " + soup.find("div", class_="BNeawe s3v9rd AP7Wnd").get_text())
            main()


        #Random number picker
        if "helix" in inp and "random" in inp and "number" in inp:
            print(inp.split())
            for word in inp.split():
                if word.isdigit():
                    print("\nHelix: " + random.randrange(int(word)))
                    main()
                else:
                    main()


        #Lyrics
        if "helix " in inp and "lyrics" in inp:
            song = input("\n[Artist - Song]: ").lower()
            fSong = song.replace(" - ", "/")
            url = "https://api.lyrics.ovh/v1/" + str(fSong)
            response = requests.get(url)
            json_data = json.loads(response.content)
            lyrics = json_data['lyrics']
            print("\nHelix: " + lyrics)
            main()


        #Reply to the input
        print("\nHelix: " + str(helix.get_response(inp)))


main()





#random number gen
#math problem solver with steps
#guess the song
#pet health
#ADD SPEACH RECOGNITION https://stackoverflow.com/questions/48777294/python-app-listening-for-a-keyword-like-cortana