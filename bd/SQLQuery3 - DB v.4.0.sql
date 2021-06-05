/*-----------------------------------------------------------------*/
/*---------------------------TABLES-------------------------------*/
/*-----------------------------------------------------------------*/

CREATE TABLE [dbo].[Player]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[weapon_ID] [int] NULL,
	[player_move] [bit] NULL,
	[win] [bit] NULL,
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

CREATE TABLE [dbo].[Weapon]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[base_weapon] [bit] NOT NULL,
	[bang_player] [bit] NOT NULL,
	[firing_range] [int] NOT NULL,
	[endless_bang] [bit] NOT NULL,
	[weapon_card_ID] [int] NULL
)
GO
ALTER TABLE [dbo].[Weapon]
ADD CONSTRAINT [PK_Weapon_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Character]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[characters_ID] [int] NOT NULL,
	[alive] [bit] NOT NULL,
	[lives][int] NOT NULL

)
GO
ALTER TABLE [dbo].[Character]
ADD CONSTRAINT [PK_Character_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Characters]
(
	[ID] [int] NOT NULL,
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

CREATE TABLE [dbo].[Role]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[roles_ID] [int] NOT NULL,
	[status] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Role]
ADD CONSTRAINT [PK_Role_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Roles]
(
	[ID] [int] NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[card_image] [bit] NULL,
	[card_back] [bit] NULL,
	[description] [nvarchar](500) NULL

)
GO
ALTER TABLE [dbo].[Roles]
ADD CONSTRAINT [PK_Roles_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[User]
(
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

CREATE TABLE [dbo].[Achievements]
(
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

CREATE TABLE [dbo].[Room]
(
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

CREATE TABLE [dbo].[Dropping]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[count_of_cards] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Dropping]
ADD CONSTRAINT [PK_Dropping_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Deck]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[count_of_cards] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Deck]
ADD CONSTRAINT [PK_Deck_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Card]
(
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

CREATE TABLE [dbo].[Cards]
(
	[ID] [int] NOT NULL,
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

CREATE TABLE [dbo].[Players_range]
(
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

/*-----------------------------------------------------------------------------*/
/*---------------------------FUNCTIONS/PROCEDURES------------------------------*/
/*-----------------------------------------------------------------------------*/

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 1.1) ������ �� ����������� - ���� �� ������������ � ���� ������
CREATE FUNCTION dbo.Registration_request(@mail nvarchar(50), @password nvarchar(50), @login nvarchar(50))
=======
/*-----------------------------------------------------------------*/
/*---------------------------TRIGGERS------------------------------*/
/*-----------------------------------------------------------------*/


/*---------------------------TRIGGER_1------------------------------*/

-- Ñîçäàíèå çàïèñè â òàáëèöå [Achievements] ïðè ñîçäàíèè çàïèñè â òàáëèöå [User]
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

-- Ñîçäàíèå çàïèñè â òàáëèöàõ [Deck] è [Dropping] ïðè ñîçäàíèè çàïèñè â òàáëèöå [Room]
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


-- Cîçäàíèå çàïèñè â òàáëèöå [Weapon] ïðè ñîçäàíèè çàïèñè â òàáëèöå [Player]
CREATE TRIGGER [dbo].[Create weapon]
ON [dbo].[Player]
AFTER INSERT
AS
BEGIN
-- Çàïîìèíàåì ID êîìíàòû
--declare @Player_ID [int] = SCOPE_IDENTITY()
declare @Player_ID [int] = (select ID from inserted)
-- Ñîçäà¸ì çààïèñü â òàáëèöå [Weapon]
INSERT INTO [Weapon] ([name], [base_weapon], [bang_player], [firing_range], [endless_bang])
VALUES ('colt', 1, 0, 1, 0)
-- Çàïîìèíàåì ID äîáàâëåííîé çàïèñè â òàáëèöó [Weapon]
declare @Weapon_ID [int] = SCOPE_IDENTITY()
-- Äîáàâëÿåì âòîðè÷íûé êëþ÷ â çàïèñü òàáëèöû [Player] íà çàïèñü â òàáëèöå [Weapon]
update [Player]
set [weapon_ID] = @Weapon_ID
where [ID] = @Player_ID
END
GO


/*---------------------------TRIGGER_4------------------------------*/


-- Êîïèðîâàíèå äàííûõ èç òàáëèöû [Cards] â òàáëèöó [Card] ïðè ñîçäàíèè êîìíàòû
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

/*---------------------------TRIGGER_5------------------------------*/

-- 3.22) Ïåðåìåøèâàíèå êàðò èç ñáðîñà è äîáàâëåíèå èõ â êîëîäó
CREATE TRIGGER [dbo].[Shuffle_cards_in_Dropping_trigger]
ON [dbo].[Card]
AFTER UPDATE
AS
BEGIN

-- Ïîëó÷åíèå êîëè÷åñòâà êàðò â êîëîäå
declare @count_of_cards_in_Deck int = NULL
set @count_of_cards_in_Deck =
(
	select max(index_number)
	from [Card]
	where (card_location = 2) and (room_ID = (select room_ID from [inserted]))
)

if(@count_of_cards_in_Deck is NULL)
	BEGIN

		-- Ïîëó÷åíèå êîëè÷åñòâà êàðò â ñáðîñå
		declare @max_index_number int =
		(
			select max(index_number)
			from [Card]
			where (card_location = 1) and (room_ID = (select room_ID from [inserted]))
		);

		WITH Series(a, b) AS
		(
			SELECT 1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
			UNION ALL
			SELECT a+1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
			FROM Series
			WHERE a < @max_index_number
		),
		Helper(a1, a2) as
		(
			select [Series_1].a as a1, [Series_2].a as a2
			from
			(
				select a, row_number()over(order by [b]) npp
				from Series
			) Series_1
			left join
			(
				select a, row_number()over(order by [b]) npp
				from Series
			) Series_2 on Series_1.npp = Series_2.npp
		)

		UPDATE [Card_]
		SET [Card_].index_number = [Helper_].a2,
		[Card_].card_location = 2
		from [Card] as [Card_]
		join [Helper] as [Helper_]
		on [Card_].cards_ID = [Helper_].a2

	END

END
GO

/*-----------------------------------------------------------------*/
/*-------------------------TRIGGERS END----------------------------*/
/*-----------------------------------------------------------------*/


/*-----------------------------------------------------------------*/
/*---------------------------FUNCTIONS------------------------------*/
/*-----------------------------------------------------------------*/

-- 1.1)
/*---------------------REGISTRATION REQUEST------------------------*/

/*---------------------------FUNCTION 1 (1)------------------------------*/
CREATE FUNCTION  dbo.Registration_request (@mail nvarchar(50), @password nvarchar(50), @login nvarchar(50))
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
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

-- 1.2) ����������� ������������
CREATE PROCEDURE dbo.Registration(@mail nvarchar(50), @password nvarchar(50), @login nvarchar(50))
AS
BEGIN
SET NOCOUNT ON;

DECLARE @message int = 0
INSERT INTO [User] ([e-mail], [password], [nick])
VALUES (@mail, @password, @login)
RETURN @message

SET NOCOUNT OFF;
END


/*-----------------------END REGISTRATION--------------------------*/

-- 1.3)
/*--------------------AUTHORIZATION REQUEST------------------------*/

