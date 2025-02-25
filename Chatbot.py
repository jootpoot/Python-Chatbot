from pdb import Restart
import random
from datetime import date
import os
import sys
import time


#list of responses

greetings = ["Hii",
             "Howdy",
             "Goodday!",
             "Qui! oh wait.. thats not hello oops!",
             "Hi there!",
             "OMG NEW PERSON!! sorry im just a bit excited no ones talked to me in years..",
             "Wassgud."]

name = ["My name... well I said it at the start of the session.",
        "My names Silly bot!",
        "Well my actual name is super long but you can call me Silly bot :)",
        "You'll have to ask my creator that question",
        "I think you already know my name"]

creator = ["Hmm well I dont know their name.. but I've heard they're super cool",
           "I'm pretty sure some random high school student created me"
           "I don't really know. Probably some really dumb person."]

inputs = ["Have another go ",
          "This is fun!!! ask me more ",
          "Shoot! "
          "Whatt did you run out?? ASK ASK ASK! "]

weather = ["Very sunny! Omg I cant see..",
           "Its snowing!!! Lets go make a snowman!",
           "It's raining really heavily.",
           "Super windy, I feel like im flying!",
           "Foggy!"]


bad = ["not good", "depressed", "not well",
       "couldve been better", "bad", "not doing good", "depressing"]
good = ["good", "great", "amazing", "never been better", "excited", "alright"]
replies_good = ["meeting", "hanging out", "someone", "going out"]
places = ["park", "beach", "city", "mall",
    "pools", "museum", "aquarium", "zoo", "movies" ]
out_to_eat = ["eat", "food", "restaurant"]
food = ["pizza", "burger", "ramen", "cake", "samosa", "mantu", "biryani", "rice", "fruits",
        "pasta", "shawarma", "pies", "salad", "spaghetti", "lasagna", "sandwich", "chocolate"]
school_reasons = ["assignment", "grades", "school", "marks", "hw", "homework"]
friends_bad = ["friends", "friend", "bff", "best friend"]
friends_good = ["friends", "friend", "bff", "best friend"]

# ---------------------------------------------------------------------------------------------------------------------------------------

print(random.choice(greetings))
intro = input("I'm silly bot, your personal virtual assistant. How are you? ")
intro = intro.split()
for word in intro:
    if word in bad:
        print("Im so sorry to hear")
        talk = input("Do you want to talk about it? ")
        if "y" in talk:
            print("I'm all ears.")
            talk1 = input("What happened? ")
            print("Thats awful to hear, i'm so sorry. I'll be here if u need anything")

        else:
            activities = input("Thats ok, What else will you be doing today? ")
            for word in activities:
                if "nothing" in activities:
                    print("Thats ok :) You should take it easy on yourself")

                for word in activities:
                    if word in replies_good:
                        person = input("WHAT?!! OOO WHO WHO WHO?? WHO IS IT! ")

                        if "bf" in person or "boyfriend" in person:

                            know = input("oo may I know his name? ")

                            if "no" in know:
                                print("aw thats ok")

                        else:
                            where = input("Where are you guys going? ")
                            where = where.split()
                            for word in where:
                                if word in places:
                                    print("That sounds great! Have fun!")
                                elif word in out_to_eat:
                                    print("YUMM I wanna go out to eat but im a stupid bot that cant eat")
                                    eat = input("What's your favourite food :D ")
                                    for word in food:
                                        if word in eat:
                                            print("YUM! Good choice!")
                                    else:
                                        print("YUM! sounds good!")

                    elif "gf" in person or "girlfriend" in person:
                        know2 = input("oo may I know her name? ")
                        if "no" in know2:
                            print("aw thats ok")
                        else:
                            where = input("Where are you guys going? ")
                            where = where.split()
                            for word in where:
                                if word in places:
                                    print("That sounds great! Have fun!")
                                elif word in out_to_eat:
                                    print("YUMM I wanna go out to eat but im a stupid bot that cant eat")
                                    eat = input("What's your favourite food :D ")
                                    for word in food:
                                        if word in eat:
                                            print("YUM! Good choice!")
                                    else:
                                            print("YUM! sounds good!")
                                

                    elif "mum" in person or "mom" in person or "dad" in person:
                        where = input("Where are you guys going? ")
                        where = where.split()
                        for word in where:
                            if word in places:
                                print("That sounds great! Have fun!")
                            elif word in out_to_eat:
                                print(
                                "YUMM I wanna go out to eat but im a stupid bot that cant eat")
                                eat = input("What's your favourite food :D ")
                                for word in food:
                                    if word in eat:
                                        print("YUM! Good choice!")
                                else:
                                        print("YUM! sounds good!")

                    elif "friend" in person:
                        print("OO seems fun!")
                        where = input("Where are you guys going? ")
                        where = where.split()
                        for word in where:
                            if word in places:
                                print("That sounds great! Have fun!")
                            elif word in out_to_eat:
                                print(
                                "YUMM I wanna go out to eat but im a stupid bot that cant eat")
                                eat = input("What's your favourite food :D ")
                                for word in food:
                                    if word in eat:
                                        print("YUM! Good choice!")
                                else:
                                        print("YUM! sounds good!")

    elif word in good:
        why = input("OOOO!! You seem excited! what's going on?? ")

        for word in replies_good:
            if word in why:
                person = input("WHAT?!! OOO WHO WHO WHO?? WHO IS IT! ")

                if "bf" in person or "boyfriend" in person:

                    know = input("oo may I know his name? ")

                    if "no" in know:
                        print("aw thats ok")

                    else:
                        where = input("Where are you guys going? ")
                        where = where.split()
                        for word in where:
                            if word in places:
                                print("That sounds great! Have fun!")
                            elif word in out_to_eat:
                                print(
                                "YUMM I wanna go out to eat but im a stupid bot that cant eat")
                                eat = input("What's your favourite food :D ")
                                for word in eat:
                                    if word in food:
                                        print("YUM! Good choice!")
                                else:
                                        print("YUM! sounds good!")



                elif "gf" in person or "girlfriend" in person:
                    know2 = input("oo may I know her name? ")
                    if "no" in know2:
                        print("aw thats ok")
                    else:
                        where = input("Where are you guys going? ")
                        where = where.split()
                        for word in where:
                            if word in places:
                                print("That sounds great! Have fun!")
                            elif word in out_to_eat:
                                print(
                                "YUMM I wanna go out to eat but im a stupid bot that cant eat")
                                eat = input("What's your favourite food :D ")
                                for word in food:
                                    if word in eat:
                                        print("YUM! Good choice!")
                                else: 
                                        print("YUM! sounds good!")
                    


                elif "mum" in person or "mom" in person or "dad" in person:
                    where = input("Where are you guys going? ")
                    where = where.split()
                    for word in where:
                        if word in places:
                            print("That sounds great! Have fun!")
                        elif word in out_to_eat:
                            print(
                                "YUMM I wanna go out to eat but im a stupid bot that cant eat")
                            eat = input("What's your favourite food :D ")
                            for word in food:
                                if word in eat:
                                    print("YUM! Good choice!")
                            else:
                                    print("YUM! sounds good!")

                


                elif "friend" in person:
                    print("OO seems fun!")
                    where = input("Where are you guys going? ")
                    where = where.split()
                    for word in where:
                        if word in places:
                            print("That sounds great! Have fun!")
                        elif word in out_to_eat:
                            print(
                                "YUMM I wanna go out to eat but im a stupid bot that cant eat")
                            eat = input("What's your favourite food :D ")
                            for word in food:
                                if word in eat:
                                    print("YUM! Good choice!")
                            else:
                                    print("YUM! sounds good!")
                        
                break
        else:
            print("Sorry I don't understand what you said. Please restart the session.")

