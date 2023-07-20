"""A collection of function for doing my project."""
import random as rd
import sys
import time

from my_module.variables import trainer, wild_pokemon, team_rocket_names, team_rocket_pokemon, trainer2_names, trainer2_pokemons, legendaries
from my_module.classes import Pokemon, Trainer

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def wild_battle():
    """ Battle and catch pokemon in the wild.
    
    Returns
    -------
    output : bool
        bool returns True if player defeats the wild pokemon, False if otherwise
    """
    # generate a random wild Pokemon to battle against
    random_pokemon = rd.choice(wild_pokemon)
    random_pokemon_level = rd.randint(1, 3)
    opponent_pokemon = Pokemon(random_pokemon["name"], random_pokemon["type"], random_pokemon_level)
    trainer_pokemon = trainer.pokemon_buddy
    caught = False
    
    # begin the battle
    time.sleep(2)
    delay_print(f"A wild {opponent_pokemon.name} appears!\n")
    time.sleep(1.5)
    delay_print(f"Go, {trainer_pokemon.name}!")

    while trainer.has_pokemon() and not opponent_pokemon.knock_out:
        print()
        # display the opponent's pokemon and player's pokemon
        opponent_pokemon.status()
        trainer_pokemon.status()
        
        option = input("1)Attack\n" 
                       "2)Switch Pokemon\n" 
                       "3)Use potions\n")
        
        # Attack the wild pokemon
        if option == '1':
            trainer_pokemon.attack(opponent_pokemon)
            if opponent_pokemon.knock_out == True:
                print(f"{opponent_pokemon.name} has been knocked out!")
                if trainer_pokemon.experience >= 10:
                    trainer_pokemon.level_up()
                #else:
                    #continue
            else:
                time.sleep(1)
                print()
                opponent_pokemon.attack(trainer_pokemon)
    
            if trainer_pokemon.knock_out == True:
                print(f"{trainer_pokemon.name} has been knocked out!")
                if trainer.has_pokemon():
                    delay_print(f"{trainer.name}: Return, {trainer_pokemon.name}.\n")
                    time.sleep(1)
                    print("Switch in a new Pokemon:")
                    trainer.swap_buddy()
                    trainer_pokemon = trainer.pokemon_team[0]
                    delay_print(f"{trainer.name}: Go {trainer_pokemon.name}!\n")
                #else:
                    #break
        
        # Switch out current Pokemon
        elif option == '2':
            trainer.swap_buddy()
            trainer_pokemon = trainer.pokemon_team[0]
        
        # Use potions to heal or revive Pokemon
        elif option == '3':
            trainer.use_inventory()
    
    # exit the game if player runs out of usable pokemon
    if not trainer.has_pokemon():
        print("You have no more Pokemon! You lose!")
        return False
    
    # catch the pokemon if player wins the battle
    elif opponent_pokemon.knock_out:
    #while opponent_pokemon.knock_out:
        
        # Earn coins for beating the wild pokemon
        time.sleep(2)
        print("You win! You found 10 coins.")
        trainer.coins += 10
        print()
            
        # Catch the wild pokemon
        delay_print("Catch that Pokemon!\n")
        time.sleep(0.5)
        delay_print(f"{trainer.name}: Go Pokeball!\n")
        while trainer.pokeballs > 0:
            caught = trainer.catching_pokemon('wild')
            if caught == True:
                print(f"{opponent_pokemon.name} has been registered to your Pokemon team!")
                trainer.pokemon_team.append(opponent_pokemon)
                time.sleep(1.5)
                break
            elif caught == False:
                more_throws = input("Do you want use another Pokeball to try again? (y/n)")
                if more_throws == 'y':
                    continue
                elif more_throws == 'n':
                    break
                else:
                    print("Please input 'y' or 'n'")  
        if trainer.pokeballs <= 0:
            print("You are out of Pokeballs! Please go to the Pokemon Center to buy more.")
    
    return True


