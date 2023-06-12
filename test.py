import random
import time
#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘
#" ┌─────────┐ "
#" │         │ "
#" │         │ "
#" │         │ "
#" └─────────┘ "


def initialstep(num):
    dice_draw={
    1:(" ┌─────────┐ ",
       " │         │ ",
       " │    ●    │ ",
       " │         │ ",
       " └─────────┘ "),
    2:(" ┌─────────┐ ",
       " │ ●       │ ",
       " │         │ ",
       " │       ● │ ",
       " └─────────┘ "),
    3:(" ┌─────────┐ ",
       " │ ●       │ ",
       " │    ●    │ ",
       " │       ● │ ",
       " └─────────┘ "),
    4:(" ┌─────────┐ ",
       " │ ●     ● │ ",
       " │         │ ",
       " │ ●     ● │ ",
       " └─────────┘ "),
    5:(" ┌─────────┐ ",
       " │ ●     ● │ ",
       " │    ●    │ ",
       " │ ●     ● │ ",
       " └─────────┘ "),
    6:(" ┌─────────┐ ",
       " │ ●     ● │ ",
       " │ ●     ● │ ",
       " │ ●     ● │ ",
       " └─────────┘ "),

    }
 
    dice1=[]
    dice2=[]
    player_sum=bot_sum=0
    print("Starting...")
    time.sleep(1)
    for k in range(num):
        dice1.append(random.randint(1,6))
        time.sleep(2)
        print("You got:",dice1[k])
    time.sleep(2)
    for k in range(num):
        for j in dice_draw.get(dice1[k]):
            print(j)
    time.sleep(2)

    for k in dice1:
        player_sum=player_sum+k
    print("\n Your sum is :",player_sum)
    
       
    time.sleep(2)
    print("\n It's time for the bot to play.")
    time.sleep(2)
    for k in range(num):
        dice2.append(random.randint(1,6))
        time.sleep(2)
        print("Bot got:",dice2[k])
    for k in range(num):
        for j in dice_draw.get(dice2[k]):
            print(j)
    time.sleep(2)
  
    for k in dice2:
       bot_sum=bot_sum+k
    print("\n Sum of bot is :",bot_sum)

        
    time.sleep(2)
   
    time.sleep(3)
    if (player_sum > bot_sum):
        print("\n Congratulations,you won!!!")
    elif(player_sum< bot_sum):
        print("\n Hard luck,bot won.")
    else:
        print("\n Tie between player and bot.")
    time.sleep(2)
def secondstep():
    i=0
    rolling=""
    while i==0:
        num=int(input("How many times you want to roll, (1-5):"))
        if num>0 and num<6:
            initialstep(num)
            break
        else:
            print("Please enter the correct choice:")
    print("Do you want to continue (yes/no):")
    while rolling!="Yes":
        rolling=input().lower().capitalize()
        if rolling=="Yes":
            secondstep()
        else:
            print("Thank you.Hope you enjoyed it!!")
            break
secondstep()
       















