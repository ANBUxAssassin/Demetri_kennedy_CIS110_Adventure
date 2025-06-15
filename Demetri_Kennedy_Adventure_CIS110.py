print(f"Welcome to my quick little story. ")
print(f"So before we can begins our little adventure, I will like to ask just a few questions.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    name = input(f"\nGive me a name you like:  ")
    while len(name) == 0:
        name = input(f"Please enter a name:  ")
    time = input(f"Pick a time 30 or 60 mins. Please enter a numeric Value:  ")
    while not time.isdigit():
        time = input(f"Please enter a time: ")
    level = input(f"Do you like easy or hard challanges:  ")
    while len(level) == 0:
        while  level.lower() not in ["easy","hard"]:
            level = input(f"Room level:  ")
    day = input(f"Do you like daytime or nighttime:  ")
    while len(day) == 0:
        while day.lower() not in ["daytime","nighttime"]:
            day = input(f"Please choose daytime or nighttime:  ")
    players = input(f"how many people do you like to hangout with:  ")
    while not players.isdigit():
        players = input(f"Please enter a numeric value:  ")

    print(f"\nLET'S GO!!!")
    print(f"\nYou have just arrive at {name} Escape room during the {day}. ")
    print(f"You have choosen {level} and you have a time limit of {time}. ")
    print(f"You and {players} other people will be trapped inside of this room. ")
    print(f"After the rules and the story was told aswell as where the key is to leave the room if you decide to give up.")
    print(f"The door is now locked will you start right away? ")
    
    startGame = input(f"\nDo you wish to look for clues right away?  Type yes or no:  ")
    while startGame.lower() != "yes" and startGame.lower() != "no":
        startGame = input("Please type yes or no:  ")

    if startGame == "yes":
        print(f"\nYou started looking for the first clue. ")
        print(f"After a few minutes you have solved a few of the clues. ")
        print(f"After alittle more time your team has solved half of the clues. ")
        print(f"In no time at all you and your group has solved the room. ")
        print(f"You place the key you all found in the door lock and opened the door. ")
        print(f"You have found out that {name} escape has another room. ")
    else:
        print(f"\nYou decided to standing around to watch you teammates. ")
        print(f"After a few minutes of standing around you decide to walk around and look at the clues. ")
        print(f"You have started to solve the clues with your teammates.. ")
        print(f"Unfortunately, you spent alot of time in this room. ")
        print(f"Your team has completed the room and used the key on the locked door and found it leads to another room. ")

    print(f"After going in to the next room you make another choice. ")
    
    endGame = input(f"\nWould you like to start the next room right away? Type yes or no:  ")
    while endGame.lower() != "yes" and endGame.lower() != "no":
        endGame = input(f"Please type yes or no:  ")

    if endGame == "yes":
        print(f"\nThe moment you enter you and almost tripped grabbing the first clue for the new room. ")
        print(f"Your teammates checked up on you. After a few minutes your team splits up. ")
        print(f"After just 5 minutes in the room all the clues and puzzles were completed. ")
        print(f"When you completed your puzzle you meet up with the rest of the team. ")
        print(f"Amazingly, the room was so quick to complete that you found another key and used it to open the next door. ")
    else:
        print(f"\nYou decided to talk with your teammates on their opinion on the first room. ")
        print(f"As you all are feeling pressed on time everyone decided to cover different area of the next room. ")
        print(f"With everyone spreaded out you all completed the room fast and unlocked the next door. ")

    if startGame == "yes" and endGame == "yes":
        print(f"\nAfter spending a wonderful day at {name} escape room. ")
        print(f"Your team has place the key in the lock and opened the door. ")
        print(f"Luckily, you and your team wanted to speed run {name} escape room. ")
        print(f"stepping out of the room you hear a congraulation you have cleared {name} with time to spare. ")
    elif startGame == "no" and endGame == "no":
        print(f"\nAs you opened the door you have learned it was the last room. ")
        print(f"Your team gathered around and started to go over the experience they felt for each clue. ") 
        print(f"You learned that you wasted time that could have help your team to finish faster. ")
        print(f"You all have made a choice you will all do another escape room and pass it this thime then fail it. ")    
    else:
        print(f"\nAfter unlocking and entering the door you lrean you completed {name} escape room. ")
        print(f"Luckily, you and you team just pass the room with 1 minute left. ")
        print(f"Your team wants to do a victory picture and talk about their experience. ")
        print(f"After a few minutes of enjoying the victory everyone says their goodbyes. ")
    print(f"\nThe End")
    
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")

