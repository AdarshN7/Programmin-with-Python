#The main programm file to computes the top player amongst the 5 given players.

import score_module        #importing module in main programm.

p1={ 'name' : 'Virat Kohli' , 'role' : 'bat' , 'runs' :112, '4' :10, '6' :0,
'balls' :119, 'field' :0}
p2={ 'name' : 'du Plessis' , 'role' : 'bat' , 'runs' :120, '4' :11, '6' :2,
'balls' :112, 'field' :0}
p3={ 'name' : 'Bhuvneshwar Kumar' , 'role' : 'bowl' , 'wkts' :1, 'overs' :10,
'runs' :71, 'field' :1}
p4={ 'name' : 'Yuzvendra Chahal' , 'role' : 'bowl' , 'wkts' :2, 'overs' :10,
'runs' :45, 'field' :0}
p5={ 'name' : 'Kuldeep Yadav' , 'role' : 'bowl' , 'wkts' :3, 'overs' :10, 'runs' :34,
'field' :0}

player_list=[p1,p2,p3,p4,p5]  #creating list of player p1,p2, so on.

for player in player_list:

    if player.get('role')=='bat':
        print(score_module.batting(player)) #passing player of dict. data type as argument.

    elif player.get('role')=='bowl':
        print(score_module.bowling(player))
