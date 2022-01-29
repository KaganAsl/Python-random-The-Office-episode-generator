import random
import webbrowser
# Paste link below. Place {season} and {episode} to their places in link.
# If you want without using link uncomment print line and comment webbrowser line.
season = random.randint(1,9)
if season == 1:
    epsiode = random.randint(1,6)
elif season == 2:
    epsiode = random.randint(1,22)
elif season == 3:
    epsiode = random.randint(1,25)
elif season == 4:
    epsiode = random.randint(1,19)
elif season == 5:
    epsiode = random.randint(1,28)
elif season == 6:
    epsiode = random.randint(1,26)
elif season == 7 or 9 :
    epsiode = random.randint(1,27)
elif season == 8:
    epsiode = random.randint(1,24)
webbrowser.open("www.dizigom1.com/the-office-{season}-sezon-{episode}-bolum/".format(season = season, episode = epsiode))
#print("Season {season}. Epsiode {episode}./".format(season = season, episode = epsiode))