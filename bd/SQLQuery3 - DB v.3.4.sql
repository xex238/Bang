/*-----------------------------------------------------------------*/
/*---------------------------TABLES-------------------------------*/
/*-----------------------------------------------------------------*/


CREATE TABLE [dbo].[Player](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[weapon_ID] [int] NULL,
	[player_move] [bit] NOT NULL,
	[win] [bit] NOT NULL,
	[character_ID] [int] NULL,
	[role_ID] [int] NULL,
	[user_ID] [int] NULL,	
	[room_ID][int] NULL,
	[is_ready] [bit] NOT NULL,
	[queue] [int] NULL,
	[additional_attack_range] [int] NOT NULL,
	[additional_defence_range] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Player]
ADD CONSTRAINT [PK_Player_ID] PRIMARY KEY CLUSTERED ([ID])
GO

 
CREATE TABLE [dbo].[Weapon](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[base_weapon] [bit] NOT NULL,
	[bang_player] [bit] NOT NULL,
	[firing_range] [int] NOT NULL,
	[endless_bang] [bit] NOT NULL
)
GO
ALTER TABLE [dbo].[Weapon]
ADD CONSTRAINT [PK_Weapon_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Character](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[characters_ID] [int] NOT NULL,
	[alive] [bit] NOT NULL,
	[lives][int] NOT NULL

)
GO
ALTER TABLE [dbo].[Character]
ADD CONSTRAINT [PK_Character_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Characters](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[card_image] [bit] NULL,
	[card_back] [bit] NULL,
	[description][nvarchar](500) NULL,
	[max_lives] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Characters]
ADD CONSTRAINT [PK_Characters_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Role](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[roles_ID] [int] NOT NULL,
	[status] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Role]
ADD CONSTRAINT [PK_Role_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Roles](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[card_image] [bit] NULL,
	[card_back] [bit] NULL,
	[description] [nvarchar](500) NULL

)
GO
ALTER TABLE [dbo].[Roles]
ADD CONSTRAINT [PK_Roles_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[User](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[e-mail] [nvarchar](50) NOT NULL,
	[password] [nvarchar](50) NOT NULL,
	[nick] [nvarchar](50) NOT NULL,
	[achievements_ID] [int] NULL
)
GO
ALTER TABLE [dbo].[User]
ADD CONSTRAINT [PK_User_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Achievements](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[single_player_finished] [int] NOT NULL,
	[single_player_unfinished] [int] NOT NULL,
	[single_player_wins] [int] NOT NULL,
	[single_player_defeats] [int] NOT NULL,
	[single_player_wins_percentage] [real] NULL,	
	[multi_player_finished] [int] NOT NULL,
	[multi_player_wins] [int] NOT NULL,
	[multi_player_defeats] [int] NOT NULL,
	[multi_player_wins_percentage] [real] NULL
)
GO
ALTER TABLE [dbo].[Achievements]
ADD CONSTRAINT [PK_Achievements_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Room](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[status] [int] NOT NULL,
	[play_time] [time] NULL,
	[count_of_players] [int] NOT NULL,
	[dropping_ID] [int] NULL,
	[deck_ID] [int] NULL,
	[max_count_of_players] [int] NOT NULL,
	[owner_ID] [int] NULL
)
GO
ALTER TABLE [dbo].[Room]
ADD CONSTRAINT [PK_Room_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Dropping](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[count_of_cards] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Dropping]
ADD CONSTRAINT [PK_Dropping_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Deck](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[count_of_cards] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Deck]
ADD CONSTRAINT [PK_Deck_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Card](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[cards_ID] [int] NOT NULL,
	[player_ID] [int] NULL,
	[room_ID] [int] NOT NULL,
	[card_location] [int] NOT NULL,
	[index_number] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Card]
ADD CONSTRAINT [PK_Card_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Cards](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[card_image] [bit] NULL,
	[card_back] [bit] NULL,
	[description] [nvarchar](500) NULL,
	[color] [nvarchar](50) NOT NULL,
	[suit] [nvarchar](50) NOT NULL,
	[rating] [nvarchar](50) NOT NULL

)
GO
ALTER TABLE [dbo].[Cards]
ADD CONSTRAINT [PK_Cards_ID] PRIMARY KEY CLUSTERED ([ID])
GO


/*-----------------------------------------------------------------*/
/*---------------------TABLES WITHOUT LINKS -----------------------*/
/*-----------------------------------------------------------------*/


CREATE TABLE [dbo].[Lives](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[image] [bit] NOT NULL
)

GO
ALTER TABLE [dbo].[Lives]
ADD CONSTRAINT [PK_Lives_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Rules](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[image] [bit] NOT NULL
)
GO
ALTER TABLE [dbo].[Rules]
ADD CONSTRAINT [PK_Rules_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Tablet](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[image] [bit] NOT NULL
)
GO
ALTER TABLE [dbo].[Tablet]
ADD CONSTRAINT [PK_Tablet_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Reference](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[image] [bit] NOT NULL
)
GO
ALTER TABLE [dbo].[Reference]
ADD CONSTRAINT [PK_Reference_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Players_range](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[player_out_ID] [int] NOT NULL,
	[player_in_ID] [int] NOT NULL,
	[range] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Players_range]
ADD CONSTRAINT [PK_Players_range_ID] PRIMARY KEY CLUSTERED ([ID])
GO

/*-----------------------------------------------------------------*/
/*--------------------------TABLES END ----------------------------*/
/*-----------------------------------------------------------------*/


/*-----------------------------------------------------------------*/
/*-----------------------FOREIGN KEYS------------------------------*/
/*-----------------------------------------------------------------*/


ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_weapon_ID] FOREIGN KEY([weapon_ID])
REFERENCES [dbo].[Weapon] ([ID])
GO


ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_character_ID] FOREIGN KEY([character_ID])
REFERENCES [dbo].[Character] ([ID])
GO


