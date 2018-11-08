# solution to level 6 in
# http://www.pythonchallenge.com/pc/def/channel.html

# the trick is change channel.html by channel.zip 
# and then unzip the file to start with the puzzle

start = 90052

f = open("channel/" + str(start)+".txt")
data = f.read()
f.close()
nothing_num = 0
msg = ""

while True:
    next_nothing = data.split()[-1]
    if next_nothing.isdigit():
        nothing_num = int(next_nothing)
        #unichr(nothing_num)
    #print(msg)
    try:
        f = open("channel/" + next_nothing + ".txt")
        data = f.read()
        f.close()
    except IOError as e:
        print("Last nothing found")      
        break

    print(data + ": " + hex(nothing_num))

#print(msg)