def find_team_rocket():
    """ Generate a Team Rocket member and their pokemon
    
    Returns
    -------
    tr_member : object
        object refers to the Team Rocket member's name, their current pokemon, their pokemon collection, and their coins
    """
    tr_name = rd.choice(team_rocket_names)
    tr_team = []
    n_pokemon = 0
    
    for number in range(rd.randint(2,4)):
        tr_pokemon = rd.choice(team_rocket_pokemon)
        tr_pokemon_level = rd.randint(2,4)
        tr_team.append(Pokemon(tr_pokemon["name"], tr_pokemon["type"], tr_pokemon_level))
        n_pokemon += 1
    
    tr_pokemon_buddy = tr_team[0]
    tr_coins = n_pokemon * 8
    tr_member = Trainer(tr_name, tr_pokemon_buddy, tr_team, tr_coins)
    
    return tr_member

def team_rocket_battle():
    """ Battle against a Team Rocket member and their pokemon.
    
    Returns
    -------
    output : bool
        bool returns True if trainer wins the battle, False if otherwise
    """
    tr = find_team_rocket()
    tr_pokemon = tr.pokemon_buddy
    trainer_pokemon = trainer.pokemon_buddy
    
    # Start the battle
    print("You are challenged by Team Rocket!")
    time.sleep(1)
    delay_print("Jessie: Prepare for trouble!\n"
                "James: And make it double!\n"
                "Jessie: Team Rocket blasts off at the speed of light!\n"
                "James: Surrender now, or prepare to fight!\n")
    time.sleep(2)
    print()
    delay_print(f"{tr.name}: Ready or not! {tr_pokemon.name}!\n")
    delay_print(f"{trainer.name}: {trainer_pokemon.name}, I choose you!")

    # loop for the battle
    while trainer.has_pokemon() and tr.has_pokemon():
        print()
        tr_pokemon.status()
        trainer_pokemon.status()
        
        option = input("1)Attack\n" 
                       "2)Switch Pokemon\n" 
                       "3)Use potion\n")
        
        if option == '1':
            trainer_pokemon.attack(tr_pokemon)
            if tr_pokemon.knock_out:
                print(f"{tr_pokemon.name} has fainted!")
                if trainer_pokemon.experience >= 10:
                    trainer_pokemon.level_up()
                if tr.has_pokemon():
                    for pokemon in tr.pokemon_team:
                        if not pokemon.knock_out:
                            tr_pokemon = pokemon
                    print()
                    delay_print(f"{tr.name}: Take the stage, {tr_pokemon.name}!")      
                else:
                    continue
            else:
                time.sleep(1)
                print()
                tr_pokemon.attack(trainer_pokemon)
            
            if trainer_pokemon.knock_out:
                print(f"{trainer_pokemon.name} has fainted!")
                if trainer.has_pokemon():
                    delay_print(f"{trainer.name}: Return, {trainer_pokemon.name}\n")
                    time.sleep(1)
                    print("Switch in a new Pokemon:")
                    trainer.swap_buddy()
                    trainer_pokemon = trainer.pokemon_team[0]
                    delay_print(f"{trainer.name}: Go, {trainer_pokemon.name}!\n")
        
        elif option == '2':
            trainer.swap_buddy()
            trainer_pokemon = trainer.pokemon_team[0]
            
        elif option == '3':
            trainer.use_inventory()
    
    # exit game if trainer runs out of usable pokemon
    if not trainer.has_pokemon():
        print("All of your Pokemon have fainted! You lose!")
        #for pokemon in trainer.pokemon_team:
            #lose_pokemon = rd.choice(pokemon)
        #print(f"Team Rocket steals {lose_pokemon.name} and {tr_coins} coins from you!")
        #trainer.pokemon_team.remove(lose_pokemon)
        #trainer.coins -= tr.coins
        return False
    
    # catch team rocket's pokemon if trainer wins the battle
    elif not tr.has_pokemon():
        delay_print("Team Rocket: You may have won this round, but we'll be back!\n")
        print(f"You win! You get {tr.coins} coins from {tr.name}")
        trainer.coins += tr.coins
        
        print()
        delay_print("Catch Team Rocket's Pokemon!\n")
        time.sleep(0.5)
        delay_print(f"{trainer.name}: Go Pokeball!\n")
        while trainer.pokeballs > 0:
            caught = trainer.catching_pokemon('wild')
            if caught == True:
                print(f"{tr_pokemon.name} has been registered to your Pokemon team!")
                trainer.pokemon_team.append(tr_pokemon)
                time.sleep(3)
                break
            elif caught == False:
                more_throws = input("Do you want use another Pokeball to try again? (y/n)")
                if more_throws == 'y':
                    continue
                elif more_throws == 'n':
                    break
                else:
                    print("Please input 'y' or 'n'")
        
        if trainer.pokeballs <= 0:
            print("You are out of Pokeballs! Please go to the Pokemon Center to buy more.")
    
    return True 