/*---------------------------FUNCTION 2 (3)------------------------------*/
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

-- 1.3) ����������� ������������ - ���� �� ������������ � ���� ������
CREATE FUNCTION dbo.Authorization_request(@mail nvarchar(50), @password nvarchar(50))
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

-- 1.4) ��������� ������ ������
CREATE PROCEDURE dbo.Available_rooms 
AS
BEGIN
SET NOCOUNT ON;

SELECT [ID], [count_of_players], [max_count_of_players] 
from dbo.Room
WHERE dbo.Room.status = 1 AND (dbo.Room.max_count_of_players - dbo.Room.count_of_players) > 0 

SET NOCOUNT OFF;
END


/*------------------END AVAILABLE ROOMS REQUEST--------------------*/

-- 1.5)
/*----------------------USER'S ACHIVEMENTS-------------------------*/


CREATE PROCEDURE  dbo.Achivements_request (@mail nvarchar(50), @password nvarchar(50))
AS
BEGIN
SET NOCOUNT ON;

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

SET NOCOUNT OFF;
END
GO

-- 1.5) ��������� ������ ���������� ��� ���������� ������������
CREATE PROCEDURE dbo.Achivements_request(@mail nvarchar(50), @password nvarchar(50))
AS
BEGIN
SET NOCOUNT ON;

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

SET NOCOUNT OFF;
END
GO

-- 1.6) �������� �������
CREATE PROCEDURE dbo.Creating_room(@mail nvarchar(50), @password nvarchar(50), @max_count_of_players int)
AS
BEGIN
SET NOCOUNT ON;

declare @owner_ID int = NULL
set @owner_ID = 
(
	select [ID]
	from [User]
	where ([User].[e-mail] = @mail) and ([User].[password] = @password)
)

INSERT INTO [Player] ([user_ID], [is_ready], [additional_attack_range], [additional_defence_range])
VALUES (@owner_ID, 0, 0, 0)

declare @player_ID int = IDENT_CURRENT('Player')