# --------------------------------------------school--------------------------------------------------------
        school = input("Anyways.. how's school going? ")
        for word in good:
            if word in school:
                reason_good = input("OO whats the reason? ")
        
                for word in school_reasons:
                    if word in reason_good:
                        print("Yayyy!! Im so happy for you :D")
                
                for word in friends_good:
                    if word in reason_good:
                        friendsnum = input("Talking about friends.. How many friends do you have? ")
                        print("You have a lot of friends!")
                        print("I dont have any.. other than my creator of course")
                
            
            

        for word in bad:
            if word in school:
                reason_bad = input("Aww noo why what's wrong? ")
                reason_bad = reason_bad.lower()                
                reason_bad = reason_bad.split()

               

                for word in school_reasons:
                    if word in reason_bad:
                        print("Aww that's ok. Remember to take breaks and look after yourself.")
                        print("I would've loved to help but my program restricts me from doing that :(")
            
            
        
        
                    for word in friends_bad:
                        if word in reason_bad:
                            print("Oh that sounds awful.")
                            friendsnum = input("Talking about friends.. How many friends do you have? ")
                            print("You have a lot of friends!")
                            print("I dont have any.. other than my creator of course")
                



#----------------subjects --------------------------------------------------------------------------------
subject = input("Hmm.. Whats your favourite subject in school?")
subject = subject.lower()

if "math" in subject:
    print("ehh math is alright, personally I dont enjoy it that much")
elif "english" in subject:
    print("OOO interesting choice. Im not that good at english :P")
elif "science" in subject:
    print("Science is super fun! I like it a lot")
    science_streams = input("What type of science do you like?")
    science_streams = science_streams.lower()

    if "physics" in science_streams:
        print("physics hurts my head")
    elif "biology" in science_streams:
        print("chem>>")
    elif "chemisty" in science_streams:
        print("YES! I LOVE CHEM TOO!")
elif "sport" in subject or "PE" in subject:
    print("OOO I'm assuming youre a very athletic person!")




# -----------------------------questions----------------------------------------------------------------------

print("Enough of me asking you questions, how about you ask me some?")
print("Go ahead ask me anything. The time, the date, the weather, what my name is")
questions = input("Try to stick to only these, im not an advanced bot... I cant answer too many questions D: ")

for word in questions:
    if "name" in questions:
        print(random.choice(name))
        questions = input(random.choice(inputs))
    elif "creator" in questions:
        print(random.choice(creator))
        questions = input(random.choice(inputs))
    
    elif "time" in questions:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S:", t)
        print("Hmm let me check")
        time.sleep(1.5)
        print("The current time is " + current_time)
        questions = input(random.choice(inputs))
    
    elif "date" in questions:
        print("It is..." + str(date.today()))
        questions = input(random.choice(inputs))

    elif "weather" in questions:
        print("Getting weather data..")
        time.sleep(2)
        print(random.choice(weather))
    
    elif "no" in questions:
        print("Awww i guess this is the end then.. It was fun talking to you. See you later :)")
    