def find_opponent_trainer():
    """ Generate a random trainer and their Pokemon team.
    
    Returns
    -------
    opponent_trainer : object
        object represents the opponent trainer's name, their current pokemon, pokemon collection, and coins
    """
    opponent_name = rd.choice(trainer2_names)
    opponent_team = []
    n_pokemon = 0
    
    for number in range(rd.randint(2,6)):
        opponent_pokemon = rd.choice(trainer2_pokemons)
        opponent_pokemon_level = rd.randint(3,6)
        opponent_team.append(Pokemon(opponent_pokemon["name"], opponent_pokemon["type"], opponent_pokemon_level))
        n_pokemon += 1
    
    opponent_pokemon_buddy = opponent_team[0]
    opponent_coins = n_pokemon * 10
    
    opponent_trainer = Trainer(opponent_name, opponent_pokemon_buddy, opponent_team, opponent_coins)
    return opponent_trainer

def trainer_battle():
    """ Battle against another trainer and their pokemon.
    
    Returns
    -------
    output : bool
        bool returns True if player wins the battle, False if otherwise
    """
    # Set the opponent 
    opponent = find_opponent_trainer()
    opponent_pokemon = opponent.pokemon_buddy
    trainer_pokemon = trainer.pokemon_buddy
    
    # Start the battle
    time.sleep(2)
    delay_print(f"{opponent.name} challenges {trainer.name} to a battle!\n")
    time.sleep(1)
    delay_print(f"{opponent.name}: {opponent_pokemon.name}, let's go!\n")
    delay_print(f"{trainer.name}: I choose you, {trainer_pokemon.name}!")

    # loop for the battle
    while trainer.has_pokemon() and opponent.has_pokemon():
        print()
        opponent_pokemon.status()
        trainer_pokemon.status()
        
        option = input("1)Attack\n" 
                       "2)Switch Pokemon\n" 
                       "3)Use potions\n")
        
        if option == '1':
            trainer_pokemon.attack(opponent_pokemon)
            if opponent_pokemon.knock_out:
                print(f"{opponent_pokemon.name} has fainted!")
                if trainer_pokemon.experience >= 10:
                    trainer_pokemon.level_up()
                if opponent.has_pokemon():
                    for pokemon in opponent.pokemon_team:
                        if not pokemon.knock_out:
                            opponent_pokemon = pokemon
                    print()
                    delay_print(f"{opponent.name}: {opponent_pokemon.name}, standby for battle!")           
                else:
                    continue
            else:
                time.sleep(1)
                print()
                opponent_pokemon.attack(trainer_pokemon)
            
            if trainer_pokemon.knock_out:
                print(f"{trainer_pokemon.name} has fainted!")
                if trainer.has_pokemon():
                    delay_print(f"{trainer.name}: Return, {trainer_pokemon.name}.\n")
                    time.sleep(1)
                    print("Switch in a new Pokemon:")
                    trainer.swap_buddy()
                    trainer_pokemon = trainer.pokemon_team[0]
                    delay_print(f"{trainer.name}: Go {trainer_pokemon.name}!\n")
        
        elif option == '2':
            trainer.swap_buddy()
            trainer_pokemon = trainer.pokemon_team[0]
            
        elif option == '3':
            trainer.use_inventory()
    
    # exit the game if player runs out of usable pokemon
    if not trainer.has_pokemon():
        print("All of your Pokemon have fainted! You lose!")
        return False
    
    # earn coins from opponent if player wins the battle
    elif not opponent.has_pokemon():
        print(f"You win! You get {opponent.coins} coins from {opponent.name}")
        trainer.coins += opponent.coins
    return True


