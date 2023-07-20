#from my_module.functions import ...
#from my_module.classes import ...
import random as rd
import sys
import time


from my_module.functions import delay_print, wild_battle, find_team_rocket, team_rocket_battle, find_opponent_trainer, trainer_battle,  gym_raid, view_status, buy, shop
from my_module.variables import trainer, wild_pokemon, team_rocket_names, team_rocket_pokemon, trainer2_names, trainer2_pokemons, legendaries
from my_module.classes import Pokemon, Trainer


# Start the game
def main():
    # Player inputs desired name
    delay_print("Welcome to the World of Pokemon! I'm Professor Oak. What's your name? ")
    trainer.name = input()
    
    delay_print(f"Nice to meet you, {trainer.name}!...Wait! Don't leave just yet! "
          "Wild Pokemon live outside, and it can get dangerous. You need your own Pokemon for your protection. Come with me! ")
    time.sleep(2)
    delay_print(f"Here, {trainer.name}! Looks like I still have three pokeballs left in the lab. ") 
    delay_print("Since you're new here, I'll let you take one! Go ahead and choose!\n")
    delay_print("Your options are: \n"
                "1) Bulbasaur\n"
                "2) Charmander\n"
                "3) Squirtle\n")
    
    valid_options = True
    
    # player inputs the pokemon they want to start with
    while valid_options:
        trainer_starter = input('Please input a number corresponding to the Pokemon you would like to play: ')
        if trainer_starter == "1":
            confirm_trainer_starter = input("Do you want the grass Pokemon, Bulbasaur? (y/n)")
            if confirm_trainer_starter == 'y':
                trainer.pokemon_buddy = Pokemon("Bulbasaur", 'Grass', 3)
                trainer.pokemon_team.append(trainer.pokemon_buddy)
                delay_print(f"You and {trainer.pokemon_buddy.name} are looking great! Now go catch 'em all!\n")
                break
            else:
                continue
        if trainer_starter == "2":
            confirm_trainer_starter = input("Do you want the fire Pokemon, Charmander? (y/n)")
            if confirm_trainer_starter == 'y':
                trainer.pokemon_buddy = Pokemon("Charmander", 'Fire', 3)
                trainer.pokemon_team.append(trainer.pokemon_buddy)
                delay_print(f"You and {trainer.pokemon_buddy.name} are looking great! Now go catch 'em all!\n")
                break
            else:
                continue
        if trainer_starter == "3":
            confirm_trainer_starter = input("Do you want the water Pokemon, Squirtle? (y/n)")
            if confirm_trainer_starter == 'y':
                trainer.pokemon_buddy = Pokemon("Squirtle", 'Water', 3)
                trainer.pokemon_team.append(trainer.pokemon_buddy)
                delay_print(f"You and {trainer.pokemon_buddy.name} are looking great! Now go catch 'em all!\n")
                break
            else:
                continue
        # used for testing purposes to observe all the battles and game elements
        if trainer_starter == "test":
            confirm_trainer_starter = input("Do you want the Mythical Pokemon, Arceus? (y/n)")
            if confirm_trainer_starter == 'y':
                trainer.pokemon_buddy = Pokemon("Arceus", 'Water', 1000)
                trainer.pokemon_team.append(trainer.pokemon_buddy)
                delay_print(f"You and {trainer.pokemon_buddy.name} are looking great! Now go catch 'em all!\n")
            break
            
        else:
            print("Please enter a valid number")
            continue
        
    # Player inputs what they want to do in their pokemon adventure
    journey = True
    while journey:
        path = input("What would you like to do? I recommend viewing your inventory and then searching the wild to catch more pokemon first! \n"
                       "1) Search in the wild\n"
                       "2) Team Rocket Battle\n"
                       "3) Trainer Battle\n"
                       "4) Gym Raid\n"
                       "5) Check Inventory\n"
                       "6) Pokemon Center\n"
                       "7) Quit\n")
        
        if path == '1':
            journey = wild_battle()
        elif path == '2':
            journey = team_rocket_battle()
        elif path == '3':
            journey = trainer_battle()
        elif path == '4': 
            journey = gym_raid()
        elif path == '5':
            view_status()
        elif path == '6':
            shop()
        elif path == '7': 
            journey = False
        else:
            print("Please enter a valid number.")
            continue
    
    delay_print("You are now one step closer to becoming a Pokemon Master!")
    delay_print("Thank you for playing!")

#main()