ALTER TABLE [dbo].[Character]  
WITH CHECK ADD  CONSTRAINT [FK_Character_characters_ID] FOREIGN KEY([characters_ID])
REFERENCES [dbo].[Characters] ([ID])
GO


ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_role_ID] FOREIGN KEY([role_ID])
REFERENCES [dbo].[Role] ([ID])
GO


ALTER TABLE [dbo].[Role]  
WITH CHECK ADD  CONSTRAINT [FK_Role_roles_ID] FOREIGN KEY([roles_ID])
REFERENCES [dbo].[Roles] ([ID])
GO


ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_user_ID] FOREIGN KEY([user_ID])
REFERENCES [dbo].[User] ([ID])
GO


ALTER TABLE [dbo].[User]  
WITH CHECK ADD  CONSTRAINT [FK_User_achievements_ID] FOREIGN KEY([achievements_ID])
REFERENCES [dbo].[Achievements] ([ID])
GO


ALTER TABLE [dbo].[Player] 
WITH CHECK ADD  CONSTRAINT [FK_Player_room_ID] FOREIGN KEY([room_ID])
REFERENCES [dbo].[Room] ([ID])
GO


ALTER TABLE [dbo].[Room]  
WITH CHECK ADD  CONSTRAINT [FK_Room_dropping_ID] FOREIGN KEY([dropping_ID])
REFERENCES [dbo].[Dropping] ([ID])
GO


ALTER TABLE [dbo].[Room]  
WITH CHECK ADD  CONSTRAINT [FK_Room_deck_ID] FOREIGN KEY([deck_ID])
REFERENCES [dbo].[Deck] ([ID])
GO


ALTER TABLE [dbo].[Card]  
WITH CHECK ADD  CONSTRAINT [FK_Card_player_ID] FOREIGN KEY([player_ID])
REFERENCES [dbo].[Player] ([ID])
GO


ALTER TABLE [dbo].[Card]  
WITH CHECK ADD  CONSTRAINT [FK_Card_room_ID] FOREIGN KEY([room_ID])
REFERENCES [dbo].[Room] ([ID])
GO


ALTER TABLE [dbo].[Card]  
WITH CHECK ADD  CONSTRAINT [FK_Card_cards_ID] FOREIGN KEY([cards_ID])
REFERENCES [dbo].[Cards] ([ID])
GO


/*-----------------------------------------------------------------*/
/*-----------------------FOREIGN KEYS END--------------------------*/
/*-----------------------------------------------------------------*/


/*-----------------------------------------------------------------*/
/*---------------------------TRIGGERS------------------------------*/
/*-----------------------------------------------------------------*/


/*---------------------------TRIGGER_1------------------------------*/


/* Write a trigger for creating achievements when creating a user and linking it to the User table */
CREATE TRIGGER [dbo].[Create user achievements]
ON [dbo].[User]
AFTER INSERT
AS
BEGIN
INSERT INTO [Achievements] ([single_player_finished], [single_player_unfinished], [single_player_wins], [single_player_defeats], [multi_player_finished], [multi_player_wins], [multi_player_defeats])
VALUES (0,0,0,0,0,0,0);

declare @achievements_ID [int] = IDENT_CURRENT('Achievements')  

BEGIN
UPDATE [User]
SET [achievements_ID]  = @achievements_ID where ID = IDENT_CURRENT('User')  
END
END
GO


/*---------------------------TRIGGER_2------------------------------*/


/* Write a trigger to create records in the "Dropping" and "Deck" tables when creating a Room */
CREATE TRIGGER [dbo].[Create Dropping and Deck default record]
ON [dbo].[Room]
AFTER INSERT
AS
BEGIN
INSERT INTO [Dropping] ([count_of_cards])
VALUES (0);
INSERT INTO [Deck] ([count_of_cards])
VALUES (80);

