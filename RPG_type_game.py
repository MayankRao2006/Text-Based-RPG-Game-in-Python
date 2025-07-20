import random

class Character:
    def __init__(self, name, max_hp, current_hp, attack_power, max_mana, current_mana):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.attack_power = attack_power
        self.max_mana = max_mana
        self.current_mana = current_mana

class Player(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=35, current_hp=35, max_mana = 15, current_mana = 15, attack_power=random.randint(2, 7))

class Enemy(Character):
    def __init__(self):
        super().__init__(name="Goblin", max_hp=25, current_hp=25, attack_power=random.randint(1, 5), max_mana=0, current_mana=0)

class Game:
    def __init__(self):
        player_name = input("Enter your character's name: ")
        self.player = Player(player_name)
        self.enemy = Enemy()
    
    def enemy_attack(self):
        enemy_damage = random.randint(1, 5)
        self.player.current_hp -= enemy_damage
        print(f"\n{self.enemy.name} 🗡 attacks {self.player.name}! Total damage dealt: {enemy_damage}")
        print(f"\n{self.player.name} HP: {self.player.current_hp}/{self.player.max_hp} Mana: {self.player.current_mana}/{self.player.max_mana}")
        print(f"{self.enemy.name} HP: {self.enemy.current_hp}/{self.enemy.max_hp}")
    

    def show(self):
        print(f"Beware! {self.player.name}, a wild {self.enemy.name} has appeared!")
        print(f"\n{self.player.name} HP: {self.player.current_hp}/{self.player.max_hp} Mana: {self.player.current_mana}/{self.player.max_mana}")
        print(f"{self.enemy.name} HP: {self.enemy.current_hp}/{self.enemy.max_hp}")

        while self.player.current_hp > 0 and self.enemy.current_hp > 0:
            try:
                action = int(input("\nActions:\n1) 🗡 Attack\n2) ❤ Heal(5 Mana)\n3) 🔥 Fireball(10 Mana) \n4)🏃🏻💨 Run\nChoose your action: "))
            except ValueError:
                print("Please enter a value between 1-4")
                continue
            
            if action == 1:
                    damage = random.randint(2, 7)
                    self.enemy.current_hp -= damage
                    print(f"\n{self.player.name} 🗡 attacks {self.enemy.name}! Total damage dealt: {damage}")
                    

                    if self.enemy.current_hp <= 0:
                        print(f"{self.enemy.name} has been Slain!")
                        break
                    
                    self.enemy_attack()

                    if self.player.current_hp <= 0:
                        print(f"{self.player.name} has been defeated! Game Over.")
                        break
            
            elif action == 2:
                if self.player.current_hp == self.player.max_hp:
                    print("\nHealth is already full, cannot heal")
                    continue

                elif self.player.current_mana < 5:
                        print("\nNot enough Mana to heal")
                        continue
                
                else:
                    if self.player.current_mana >= 5:
                        self.player.current_mana -= 5
                        heal_amount = random.randint(5, 10)
                        if self.player.current_hp + heal_amount > self.player.max_hp:
                            heal_amount = self.player.max_hp - self.player.current_hp
                        self.player.current_hp += heal_amount
                        print(f"\n{self.player.name} uses ❤ heal! {heal_amount} HP healed")
                        self.enemy_attack()
                    
                if self.player.current_hp <= 0:
                    print(f"{self.player.name} has been defeated! Game Over.")
                    break
		    

            elif action == 3:
                if self.player.current_mana >= 10:
                    fire_damage = random.randint(9,14)
                    self.enemy.current_hp -= fire_damage
                    self.player.current_mana -= 10
                    print(f"\n{self.player.name} uses Fireball 🔥! It dealt {fire_damage} damage!")

                    if self.enemy.current_hp <= 0:
                        print(f"{self.enemy.name} has been slain")
                        break

                    self.enemy_attack()

                    if self.player.current_hp <= 0:
                        print(f"\n{self.player.name} has been defeated! Game Over.")
                        break

                else:
                    print("Not enough Mana to cast Fireball")
                    continue

            elif action == 4:
                print(f"\n{self.player.name} runs away! 🏃🏻💨")
                break
            else:
                print("Invalid response, please choose again.")

# Running the game
o = Game()
o.show()