INSERT INTO [Room] ([status], [play_time], [count_of_players], [max_count_of_players], [owner_ID])
VALUES (1, '00:00:00', 1, @max_count_of_players, @player_ID)

declare @room_ID [int] = IDENT_CURRENT('Room')

UPDATE [Player]
set [room_ID] = @room_ID where ID = @player_ID

SELECT @room_ID

SET NOCOUNT OFF;
END
GO

-- 2.1.1) ���������� ������ � �������
CREATE PROCEDURE dbo.Add_player_to_room(@mail nvarchar(50), @password nvarchar(50), @room_ID int)
AS
BEGIN
SET NOCOUNT ON;

declare @user_ID int = NULL
set @user_ID = 
(
	select [ID]
	from [User]
	where ([User].[e-mail] = @mail) and ([User].[password] = @password)
)

INSERT INTO [Player] ([user_ID], [is_ready], [additional_attack_range], [additional_defence_range], [room_ID])
VALUES (@user_ID, 0, 0, 0, @room_ID)

SELECT [Room].count_of_players, [Room].max_count_of_players
FROM [Room]
WHERE ([Room].ID = @room_ID)

SET NOCOUNT OFF;
END
GO

-- 2.1.2) ��������� n ��������� ���������� (��� ����������)
CREATE TABLE [dbo].[For_get_characters]
(
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[cahr_ID] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[For_get_characters]
ADD CONSTRAINT [PK_For_get_characters_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE PROCEDURE dbo.Getting_characters(@n int)
AS
BEGIN
SET NOCOUNT ON;

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

SET NOCOUNT OFF;
END
GO

-- 2.1.4) ���������� ���������� ��������� � ������
CREATE PROCEDURE dbo.Add_character_to_player(@player_ID int, @characters_ID int)
AS
BEGIN
SET NOCOUNT ON;

INSERT INTO [Character] (characters_ID, alive, lives)
VALUES (@characters_ID, 1, 4)

declare @Character_ID [int] = IDENT_CURRENT('Character')

UPDATE [Player]
SET [character_ID]  = @Character_ID where ID = @player_ID

SET NOCOUNT OFF;
END
GO

-- 2.1.5) ���������� ���� � ������
CREATE PROCEDURE dbo.Add_role_to_player(@player_ID int, @roles_ID int)
AS
BEGIN
SET NOCOUNT ON;

INSERT INTO [Role] (roles_ID, [status])
VALUES (@roles_ID, 1)

declare @role_ID [int] = IDENT_CURRENT('Role')

UPDATE [Player]
SET [role_ID]  = @role_ID where ID = @player_ID

SET NOCOUNT OFF;
END
GO

-- 2.1.7) ��������� ID ������������ �� ��� ����� � ������
CREATE PROCEDURE dbo.Get_user_ID(@mail nvarchar(50), @password nvarchar(50))
AS
BEGIN
SET NOCOUNT ON;

SELECT [User].ID
FROM [User]
WHERE ([User].[e-mail] = @mail) and ([User].[password] = @password)

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 2.1.8) ��������� ID ������ �� ��� ����� � ������
CREATE PROCEDURE dbo.Get_player_ID(@mail nvarchar(50), @password nvarchar(50))
=======

/*--------------END GETTING START CARDS TO PLAYER------------------*/

-- 2.1.7)
/*----------------GETTING START CARDS TO PLAYER--------------------*/

CREATE PROCEDURE  dbo.Get_user_ID(@mail nvarchar(50), @password nvarchar(50))
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
AS
BEGIN
SET NOCOUNT ON;

SELECT [Player].ID
FROM [User]
join [Player]
on [Player].[user_ID] = [User].ID
WHERE ([User].[e-mail] = @mail) and ([User].[password] = @password)

SET NOCOUNT OFF;
END
GO

-- 2.1.9) ��������� ������������� ���������� ������ ��������� ������
CREATE PROCEDURE dbo.Get_max_lives(@plater_ID int)
AS
BEGIN
SET NOCOUNT ON;

select [Characters].max_lives
from [Player]
join [Character]
on [Player].character_ID = [Character].ID
join [Characters]
on [Character].characters_ID = [Characters].ID
where [Player].ID = @player_ID

SET NOCOUNT OFF;
END
GO

-- 3.1) ��������� �������� ���� ��� ��������� ������
CREATE PROCEDURE dbo.Player_turn_state(@player_ID int, @state bit)
AS
BEGIN
SET NOCOUNT ON;

UPDATE [Player]
SET [player_move] = @state WHERE ID = @player_ID

SET NOCOUNT OFF;
END
GO