declare @Dropping_ID [int] = IDENT_CURRENT('Dropping')
declare @Deck_ID [int] = IDENT_CURRENT('Deck')  

BEGIN
UPDATE [Room]
SET [dropping_ID]  = @Dropping_ID where ID = IDENT_CURRENT('Room')
UPDATE [Room]
SET [Deck_ID]  = @Deck_ID where ID = IDENT_CURRENT('Room')  
END

END
GO


/*---------------------------TRIGGER_3------------------------------*/


-- Cоздание записи в таблице [Weapon] при создании игрока [Player]
CREATE TRIGGER [dbo].[Create weapon]
ON [dbo].[Player]
AFTER INSERT
AS
BEGIN
-- Запоминаем ID комнаты
--declare @Player_ID [int] = SCOPE_IDENTITY()
declare @Player_ID [int] = (select ID from inserted)
-- Создаём заапись в таблице [Weapon]
INSERT INTO [Weapon] ([name], [base_weapon], [bang_player], [firing_range], [endless_bang])
VALUES ('colt', 1, 0, 1, 0)
-- Запоминаем ID добавленной записи в таблицу [Weapon]
declare @Weapon_ID [int] = SCOPE_IDENTITY()
-- Добавляем вторичный ключ в запись таблицы [Player] на запись в таблице [Weapon]
update [Player]
set [weapon_ID] = @Weapon_ID
where [ID] = @Player_ID
END
GO


/*---------------------------TRIGGER_4------------------------------*/


-- Копирование данных из таблицы [Cards] в таблицу [Card]
CREATE TRIGGER [dbo].[Duplicate cards]
ON [dbo].[Room]
AFTER INSERT
AS
BEGIN
WITH Series(a, b) AS
(
 SELECT 1, cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
 UNION ALL
 SELECT a+1, cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
 FROM Series
 WHERE a < 80
)
INSERT INTO [Card] ([cards_ID], [room_ID], [card_location], [index_number])
select Cards_.ID, [inserted].[ID], 2, Series_.a 
from  [inserted], (
  select [ID], row_number()over(order by [ID]) npp
  from Cards
  )Cards_
left join(
  select a, row_number()over(order by [b]) npp
  from Series
  )Series_ on Series_.npp=Cards_.npp
END
GO
/*-----------------------------------------------------------------*/
/*-------------------------TRIGGERS END----------------------------*/
/*-----------------------------------------------------------------*/


/*-----------------------------------------------------------------*/
/*---------------------------FUNCTIONS------------------------------*/
/*-----------------------------------------------------------------*/


/*---------------------REGISTRATION REQUEST------------------------*/


CREATE FUNCTION  dbo.Registration_request (@mail nvarchar(50), @password nvarchar(50), @login nvarchar(50))
RETURNS INT 
AS
BEGIN

DECLARE @Code int
SELECT @Code = 0

DECLARE @CheckMail nvarchar(50) 
SELECT @CheckMail = [e-mail]
FROM dbo.[User]
WHERE [e-mail] = @mail
IF @CheckMail IS NOT NULL
BEGIN
SELECT @Code = 2
END

DECLARE @CheckNick nvarchar(50) 
SELECT @CheckNick = [nick]
FROM dbo.[User]
WHERE [nick] = @login
IF @CheckNick IS NOT NULL
BEGIN
SELECT @Code = 1
END

RETURN @Code
END
GO


/*-------------------END REGISTRATION REQUEST----------------------*/


/*-------------------------REGISTRATION----------------------------*/


CREATE PROCEDURE  dbo.Registration (@mail nvarchar(50), @password nvarchar(50), @login nvarchar(50))
AS
BEGIN

DECLARE @message int = 0
INSERT INTO [User] ([e-mail], [password], [nick])
VALUES (@mail, @password, @login)
RETURN @message

END


/*-----------------------END REGISTRATION--------------------------*/


/*--------------------AUTHORIZATION REQUEST------------------------*/


CREATE FUNCTION  dbo.Authorization_request (@mail nvarchar(50), @password nvarchar(50))
RETURNS INT 
AS
BEGIN

DECLARE @message int = 1

DECLARE @CheckMail nvarchar(50) 
SELECT @CheckMail = [e-mail]
FROM dbo.[User]
WHERE [e-mail] = @mail

DECLARE @CheckPassword nvarchar(50) 
SELECT @CheckPassword = [password]
FROM dbo.[User]
WHERE [password] = @password

IF @CheckMail IS NOT NULL AND @CheckPassword IS NOT NULL
BEGIN
SELECT @message = 0
END

RETURN @message
END
GO


/*--------------------END AUTHORIZATION REQUEST--------------------*/


/*--------------------AVAILABLE ROOMS REQUEST----------------------*/


