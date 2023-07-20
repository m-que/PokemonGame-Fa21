"""Classes used throughout project"""
import random as rd
import sys
import time

class Pokemon:
    def __init__(self, name, element_type, level=1):
        """ Represent a Pokemon by its name, element type, level, health, active status, and experience points.
        
        Parameters
        ----------
        name : string
            string that displays the name of the Pokemon
        element_type : string
            string that displays the type of Pokemon, consisting of either Grass, Fire, or Water
        level: int
            integer determining the level of the Pokemon based on experience points it gains through battles
        """
        self.name = name
        self.element_type = element_type
        self.level = level
        self.max_health = level * 100
        self.health = level * 100
        self.knock_out = False
        self.experience = 0

    def status(self):
        """ Displays information about the Pokemon's type, level, and health.
        """
        print(f'{self.name} ', end=" ")
        print(f'Type:{self.element_type}', end=" ")
        print(f'Level:{self.level}', end=" ")
        print(f'Health:{self.health}/{self.max_health}', end=" ")
        print()
    
    def knock_out(self):
        """ Knocks out the Pokemon when it reaches 0 health. 
        """
        self.knock_out == True
        if self.health != 0:
            self.health = 0
        # print(f"{self.name} is knocked out!")

    def lose_health(self, damage):
        """ Prints the health lost and health remaining for the Pokemon during battles.
        
        Parameters
        ----------
        damage : int
            integer representing the amount of damage the Pokemon takes from opponent's attack
        """
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")
        if self.health > 0:
            print(f"{self.name} has {self.health} health remaining.")
        elif self.health <= 0:
            self.health = 0
            self.knock_out

    def heal(self, heal):
        """ Heals the Pokemon so it regains health.
        
        Parameters
        ----------
        heal : int
            integer representing the amount of health the Pokemon regains from potions
        """
        if self.health + heal >= self.max_health:
            self.health = self.max_health
        else:
            self.health += heal
    
    def revive(self):
        """ Revives a Pokemon from a knock out to full health.
        """
        if self.knock_out:
            self.health = self.max_health
            self.knock_out = False
        #else:
            #print(f"{self.name} is not knocked out yet!")
    
    def attack(self, other_pokemon):
        """ Begins a battle with another Pokemon.
        
        Parameters
        ----------
        other_pokemon : object
            Properties of the opponent Pokemon that is engaged in the battle
        """
        # amount of damage dealt depends whether the pokemon has an element advantage over its opponent. 
        # pokemon can gain experience points based on the damage dealt.
        print(f"{self.name} attacks {other_pokemon.name}! ")
        
        # damage dealt by grass type pokemon
        if self.element_type == 'Grass':
            if other_pokemon.element_type == 'Water':
                damage = (self.level * 10) * 2
                self.experience += 3
                print("Attack super effective!")
            if other_pokemon.element_type == 'Fire':
                damage = (self.level * 10) / 2
                self.experience += 1
                print("Attack not very effective!")
            if other_pokemon.element_type == self.element_type:
                damage = self.level * 10
                self.experience += 2
                print("Attack somewhat effective!")
        
        # damage dealt by fire type pokemon
        if self.element_type == 'Fire':
            if other_pokemon.element_type == 'Grass':
                damage = (self.level * 10) * 2
                self.experience += 3
                print("Attack super effective!")
            if other_pokemon.element_type == 'Water':
                damage = (self.level * 10) / 2
                self.experience += 1
                print("Attack not very effective!")
            if other_pokemon.element_type == self.element_type:
                damage = self.level * 10
                self.experience += 2
                print("Attack somewhat effective!")
        
        # damage dealt by water type pokemon
        if self.element_type == 'Water':
            if other_pokemon.element_type == 'Fire':
                damage = (self.level * 10) * 2
                self.experience += 3
                print("Attack super effective!")
            if other_pokemon.element_type == 'Grass':
                damage = (self.level * 10) / 2
                self.experience += 1
                print("Attack not very effective!")
            if other_pokemon.element_type == self.element_type:
                damage = self.level * 10
                self.experience += 2
                print("Attack somewhat effective!")
        
        # opponent loses health corresponding to the amount of damage dealt
        other_pokemon.lose_health(damage)
        #print(f"{self.name} has dealt {damage} damage to {other_pokemon.name}!")
        
        # knocks out the Pokemon once its health decreases to zero
        if other_pokemon.health <= 0:
            other_pokemon.knock_out = True
        if self.health <= 0:
            self.knock_out = True
    
    def level_up(self):
        """ Levelling up a Pokemon by increasing its max health and resetting its experience points
        """
        self.level += 1
        self.experience = 0
        self.max_health += 10
        self.health = self.max_health
        delay_print(f"{self.name} leveled up to level {self.level}! Health has fully recovered and is now {self.max_health}.\n")