-- 3.2) �������� �� ������� �������� ����� � ������
CREATE FUNCTION dbo.Check_card_availability(@player_ID int, @card_ID int)
RETURNS INT
AS
BEGIN

DECLARE @Flag int
DECLARE @Card_player int
SELECT @Card_player = player_ID from [Card] where ID = @card_ID


IF @Card_player = @player_ID
	BEGIN
	SELECT @Flag = 1
	END
ELSE
	BEGIN
	SELECT @Flag = 0
	END

RETURN @Flag
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.3) �������� �� ������� �������� ����� ��������� � ������
CREATE FUNCTION dbo.Check_character_availability(@player_ID int, @character_ID int)
=======

/*-----------END CHECK AVAILABILITY PLAYER HAVE CARD---------------*/

-- 3.3)
/*-----=-----CHECK AVAILABILITY PLAYER HAVE ÑHARACTER--------------*/


CREATE FUNCTION  dbo.Check_character_availability (@player_ID int, @character_ID int)
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
RETURNS INT
AS
BEGIN

DECLARE @Flag int
DECLARE @Character_player int
SELECT @Character_player = character_ID from [Player] where ID = @player_ID


IF @Character_player = @character_ID
	BEGIN
	SELECT @Flag = 1
	END
ELSE
	BEGIN
	SELECT @Flag = 0
	END

RETURN @Flag
END
GO

-- 3.4) �������� ����������� ���������� � ������ (����������� ���������� ����� �������� � ��������� �������� �� ������)
CREATE FUNCTION dbo.Check_shoot_opportunity(@player_ID int, @target_ID int)
RETURNS INT
AS
BEGIN

DECLARE @Flag int

DECLARE @firing_range int

SELECT @firing_range = [firing_range] FROM [Weapon] WHERE [ID] = (SELECT [weapon_ID] FROM [Player] WHERE [ID] = @player_ID)
SELECT @firing_range = @firing_range + [additional_attack_range] FROM [Player] WHERE ID = @player_ID


DECLARE @range int
SELECT @range = [range] FROM [Players_range] WHERE [player_in_ID] = @player_ID AND [player_out_ID] = @target_ID

DECLARE @defence_range int

SELECT @defence_range = [additional_defence_range] FROM [Player] WHERE [ID] = @target_ID
SELECT @defence_range = @defence_range + @range


IF @firing_range = @defence_range
	BEGIN
	SELECT @Flag = 1
	END
ELSE
	BEGIN
	SELECT @Flag = 0
	END

RETURN @Flag
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.5) ������ ����� ������ �� ������
=======

/*-----------------END CHECK SHOOT OPPORTUNITY---------------------*/

-- 3.5) Âûäà÷à êàðòû èãðîêó èç êîëîäû
/*-------------------SET_CARD_TO_PLAYER_FROM_DECK-----------------------*/


>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Set_card_to_player_from_Deck(@player_ID int, @room_ID int)
AS
BEGIN
SET NOCOUNT ON;

declare @card_ID int =
(
	select [Card].ID
	from [Card]
	where (card_location = 2) and (room_ID = @room_ID) and (index_number = 
	(
		select max(index_number)
		from [Card]
		where (card_location = 2) and (room_ID = @room_ID)
	))
)

UPDATE [Card]
SET player_ID = @player_ID,
card_location = 3
WHERE [Card].ID = @card_ID

SELECT @card_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.6) ������ ����� ������ �� ������
=======
/*-------------------END SET_CARD_TO_PLAYER_FROM_DECK-----------------------*/

/*-------------------SET_CARD_TO_PLAYER_FROM_DROPPING-----------------------*/
-- 3.6) Âûäà÷à êàðòû èãðîêó èç ñáðîñà
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Set_card_to_player_from_Dropping(@player_ID int, @room_ID int)
AS
BEGIN
SET NOCOUNT ON;

declare @card_ID int =
(
	select [Card].ID
	from [Card]
	where (card_location = 1) and (room_ID = @room_ID) and (index_number = 
	(
		select max(index_number)
		from [Card]
		where (card_location = 1) and (room_ID = @room_ID)
	))
)

SELECT @card_ID

UPDATE [Card]
SET player_ID = @player_ID,
card_location = 3
WHERE [Card].ID = @card_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.7) ������� ����� ������ � �����
=======
/*-------------------END SET_CARD_TO_PLAYER_FROM_DROPPING-----------------------*/

/*-------------------SEND_CARD_TO_DROPPING-----------------------*/

-- 3.7) Ïåðåõîä êàðòû èãðîêà â ñáðîñ
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Send_card_to_Dropping(@card_ID int, @room_ID int)
AS
BEGIN
SET NOCOUNT ON;

