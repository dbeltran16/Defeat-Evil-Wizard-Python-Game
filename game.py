import random


# Base Character Class

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.shield = False
        self.evade = False

    def attack(self, enemy):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)

        # Check if enemy blocks or evades
        if enemy.shield:
            print(f"{enemy.name} blocked the attack with a shield!")
            enemy.shield = False
            return

        if enemy.evade:
            print(f"{enemy.name} evaded the attack!")
            enemy.evade = False
            return

        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def heal(self):
        heal_amount = random.randint(15, 25)
        self.health += heal_amount

        # Prevent health from going over max
        if self.health > self.max_health:
            self.health = self.max_health

        print(f"{self.name} heals for {heal_amount} health!")

    def display_stats(self):
        print("\n-------------------")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print("-------------------\n")


# Warrior Class

class Warrior(Character):
    def power_strike(self, enemy):
        damage = self.attack_power + 15
        enemy.health -= damage
        print(f"{self.name} uses Power Strike for {damage} damage!")

    def battle_cry(self):
        self.attack_power += 5
        print(f"{self.name} uses Battle Cry! Attack power increased.")


# Mage Class

class Mage(Character):
    def fireball(self, enemy):
        damage = self.attack_power + 20
        enemy.health -= damage
        print(f"{self.name} casts Fireball for {damage} damage!")

    def lightning(self, enemy):
        damage = self.attack_power + 10
        enemy.health -= damage
        print(f"{self.name} uses Lightning Bolt for {damage} damage!")



# Archer Class
class Archer(Character):
    def quick_shot(self, enemy):
        damage = random.randint(10, 20) * 2
        enemy.health -= damage
        print(f"{self.name} uses Quick Shot for {damage} damage!")

    def evade_attack(self):
        self.evade = True
        print(f"{self.name} prepares to evade the next attack!")



# Paladin Class

class Paladin(Character):
    def holy_strike(self, enemy):
        damage = self.attack_power + 18
        enemy.health -= damage
        print(f"{self.name} uses Holy Strike for {damage} damage!")

    def divine_shield(self):
        self.shield = True
        print(f"{self.name} activates Divine Shield!")



# Evil Wizard Class

class EvilWizard(Character):
    def regenerate(self):
        heal_amount = random.randint(10, 20)
        self.health += heal_amount

        if self.health > self.max_health:
            self.health = self.max_health

        print(f"Evil Wizard regenerates {heal_amount} health!")

    def dark_magic(self, enemy):
        damage = random.randint(15, 30)

        if enemy.shield:
            print(f"{enemy.name}'s shield blocked Dark Magic!")
            enemy.shield = False
            return

        if enemy.evade:
            print(f"{enemy.name} evaded Dark Magic!")
            enemy.evade = False
            return

        enemy.health -= damage
        print(f"Evil Wizard casts Dark Magic for {damage} damage!")



# Character Selection

print("Choose Your Character:")
print("1. Warrior")
print("2. Mage")
print("3. Archer")
print("4. Paladin")

choice = input("Enter choice: ")

if choice == "1":
    player = Warrior("Warrior", 120, 20)

elif choice == "2":
    player = Mage("Mage", 90, 25)

elif choice == "3":
    player = Archer("Archer", 100, 18)

elif choice == "4":
    player = Paladin("Paladin", 130, 15)

else:
    print("Invalid choice. Defaulting to Warrior.")
    player = Warrior("Warrior", 120, 20)

wizard = EvilWizard("Evil Wizard", 150, 20)


# Battle System

print("\nThe battle begins!\n")

while player.health > 0 and wizard.health > 0:

    print("Choose an action:")
    print("1. Attack")
    print("2. Heal")
    print("3. Use Ability 1")
    print("4. Use Ability 2")
    print("5. View Stats")

    action = input("Enter action: ")

    # Basic attack
    if action == "1":
        player.attack(wizard)

    # Heal
    elif action == "2":
        player.heal()

    # Ability 1
    elif action == "3":

        if isinstance(player, Warrior):
            player.power_strike(wizard)

        elif isinstance(player, Mage):
            player.fireball(wizard)

        elif isinstance(player, Archer):
            player.quick_shot(wizard)

        elif isinstance(player, Paladin):
            player.holy_strike(wizard)

    # Ability 2
    elif action == "4":

        if isinstance(player, Warrior):
            player.battle_cry()

        elif isinstance(player, Mage):
            player.lightning(wizard)

        elif isinstance(player, Archer):
            player.evade_attack()

        elif isinstance(player, Paladin):
            player.divine_shield()

    # View stats
    elif action == "5":
        player.display_stats()
        wizard.display_stats()
        continue

    else:
        print("Invalid action.")
        continue

    # Check if wizard is defeated
    if wizard.health <= 0:
        print("\nYou defeated the Evil Wizard!")
        break

    # Wizard turn
    print("\nEvil Wizard's turn!")

    wizard.regenerate()
    wizard.dark_magic(player)

    # Display health after each round
    print(f"\n{player.name} Health: {player.health}")
    print(f"Evil Wizard Health: {wizard.health}\n")

    # Check if player loses
    if player.health <= 0:
        print("\nThe Evil Wizard has defeated you!")

print("\nGame Over")