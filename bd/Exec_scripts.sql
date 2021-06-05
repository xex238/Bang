exec dbo.Clear_bd

-- 1.1) ������ �� ����������� - ���� �� ������������ � ���� ������
select dbo.Registration_request('alyona@yandex.ru', '12345', 'alyona238')

-- 1.2) ����������� ������������
exec dbo.Registration
@mail = 'alyona@yandex.ru',
@password = '12345',
@login = 'alyona238'
truncate table [User]

-- 1.3) ����������� ������������ - ���� �� ������������ � ���� ������
select dbo.Authorization_request('alyona@yandex.ru', '12345')

-- 1.4) ��������� ������ ������
exec dbo.Available_rooms

-- 1.5) ��������� ������ ���������� ��� ���������� ������������
exec dbo.Achivements_request
@mail = 'alyona@yandex.ru',
@password = '12345'

-- 1.6) �������� �������
exec dbo.Creating_room
@mail = 'alyona@yandex.ru',
@password = '12345',
@max_count_of_players = 6

-- 2.1.1) ���������� ������ � �������
exec dbo.Add_player_to_room
@mail = 'alyona@yandex.ru',
@password = '12345',
@room_ID = 1

-- 2.1.2) ��������� n ��������� ���������� (��� ����������)
exec dbo.Getting_characters
@n = 6

-- 2.1.4) ���������� ���������� ��������� � ������
exec dbo.Add_character_to_player
@player_ID = 1,
@characters_ID = 1

-- 2.1.5) ���������� ���� � ������
exec dbo.Add_role_to_player
@player_ID = 1,
@roles_ID = 1

-- 2.1.7) ��������� ID ������������ �� ��� ����� � ������
exec dbo.Get_user_ID
@mail = 'alyona@yandex.ru',
@password = '12345'

-- 2.1.8) ��������� ID ������ �� ��� ����� � ������
exec dbo.Get_player_ID
@mail = 'alyona@yandex.ru',
@password = '12345'

-- 2.1.9) ��������� ������������� ���������� ������ ��������� ������
exec dbo.Get_max_lives
@player_ID = 1

-- 3.1) ��������� �������� ���� ��� ��������� ������
exec dbo.Player_turn_state
@player_ID = 1,
@state = 1

-- 3.2) �������� �� ������� �������� ����� � ������
select dbo.Check_card_availability(1, 1)

-- 3.3) �������� �� ������� �������� ����� ��������� � ������
select dbo.Check_character_availability(1, 1)

-- 3.4) �������� ����������� ���������� � ������ (����������� ���������� ����� �������� � ��������� �������� �� ������)
select dbo.Check_shoot_opportunity(1, 1)

-- 3.5) ������ ����� ������ �� ������
exec dbo.Set_card_to_player_from_Deck
@player_ID = 1,
@room_ID = 1

-- 3.6) ������ ����� ������ �� ������
exec dbo.Set_card_to_player_from_Dropping
@player_ID = 1,
@room_ID = 1

-- 3.7) ������� ����� ������ � �����
exec dbo.Send_card_to_Dropping
@card_ID = 1,
@room_ID = 1

-- 3.8) ��������� ����� ������ 1 �����
exec dbo.Lose_health
@player_ID = 1

-- 3.9) ��������� ����� ��������������� ������� ��������
exec dbo.Recovery_health
@player_ID = 1

-- 3.10) ����� ����� � ������
exec dbo.Stealing_card_from_player
@player_ID_to = 1,
@card_ID = 1

-- 3.11) ��������� ������ ����, ����������� � ���� � ������
exec dbo.Get_player_cards
@player_ID = 1

-- 3.12) ��������� ������ ������ ��� ������
exec dbo.Set_weapon
@player_ID = 1,
@name = 'volcanic',
@base_weapon = 1,
@firing_range = 1,
@endless_bang = 1

-- 3.13) ��������� ����� �� ������ ��� �������� (����������� ����� ������ � �����)
exec dbo.Get_card_for_checking
@room_ID = 1

-- 3.14) �������� �������������� ������ ������ �� n
exec dbo.Change_additional_defence_range
@player_ID = 1,
@n = 1

-- 3.15) �������� �������������� ��������� ����� ������ �� n
exec dbo.Change_additional_attack_range
@player_ID = 1,
@n = 1

-- 3.16) ��������, ���� �� � ������ �� ����� ����� � ����������� ���������
exec dbo.Check_player_name_card
@player_ID = 1,
@name = 'barrel'

-- 3.17) �������� ����� �� ������ � �������� � �� ����
exec dbo.Set_cards_to_table
@room_ID = 1

-- 3.18) �������� ����� ������
exec dbo.Passing_card_to_player
@player_ID = 1,
@card_ID = 1,
@card_location = 1

-- 3.19) �������������� ������� ����� ���� �������, ���� ��� ��������
exec dbo.Recovery_health_all_players
@room_ID = 1

-- 3.20) �������� ������� ����� �� ������ � �������� � � ������ ������
exec dbo.Set_cards_to_selection_stage
@room_ID = 1

-- 3.21) ����������� ����� � ������
exec dbo.Return_card_to_Deck
@card_ID = 1,
@room_ID = 1

-- 3.22) ������������� ���� �� ������ � ���������� �� � ������
exec dbo.Shuffle_cards_in_Dropping
@room_ID = 1

-- 3.23) ��������� �������� ���� [name] � ������� [Card] ��� �������� ID
exec dbo.Get_card_name
@card_ID = 1

-- 3.24) ��������� ��������� �������� ���� [card_location] ������� [Card] �� �������� ��������
exec dbo.Change_card_location
@card_ID = 1,
@card_location = 1