def gym_raid():
    """ Battle against stronger legendary Pokemon in the gym.
    
    Returns
    -------
    output : bool
        bool returns True if player wins the battle, returns False if otherwise
    """
    # generate a random legendary pokemon 
    gym_pokemon = rd.choice(legendaries)
    gym_pokemon_level = rd.randint(10, 20)
    gym_pokemon = Pokemon(gym_pokemon["name"], gym_pokemon["type"], gym_pokemon_level)
    trainer_pokemon = trainer.pokemon_buddy
    caught = False
    
    # Start the gym raid
    time.sleep(2)
    delay_print(f"The legendary Pokemon {gym_pokemon.name} appears!\n")
    time.sleep(1.5)
    delay_print(f"{trainer.name}: Victory will be ours! Here we go, {trainer_pokemon.name}!\n")
    delay_print(f"{trainer.name} VS {gym_pokemon.name}")
    
    # loop for the battle
    while trainer.has_pokemon() and not gym_pokemon.knock_out:
        print()
        gym_pokemon.status()
        trainer_pokemon.status()
        
        option = input("1)Attack\n" 
                       "2)Switch Pokemon\n" 
                       "3)Use potion\n")
        
        # Attack the legendary pokemon
        if option == '1':
            trainer_pokemon.attack(gym_pokemon)
            if gym_pokemon.knock_out:
                print(f"{gym_pokemon.name} has fainted!")
                if trainer_pokemon.experience >= 20:
                    trainer_pokemon.level_up()
                    trainer_pokemon.level_up()
                #else:
                    #continue
            else:
                time.sleep(1)
                print()
                gym_pokemon.attack(trainer_pokemon)
            
            if trainer_pokemon.knock_out:
                print(f"{trainer_pokemon.name} has fainted!")
                if trainer.has_pokemon():
                    delay_print(f"{trainer.name}: Return, {trainer_pokemon.name}\n")
                    time.sleep(1)
                    print("Switch in a new Pokemon:")
                    trainer.swap_buddy()
                    trainer_pokemon = trainer.pokemon_team[0]
                    delay_print(f"{trainer.name}: Go {trainer_pokemon.name}!\n")
        
        # Switch out current Pokemon
        elif option == '2':
            trainer.swap_buddy()
            trainer_pokemon = trainer.pokemon_team[0]
            
        # Use potions to heal or revive damaged pokemon
        elif option == '3':
            trainer.use_inventory()
    
    # exit game if trainer runs out of usable Pokemon
    if not trainer.has_pokemon():
        print("You are out of pokemon! You lose!")
        return False
    
    # catch pokemon if trainer wins the battle
    elif gym_pokemon.knock_out:
        #while gym_pokemon.knockout:
        # Earn coins for beating the legendary pokemon
        print("You win! You found 100 coins.")
        trainer.coins += 100
        print()
        
        # Catch the pokemon - low probability of successfully catching
        delay_print("Catch that Pokemon!\n")
        time.sleep(0.5)
        delay_print(f"{trainer.name}: Go Pokeball!\n")
        while trainer.pokeballs > 0:
            caught = trainer.catching_pokemon('gym')
            if caught == True:
                print(f"{gym_pokemon.name} has been registered to your Pokemon team!")
                trainer.pokemon_team.append(gym_pokemon)
                time.sleep(3)
                break
            elif caught == False:
                more_throws = input("Do you want use another Pokeball to try again? (y/n)")
                if more_throws == 'y':
                    continue
                elif more_throws == 'n':
                    break
                else:
                    print("Please input 'y' or 'n'")
        
        if trainer.pokeballs <= 0:
            print("You are out of Pokeballs! Please go to the Pokemon Center to buy more.")
    
    return True   


