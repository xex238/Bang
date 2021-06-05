exec dbo.Clear_bd

-- 1.1) Запрос на регистрацию - есть ли пользователь в базе данных
select dbo.Registration_request('alyona@yandex.ru', '12345', 'alyona238')

-- 1.2) Регистрация пользователя
exec dbo.Registration
@mail = 'alyona@yandex.ru',
@password = '12345',
@login = 'alyona238'
truncate table [User]

-- 1.3) Авторизация пользователя - есть ли пользователь в базе данных
select dbo.Authorization_request('alyona@yandex.ru', '12345')

-- 1.4) Получение списка комнат
exec dbo.Available_rooms

-- 1.5) Получение списка достижений для выбранного пользователя
exec dbo.Achivements_request
@mail = 'alyona@yandex.ru',
@password = '12345'

-- 1.6) Создание комнаты
exec dbo.Creating_room
@mail = 'alyona@yandex.ru',
@password = '12345',
@max_count_of_players = 6

-- 2.1.1) Добавление игрока в комнату
exec dbo.Add_player_to_room
@mail = 'alyona@yandex.ru',
@password = '12345',
@room_ID = 1

-- 2.1.2) Получение n случайных персонажей (без повторений)
exec dbo.Getting_characters
@n = 6

-- 2.1.4) Добавление выбранного персонажа к игроку
exec dbo.Add_character_to_player
@player_ID = 1,
@characters_ID = 1

-- 2.1.5) Добавление роли к игроку
exec dbo.Add_role_to_player
@player_ID = 1,
@roles_ID = 1

-- 2.1.7) Получение ID пользователя по его почте и паролю
exec dbo.Get_user_ID
@mail = 'alyona@yandex.ru',
@password = '12345'

-- 2.1.8) Получение ID игрока по его почте и паролю
exec dbo.Get_player_ID
@mail = 'alyona@yandex.ru',
@password = '12345'

-- 2.1.9) Получение максимального количества жизней персонажа игрока
exec dbo.Get_max_lives
@player_ID = 1

-- 3.1) Установка значения хода для заданного игрока
exec dbo.Player_turn_state
@player_ID = 1,
@state = 1

-- 3.2) Проверка на наличие заданной карты у игрока
select dbo.Check_card_availability(1, 1)

-- 3.3) Проверка на наличие заданной карты персонажа у игрока
select dbo.Check_character_availability(1, 1)

-- 3.4) Проверка возможности выстрелить в игрока (учитывается расстояние между игроками и дальность стрельбы из оружия)
select dbo.Check_shoot_opportunity(1, 1)

-- 3.5) Выдача карты игроку из колоды
exec dbo.Set_card_to_player_from_Deck
@player_ID = 1,
@room_ID = 1

-- 3.6) Выдача карты игроку из сброса
exec dbo.Set_card_to_player_from_Dropping
@player_ID = 1,
@room_ID = 1

-- 3.7) Переход карты игрока в сброс
exec dbo.Send_card_to_Dropping
@card_ID = 1,
@room_ID = 1

-- 3.8) Выбранный игрок теряет 1 жизнь
exec dbo.Lose_health
@player_ID = 1

-- 3.9) Выбранный игрок восстанавливает единицу здоровья
exec dbo.Recovery_health
@player_ID = 1

-- 3.10) Кража карты у игрока
exec dbo.Stealing_card_from_player
@player_ID_to = 1,
@card_ID = 1

-- 3.11) Получение списка карт, находящихся в руке у игрока
exec dbo.Get_player_cards
@player_ID = 1

-- 3.12) Установка нового оружия для игрока
exec dbo.Set_weapon
@player_ID = 1,
@name = 'volcanic',
@base_weapon = 1,
@firing_range = 1,
@endless_bang = 1

-- 3.13) Получение карты из колоды для проверки (проверенная карта уходит в сброс)
exec dbo.Get_card_for_checking
@room_ID = 1

-- 3.14) Изменить дополнительную защиту игрока на n
exec dbo.Change_additional_defence_range
@player_ID = 1,
@n = 1

-- 3.15) Изменить дополнительную дальность атаки игрока на n
exec dbo.Change_additional_attack_range
@player_ID = 1,
@n = 1

-- 3.16) Проверка, есть ли у игрока на столе карта с аналогичным названием
exec dbo.Check_player_name_card
@player_ID = 1,
@name = 'barrel'

-- 3.17) Получить карту из колоды и добавить её на стол
exec dbo.Set_cards_to_table
@room_ID = 1

-- 3.18) Передача карты игроку
exec dbo.Passing_card_to_player
@player_ID = 1,
@card_ID = 1,
@card_location = 1

-- 3.19) Восстановление единицы жизни всем игрокам, если это возможно
exec dbo.Recovery_health_all_players
@room_ID = 1

-- 3.20) Получить верхнюю карту из колоды и добавить её в стадию выбора
exec dbo.Set_cards_to_selection_stage
@room_ID = 1

-- 3.21) Возвращение карты в колоду
exec dbo.Return_card_to_Deck
@card_ID = 1,
@room_ID = 1

-- 3.22) Перемешивание карт из сброса и добавление их в колоду
exec dbo.Shuffle_cards_in_Dropping
@room_ID = 1

-- 3.23) Получение значение поля [name] в таблице [Card] для заданной ID
exec dbo.Get_card_name
@card_ID = 1

-- 3.24) Процедура позволяет изменить поле [card_location] таблицы [Card] на заданное значение
exec dbo.Change_card_location
@card_ID = 1,
@card_location = 1