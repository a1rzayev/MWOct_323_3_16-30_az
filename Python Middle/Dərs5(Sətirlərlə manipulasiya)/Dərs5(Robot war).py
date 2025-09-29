# Silahların qiymətləri
details_damage_price = {
    "energy_gun": 100,
    "minigun": 70,
    "thor_hammer": 50,
    "laser_gun": 80,
    "rail_gun": 90,
    "sniper_rifle": 150 
}

# Müdafiə əşyalarının qiymətləri
details_survive_price = {
    "shield": 50,
    "energy shield": 80,
    "resist": 30, 
    "evasion": 100,
    "armor": 140
}

# Oyunçular və onların robotları
users_bot = {}
users_list = []

# Oyunçuları əlavə etmək funksiyası
def player_maker(player_list):
    user_choice = "yes"
    while user_choice in ["yes", "y"]:
        user_input = input("Oyunçunun adını daxil edin: ")
        if len(user_input) < 3:
            print("Ad çox qısadır!")
            continue
        player_list.append(str.capitalize(user_input))
        user_choice = input("Daha oyunçu əlavə edilsin? (y/n): ").lower()
        print("Oyunçular:")
        for i, name in enumerate(player_list, start=1):
            print(f"{i}) {name}")

# Robotları yaratmaq və alış-veriş etmək funksiyası
def bot_maker(start_sum, player_list):
    for player in player_list:
        wallet = start_sum
        # Robot üçün başlanğıc məlumatlar
        users_bot[player] = {"hp": 100, "damage": [], "survive": []}

        # Oyunçu pulu bitməyincə alış-veriş
        while wallet >= min(details_damage_price.values()):
            print(f"\n{player}, sənin {wallet} pulun var".center(82, "="))
            print("Almaq olar:".center(82, "-"))
            print("{:^80}".format("Hücum əşyaları"))
            for gun, price in details_damage_price.items():
                print(f"{gun}: {price}")
            print("{:^80}".format("Müdafiə əşyaları"))
            for survive, price in details_survive_price.items():
                print(f"{survive}: {price}")
            
            user_choice = input("Detal seçin (və ya 'exit' yazıb çıxın): ").lower()
            if user_choice == "exit":
                break

            # Hücum əşyasını almaq
            if user_choice in details_damage_price:
                price = details_damage_price[user_choice]
                if wallet >= price:
                    wallet -= price
                    users_bot[player]["damage"].append(user_choice)
                    print(f"{user_choice} alındı!")
                else:
                    print("Kifayət qədər pul yoxdur!")
            # Müdafiə əşyasını almaq
            elif user_choice in details_survive_price:
                price = details_survive_price[user_choice]
                if wallet >= price:
                    wallet -= price
                    users_bot[player]["survive"].append(user_choice)
                    print(f"{user_choice} alındı!")
                else:
                    print("Kifayət qədər pul yoxdur!")
            else:
                print("Yanlış seçim!")

# Döyüş funksiyası
def fight():
    players = list(users_bot.keys())
    alive_players = [p for p in players if users_bot[p]["hp"] > 0]

    while len(alive_players) > 1:
        for attacker in alive_players:
            # Əgər oyunçu ölübsə keç
            if users_bot[attacker]["hp"] <= 0:
                continue

            # İlk sağ qalan rəqibə hücum et
            for defender in alive_players:
                if defender != attacker and users_bot[defender]["hp"] > 0:
                    attack = sum(details_damage_price.get(item, 0) for item in users_bot[attacker]["damage"])
                    defense = sum(details_survive_price.get(item, 0) for item in users_bot[defender]["survive"])
                    damage = max(attack - defense, 0)
                    users_bot[defender]["hp"] -= damage
                    print(f"{attacker} {defender}-ə {damage} zərbə vurdu! ({defender} HP: {users_bot[defender]['hp']})")
                    if users_bot[defender]["hp"] <= 0:
                        print(f"{defender} məğlub oldu!")
                        alive_players = [p for p in players if users_bot[p]["hp"] > 0]
                    break  # hər turda yalnız bir rəqibə hücum
        alive_players = [p for p in players if users_bot[p]["hp"] > 0]

    print(f"\n{alive_players[0]} döyüşün qalibi oldu!")

# Oyunu başlatmaq
def play_game():
    print("Döyüş Robotları oyununa xoş gəlmisiniz!")
    player_maker(users_list)
    bot_maker(200, users_list)
    print("\nBütün alış-verişlər bitdi. Döyüş başlayır!\n")
    fight()

play_game()
