# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 11:42:37 2018

@author: Sumit
"""



import Levenshtein

#  transposition flag allows transpositions edits (e.g., “ab” -> “ba”),
Tweet1= "OnePlus 6T Launch Event in NYC.  why we changed our launch to October 30."
Tweet2= "It doesn't feel like I'm truly home for the holidays until I've taken my parents' phones and said Here let me show you at least 25 times."
Tweet3= "3 days until the @IRONMANtri World Championship brought to you by Amazon! Who do you think will take home gold this year in Kailua-Kona, Hawai`i?"
Tweet4= "BelieveInYourself: RT DailyO_: Why I'm worried about the health of India's #democracy | riju_agrawal | http://ift.tt/2mSZxiC  …"
Tweet5= "What are 5 Major Sectors in #SmartCities? Infographic #CyberSecurity #AI #P2P #SmartCity @fisher85m #CX #Healthcare #infosec #fintech #IoT #BigData "

s1="OnePlus #6T Launch Event in NYC.  why we changed our launch to October 30. Check it out now! https://onepl.us/W253 "
s2="OnePlus 6T Launch Event in NYC.  why we changed our launch to October #OnePlus6T. Take a look."
s3="Join us for our #OnePlus6T launch on October 30. It's sure to be our biggest and best yet. https://onepl.us/6T_launchtw "
s4="OnePlus 6T Launch #Event in NYC.  why we changed our launch #speed#oneplus https://onepl.us/6tlab "
s5="Play #UnlockYourSpeed to win a #FastandSmooth #OnePlus6T launch to October 30"
s6="OnePlus 6T Launch Event in NYC. Introducing our all-new Explorer Backpack with oneplus6T"
s7="The best is yet to come! Wait for the #OnePlus6T to make its debut on October 30th. http://onepl.us/WaitForT "
s8="(You could even win OnePlus devices for life) at OnePlus 6T Launch Event in NYC."
s9="Can't wait to get your hands on the #OnePlus6T?  https://onepl.us/6tmega # lauch # event"
s10="No matter what you do, do not Google 'OnePlus 6T Speed'#book the data #october #30"
s11="This is your chance to win new OnePlus devices for life, starting with the #OnePlus6T! Coming tomorrow."
s12="Your invitations are in the mail. See you on October 30 lauch event for the #OnePlus6T launch. https://onepl.us/6Tinvitation "
s13="Stay up to date on all things OnePlus redesigned check the oneplus6T launch event "
s14="Oneplus6 launch on October 30#get Bullets #hurry."
s15="Early bird tickets to our #OnePlus6T NYC launch 30 oct are all sold out. https://onepl.us/6T_ticketfb "
s16="Going to our #OnePlus6T NYC launch on October 30? Visit our megathread for helpful tips on all things launch related."
s17="OnePlus 6T Launch #Event in NYC.  why we changed our launch? https://onepl.us/sooppro"
s18="Join our #OnePlus6T Launch Event in New York City. Early Bird tickets are available now!"
s19="The #OnePlus6T is coming. Unlock The Speed on October 30. https://onepl.us/6T_launchtw "
s20="OnePlus 6T Launch Event in NYC.#October#30 #speed is here"


base_Tweets = [Tweet1,Tweet2,Tweet3,Tweet4,Tweet5]
spams = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20]
distance_Values = []

for i in base_Tweets:
    temp =[]
    for j in spams:
        temp.append(Levenshtein.distance(i,j))
    distance_Values.append(temp)

print(distance_Values)


import matplotlib.pyplot as plt
plt.plot(distance_Values[0], 'b-')
plt.plot(distance_Values[1], 'g-')
plt.plot(distance_Values[2], 'r-')
plt.plot(distance_Values[3], 'y-')
plt.plot(distance_Values[4], 'c-')

plt.axis([-1, 21, 10, 130])
plt.show()
