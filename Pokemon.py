import csv
from random import randint
import random


def open_file():
    """This function opens the file input by the user. If the file cannot be found
    then the user is prompted for input again. Once the file is found and opened,
    it is returned as a file pointer."""
    fp=0
    file_name=input("Input a file name: ")#prompts user for input
    while fp==0:#continues to loop until a file is opened successfully
        
        try:
            fp=open(file_name,"r")#attempts to open input file
            return fp# returns the file pointer if no errors occur
        except FileNotFoundError:#if file no found
            print("Unable to open the file. Please try again.")#error message
            file_name=input("Input a file name: ")#reprompt for input
def read_file(fp):
    reader = csv.reader(fp)
    pokedex={}
    for line in reader:
        pokedex[line[0]]=line[1]
    return pokedex
def pokedex_length(pokedex):
    count=0
    for key in pokedex:
        count+=1
    return count
def random_opp(pokedex,length):
    rand_opp_num=randint(0,length)
    count=0
    for key in pokedex:
        count+=1
        if(count==rand_opp_num):
            return key
def choose_pokemon(pokedex,length):
    count=0
    choice=input("Choose 1 to select a Pokemon or 2 for random:")
    pokemon=''
    if(choice=="1"):
        for item in pokedex:
            print("{:d} : {:s}".format(count,item))
            count+=1
        pokemon=input("Choose a Pokemon from the Pokedex:")
        for item in pokedex:
            if(pokemon==str(item)):
                return item
    elif(choice=="2"):
        return random_opp(pokedex,length)
def random_moves(pokedex,pokemon):
    move_list=pokedex[pokemon]
    rand_list=[]
    
    for i in range(0,4):
        random_move=random.choice(move_list.strip("'").strip().split(","))
        move=''
        for item in random_move:
            if(item.isalpha()):
                move+=item
        rand_list.append(move)
    #fix random move repeating
    return rand_list
#def choose_your_move():
#def choose_opp_move():
#def random_multipliter():
#def check_winner():    
def calculate_health(health,damage=0):
    return health-damage
    
def output(rand_opp,rand_moves_opp,your_pokemon,rand_your_moves,your_health,opp_health):
    print("Opponent: {:s} \t\t {:d}".format(rand_opp,opp_health))#print health
    
    print("1.{:s}\t2.{:<s}\n3.{:s}\t4.{:s}\n".format(rand_moves_opp[0],rand_moves_opp[1],\
          rand_moves_opp[2],rand_moves_opp[3]))
    
    print("Your Pokemon: {:s} \t\t {:d}".format(your_pokemon,your_health))#print health
    
    print("1.{:s}\t2.{:s}\n3.{:s}\t4.{:s}\n".format(rand_your_moves[0],rand_your_moves[1],\
          rand_your_moves[2],rand_your_moves[3]))
    
def main():
    fp=open_file()
    pokedex=read_file(fp)
    length=pokedex_length(pokedex)#File manip and length
    
    rand_opp=random_opp(pokedex,length)
    rand_moves_opp=random_moves(pokedex,rand_opp)
    your_pokemon=choose_pokemon(pokedex,length)
    rand_your_moves=random_moves(pokedex,rand_opp)#set-up of fight 
    health=100
    your_health=calculate_health(health)
    opp_health=calculate_health(health)

    winner=False
    while(winner==False):
        output(rand_opp,rand_moves_opp,your_pokemon,rand_your_moves,your_health,opp_health)
#        opp_move=choose_opp_move()
#        your_move=choose_your_move()
#        
#        opp_dam_dealt=random_multipliter():
#        your_dam_dealt=random_multipliter():
#        
#        your_health=calculate_health(your_health,opp_dam_dealt)
#        opp_health=calculate_health(opp_health,your_dam_dealt)
#        
#        winner=check_winner(your_health,opp_health)
#    
if __name__ == "__main__":
    main()          