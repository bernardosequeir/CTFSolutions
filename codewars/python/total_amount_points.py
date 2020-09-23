def points(games):
    total_score  =0
    for game in games:
        if(game[0] > game[-1]):
            total_score+=3
        elif(game[0] == game[-1]):
            total_score+=1
    return total_score             

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])) #30
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'])) #10