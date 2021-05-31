-- Базовые данные
INSERT INTO [Cards] ([ID], [name], [color], [suit], [rating])
VALUES
(1,	'bang', 'Br', 'C', '5'),
(2,	'bang',	'Br', 'C', '7'),
(3, 'bang', 'Br', 'D', '7'),
(4, 'scope', 'Bl', 'S', 'A'),
(5, 'barrel', 'Bl', 'S', 'K'),
(6, 'general_store', 'Br', 'C', '9'),
(7, 'missed', 'Br', 'S', '6'),
(8, 'bang', 'Br', 'D', 'K'),
(9, 'missed', 'Br', 'S', '3'),
(10, 'volcanic', 'Bl', 'S', '10'),
(11, 'stagecoach', 'Br', 'S', '9'),
(12, 'saloon', 'Br', 'H', '5'),
(13, 'schofield', 'Bl', 'S', 'K'),
(14, 'bang', 'Br', 'C', '2'),
(15, 'missed', 'Br', 'S', '5'),
(16, 'missed', 'Br', 'C', '10'),
(17, 'remington', 'Bl', 'C', 'K'),
(18, 'cat_balou', 'Br', 'D', '9'),
(19, 'bang', 'Br', 'D', '8'),
(20, 'bang', 'Br', 'D', '5'),
(21, 'bang', 'Br', 'C', '6'),
(22, 'cat_balou', 'Br', 'D', 'J'),
(23, 'gatling', 'Br', 'H', '10'),
(24, 'schofield', 'Bl', 'C', 'J'),
(25, 'beer', 'Br', 'H', '7'),
(26, 'dynamite', 'Bl', 'H', '2'),
(27, 'missed', 'Br', 'S', '4'),
(28, 'bang', 'Br', 'D', '2'),
(29, 'schofield', 'Br', 'C', 'Q'),
(30, 'cat_balou', 'Br', 'D', '10'),
(31, 'volcanic', 'Bl', 'C', '10'),
(32, 'bang', 'Br', 'C', '4'),
(33, 'bang', 'Br', 'D', 'Q'),
(34, 'panic', 'Br', 'H', 'A'),
(35, 'bang', 'Br', 'D', '4'),
(36, 'bang', 'Br', 'C', '3'),
(37, 'bang', 'Br', 'H', 'K'),
(38, 'mustang', 'Bl', 'H', '9'),
(39, 'bang', 'Br', 'D', '9'),
(40, 'missed', 'Br', 'C', 'J'),
(41, 'bang', 'Br', 'D', '6'),
(42, 'beer', 'Br', 'H', 'J'),
(43, 'panic', 'Br', 'D', '8'),
(44, 'bang', 'Br', 'C', '9'),
(45, 'duel', 'Br', 'D', 'Q'),
(46, 'bang', 'Br', 'S', 'A'),
(47, 'barrel', 'Bl', 'S', 'Q'),
(48, 'panic', 'Br', 'H', 'Q'),
(49, 'bang', 'Br', 'D', 'A'),
(50, 'wells_fargo', 'Br', 'H', '3'),
(51, 'stagecoach', 'Br', 'S', '9'),
(52, 'duel', 'Br', 'C', '8'),
(53, 'beer', 'Br', 'h', '6'),
(54, 'missed', 'Br', 'S', '8'),
(55, 'indians', 'Br', 'D', 'A'),
(56, 'panic', 'Br', 'H', 'J'),
(57, 'missed', 'Br', 'C', 'A'),
(58, 'bang', 'Br', 'D', 'J'),
(59, 'indians', 'Br', 'D', 'K'),
(60, 'bang', 'Br', 'H', 'Q'),
(61, 'bang', 'Br', 'D', '3'),
(62, 'winchester', 'Bl', 'S', '8'),
(63, 'rev_carabine', 'Bl', 'C', 'A'),
(64, 'beer', 'Br', 'H', '10'),
(65, 'jail', 'Bl', 'H', '4'),
(66, 'duel', 'Br', 'S', 'J'),
(67, 'bang', 'Br', 'C', '8'),
(68, 'general_store', 'Br', 'S', 'Q'),
(69, 'missed', 'Br', 'C', 'Q'),
(70, 'bang', 'Br', 'D', '10'),
(71, 'missed', 'Br', 'S', '7'),
(72, 'missed', 'Br', 'C', 'K'),
(73, 'cat_balou', 'Br', 'H', 'K'),
(74, 'bang', 'Br', 'H', 'A'),
(75, 'mustang', 'Bl', 'H', '8'),
(76, 'missed', 'Br', 'S', '2'),
(77, 'jail', 'Bl', 'S', '10'),
(78, 'jail', 'Bl', 'S', 'J'),
(79, 'beer', 'Br', 'H', '9'),
(80, 'beer', 'Br', 'H', '8')

