import csv
import requests
from bs4 import BeautifulSoup

def names():
    url = "https://pokemondb.net/pokedex/game/red-blue-yellow"
    r = requests.get(url)
    
    soup=BeautifulSoup(r.text,"html.parser")
    pokedex=soup.find_all("div","infocard game-red-blue")
    poke_list=[]
    for pokemon in pokedex:
        name=pokemon.find("a","ent-name").text.strip()
        poke_list.append(name)
    return poke_list
def moves(poke_list):
    poke_dict={}
    
    for pokemon in poke_list:
#        time.sleep(1)
        move_list=[]
        url = "https://pokemondb.net/pokedex/{:s}/moves/1".format(pokemon)
        r = requests.get(url)
        soup=BeautifulSoup(r.text,"html.parser")
        
        if(r.status_code==200):
            moves=soup.find_all("td","cell-name")
            for move in moves:
                move_name=move.find("a","ent-name").text.strip()
                move_list.append(move_name)
            poke_dict[pokemon]=move_list
    return poke_dict

def write_file(poke_dict):
    with open("Pokedex.csv","w") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in poke_dict.items():
            writer.writerow([key, value])
            
def main():
    poke_list=names()
    poke_dict=moves(poke_list)
    write_file(poke_dict)
    print(poke_dict)
    
if __name__ == '__main__':
   main()