CREATE PROCEDURE  dbo.Available_rooms 
AS
BEGIN

SELECT [ID], [count_of_players], [max_count_of_players] 
from dbo.Room
WHERE dbo.Room.status = 1 AND (dbo.Room.max_count_of_players - dbo.Room.count_of_players) > 0 

END


/*------------------END AVAILABLE ROOMS REQUEST--------------------*/


/*----------------------USER'S ACHIVEMENTS-------------------------*/


CREATE PROCEDURE  dbo.Achivements_request (@mail nvarchar(50), @password nvarchar(50))
AS
BEGIN

DECLARE @massage int
SELECT @massage = -1

DECLARE @CheckMail nvarchar(50) 
SELECT @CheckMail = [e-mail]
FROM dbo.[User]
WHERE [e-mail] = @mail

DECLARE @CheckPassword nvarchar(50) 
SELECT @CheckPassword = [password]
FROM dbo.[User]
WHERE [password] = @password

DECLARE @Aachievement_ID int

IF @CheckMail IS NOT NULL AND @CheckPassword IS NOT NULL
BEGIN
SELECT @Aachievement_ID = achievements_ID FROM [dbo].[User] WHERE [e-mail] = @mail AND password = @password 
SELECT *
FROM [Achievements]
WHERE ID = @Aachievement_ID
END

END
GO


/*--------------------END USER'S ACHIVEMENTS-----------------------*/


/*------------------------CREATING ROOM----------------------------*/


CREATE PROCEDURE  dbo.Creating_room (@owner_ID int, @max_count_of_player int)
AS
BEGIN


INSERT INTO [Room] ([status], [play_time], [count_of_players], [max_count_of_players], [owner_ID])
VALUES (1, '00:00:00', 1, @max_count_of_player, @owner_ID)

declare @Room_ID [int] = IDENT_CURRENT('Room')

BEGIN
UPDATE [Player]
set [room_ID] = @Room_ID where ID = @owner_ID
END  

END
GO


/*----------------------END CREATING ROOM--------------------------*/


/*----------------------GETTING CHARACTERS-------------------------*/


CREATE TABLE [dbo].[For_get_characters](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[cahr_ID] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[For_get_characters]
ADD CONSTRAINT [PK_For_get_characters_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE PROCEDURE  dbo.Getting_characters (@n int)
AS
BEGIN

TRUNCATE TABLE [For_get_characters]

DECLARE @count_of_characters [int] = 0
DECLARE @This_variables [int] = 0
SELECT @count_of_characters = COUNT(*) FROM [Characters]

IF @n <  @count_of_characters
BEGIN
WHILE @n > 0 
		BEGIN
		SELECT @This_variables = FLOOR(RAND()*(@count_of_characters-0)+0);
		IF NOT EXISTS(SELECT [cahr_ID] FROM [For_get_characters] WHERE [cahr_ID] = @This_variables)
			BEGIN
			INSERT INTO [For_get_characters] (cahr_ID)
			VALUES (@This_variables)
			SELECT @n = @n - 1
			END
		END
END
SELECT (cahr_ID) FROM [For_get_characters]
END
GO



/*--------------------END GETTING CHARACTERS-----------------------*/


/*-----------------ADDING CHARACTER TO PLAYER----------------------*/


CREATE PROCEDURE  dbo.Add_character_to_player (@player_ID int, @characters_ID int)
AS
BEGIN

INSERT INTO [Character] (characters_ID, alive, lives)
VALUES (@characters_ID, 1, 4)

declare @Character_ID [int] = IDENT_CURRENT('Character')

UPDATE [Player]
SET [character_ID]  = @Character_ID where ID = @player_ID

END
GO


/*-----------------END ADDING CHARACTERS TO PLAYER-----------------*/


/*--------------------ADDING ROLE TO PLAYER------------------------*/


CREATE PROCEDURE  dbo.Add_role_to_player (@player_ID int, @roles_ID int)
AS
BEGIN

INSERT INTO [Role] (roles_ID, [status])
VALUES (@roles_ID, 1)

declare @role_ID [int] = IDENT_CURRENT('Role')

UPDATE [Player]
SET [role_ID]  = @role_ID where ID = @player_ID

END
GO


/*------------------END ADDING ROLE TO PLAYER----------------------*/


/*----------------GETTING START CARDS TO PLAYER--------------------*/


CREATE PROCEDURE  dbo.Get_start_cards_to_player (@player_ID int, @room_ID int)
AS
BEGIN
DECLARE @Card_id int
SELECT @Card_id = ID FROM [Card] WHERE (card_location = 2 AND room_ID = @room_ID AND index_number = (select max (index_number) from [Card]))

UPDATE [Card]
SET [player_ID] = @player_ID WHERE ID = @Card_id

END
GO


/*--------------END GETTING START CARDS TO PLAYER------------------*/