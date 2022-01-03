import os
from fuzzywuzzy import fuzz

def getPlayer(player, folder):
    #similar = [[0 for x in range(2)] for y in range(3)]
    flag = 0
    for file in os.listdir('players/' + folder):
        #print("File: " + file)
        fname = file.split('.')
        flag = 0
        if fname[0].lower() == player.lower():
            player = file
            flag = 1
            #print(' yes ' + file)
            break
    #print(player)
    if flag == 0:
        return 0
    if folder == 'times':
        return 'players/times/' + player
    else:
        return 'players/coords/' + player

def getSimilar(player):
    similar = [[0 for x in range(2)] for y in range(3)]
    for file in os.listdir('players/coords'):
        fname = file.split('.')
        ratio = fuzz.ratio(fname[0].lower(), player.lower())
        for i in range(3):
            if ratio > similar[i][1]:
                if i == 0:
                    similar[i+2][0] = similar[i+1][0]
                    similar[i+2][1] = similar[i+1][1]
                    similar[i+1][0] = similar[i][0]
                    similar[i+1][1] = similar[i][1]
                    similar[i][0] = fname[0]
                    similar[i][1] = ratio
                    break
                if i == 1:
                    similar[i+1][0] = similar[i][0]
                    similar[i+1][1] = similar[i][1]
                    similar[i][0] = fname[0]
                    similar[i][1] = ratio
                    break
                if i == 2:
                    similar[i][0] = fname[0]
                    similar[i][1] = ratio
                    break
    return similar