def view_status():
    """ Displays the players's inventory, Pokemon collection, and Pokemon properties.
    """
    trainer.status_trainer()
    for pokemon in trainer.pokemon_team:
        pokemon.status()

        
def buy(item, amount):
    """ Purchase items from the shop.
    
    Parameters
    ----------
    item : dictionary
        dictionary provides the name and the cost of the item.
    amount : string
        string provided by user, specifies the amount of the item that is being purchased
    """
    if item["name"] == "Potion":
        if amount == "1" and trainer.coins >= item["cost"]:
            trainer.potions += 1
            trainer.inventory["Potions"] = trainer.potions
            trainer.coins -= item["cost"]
        elif amount == "2" and trainer.coins >= item["cost"] * 10:
            trainer.potions += 10
            trainer.inventory["Potions"] = trainer.potions
            trainer.coins -= item["cost"] * 10
        elif amount == "3" and trainer.coins >= item["cost"] * 20:
            trainer.potions += 20
            trainer.inventory["Potions"] = trainer.potions
            trainer.coins -= item["cost"] * 20
    if  item["name"] == "Revive Potion":
        if amount == "1" and trainer.coins >= item["cost"]:
            trainer.revive_potions += 1
            trainer.inventory["Revive Potions"] = trainer.revive_potions
            trainer.coins -= item["cost"]
        elif amount == "2" and trainer.coins >= item["cost"] * 10:
            trainer.revive_potions += 10
            trainer.inventory["Revive Potions"] = trainer.revive_potions
            trainer.coins -= item["cost"] * 10
        elif amount == "3" and trainer.coins >= item["cost"] * 20:
            trainer.revive_potions += 20
            trainer.inventory["Revive Potions"] = trainer.revive_potions
            trainer.coins -= item["cost"] * 20
    if  item["name"] == "Pokeball":
        if amount == "1" and trainer.coins >= item["cost"]:
            trainer.pokeballs += 1
            trainer.coins -= item["cost"]
        elif amount == "2" and trainer.coins >= item["cost"] * 10:
            trainer.pokeballs += 10
            trainer.coins -= item["cost"] * 10
        elif amount == "3" and trainer.coins >= item["cost"] * 20:
            trainer.pokeballs += 20
            trainer.coins -= item["cost"] * 20
            
def shop():
    """ Displays items for the player to purchase and adds it to the player's inventory.
    """
    delay_print("Welcome to the Pokemon Center! What would you like to buy?")
    
    stock =  {"1": {"name": "Potion", "cost": 5},
              "2": {"name": "Revive Potion", "cost": 10},
              "3": {"name": "Pokeball", "cost": 5}}
    
    # display the items in the shop
    for product_number in stock:
        print("\nProduct No.", product_number)
        print("Name:", stock[product_number]['name'])
        print("Price:", stock[product_number]['cost'])
    
    # player inputs the number for the item they want to purchase
    print(f"\nYou have {trainer.coins} Pokecoins.")
    purchase = input()
    
    # player inputs the number for the amount they want to purchase
    if purchase in stock:
        delay_print("How many would you like?\n")
        print("1) 1\n" 
              "2) 10\n"
              "3) 20\n")
        purchase_amount = input()
        buy(stock[purchase], purchase_amount)
    
    print(f"\nYou have {trainer.coins} Pokecoins left.")
    delay_print("Thank you for shopping at the Pokemon Center! Please come again!")
