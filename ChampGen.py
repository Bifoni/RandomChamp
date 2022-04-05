import random

mid_champ = ['Lillia', 'Yone', 'Vex', 'Pyke', 'Neeko', 'Sylas', 'Bard', 'Azir', 'Qiyana', 'Ekko', 'Zed', 'Lucian',
             'Akshan',
             'Taliyah', "Vel'Koz", 'Yasuo', 'Seraphine', "Kai'sa", 'Zyra', 'Zoe', 'Aurelion Sol', 'Syndra', 'Diana',
             'Lissandra', 'Jayce', 'Ziggs', 'Viktor', 'Fizz', 'Ahri', 'Xerath', 'Lux', "Kog'Maw", 'Talon', 'Malzahar',
             'Akali',
             'Ezreal', 'Pantheon', 'Gragas', 'Heimerdinger', 'Cassiopeia', 'Rumble', 'Brand', 'Orianna', 'Nocturne',
             'Katarina',
             'Malphite', 'Swain', 'Caitlyn', 'Veigar', 'Corki', 'Irelia', 'Kassadin', 'Anivia', "Cho'Gath", 'Karthus',
             'Zilean', 'Morgana', 'Teemo', 'Ryze', 'Vladimir', 'LeBlanc', 'Urgot', 'Twisted Fate', 'Galio', 'Annie', ]

jug_champ = ['Lillia', 'Gwen', 'Ivern', "Rek'Sai", 'Vi', 'Qiyana', 'Ekko', 'Zed', 'Viego', 'Kindred', 'Taliyah', 'Zac',
             'Kayn',
             'Diana', "Kha'Zix", 'Hecarim', 'Sejuani', 'Rengar', 'Volibear', 'Graves', 'Shyvana', 'Talon',
             'Mordekaiser',
             'Gragas', 'Poppy', 'Udyr', 'Nidalee', 'Skarner', 'Rumble', 'Lee Sin', 'Elise', 'Jarvan IV', 'Nocturne',
             'Trundle', 'Shaco', 'Rammus', 'Amumu', "Cho'Gath", 'Karthus', 'Twitch', 'Evelynn', 'Jax', 'Tryndamere',
             'Nunu & Willump', 'Warwick', 'Master Yi', 'Fiddlesticks', 'Xin Zhao', 'Olaf', ]

sup_champ = ['Renata Glasc', 'Vex', 'Sett', 'Pyke', 'Neeko', 'Rell', 'Rakan', 'Bard', 'Thresh', 'Yuumi', 'Nami',
             'Senna',
             'Tahm Kench', 'Braum', "Vel'Koz", 'Zac', 'Seraphine', 'Zyra', 'Lulu', 'Nautilus', 'Xerath', 'Lux', 'Shen',
             'Leona', 'Pantheon', 'Brand', 'Maokai', 'Malphite', 'Blitzcrank', 'Swain', 'Taric', 'Karma', 'Janna',
             'Sona',
             'Anivia', 'Amumu', 'Zilean', 'Morgana', 'Soraka', 'Alistar', 'Galio', ]

adc_champ = ['Aphelios', 'Xayah', 'Kalista', 'Samira', 'Lucian', 'Jinx', 'Jhin', 'Akshan', 'Yasuo', 'Seraphine',
             "Kai'sa",
             'Quinn', 'Draven', 'Ziggs', 'Varus', "Kog'Maw", 'Ezreal', 'Heimerdinger', 'Vayne', 'Brand', 'Caitlyn',
             'Swain',
             'Veigar', 'Corki', 'Twitch', 'Morgana', 'Ashe', 'Miss Fortune', 'Tristana', 'Sivir', 'Twisted Fate', ]

top_champ = ['Lillia', 'Gwen', 'Yone', 'Sett', 'Neeko', 'Sylas', 'Ornn', 'Illaoi', 'Aatrox', 'Kled', 'Tahm Kench',
             'Camille',
             'Akshan', 'Yasuo', 'Gnar', 'Aurelion Sol', 'Quinn', 'Jayce', 'Darius', 'Fiora', 'Sejuani', 'Rengar',
             'Volibear',
             'Graves', 'Shen', 'Riven', 'Garen', 'Kennen', 'Akali', 'Yorick', 'Mordekaiser', 'Pantheon', 'Gragas',
             'Poppy',
             'Udyr', 'Nasus', 'Heimerdinger', 'Rumble', 'Vayne', 'Lee Sin', 'Wukong', 'Renekton', 'Maokai', 'Nocturne',
             'Malphite', 'Trundle', 'Gangplank', 'Irelia', 'Dr. Mundo', "Cho'Gath", 'Singed', 'Jax', 'Tryndamere',
             'Warwick',
             'Tristana', 'Teemo', 'Sion', 'Ryze', 'Kayle', 'Vladimir', 'Urgot', 'Olaf', ]
lanes = ['Toplane', 'Jungle', 'Midlane', 'ADC', 'Support']

while True:
    nome_jogador = input('Digite o nome do jogador: ')
    nome_jogador = nome_jogador.upper()
    perg_lane = input('Gostaria de escolher a Lane?(s/n) ')
    lanes_rng = random.choice(lanes)
    if perg_lane == 'n':
        if lanes_rng == 'Toplane':
            print(
                f'--------------------------\n{nome_jogador}\nLane: {lanes_rng}\nChampion: {random.choice(top_champ)}\n--------------------------')
        elif lanes_rng == 'Jungle':
            print(
                f'--------------------------\n{nome_jogador}\nLane: {lanes_rng}\nChampion: {random.choice(jug_champ)}\n--------------------------')
        elif lanes_rng == 'Midlane':
            print(
                f'--------------------------\n{nome_jogador}\nLane: {lanes_rng}\nChampion: {random.choice(mid_champ)}\n--------------------------')
        elif lanes_rng == 'ADC':
            print(
                f'--------------------------\n{nome_jogador}\nLane: {lanes_rng}\nChampion: {random.choice(adc_champ)}\n--------------------------')
        elif lanes_rng == 'Support':
            print(
                f'--------------------------\n{nome_jogador}\nLane: {lanes_rng}\nChampion: {random.choice(sup_champ)}\n--------------------------')

    elif perg_lane == 's':
        escolha_lane = input('Escolha sua lane(Toplane, Jungle, Midlane, ADC, Support): ')
        escolha_lane = escolha_lane.lower()
        if 'top' in escolha_lane:
            print(
                f'--------------------------\n{nome_jogador}\nLane: Toplane\nChampion: {random.choice(top_champ)}\n--------------------------')
        elif 'jun' in escolha_lane:
            print(
                f'--------------------------\n{nome_jogador}\nLane: Jungle\nChampion: {random.choice(jug_champ)}\n--------------------------')
        elif 'mid' in escolha_lane:
            print(
                f'--------------------------\n{nome_jogador}\nLane: Midlane\nChampion: {random.choice(mid_champ)}\n--------------------------')
        elif 'ad' in escolha_lane:
            print(
                f'--------------------------\n{nome_jogador}\nLane: ADC\nChampion: {random.choice(adc_champ)}\n--------------------------')
        elif 'sup' in escolha_lane:
            print(
                f'--------------------------\n{nome_jogador}\nLane: Support\nChampion: {random.choice(sup_champ)}\n--------------------------')
        else:
            print('Digite uma lane válida')