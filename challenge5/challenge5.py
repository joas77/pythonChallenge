#solution to level 5 in
# http://www.pythonchallenge.com/pc/def/peak.html

import pickle

banner_file = open("banner.p")

unpickler = pickle.Unpickler(banner_file)
banner = unpickler.load()

banner_file.close()

hidden_msg=""

for listelem in banner:
    for tup in listelem:
        hidden_msg += tup[0] * tup[1]

    hidden_msg += "\n"

print(hidden_msg)