class Trainer:
    def __init__(self, name, pokemon_buddy, pokemon_team, coins=500):
        """ Represents the Trainer by their name, current Pokemon in use, total Pokemon, and money.
        
        Parameters
        ----------
        name : string
            string that displays the name of the Trainer
        pokemon_buddy : object
            object that refers to the Pokemon that the Trainer is currently using
        pokemon_team : list
            list that refers to the total Pokemon the Trainer has collected
        coins : int
            integer that depict that amount of Pokecoins that the Trainer has in their wallet
        """
        self.name = name
        self.pokemon_buddy = pokemon_buddy
        self.pokemon_team = pokemon_team
        self.coins = coins
        self.inventory = {"Potions": rd.randint(2, 5), "Revive Potions": rd.randint(2, 5)}
        self.potions = self.inventory["Potions"]
        self.revive_potions = self.inventory["Revive Potions"]
        self.pokeballs = rd.randint(5, 30)
        
    def status_trainer(self):
        """ Displays information about items in the player's inventory.
        """
        print(f"{self.name}'s Inventory':\n")
        print(f'1) Pokecoins: {self.coins}')
        print(f'2) Potions: {self.inventory["Potions"]}')
        print(f'3) Revive Potions: {self.inventory["Revive Potions"]}')
        print(f'4) Pokeballs: {self.pokeballs}')
        print(f'5) Pokemon Buddy: {self.pokemon_buddy.name}')
        print('6) Pokemons:', end=" ")
        
        # prints the player's pokemons in one line with names seperated by commas
        for pokemon in self.pokemon_team:
            pokemon_name = pokemon.name
            if pokemon == self.pokemon_team[len(self.pokemon_team)-1]:
                print(f'{pokemon.name}')
            else:
                print(f'{pokemon.name},', end=" ")


    def has_pokemon(self):
        """ Determines if the Trainer has any active Pokemon remaining in their collection to use in battle.
        
        Returns
        -------
        output : bool
            bool returns False is all Pokemon in Trainer's collection is knocked out, returns True if otherwise 
        """
        for pokemon in self.pokemon_team:
            if not pokemon.knock_out:
                return True
        return False
    
    def use_potion(self, pokemon):
        """ Uses a potion to heal a Pokemon so it regains health.
        
        Parameters
        ----------
        pokemon : object
            object refers to the Pokemon whose health is being healed
        """
        if self.potions > 0 and pokemon.health > 0 and pokemon.health < pokemon.max_health:
            pokemon.heal(30)
            self.potions -= 1
            self.inventory["Potions"] = self.potions
            print(f"You used a potion! {pokemon.name} gained 30 health and now has {pokemon.health} health")
        elif pokemon.health == pokemon.max_health:
            print(f"{pokemon.name} is already at full health!")
        elif pokemon.knock_out:
            print(f"{pokemon.name} is at 0 health and needs a revive potion!")
        elif self.potions <= 0:
            print("You don't have enough potions!")
    
    def use_revive_potion(self, pokemon):
        """ Uses a potion to revive a Pokemon from its knock out state to full health.
        
        Parameters
        ----------
        pokemon : object
            object refers to the Pokemon who is being revived from zero health to full health
        """
        if self.revive_potions > 0 and pokemon.health == 0:
            pokemon.revive()
            self.revive_potions -= 1
            self.inventory["Revive Potions"] = self.revive_potions
            print(f"You used a revive potion! {pokemon.name} has revived and has its max health of {pokemon.max_health}.")
        elif pokemon.health > 0:
            print("That Pokemon is not knocked out! Please use a regular potion instead.")
        elif self.revive_potions <= 0:
            print("You don't have enough potions!")
    
    def swap_buddy(self):
        """ Switches the player's current Pokemon to a different Pokemon in their collection.
        """
        # loops through the player's pokemon collection to print out each pokemon's name, type, level, and health status
        print(f"{self.name}'s Pokemon:")
        for number, pokemon in enumerate(self.pokemon_team):
            pokemon_fainted = ''
            if pokemon.knock_out:
                pokemon_fainted = "- fainted"
            print(f"{number+1}) {pokemon.name}- {pokemon.element_type} Lvl.{pokemon.level} HP.{pokemon.health}/{pokemon.max_health} {pokemon_fainted}")
        
        print(f"Input the number for the Pokemon you would like to change to.")
        new_pokemon = input()
        
        for i in range(len(self.pokemon_team)):
            if new_pokemon in str(i + 1):
                
                # move the player's chosen pokemon to the beginning of the list if it still has health left
                if not self.pokemon_team[int(new_pokemon) - 1].knock_out:
                    self.pokemon_team.insert(0, self.pokemon_team.pop(self.pokemon_team.index(self.pokemon_team[int(new_pokemon) - 1])))
                else:
                    self.swap_buddy()
            #elif self.pokemon_team[0].knock_out:
                #self.swap_buddy()
    
    def catching_pokemon(self, place):
        """ Catching more Pokemon after defeating them using Pokeballs.
        
        Parameters
        ----------
        place : string
            string that represents whether the pokemon is a wild Pokemon or a gym Pokemon
        
        Returns
        -------
        output : bool
            bool returns True if player receives the correct phrase for a successful capture, returns False if otherwise
        """
        self.pokeballs -= 1
        print("You throw a pokeball!")
        catch_phrases = ["You missed the Pokemon!", "Oh no! The Pokemon broke free!", 
                         "So close! You almost had it!", "Gotcha! Pokemon was caught!"]
        
        time.sleep(2)
        #for i in range(3):
        if place == 'wild':
            catch = rd.choice(catch_phrases)
        if place == 'gym':
            # formatting
            catch = rd.choices(catch_phrases, weights=[30, 30, 30, 10])
            
        if catch == catch_phrases[3]:
            print(catch)
            return True
        else:
            print(catch)
            time.sleep(1.5) 
            #print("Oh no! The wild Pokemon has woken up and fled!")
            return False

    def use_inventory(self):
        """ Uses chosen item in player's inventory and applies the item's effect on the desired Pokemon.
        
        Parameters
        ----------
        catch : bool
            bool represents whether the player can use a Pokeball to catch Pokemon, is False when the player cannot
        
        Returns
        -------
        output : bool
            bool returns False for invalid user inputs, True if otherwise
        """
        # displays the player's coins, potions, revive potions, and pokeballs in their inventory
        print(f"Pokecoins: {self.coins}")
        number = 1
        for key, value in self.inventory.items():
            print(f"{number}) {key}: {value}")
            number += 1
        
        option = input("\nInput the number for the item you would like to use.\n")
        total_options = ['1', '2']
        
        if option in total_options:
            if option == '1':
                # displays all pokemon and their properties in the player's pokemon collection
                for number, pokemon in enumerate(self.pokemon_team):
                    pokemon_fainted = ''
                    if pokemon.knock_out:
                        pokemon_fainted = "- fainted"
                    print(f"{number+1})- {pokemon.name} {pokemon.element_type} Lvl.{pokemon.level} HP.{pokemon.health}/{pokemon.max_health} {pokemon_fainted}")
                
                # apply the potion's effect on inputted pokemon number
                print("Choose which Pokemon to use the potion on.")
                choose_pokemon = input()
                for i in range(len(self.pokemon_team)):
                    if choose_pokemon in str(i + 1):
                        self.use_potion(self.pokemon_team[int(choose_pokemon)-1])
                    #return False
            
            elif option == '2':
                for number, pokemon in enumerate(self.pokemon_team):
                    pokemon_fainted = ''
                    if pokemon.knock_out:
                        pokemon_fainted = "- fainted"
                    print(f"{number+1})- {pokemon.name} {pokemon.element_type} Lvl.{pokemon.level} HP.{pokemon.health}/{pokemon.max_health} {pokemon_fainted}")

                print("Choose which Pokemon to use the potion on")
                choose_pokemon = input()
                for i in range(len(self.pokemon_team)):
                    if choose_pokemon in str(i + 1):
                        self.use_revive_potion(self.pokemon_team[int(choose_pokemon)-1])
                    #return False
        return False