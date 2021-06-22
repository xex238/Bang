class request:
    # Приветствие 1
    hello = ''
    new_player = ''

    # Передача подтверждения готовности
    total_request1 = ''
    set_ready = ''

    #Начало стадии планирования
    planning = ''

    #4.2) Сервер отправляет случайного сгенерированного персонажа
    set_character = ''

    #5.2) Сервер отправляет случайно сгенерированную роль
    set_role = ''

    #7.2) Отправка ответа с данными об игроках.
    player_data = ''

    #8.2) Отправка карт игроку
    set_start_card = ''

    #9.2) Сообщает игрокам, кто ходит первым
    start_game = ''

    #1.1) Розыгрыш карты «бэнг»
    play_bang = ''

    #1.2) Розыгрыш карты «мимо»
    play_missed = ''

    #1.3) Розыгрыш карты «пиво»
    play_beer = ''

    #1.4) Розыгрыш карты «дуэль»
    play_duel = ''
    use_bang = ''
    lose_HP = ''

    #1.5) Розыгрыш карты «паника»
    play_panic1 = ''
    play_panic2 = ''
    lose_card = ''
    get_cards = ''

    #1.6) Розыгрыш карты «красотка»
    play_cat_balou = ''

    #1.7) Розыгрыш оружия
    play_weapon = ''

    #1.12)  Розыгрыш карты «бочка». Использование бочки
    play_barrel = ''
    check_barrel = ''

    #1.13)  Розыгрыш карты «уэллс фарго»
    play_fargo = ''

    #1.14)  Розыгрыш карты «дилижанс»
    play_diligence = ''

    #1.15)  Розыгрыш карты «мустанг»
    play_mustang = ''

    #1.16)  Розыгрыш карты «тюрьма». Проверка тюрьмы перед началом хода игрока
    play_jail = ''
    check_jail = ''
    jail_set_move = ''

    #1.17)   Розыгрыш карты «индейцы»
    play_indians1 = ''
    play_indians2 = ''

    #1.18)  Розыгрыш карты «гатлинг»
    play_gatling1 = ''
    play_gatling2 = ''
    play_gatling3 = ''

    #1.19)  Розыгрыш карты «динамит». Проверка динамита в начале игры
    play_dynamite = ''
    check_dynamite = ''

    #1.20)  Розыгрыш карты «магазин»
    play_store1 = ''
    play_store2 = ''

    #1.21)  Розыгрыш карты «салун»
    play_saloon = ''

    #1.22)  Розыгрыш карты «прицел» 
    play_aim = ''

    #2.1)  Использование свойства персонажа «Счастливчик Люк»
    use_Luke = ''

    #2.2)  Использование свойства персонажа «Неуловимый Джо»
    use_Joe = ''

    #2.4)  Использование свойства персонажа «Большой Змей»
    use_Snake1 = ''
    use_Snake2 = ''

    #2.5)  Использование свойства персонажа «Туко»
    use_Tuco1 = '' 
    use_Tuco2 = '' 
    use_Tuco3 = '' 

    #2.6)  Использование свойства персонажа «Кит Карсон»
    use_Kit1 = ''
    use_Kit2 = ''
    use_Kit3 = ''
    use_Kit4 = ''

    #2.7)  Использование свойства персонажа «Джанго»
    use_Django1 = ''
    use_Django2 = ''
    use_Django3 = ''
    use_Django4 = ''

    #2.8)  Использование свойства персонажа «Джесси Джеймс»
    use_Jesse1 = ''
    use_Jesse2 = ''
    use_Jesse3 = ''
    use_Jesse4 = ''
    use_Jesse5 = ''
    use_Jesse6 = ''

    #2.9)  Использование свойства персонажа «Хладнокровная Рози»
    use_Rosie = ''

    #2.10)  Использование свойства персонажа «Человек-без-имени»
    use_noname1 = ''
    use_noname2 = ''
    
    #2.11)  Использование свойства персонажа «Бедовая Джейн»
    use_Jane1 = ''
    use_Jane2 = ''

    #2.12)  Использование свойства персонажа «Сюзи Лафайет»
    use_Suzy1 = ''
    use_Suzy2 = ''

    #2.13)  Использование свойства персонажа «Бешеный Пёс»
    use_mad_dog1 = ''
    use_mad_dog2 = ''
    use_mad_dog3 = ''
    use_mad_dog4 = ''
    use_mad_dog5 = ''
    use_mad_dog6 = ''

    #2.14)  Использование свойства персонажа «Том Кетчум»
    use_Tom = ''
    
    #2.15)  Использование свойства персонажа «Ангельские Глазки»
    use_angel_eyes1 = ''
    use_angel_eyes2 = ''

    #2.16)  Использование свойства персонажа «Бутч Кэссиди»
    use_Butch1 = ''
    use_Butch2 = ''
    use_Butch3 = ''

    #3.1)  Сообщение об окончании хода
    move_end = ''
    
    #3.2)  Выдача двух карт в начале хода'
    get_cards1 = ''
    get_cards2 = ''

    #Обмен данными во время игры
    #1) Убит игрок
    player_died1 = ''

    #1.1) Убит игрок с ролью «бандит»
    player_died2 = ''
    player_died3 = ''

    #1.2) Убит игрок с ролью «помощник» игроком с ролью «шериф»
    player_died4 = ''
    player_died5 = ''

    #2) Потеря карт погибшим игроком
    dead_lose_card = ''

    #3) Игрок погиб – игра окончена
    dead_game_over = ''

    #4) Проверка соединения с каждым клиентом
    ping = ''

    def __init__(self):
        self.hello = 'HELLO\n'
        self.hello += '{count_of_players}, {max_count_of_players}\n'
        self.hello += '{player_ID}'

        self.new_player = 'NEW PLAYER\n'
        self.new_player += '{count_of_players}'

        self.total_request = '{code} {message}'

        self.set_ready = 'SET READY: {value}\n'
        self.set_ready += '{player_ID}'

        self.planning = 'PLANNING STAGE IS STARTING'

        self.set_character = 'SET CHARACTER\n'
        self.set_character += '{character_ID}'

        self.set_role = 'SET ROLE\n'
        self.set_role += '{role_ID}'

        self.player_data = '{number}, {player_ID}, {character_ID}'

        self.set_start_card = 'SET START CARD\n'
        self.set_start_card += '{card_ID}'

        self.start_game = 'GAME IS START\n'
        self.start_game += 'SET MOVE\n'
        self.start_game += '{player_ID}'

        self.play_bang = 'PLAY BANG\n'
        self.play_bang += '{player_ID}, {target_ID}\n'
        self.play_bang += '{card_ID}'

        self.play_missed = 'PLAY MISSED\n'
        self.play_missed += '{target_ID}\n'
        self.play_missed += '{card_ID}'

        self.play_beer = 'PLAY BEER\n'
        self.play_beer += '{player_ID}\n'
        self.play_beer += '{card_ID}\n'
        self.play_beer += 'GET 1 HP'

        self.play_duel = 'PLAY DUEL\n'
        self.play_duel += '{player_ID}, {target_ID}\n'
        self.play_duel += '{card_ID}'

        self.use_bang = 'USE BANG\n'
        self.use_bang += '{target_ID}\n'
        self.use_bang += '{card_ID}'
     
        self.lose_HP = 'LOSE 1 HP\n'
        self.lose_HP += '{player_ID}'

        self.play_panic1 = 'PLAY PANIC\n'
        self.play_panic1 += '{player_ID}, {target_ID}\n'
        self.play_panic1 += '{card_ID}\n'
        self.play_panic1 += 'STEAL 1 CARD FROM {location}\n'
        self.play_panic1 += '{card_ID}'

        self.play_panic2 = 'PLAY PANIC\n'
        self.play_panic2 += '{player_ID}, {target_ID}\n'
        self.play_panic2 += '{card_ID}\n'
        self.play_panic2 += 'STEAL 1 CARD FROM {location}'
       
        self.lose_card = 'LOSE 1 CARD\n'
        self.lose_card += '{card_ID}'

        self.get_cards = 'GET {n} CARDS\n'
        self.get_cards += '{card_ID}'

        self.play_cat_balou = 'PLAY CAT BALOU\n'
        self.play_cat_balou += '{player_ID}, {target_ID}\n'
        self.play_cat_balou += '{card_ID}\n'
        self.play_cat_balou += 'DISCARD 1 CARD FROM {location}\n'
        self.play_cat_balou += '{card_ID}'

        self.play_weapon = 'PLAY {name}\n'
        self.play_weapon += '{player_ID}\n'
        self.play_weapon += '{card_ID}'

        self.play_barrel = 'PLAY BARREL\n'
        self.play_barrel += '{player_ID}\n'
        self.play_barrel += '{card_ID}'

        self.check_barrel = 'CHECK BARREL\n'
        self.check_barrel += '{target_ID}\n'
        self.check_barrel += '{card_ID}\n'
        self.check_barrel += 'CHECK {result}\n'
        self.check_barrel += '{card_ID}'

        self.play_fargo = 'PLAY WELLS FARGO\n'
        self.play_fargo += '{player_ID}\n'
        self.play_fargo += '{card_ID}'

        self.play_diligence = 'PLAY DILIGENCE\n'
        self.play_diligence += '{player_ID}\n'
        self.play_diligence += '{card_ID}'

        self.play_mustang = 'PLAY MUSTANG\n'
        self.play_mustang += '{player_ID}\n'
        self.play_mustang += '{card_ID}'

        self.play_jail = 'PLAY JAIL\n'
        self.play_jail += '{player_ID}, {target_ID}\n'
        self.play_jail += '{card_ID}'

        self.check_jail = 'CHECK JAIL\n'
        self.check_jail += '{player_ID}\n'
        self.check_jail += '{card_ID}\n'
        self.check_jail += 'CHECK {result}\n'
        self.check_jail += '{card_ID}'

        self.jail_set_move = 'SET MOVE\n'
        self.jail_set_move += '{player_ID}'

        self.play_indians1 = 'PLAY_INDIANS\n'
        self.play_indians1 += '{player_ID}, {target_ID}\n'
        self.play_indians1 += '{card_ID}'

        self.play_indians2 = 'USE BANG\n'
        self.play_indians2 += '{target_ID}\n'
        self.play_indians2 += '{card_ID}\n'
        self.play_indians2 = 'PLAY_INDIANS'

        self.play_gatling1 = 'PLAY_GATLING\n'
        self.play_gatling1 += '{player_ID}, {target_ID}\n'
        self.play_gatling1 += '{card_ID}'

        self.play_gatling2 = 'CHECK BARREL\n'
        self.play_gatling2 += '{target_ID}\n'
        self.play_gatling2 += '{card_ID}\n'
        self.play_gatling2 += 'CHECK FAIL\n'
        self.play_gatling2 += '{card_ID}\n'
        self.play_gatling2 += 'PLAY GATLING'

        self.play_gatling3 = 'USE MISSED\n'
        self.play_gatling3 += '{target_ID}\n'
        self.play_gatling3 += '{card_ID}\n'
        self.play_gatling3 += 'PLAY GATLING'

        self.play_dynamite = 'PLAY DYNAMITE\n'
        self.play_dynamite += '{player_ID}\n'
        self.play_dynamite += '{card_ID}'

        self.check_dynamite = 'CHECK DYNAMITE\n'
        self.check_dynamite += '{player_ID}\n'
        self.check_dynamite += '{card_ID}\n'
        self.check_dynamite += 'CHECK FAIL\n'
        self.check_dynamite += '{card_ID}\n'
        self.check_dynamite += 'LOSE 3 HP'

        self.play_store1 = 'PLAY GENERAL STORE\n'
        self.play_store1 += '{player_ID}\n'
        self.play_store1 += '{card_ID}'

        self.play_store2 = 'CHOOSE 1 CARD FROM GENERAL STORE\n'
        self.play_store2 += '{player_ID}\n'
        self.play_store2 += '{card_ID}\n'
        self.play_store2 += 'LEFT'

        self.play_saloon = 'PLAY SALOON\n'
        self.play_saloon += '{player_ID}\n'
        self.play_saloon += '{card_ID}\n'
        self.play_saloon += 'GET 1 HP'   

        self.play_aim = 'PLAY AIM\n'
        self.play_aim += '{player_ID}\n'
        self.play_aim += '{card_ID}'

        self.use_Luke = 'USE CHARACTER\n'
        self.use_Luke += '{character_ID}\n'
        self.use_Luke += '{player_ID}\n'
        self.use_Luke += 'CHECK BARREL\n'
        self.use_Luke += '{target_ID}\n'
        self.use_Luke += '{card_ID}\n'
        self.use_Luke += 'CHECK FAIL\n'
        self.use_Luke += '{card_ID}'

        self.use_Joe = '{code} {message}'

        self.use_Snake1 = 'PLAYER DIED\n'
        self.use_Snake1 += '{player_ID}, {killer_ID} \n'
        self.use_Snake1 += '{role_ID}'

        self.use_Snake2 = 'USE CHARACTER\n'
        self.use_Snake2 += '{character_ID}\n'
        self.use_Snake2 += '{player_ID}\n'
        self.use_Snake2 += 'GET ALL CARDS FROM PLAYER\n'
        self.use_Snake2 += '{target_ID}'

        self.use_Tuco1 = 'SET MOVE\n'
        self.use_Tuco1 += '{player_ID}'

        self.use_Tuco2 = 'USE CHARACTER\n'
        self.use_Tuco2 += '{character_ID}\n'
        self.use_Tuco2 += '{player_ID}\n'
        self.use_Tuco2 += 'GET 1 CARD CLOSED FROM DROPPING\n'
        self.use_Tuco2 += 'GET 1 CARD CLOSED FROM DECK'

        self.use_Tuco3 = 'GET 1 CARD CLOSED FROM DROPPING\n'
        self.use_Tuco3 += '{card_ID}\n'
        self.use_Tuco3 += 'GET 1 CARD CLOSED FROM DECK\n'
        self.use_Tuco3 += '{card_ID}'

        self.use_Kit1 = 'SET MOVE\n'
        self.use_Kit1 += '{player_ID}'

        self.use_Kit2 = 'USE CHARACTER\n'
        self.use_Kit2 += '{character_ID}\n'
        self.use_Kit2 += '{player_ID}\n'
        self.use_Kit2 += 'GET 3 CARDS CLOSED FROM DECK'

        self.use_Kit3 = 'GET 3 CARDS CLOSED FROM DECK\n'
        self.use_Kit3 += '{card_ID}, {card_ID}, {card_ID}'

        self.use_Kit4 = 'RETURN 1 CARD CLOSED ON DECK\n'
        self.use_Kit4 += '{player_ID}'

        self.use_Django1 = 'LOSE 1 HP\n'
        self.use_Django1 += '{player_ID}, {killer_ID}'
        
        self.use_Django2 = 'USE CHARACTER\n'
        self.use_Django2 += '{character_ID}\n'
        self.use_Django2 += '{player_ID}\n'
        self.use_Django2 += 'STEAL 1 CARD FROM HAND\n'
        self.use_Django2 += '{target_ID}'

        self.use_Django3 = 'LOSE 1 CARD\n'
        self.use_Django3 += '{card_ID}'

        self.use_Django4 = 'GET 1 CARD\n'
        self.use_Django4 += '{card_ID}'

        self.use_Jesse1 = 'SET MOVE\n'
        self.use_Jesse1 += '{player_ID}'

        self.use_Jesse2 = 'USE CHARACTER\n'
        self.use_Jesse2 += '{character_ID}\n'
        self.use_Jesse2 += '{player_ID}\n'
        self.use_Jesse2 += 'STEAL 1 CARD FROM HAND\n'
        self.use_Jesse2 += '{target_ID}'

        self.use_Jesse3 = 'LOSE 1 CARD\n'
        self.use_Jesse3 += '{card_ID}'

        self.use_Jesse4 = 'GET 1 CARD\n'
        self.use_Jesse4 += '{card_ID}'

        self.use_Jesse5 = 'GET 1 CARD CLOSED FROM DECK\n'
        self.use_Jesse5 += '{player_ID}'

        self.use_Jesse6 = 'GET 1 CARD\n'
        self.use_Jesse6 += '{card_ID}'

        self.use_Rosie = '{code} {message}'

        self.use_noname1 = 'PLAY BANG\n'
        self.use_noname1 += '{player_ID}, {target_ID}\n'
        self.use_noname1 += '{card_ID}'

        self.use_noname2 = 'USE CHARACTER\n'
        self.use_noname2 += '{character_ID}\n'
        self.use_noname2 += '{player_ID}\n'
        self.use_noname2 += 'CHECK HIT\n'
        self.use_noname2 += 'CHECK SUCCESS\n'
        self.use_noname2 += '{card_ID}'

        self.use_Jane1 = 'USE CHARACTER\n'
        self.use_Jane1 += '{character_ID}\n'
        self.use_Jane1 += '{player_ID}\n'
        self.use_Jane1 += '{PLAY MISSED LIKE BANG}\n'
        self.use_Jane1 += '{player_ID}, {target_ID}\n'
        self.use_Jane1 += '{card_ID}'

        self.use_Jane2 = 'USE CHARACTER\n'
        self.use_Jane2 += '{character_ID}\n'
        self.use_Jane2 += '{player_ID}\n'
        self.use_Jane2 += '{PLAY BANG LIKE MISSED}\n'
        self.use_Jane2 += '{player_ID}, {target_ID}\n'
        self.use_Jane2 += '{card_ID}'

        self.use_Suzy1 = 'USE CHARACTER\n'
        self.use_Suzy1 += '{character_ID}\n'
        self.use_Suzy1 += '{player_ID}\n'
        self.use_Suzy1 += '{GET 1 CARD CLOSED FROM DECK}'

        self.use_Suzy2 = 'GET 1 CARD\n'
        self.use_Suzy2 += '{card_ID}'

        self.use_mad_dog1 = 'SET MOVE\n'
        self.use_mad_dog1 += '{player_ID}'

        self.use_mad_dog2 = 'USE CHARACTER\n'
        self.use_mad_dog2 += '{character_ID}\n'
        self.use_mad_dog2 += '{player_ID}\n'
        self.use_mad_dog2 += '{CHECK CARD}\n'
        self.use_mad_dog2 += '{CHECK SUCCESS}\n'
        self.use_mad_dog2 += '{card_ID}'

        self.use_mad_dog3 = 'GET 3 CARDS CLOSED FROM DECK\n'
        self.use_mad_dog3 += '{card_ID}, {card_ID}, {card_ID}'

        self.use_mad_dog4 = 'SET MOVE\n'
        self.use_mad_dog4 += '{player_ID}'

        self.use_mad_dog5 = 'USE CHARACTER\n'
        self.use_mad_dog5 += '{character_ID}\n'
        self.use_mad_dog5 += '{player_ID}\n'
        self.use_mad_dog5 += '{CHECK CARD}\n'
        self.use_mad_dog5 += '{CHECK FAIL}\n'
        self.use_mad_dog5 += '{card_ID}'

        self.use_mad_dog6 = 'GET 2 CARDS CLOSED FROM DECK\n'
        self.use_mad_dog6 += '{card_ID}, {card_ID}'

        self.use_Tom = 'USE CHARACTER\n'
        self.use_Tom += '{character_ID}\n'
        self.use_Tom += '{player_ID}\n'
        self.use_Tom += '{GET 1 HP}\n'
        self.use_Tom += '{card_ID}, {card_ID}'

        self.use_angel_eyes1 = 'USE CHARACTER\n'
        self.use_angel_eyes1 += '{character_ID}\n'
        self.use_angel_eyes1 += '{player_ID}\n'
        self.use_angel_eyes1 += '{NEED 2 CARDS MISSED}\n'
        self.use_angel_eyes1 += '{PLAY BANG}\n'
        self.use_angel_eyes1 += '{player_ID}, {target_ID} \n'
        self.use_angel_eyes1 += '{card_ID}'

        self.use_angel_eyes2 = 'PLAY 2 MISSED\n'
        self.use_angel_eyes2 += '{target_ID} \n'
        self.use_angel_eyes2 += '{card_ID}, {card_ID}'

        self.use_Butch1 = 'LOSE 1 HP\n'
        self.use_Butch1 += '{player_ID}'

        self.use_Butch2 = 'USE CHARACTER\n'
        self.use_Butch2 += '{character_ID}\n'
        self.use_Butch2 += '{player_ID}\n'
        self.use_Butch2 += 'GET 1 CARD CLOSED FROM DECK'

        self.use_Butch3 = 'GET 1 CARD\n'
        self.use_Butch3 += '{card_ID}'

        self.move_end = 'SET MOVE\n'
        self.move_end += '{player_ID}'

        self.get_cards1 = 'GET 2 CARDS CLOSED FROM DECK\n'
        self.get_cards1 += '{player_ID}'

        self.get_cards2 = 'GET 2 CARDS\n'
        self.get_cards2 += '{card_ID}, {card_ID}'

        self.player_died1 = 'PLAYER DIED\n'
        self.player_died1 += '{player_ID}, {killer_ID}\n'
        self.player_died1 += '{role_ID}'
        
        self.player_died2 = 'PLAYER DIED\n'
        self.player_died2 += '{player_ID}, {killer_ID}\n'
        self.player_died2 += '{role_ID}'

        self.player_died3 = 'GET 3 CARDS\n'
        self.player_died3 += '{player_ID}\n'
        self.player_died3 += '{card_ID}, {card_ID}, {card_ID}'

        self.player_died4 = 'LOSE ALL CARDS\n'
        self.player_died4 += '{player_ID}'

        self.dead_lose_card = 'LOSE ALL CARDS\n'
        self.dead_lose_card += '{player_ID}'
    
        self.dead_game_over = 'LOSE ALL CARDS\n'
        self.dead_game_over += 'RENEGATE WIN\n'
        self.dead_game_over += 'WIN\n'
        self.dead_game_over += 'LOSE'

        self.ping = 'PING'