UPDATE [Card]
SET player_ID = NULL,
card_location = 1,
index_number =
(
	select max([Card].index_number) + 1
	from [Card]
	where (card_location = 1) and (room_ID = @room_ID)
)
WHERE [Card].ID = @card_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.8) ��������� ����� ������ 1 �����
=======
/*-------------------END SEND_CARD_TO_DROPPING-----------------------*/

/*-------------------LOSE_HEALTH-----------------------*/

-- 3.8) Âûáðàííûé èãðîê òåðÿåò 1 æèçíü
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Lose_health(@player_ID int)
AS
BEGIN
SET NOCOUNT ON;

declare @code int = 0
declare @lives int =
(
	select [Character].lives
	from [Player]
	join [Character]
	on [Player].character_ID = [Character].ID
	where [Player].ID = @player_ID
)

UPDATE [Character]
SET lives = lives - 1
WHERE ID =
(
	select [Character].ID
	from [Player]
	join [Character]
	on [Player].character_ID = [Character].ID
	where [Player].ID = @player_ID
)

if(@lives - 1 = 0)
	BEGIN
		UPDATE [Character]
		SET alive = 0
		WHERE ID =
		(
			select [Character].ID
			from [Player]
			join [Character]
			on [Player].character_ID = [Character].ID
			where [Player].ID = @player_ID
		)

		SET @code = 10
	END

select @code

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.9) ��������� ����� ��������������� ������� ��������
=======
/*-------------------END LOSE_HEALTH-----------------------*/

/*-------------------RECOVERY_HEALTH-----------------------*/

-- 3.9) Âûáðàííûé èãðîê âîññòàíàâëèâàåò åäèíèöó çäîðîâüÿ
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Recovery_health(@player_ID int)
AS
BEGIN
SET NOCOUNT ON;

declare @code int = 1
declare @max_lives int = 
(
	select [Characters].max_lives
	from [Player]
	join [Character]
	on [Player].character_ID = [Character].ID
	join [Characters]
	on [Character].characters_ID = [Characters].ID
	where [Player].ID = @player_ID
)
declare @lives int =
(
	select [Character].lives
	from [Player]
	join [Character]
	on [Player].character_ID = [Character].ID
	where ([Player].ID = @player_ID) and ([Character].alive = 1)
)

if(@lives < @max_lives)
	BEGIN
		UPDATE [Character]
		SET lives = lives + 1
		where ID = 
		(
			select [Character].ID
			from [Player]
			join [Character]
			on [Player].character_ID = [Character].ID
			where [Player].ID = @player_ID
		)

		SET @code = 0
	END

SELECT @code

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.10) ����� ����� � ������
CREATE PROCEDURE dbo.Stealing_card_from_player(@player_ID_to int, @card_ID int)
=======
/*-------------------END RECOVERY_HEALTH-----------------------*/

/*-------------------STEALING_CARD_FROM_PLAYER-----------------------*/

-- 3.10) Êðàæà êàðòû ó èãðîêà
CREATE PROCEDURE dbo.Stealing_card_from_player(@player_ID_from int, @player_ID_to int, @card_ID int)
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
AS
BEGIN
SET NOCOUNT ON;

UPDATE [Card]
SET player_ID = @player_ID_to,
card_location = 3
WHERE ID = @card_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.11) ��������� ������ ����, ����������� � ���� � ������
=======
/*-------------------END STEALING_CARD_FROM_PLAYER-----------------------*/

/*-------------------GET_PLAYER_CARDS-----------------------*/

-- 3.11) Ïîëó÷åíèå ñïèñêà êàðò, íàõîäÿùèõñÿ â ðóêå ó èãðîêà
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Get_player_cards(@player_ID int)
AS
BEGIN
SET NOCOUNT ON;

SELECT [Card].ID
FROM [Card]
join [Player]
on [Card].player_ID = [Player].ID
where ([Player].ID = @player_ID) and ([Card].card_location = 3)

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.12) ��������� ������ ������ ��� ������
CREATE PROCEDURE dbo.Set_weapon(@player_ID int, @name nvarchar(50), @base_weapon bit, @firing_range int, @endless_bang bit, @weapon_card_ID int, @room_ID int)
=======
/*-------------------END GET_PLAYER_CARDS-----------------------*/

/*-------------------GET_WEAPON-----------------------*/

-- 3.12) Óñòàíîâêà íîâîãî îðóæèÿ äëÿ èãðîêà
CREATE PROCEDURE dbo.Get_weapon(@player_ID int, @name nvarchar(50), @base_weapon bit, @firing_range int, @endless_bang bit)
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
AS
BEGIN
SET NOCOUNT ON;

