pokemon_advantages = { 'adv_1': ["Fire", "Grass"], 'adv_2':["Water", "Fire"], 'adv_3': ["Grass", "Water"]  }

class Pokemon:
  def __init__(self, name, level, typ):
    self.name = name
    self.level = level
    self.typ = typ
    self.max_health = 50
    self.health = 50
    self.fainted = False
    self.atk = level

  def __repr__(self):
    if self.fainted == False:
      return self.name + ", LVL " + str(self.level) + ", " + self.typ + " type. Max HP: " + str(self.max_health) + "HP. CURRENT HP: " + str(self.health) + "HP."
    else:
      return self.name + " is Fainted."

  def lose_health(self, damage):
    self.health -= damage
    return self.name + " sustained " + str(damage) + " dmg and now has " + str(self.health) + " HP"

  def gain_health(self, heal):
    self.health += heal
    return self.name + " was healed for " + str(heal) + " HP and now has " + str(self.health) + " HP out of " + str(self.max_health) + "HP"

  def faint(self):
    self.fainted = True
    self.health = 0
    return self.name + " has been knocked out"

  def revive(self):
    if self.fainted == True:
      self.fainted = False
      self.health += (self.health*0.3)

  def attack(self, other_pokemon):
    damage = self.atk
    for p1, p2 in pokemon_advantages.values():
      if self.typ == p1 and other_pokemon.typ == p2:
        damage = self.atk * 2
        break
      else:
        continue

    if other_pokemon.health < 1:
      return other_pokemon.faint()
    elif damage == self.atk:
      other_pokemon.lose_health(damage)
      return self.name + " have dealt " + str(damage) + " dmg to " + other_pokemon.name + ". It Was Not Very Effective!"
    else:
      other_pokemon.lose_health(damage)
      return self.name + " have dealt " + str(damage) + " dmg to " + other_pokemon.name + ". It Was Super Effective!"

class Trainer:
  def __init__(self, name, act_pokemon = "N/A"):
    self.name = name
    self.pokemons = []
    self.act_pokemon = act_pokemon
    self.potions = 4


  def __repr__(self):
    return self.name

  def use_potion(self):
    potion = 20
    if self.potions == 0:
      print("You don't have any potions left.")
    elif self.current_pokemon != "N/A":
      self.potions -= 1
      self.act_pokemon.gain_health(potion)
    else:
      print("You don't have a current pokemon selected, pick one.")

  def pick_pokemon(self):
    print("Your pokemons in hand: " + str(self.pokemons))
    poke_input = input("Pick one")
    pokemon = poke_input.title()
    if len(self.pokemons) > 0:
      for i in range(0, len(self.pokemons)):
        if pokemon == self.pokemons[i] and self.pokemons[i].fainted == False:
          self.act_pokemon = self.pokemons[i]
          print(pokemon + " is your current pokemon")
          break

          if i < len(self.pokemons)-1:
            continue
          else:
            print(pokemon + " is not available.")
    else:
      print("You have no pokemons!")

  def attack_trainer(self):
    print("Trainers around you:")
    print(trainers)
    opponent = input("Select yout opponent: ")
    opponent = opponent.title()
    if self.name == opponent:
      print("You can't attack yourself!!!")
    else:
      for i in range(0, len(trainers)):
        if opponent == trainers[i].name:
          if self.act_pokemon != "N/A" and trainers[i].act_pokemon != "N/A":
            print(self.name + " and " + trainers[i].name + " are going to fight, get ready:" + self.act_pokemon.upper() + " VS " + trainers[i].act_pokemon.upper())
            self.act_pokemon.attack(attack_trainer[i].act_pokemon)
            break
          else:
            if self.act_pokemon == "N/A" and trainers[i].act_pokemon == "N/A":
            print("You cannot have a fist fight, use pokemons instead. Choose your pokemons!")
          elif: self.act_pokemon == "N/A":
            print(self.name + ", pick your pokemon.")
          else:
            print(trainers[i].name + ", pick your pokemon.")
        else:
          if i < len(trainers) - 1:
            continue
          else:
            print(opponent + "is not around you.")

  def add_pokemon(self):
    print("Available Pokemons:")
    print(available_pokemons)
    selected_pokemon = input("Select your Pokemon: ")
    selected_pokemon = selected_pokemon.title()

    if len(available_pokemons) > 0:
      for i in range(0, len(available_pokemons)):
        if selected_pokemon == available_pokemons[i].name:
          if not available_pokemons[i] in self.pokemons:
            self.pokemons.append(available_pokemons.pop(i))
            print(selected_pokemon + " was added to your hand")
            print("Your pokemons:")
            print(self.pokemons)
            break
          else:
            print("You have " + selected_pokemon + " in your hand already.")
            break
        else:
          if i < len(available_pokemons) - 1:
            continue
          else:
            print("This pokemon is not available")
    else:
      print("No pokemons available")

  def revive_act(self):
    self.act_pokemon.revive()




charmander = Pokemon("Charmander", 1, "Fire")
squirtle = Pokemon("Squirtle", 1, "Water")
bulbasaur = Pokemon("Bulbasaur", 1,"Grass")
blastoise = Pokemon("Blastoise", 36,"Water")
vulpix = Pokemon("Vulpix", 1,"Fire")
oddish = Pokemon("Oddish", 1,"Grass")
psyduck = Pokemon("Psydck", 1,"Water")
ponyta= Pokemon("Ponyta", 1,"Fire")

ash = Trainer("Ash")
brock = Trainer("Brock")
misty = Trainer("Misty")
gary = Trainer("Gary")

trainers = [ash, brock, misty, gary]
available_pokemons = [charmander, squirtle, bulbasaur, blastoise, vulpix, psyduck, oddish, ponyta]




print(squirtle)
print(charmander)
print(bulbasaur)
print(blastoise)




print(ash)

