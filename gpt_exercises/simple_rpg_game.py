import random

def generate_player_attack(difficulty):

    regular_dmg_high = 30
    strong_dmg_high = 65
    heal_amount_high = 100

    if difficulty == 'medium':
        regular_dmg_high = 40
        strong_dmg_high = 60
        heal_amount_high = 80
    elif difficulty == 'hard':
        regular_dmg_high = 50
        strong_dmg_high = 55
        heal_amount_high = 60


    # Generate random damage values for player's attack abilities
    regular_attack_damage = random.randint(1, regular_dmg_high)
    strong_attack_damage = random.randint(regular_dmg_high, strong_dmg_high)
    heal_amount = random.randint(1, heal_amount_high)
    return regular_attack_damage, strong_attack_damage, heal_amount

def generate_monster_attack(difficulty):

    regular_dmg_high = 30
    if difficulty == 'medium':
        regular_dmg_high = 40
    elif difficulty == 'hard':
        regular_dmg_high = 50

    # Generate random damage value for monster's attack
    monster_attack_damage = random.randint(1, regular_dmg_high)
    return monster_attack_damage

def get_ability_name(nr):
    abilities = {
        1: 'regular attack',
        2: 'strong attack',
        3: 'heal'
    }
    return abilities[nr]

def get_player_name():
    player_name = input("Enter Player Name: ")
    return player_name

def choose_difficulty():
    difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid difficulty level. Please choose again.")
        difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
    return difficulty

def save_high_scores(player_name, difficulty, turns):
    with open("high_scores.txt", "a") as file:
        file.write("Player: {} ({}), Turns: {}\n".format(player_name, difficulty, turns))

def player_turn(turns):

    # Initialize list to store available abilities
    available_abilities = []

    # Check which abilities are available based on the number of turns
    if turns % 5 == 0:
        available_abilities.append(3)
    if turns % 3 == 0:
        available_abilities.append(2)
    available_abilities.append(1)

    return available_abilities

def main():
    player_health = 100
    monster_health = 100
    turns = 1
    player = get_player_name()
    print("Welcome, {}!".format(player))
    difficulty = choose_difficulty()
    print("Difficulty level chosen:", difficulty)

    while player_health > 0 and monster_health > 0:
        print("\nTurn", turns)
        print(f"{player} Health:", player_health)
        print("Monster Health:", monster_health)

        # Determine player's available abilities for this turn
        available_abilities = player_turn(turns)
        print("Available Abilities for this turn:")
        for available_ability in available_abilities:
            print(f"{available_ability}. {get_ability_name(available_ability)}")

        # Ask player for the ability to use
        player_ability = int(input("Choose your ability: "))

        # Validate player's choice
        while player_ability not in available_abilities:
            print("Invalid ability. Please choose again.")
            player_ability = int(input("Choose your ability: "))

        # Generate player's and monster's attacks
        regular_attack_damage, strong_attack_damage, heal_amount = generate_player_attack(difficulty)
        monster_attack_damage = generate_monster_attack(difficulty)

        # Execute player's chosen ability
        player_damage = 0
        if get_ability_name(player_ability) == "regular attack":
            player_damage = regular_attack_damage
            print(f'{player} attacks for', player_damage)
        elif get_ability_name(player_ability) == "strong attack":
            player_damage = strong_attack_damage
            print(f'{player} attacks for', player_damage)
        elif get_ability_name(player_ability) == "heal":
            if (player_health + heal_amount) > 100:
                player_health = 100
            else:
                player_health += heal_amount
                print(f'{player} heals for', heal_amount)

        # Update health points
        monster_health -= player_damage

        # Determine if player has won
        if monster_health <= 0:
            print(f"{player} wins!")
            save_high_scores(player, difficulty, turns)
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                continue
            else:
                player_health = 100
                monster_health = 100
                turns = 1
                continue

        # Execute monster's attack
        monster_damage = monster_attack_damage
        print('Monster attacks for', monster_damage)

        # Update health points
        player_health -= monster_damage

        if player_health <= 0:
            print("Monster wins!")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                continue
            else:
                player_health = 100
                monster_health = 100
                turns = 1
                continue

        turns += 1

# Run the game


main()