declare @old_weapon_card_ID int = NULL
set @old_weapon_card_ID =
(
	select [Weapon].[weapon_card_ID]
	from [Player]
	join [Weapon]
	on [Player].weapon_ID = [Weapon].ID
	where [Player].ID = @player_ID
)

if(@old_weapon_card_ID IS NOT NULL)
	BEGIN

		exec dbo.Send_card_to_Dropping
		@card_ID = @old_weapon_card_ID,
		@room_ID = @room_ID

	END

UPDATE Weapon
SET [name] = @name,
[base_weapon] = @base_weapon,
[firing_range] = @firing_range,
[endless_bang] = @endless_bang,
[weapon_card_ID] = @weapon_card_ID
WHERE ID = 
(
	select [Weapon].ID
	from [Weapon]
	join [Player]
	on [Player].weapon_ID = [Weapon].ID
	where [Player].ID = @player_ID
)

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.13) ��������� ����� �� ������ ��� �������� (����������� ����� ������ � �����)
=======
/*-------------------END GET_WEAPON-----------------------*/

/*-------------------GET_CARD_FOR_CHECKING-----------------------*/

-- 3.13) Ïîëó÷åíèå êàðòû èç êîëîäû äëÿ ïðîâåðêè (ïðîâåðåííàÿ êàðòà óõîäèò â ñáðîñ)
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Get_card_for_checking(@room_ID int)
AS
BEGIN
SET NOCOUNT ON;

SELECT [Card].[ID], [Cards].[ID], [suit], [rating]
FROM [Cards]
join [Card]
on [Card].cards_ID = [Cards].ID
WHERE (card_location = 2) and (room_ID = @room_ID) and (index_number = 
(
	select max(index_number)
	from [Card]
	where (card_location = 2) and (room_ID = @room_ID)
));

WITH Main_select(Card_ID, Cards_ID, suit, rating) as
(
	SELECT [Card].[ID], [Cards].[ID], [suit], [rating]
	FROM [Cards]
	join [Card]
	on [Card].cards_ID = [Cards].ID
	WHERE (card_location = 2) and (room_ID = @room_ID) and (index_number = 
	(
		select max(index_number)
		from [Card]
		where (card_location = 2) and (room_ID = @room_ID)
	))
)
UPDATE [Card]
SET card_location = 1,
index_number =
(
	select max(index_number) + 1
	from [Card]
	where (card_location = 1) and (room_ID = @room_ID)
)
where ID =
(
	select Card_ID
	from Main_select
)

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.14) �������� �������������� ������ ������ �� n
=======
/*-------------------END GET_CARD_FOR_CHECKING-----------------------*/

/*-------------------CHANGE_ADDITIONAL_DEFENCE_RANGE-----------------------*/

-- 3.14) Èçìåíèòü äîïîëíèòåëüíóþ çàùèòó èãðîêà íà n
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Change_additional_defence_range(@player_ID int, @n int)
AS
BEGIN
SET NOCOUNT ON;

UPDATE [Player]
SET additional_defence_range = additional_defence_range + @n
WHERE ID = @player_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.15) �������� �������������� ��������� ����� ������ �� n
=======
/*-------------------END CHANGE_ADDITIONAL_DEFENCE_RANGE-----------------------*/

/*-------------------CHANGE_ADDITIONAL_ATTACK_RANGE-----------------------*/

-- 3.15) Èçìåíèòü äîïîëíèòåëüíóþ äàëüíîñòü àòàêè èãðîêà íà n
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Change_additional_attack_range(@player_ID int, @n int)
AS
BEGIN
SET NOCOUNT ON;

UPDATE [Player]
SET additional_attack_range = additional_attack_range + @n
WHERE ID = @player_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.16) ��������, ���� �� � ������ �� ����� ����� � ����������� ���������
=======
/*-------------------END CHANGE_ADDITIONAL_ATTACK_RANGE-----------------------*/

/*-------------------CHECK_PLAYER_NAME_CARD-----------------------*/

-- 3.16) Ïðîâåðêà, åñòü ëè ó èãðîêà íà ñòîëå êàðòà ñ àíàëîãè÷íûì íàçâàíèåì
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Check_player_name_card(@player_ID int, @name nvarchar(50))
AS
BEGIN
SET NOCOUNT ON;

SELECT COUNT(*)
FROM [Card]
join [Cards]
on [Card].cards_ID = [Cards].ID
WHERE (player_ID = @player_ID) and (card_location = 4) and ([Cards].[name] = @name)

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.17) �������� ����� �� ������ � �������� � �� ����
=======
/*-------------------END CHECK_PLAYER_NAME_CARD-----------------------*/

/*-------------------SET_CARDS_TO_TABLE-----------------------*/

