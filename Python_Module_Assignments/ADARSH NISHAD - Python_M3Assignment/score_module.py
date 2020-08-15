#The module programm file to define the two functions for batting or fielding and bowling.

#Fuction to calculate the points of Batsman.
def batting(player):
    score_sheet={}     #dict type variable to store name and scorepoint of player.
    point=0
    point = point + player.get('runs')/2
    if player.get('runs')>=100:
        point = point + 10
    if player.get('runs')>=50:
        point = point + 5
    if (player.get('runs')/player.get('balls'))*100 >100:
        point = point + 4
    elif (player.get('runs')/player.get('balls'))*100 >=80:
        point = point + 2
    point = point + player.get('4')*1
    point = point + player.get('6')*2
    point=point+ player.get('field')*10
    score_sheet['name']=player.get('name')
    score_sheet['batscore']=int(point)
    return score_sheet

#Fuction to calculate the points of Bowler.
def bowling(player):
    score_sheet={}      #dict type variable to store name and scorepoint of player.
    point=0
    point=point + player.get('wkts')*10
    if player.get('wkts')>=5:
        point=point+10
    elif player.get('wkts')>=3:
        point=point+5
    econ=player.get('runs')/player.get('overs')  #economy rate
    if econ>=3.5 and econ<=4.5:
        point=point+4
    elif econ>=2 and econ<3.5:
        point=point+7
    elif econ<2:
        point=point+10
    score_sheet['name']=player.get('name')
    score_sheet['bowlscore']=point
    return score_sheet

