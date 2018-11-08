#solution to Level 4 in
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib

url_base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

next_url = url_base + "12345"

for i in range(400):
    response = urllib.urlopen(next_url)
    html = response.read()
    #retrieving last world
    next_url = url_base + html.split()[-1]
    print("URL " + str(i+1) + ": " +  next_url)


print("The answer is: URL 357: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=peak.html")
#TODO: improve this script using a while found number is not a number