-- 3.17) Ïîëó÷èòü êàðòó èç êîëîäû è äîáàâèòü å¸ íà ñòîë
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Set_cards_to_table(@room_ID int)
AS
BEGIN
SET NOCOUNT ON;

declare @card_ID int = 
(
	select [ID]
	from [Card]
	WHERE ([index_number] =
		(
			select max(index_number)
			from [Card]
			where ([room_ID] = @room_ID) and ([card_location] = 2))
		) and
	([room_ID] = @room_ID) and ([card_location] = 2)
)

UPDATE [Card]
SET [card_location] = 5
WHERE [ID] = @card_ID

SELECT @card_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.18) �������� ����� ������
CREATE PROCEDURE dbo.Passing_card_to_player(@player_ID int, @card_ID int, @card_location int)
=======
/*-------------------END SET_CARDS_TO_TABLE-----------------------*/

/*-------------------PASSING_CARD_TO_PLAYER-----------------------*/

-- 3.18) Ïåðåäà÷à êàðòû èãðîêó
CREATE PROCEDURE dbo.Passing_card_to_player(@player_ID int, @card_ID int)
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
AS
BEGIN
SET NOCOUNT ON;

declare @result int = 0

UPDATE [Card]
SET card_location = @card_location,
player_ID = @player_ID
WHERE ID = @card_ID

SELECT @result

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.19) �������������� ������� ����� ���� �������, ���� ��� ��������
=======
/*-------------------END PASSING_CARD_TO_PLAYER-----------------------*/

/*-------------------RECOVERY_HEALTH_ALL_PLAYERS-----------------------*/

-- 3.19) Âîññòàíîâëåíèå åäèíèöû æèçíè âñåì èãðîêàì, åñëè ýòî âîçìîæíî
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Recovery_health_all_players(@room_ID int)
AS
BEGIN
SET NOCOUNT ON;

with Helper(ID) as
(
	select [Player].ID
	from [Player]
	join [Character]
	on [Player].character_ID = [Character].ID
	join [Characters]
	on [Character].characters_ID = [Characters].ID
	where ([room_ID] = @room_ID) and ([Character].alive = 1) and ([Character].lives < [Characters].max_lives)
)

UPDATE [Character]
SET [lives] = [lives] + 1
WHERE [ID] in (select * from Helper)

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.20) �������� ������� ����� �� ������ � �������� � � ������ ������
=======
/*-------------------END RECOVERY_HEALTH_ALL_PLAYERS-----------------------*/

/*-------------------SET_CARDS_TO_SELECTION_STAGE-----------------------*/

-- 3.20) Ïîëó÷èòü âåðõíþþ êàðòó èç êîëîäû è äîáàâèòü å¸ â ñòàäèþ âûáîðà
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Set_cards_to_selection_stage(@room_ID int)
AS
BEGIN
SET NOCOUNT ON;

declare @card_ID int = 
(
	select [ID]
	from [Card]
	WHERE ([index_number] =
		(
			select max(index_number)
			from [Card]
			where ([room_ID] = @room_ID) and ([card_location] = 2))
		) and
	([room_ID] = @room_ID) and ([card_location] = 2)
)

UPDATE [Card]
SET [card_location] = 6
WHERE [ID] = @card_ID

SELECT @card_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.21) ����������� ����� � ������
=======
/*-------------------END SET_CARDS_TO_SELECTION_STAGE-----------------------*/

/*-------------------RETURN_CARD_TO_DECK-----------------------*/

-- 3.21) Âîçâðàùåíèå êàðòû â êîëîäó
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Return_card_to_Deck(@card_ID int, @room_ID int)
AS
BEGIN
SET NOCOUNT ON;

declare @index_number int = NULL
set @index_number =
(
	select max(index_number) + 1
	from [Card]
	where ([room_ID] = @room_ID) and ([card_location] = 2)
)

if(@index_number is NULL)
	set @index_number = 1

UPDATE [Card]
SET [player_ID] = NULL,
[card_location] = 2,
[index_number] = @index_number
WHERE [Card].ID = @card_ID

SET NOCOUNT OFF;
END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
-- 3.22) ������������� ���� �� ������ � ���������� �� � ������
=======
/*-------------------END RETURN_CARD_TO_DECK-----------------------*/

/*-------------------SHUFFLE_CARDS-----------------------*/

-- 3.22) Ïåðåìåøèâàíèå êàðò èç ñáðîñà è äîáàâëåíèå èõ â êîëîäó
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
CREATE PROCEDURE dbo.Shuffle_cards_in_Dropping(@room_ID int)
AS
BEGIN
SET NOCOUNT ON;

