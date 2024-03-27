class Pokemon:
	def __init__(self, name, nature, HP, special_attack):
		self.name = name
		self.nature = nature
		self.HP = HP
		self.special_attack = special_attack
	def __repr__(self):
		description = "I am {name}, I am a {nature} pokemon and my special attack is {attack}.".format(name = self.name, nature = self.nature, attack = self.special_attack)

		if self.HP > 90:
			description += " I am a tanky pokemon."
		else:
			description += " I am fighter."
		return description

pikachu = Pokemon("Pikachu", "lightning", 85, "Fire Bolt")
squirtle = Pokemon("Squirtle", "Water", 75, "Squirt")
bulbasaur = Pokemon("Bulbasaur", "earth", 95, "Dirt attack")
charmander = Pokemon("Charmander", "fire", 85, "fireball")


class Trainer:
	def __init__(self, input_name, input_age, input_gender):
		self.name = input_name
		self.gender = input_gender
		self.age = input_age
		self.pokemons = []
	def __repr__(self):
		description = "Hey, my name is {name}, I am {age} old, and I am a {gender}.".format(name = self.name, age = self.age, gender = self.gender)
		return description

player_name = input("Hello Trainer, what is your name?\n")
player_age = input("How old are you?\n")
player_gender = input("and last qustion what gender are you?\n")
player_one = Trainer(player_name, player_age, player_gender)

print(f"\nHello, {player_name}!!\n")
answer_exited = input("It is time for you to pick a first pokemon, are you exited?\n\nA) Yeaaahhh!!!\nB) Not really.\n\n")
if answer_exited == 'A':
	print(f"\nHappy to hear that {player_name}!\n\n")
else:
	print(f"\nThat's a bummer, I hope you will get exited along your jurney.\n\n")


while True:
    pokemon_pick = input("So your options are pikachu, squirtle, charmander, bulbasaur\n\nA) Pikachu\tB)Squirtle\nC)Charmander\tD)Bulbasaur\n\nWith one will it be?\n\n")
    if pokemon_pick not in ['A', 'B', 'C', 'D']:
        print("\nWrong input!\n")
        continue
    if pokemon_pick == 'A':
        print('\n' + str(pikachu))
    elif pokemon_pick == 'B':
        print('\n' + str(squirtle))
    elif pokemon_pick == 'C':
        print('\n' + str(charmander))
    elif pokemon_pick == 'D':
        print('\n' + str(bulbasaur))
    while True:
        is_sure = input("\nAre you sure???\n\n")
        if is_sure not in ['yes', 'no']:
            print("\nWrong input!\n")
            continue
        break
    if is_sure == 'yes':
        if pokemon_pick == 'A':
            player_one.pokemons.append("Pikachu")
        elif pokemon_pick == 'B':
            player_one.pokemons.append("Squirtle")
        elif pokemon_pick == 'C':
            player_one.pokemons.append("Charmander")
        elif pokemon_pick == 'D':
            player_one.pokemons.append("Bulbasaur")
        break












