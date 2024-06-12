# Made by Chargou (@chargou on dc and @GGames78 on roblox)
# Fill out line 7-9 and then run the program to know how much time you need to AFK before getting your goal !
# Calculations are made assuming you have auto rebirth and relic 3 maxed (and you never get stuck on a level bc that's just impossible kek)
# You can use https://www.online-python.com/ to run this if you don't have python on your computer
# You may use, share, and modify this program as you want, please just keep line 1-5 ;)

T = 0                  # Your current transcendence level
R = 0                  # Your current rebirths
Goal = "Transcendence" # Put "Transcendence" here if you want the next transcendence, otherwise, put the number of rebirths you want to get

#######################################################################################################
#######################################################################################################
### Everything past this point is none of your concern unless you're interested in how this works ! ###
#######################################################################################################
#######################################################################################################

Speed = 1.63 # I calculated this value by looking at how many stages I cleared in 100 seconds, the answer was 163, so I do 163/100 = 1.63 stages per second

if Goal == "Transcendence":
    Goal = 100*(T+1) #Calculating how many rebirths you want for your current transcendence
if Goal <= R:
    print("You've already attained you goal...")
    exit()

RperR = 1         # By default, you get one rebirth per rebirth
if T != 0:
    RperR = 2     # On you first transcendence, you get one extra rebirth per rebirth
    RperR += T//5 # Afterwards, you get one extra rebirth per rebirth for every five transcendences

time = 0

while R < Goal:
    time += (R+1)/1.63
    R += RperR

print(f"You'll need to AFK for {time} seconds, which is {int(time//3600)} hours and {(time%3600)/60} minutes to get to your goal :)")