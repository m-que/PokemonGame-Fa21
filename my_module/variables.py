""" Module responsible for establising the variables used for the game, consisting of different Pokemon and their types, as well as trainer and Team Rocket member names. 
"""

from my_module.classes import Pokemon, Trainer

# Variables for my project
# Player
trainer = Trainer("", "", [])

# Wild Pokemon 
wild_pokemon = [{"name":"Bulbasaur", "type":"Grass"}, 
                {"name":"Chikorita", "type":"Grass"}, 
                {"name":"Turtwig", "type":"Grass"}, 
                {"name":"Snivy", "type":"Grass"}, 
                {"name":"Chespin", "type":"Grass"}, 
                {"name":"Charmander", "type":"Fire"}, 
                {"name":"Cyndaquil", "type":"Fire"}, 
                {"name":"Torchic", "type":"Fire"}, 
                {"name":"Chimchar", "type":"Fire"}, 
                {"name":"Tepig", "type":"Fire"}, 
                {"name":"Squirtle", "type":"Water"}, 
                {"name":"Mudkip", "type":"Water"}, 
                {"name":"Piplup", "type":"Water"}, 
                {"name":"Totodile", "type":"Water"}, 
                {"name":"Oshawott", "type":"Water"}]

#evolved_pokemon

# Team Rocket
team_rocket_names = ['Jessie', 'James', 'Giovanni']
team_rocket_pokemon = [{"name":"Roserade", "type":"Grass"}, 
                       {"name":"Gyarados", "type":"Water"}, 
                       {"name":"Houndoom", "type":"Fire"},
                       {"name":"Victreebel", "type":"Grass"}]

# Other Trainers
trainer2_names = ['Ash', 'Misty', 'Brock', 'May', 'Dawn', 'Gary']
trainer2_pokemons = [{"name":"Sceptile", "type":"Grass"}, 
                     {"name":"Cacturne", "type":"Grass"}, 
                     {"name":"Arcanine", "type":"Fire"}, 
                     {"name":"Magmortar", "type":"Fire"}, 
                     {"name":"Milotic", "type":"Water"}, 
                     {"name":"Poliwrath", "type":"Water"}]

# Gym Raid Pokemon (Legendaries)
legendaries = [{"name":"Virizion", "type":"Grass"}, 
               {"name":"Entei", "type":"Fire"}, 
               {"name":"Kyogre", "type":"Water"}]