-- Ïîëó÷åíèå êîëè÷åñòâà êàðò â ñáðîñå
declare @max_index_number int =
(
	select max(index_number)
	from [Card]
	where (card_location = 1) and (room_ID = @room_ID)
)

WITH Series(a, b) AS
(
	SELECT 1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
	UNION ALL
	SELECT a+1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
	FROM Series
	WHERE a < @max_index_number
),
Helper(a1, a2) as
(
	select [Series_1].a as a1, [Series_2].a as a2
	from
	(
		select a, row_number()over(order by [b]) npp
		from Series
	) Series_1
	left join
	(
		select a, row_number()over(order by [b]) npp
		from Series
	) Series_2 on Series_1.npp = Series_2.npp
)

UPDATE [Card_]
SET [Card_].index_number = [Helper_].a2,
[Card_].card_location = 2
from [Card] as [Card_]
join [Helper] as [Helper_]
on [Card_].cards_ID = [Helper_].a2

SET NOCOUNT OFF;
END
GO

-- 3.23) ��������� �������� ���� [name] � ������� [Card] ��� �������� ID
CREATE PROCEDURE dbo.Get_card_name(@card_ID int)
AS
BEGIN
SET NOCOUNT ON;

select [Card].[name]
from [Card]
where [Card].ID = @card_ID

SET NOCOUNT OFF;
END
GO

-- 3.24) ��������� ��������� �������� ���� [card_location] ������� [Card] �� �������� ��������
CREATE PROCEDURE dbo.Change_card_location(@card_ID int, @card_location int)
AS
BEGIN
SET NOCOUNT ON;

update [Card]
set card_location = @card_location
where ID = @card_ID

SET NOCOUNT OFF;
END
GO

/*-----------------------------------------------------------------*/
/*---------------------------TRIGGERS------------------------------*/
/*-----------------------------------------------------------------*/

-- 5.1) �������� ������ � ������� [Achievements] ��� �������� ������ � ������� [User]
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

-- 5.2) �������� ������ � �������� [Deck] � [Dropping] ��� �������� ������ � ������� [Room]
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

-- 5.3) C������� ������ � ������� [Weapon] ��� �������� ������ � ������� [Player]
CREATE TRIGGER [dbo].[Create weapon]
ON [dbo].[Player]
AFTER INSERT
AS
BEGIN

declare @Player_ID [int] = (select ID from inserted)

INSERT INTO [Weapon] ([name], [base_weapon], [bang_player], [firing_range], [endless_bang])
VALUES ('colt', 1, 0, 1, 0)

declare @Weapon_ID [int] = SCOPE_IDENTITY()

update [Player]
set [weapon_ID] = @Weapon_ID
where [ID] = @Player_ID

END
GO

-- 5.4) ����������� ������ �� ������� [Cards] � ������� [Card] ��� �������� �������
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

-- 5.5) ������������� ���� �� ������ � ���������� �� � ������
CREATE TRIGGER [dbo].[Shuffle_cards_in_Dropping_trigger]
ON [dbo].[Card]
AFTER UPDATE
AS
BEGIN

declare @count_of_cards_in_Deck int = NULL
set @count_of_cards_in_Deck =
(
	select max(index_number)
	from [Card]
	where (card_location = 2) and (room_ID = (select room_ID from [inserted]))
)

if(@count_of_cards_in_Deck is NULL)
	BEGIN

		declare @max_index_number int =
		(
			select max(index_number)
			from [Card]
			where (card_location = 1) and (room_ID = (select room_ID from [inserted]))
		);

		WITH Series(a, b) AS
		(
			SELECT 1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
			UNION ALL
			SELECT a+1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
			FROM Series
			WHERE a < @max_index_number
		),
		Helper(a1, a2) as
		(
			select [Series_1].a as a1, [Series_2].a as a2
			from
			(
				select a, row_number()over(order by [b]) npp
				from Series
			) Series_1
			left join
			(
				select a, row_number()over(order by [b]) npp
				from Series
			) Series_2 on Series_1.npp = Series_2.npp
		)

		UPDATE [Card_]
		SET [Card_].index_number = [Helper_].a2,
		[Card_].card_location = 2
		from [Card] as [Card_]
		join [Helper] as [Helper_]
		on [Card_].cards_ID = [Helper_].a2

	END

END
GO

<<<<<<< HEAD:bd/SQLQuery3 - DB v.4.0.sql
/*-----------------------------------------------------------------*/
/*-------------------------TRIGGERS END----------------------------*/
/*-----------------------------------------------------------------*/
=======
/*-------------------END SHUFFLE_CARDS-----------------------*/
>>>>>>> 986318605e38dd3aa14b0950c4baf888fc3b49fd:bd/SQLQuery3 - DB v.3.5.sql