INSERT INTO [Characters] ([ID], [name], [max_lives])
VALUES
(1, 'bart_cassidy', 4),
(2, 'black_jack', 4),
(3, 'calamity_janet', 4),
(4, 'el_gringo', 3),
(5, 'jesse_jones', 4),
(6, 'jourdonnais', 4),
(7, 'kit_carison', 4),
(8, 'lucky_duke', 4),
(9, 'paul_regret', 3),
(10, 'pedro_ramires', 4),
(11, 'rose_doolan', 4),
(12, 'sid_ketchum', 4),
(13, 'slab_the_killer', 4),
(14, 'suzy_lafayette', 4),
(15, 'vulture_sam', 4),
(16, 'willy_the_kid', 4)

INSERT INTO [Roles] ([ID], [name])
VALUES
(1, 'sheriff'),
(2, 'outlaw'),
(3, 'renegate'),
(4, 'deputy')

-- Тестовые данные
INSERT INTO [User] ([ID], [e-mail], [password], [nick])
VALUES
(1, 'dima040998@yandex.ru', '12345', 'xex238'),
(2, 'dima_n@gmail.ru', 'null', 'dima'),
(3, 'maryana_e@gmail.ru', 'qwerty', 'maryana'),
(4, 'saveliy_a@gmail.ru', 'qwerty12345', 'saveliy'),
(5, 'kostya_r@gmail.ru', 'qwerty', 'kostya'),
(6, 'lida_m@gmail.ru', 'secret', 'lida'),
(7, 'tanya_a@gmail.ru', 'password', 'tanya')

INSERT INTO [Room] ([ID], [status], [count_of_players], [max_count_of_players], [owner_ID])
VALUES
(1, 1, 1, 4, 1),
(2, 1, 2, 6, 5),
(3, 1, 3, 4, 7),
(4, 1, 1, 4, 2)

INSERT INTO [Role] ([ID], [roles_ID], [status])
VALUES
(1, 2, 'close'),
(2, 1, 'sheriff'),
(3, 3, 'close'),
(4, 2, 'close'),
(5, 2, 'close'),
(6, 3, 'close'),
(7, 4, 'close')

INSERT INTO [Character] ([ID], [characters_ID], [alive], [lives])
VALUES
(1, 5, 1, 3),
(2, 14, 1, 2),
(3, 2, 0, 0),
(4, 8, 1, 1),
(5, 6, 1, 4),
(6, 7, 1, 4),
(7, 10, 1, 1)

INSERT INTO [Player] ([ID], [is_ready], [additional_attack_range], [additional_defence_range], [user_ID], [role_ID], [character_ID], [room_ID])
VALUES
(1, 0, 0, 0, 1, 1, 1, 3),
(2, 0, 0, 0, 2, 2, 2, 3),
(3, 0, 0, 0, 3, 4, 4, 3),
(4, 0, 0, 0, 4, 3, 3, 1),
(5, 0, 0, 0, 5, 5, 5, 4),
(6, 0, 0, 0, 6, 6, 6, 2),
(7, 0, 0, 0, 7, 7, 7, 2)