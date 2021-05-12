USE [Test_3]
GO


/*-----------------------------------------------------------------*/
/*---------------------------TABLES-------------------------------*/
/*-----------------------------------------------------------------*/


CREATE TABLE [dbo].[Player](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[weapon_ID] [int] NOT NULL,
	[player_move] [bit] NOT NULL,
	[win] [bit] NOT NULL,
	[character_ID] [int] NOT NULL,
	[role_ID] [int] NOT NULL,
	[user_ID] [int] NOT NULL,	
	[room_ID][int] NULL,
	[is_ready] [bit] NOT NULL,
	[queue] [int] NOT NULL
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
	[card_image] [bit] NOT NULL,
	[card_back] [bit] NOT NULL,
	[description][nvarchar](500) NOT NULL,
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
	[card_image] [bit] NOT NULL,
	[card_back] [bit] NOT NULL,
	[description] [nvarchar](500) NOT NULL

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
	[play_time] [time] NOT NULL,
	[count_of_players] [int] NOT NULL,
	[dropping_ID] [int] NULL,
	[deck_ID] [int] NULL,
	[max_count_of_players] [int] NOT NULL
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
	[card_image] [bit] NOT NULL,
	[card_back] [bit] NOT NULL,
	[description] [nvarchar](500) NOT NULL,
	[color] [nvarchar](50) NOT NULL,
	[suit] [nvarchar](50) NOT NULL,
	[rating] [nvarchar](50) NOT NULL

)
GO
ALTER TABLE [dbo].[Cards]
ADD CONSTRAINT [PK_Cards_ID] PRIMARY KEY CLUSTERED ([ID])
GO


/*-----------------------------------------------------------------*/
/*---------------------TABLES NOT REFLECTED -----------------------*/
/*------------------------IN THE MODEL-----------------------------*/


CREATE TABLE [dbo].[Friends_User-User](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[User1_ID] [int] NOT NULL,
	[User2_ID] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Friends_User-User]
ADD CONSTRAINT [PK_Friends_User-User_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[Invitations_User-User](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[User1_ID] [int] NOT NULL,
	[User2_ID] [int] NOT NULL,
	[room_ID] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Invitations_User-User]
ADD CONSTRAINT [PK_Invitations_User-User_ID] PRIMARY KEY CLUSTERED ([ID])
GO


CREATE TABLE [dbo].[BlackList_User-User](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[User1_ID] [int] NOT NULL,
	[User2_ID] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[BlackList_User-User]
ADD CONSTRAINT [PK_BlackList_User-User_ID] PRIMARY KEY CLUSTERED ([ID])
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


/*-----------------------------------------------------------------*/
/*--------------------------TABLES END ----------------------------*/
/*-----------------------------------------------------------------*/


/*-----------------------------------------------------------------*/
/*-----------------------FOREIGN KEYS------------------------------*/
/*-----------------------------------------------------------------*/


/*-----------------------------------------------------------------*/
/*------------------FOR TABLES NOT REFLECTED ----------------------*/
/*-----------------------IN THE MODEL------------------------------*/


ALTER TABLE [dbo].[Friends_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Friends_User-User_User1_ID] FOREIGN KEY([User1_ID])
REFERENCES [dbo].[User] ([ID])
GO


ALTER TABLE [dbo].[Friends_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Friends_User-User_User2_ID] FOREIGN KEY([User2_ID])
REFERENCES [dbo].[User] ([ID])
GO


ALTER TABLE [dbo].[Invitations_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Invitations_User-User_User1_ID] FOREIGN KEY([User1_ID])
REFERENCES [dbo].[User] ([ID])
GO


ALTER TABLE [dbo].[Invitations_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Invitations_User-User_User2_ID] FOREIGN KEY([User2_ID])
REFERENCES [dbo].[User] ([ID])
GO


ALTER TABLE [dbo].[Invitations_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Invitations_User-User_room_ID] FOREIGN KEY([room_ID])
REFERENCES [dbo].[Room] ([ID])
GO


ALTER TABLE [dbo].[BlackList_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_BlackList_User-User_User1_ID] FOREIGN KEY([User1_ID])
REFERENCES [dbo].[User] ([ID])
GO


ALTER TABLE [dbo].[BlackList_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_BlackList_User-User_User2_ID] FOREIGN KEY([User2_ID])
REFERENCES [dbo].[User] ([ID])
GO


/*-----------------------------------------------------------------*/
/*------------------------FOR ATHER TABLES-------------------------*/
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
VALUES (0);

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


/*-----------------------------------------------------------------*/
/*-------------------------TRIGGERS END----------------------------*/
/*-----------------------------------------------------------------*/


/*-----------------------------------------------------------------*/
/*---------------------------FUNCTIONS------------------------------*/
/*-----------------------------------------------------------------*/


/*-------------------------CLEAR ALL BD----------------------------*/
CREATE PROCEDURE dbo.Clear_bd
AS
BEGIN

IF OBJECT_ID ('[FK_Friends_User-User_User1_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Friends_User-User]  
DROP CONSTRAINT [FK_Friends_User-User_User1_ID]
END

IF OBJECT_ID ('[FK_Friends_User-User_User2_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Friends_User-User]  
DROP CONSTRAINT [FK_Friends_User-User_User2_ID]
END

IF OBJECT_ID ('[FK_Invitations_User-User_User1_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Invitations_User-User]  
DROP CONSTRAINT [FK_Invitations_User-User_User1_ID]
END

IF OBJECT_ID ('[FK_Invitations_User-User_User2_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Invitations_User-User]  
DROP CONSTRAINT [FK_Invitations_User-User_User2_ID]
END

IF OBJECT_ID ('[FK_Invitations_User-User_room_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Invitations_User-User]  
DROP CONSTRAINT [FK_Invitations_User-User_room_ID]
END

IF OBJECT_ID ('[FK_BlackList_User-User_User1_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[BlackList_User-User]  
DROP CONSTRAINT [FK_BlackList_User-User_User1_ID]
END

IF OBJECT_ID ('[FK_BlackList_User-User_User2_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[BlackList_User-User]  
DROP CONSTRAINT [FK_BlackList_User-User_User2_ID]
END

IF OBJECT_ID ('[FK_Player_weapon_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Player]  
DROP CONSTRAINT [FK_Player_weapon_ID]
END

IF OBJECT_ID ('[FK_Player_character_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Player]  
DROP CONSTRAINT [FK_Player_character_ID]
END

IF OBJECT_ID ('[FK_Character_characters_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Character]  
DROP CONSTRAINT [FK_Character_characters_ID]
END

IF OBJECT_ID ('[FK_Player_role_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Player]  
DROP CONSTRAINT [FK_Player_role_ID]
END

IF OBJECT_ID ('[FK_Role_roles_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Role]  
DROP CONSTRAINT [FK_Role_roles_ID]
END

IF OBJECT_ID ('[FK_Player_user_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Player]  
DROP CONSTRAINT [FK_Player_user_ID]
END

IF OBJECT_ID ('[FK_User_achievements_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[User]  
DROP CONSTRAINT [FK_User_achievements_ID]
END

IF OBJECT_ID ('[FK_Player_room_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Player] 
DROP CONSTRAINT [FK_Player_room_ID]
END

IF OBJECT_ID ('[FK_Room_dropping_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Room]  
DROP CONSTRAINT [FK_Room_dropping_ID]
END

IF OBJECT_ID ('[FK_Room_deck_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Room]  
DROP CONSTRAINT [FK_Room_deck_ID]
END

IF OBJECT_ID ('[FK_Card_player_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Card]  
DROP CONSTRAINT [FK_Card_player_ID]
END

IF OBJECT_ID ('[FK_Card_room_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Card]  
DROP CONSTRAINT [FK_Card_room_ID]
END

IF OBJECT_ID ('[FK_Card_cards_ID]') IS NOT NULL
BEGIN
ALTER TABLE [dbo].[Card]  
DROP CONSTRAINT [FK_Card_cards_ID]
END


TRUNCATE TABLE [Player]
TRUNCATE TABLE [Weapon]
TRUNCATE TABLE [Character]
TRUNCATE TABLE [Characters]
TRUNCATE TABLE [Role]
TRUNCATE TABLE [Roles]
TRUNCATE TABLE [User]
TRUNCATE TABLE [Achievements]
TRUNCATE TABLE [Room]
TRUNCATE TABLE [Dropping]
TRUNCATE TABLE [Deck]
TRUNCATE TABLE [Card]
TRUNCATE TABLE [Cards]


ALTER TABLE [dbo].[Friends_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Friends_User-User_User1_ID] FOREIGN KEY([User1_ID])
REFERENCES [dbo].[User] ([ID])

ALTER TABLE [dbo].[Friends_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Friends_User-User_User2_ID] FOREIGN KEY([User2_ID])
REFERENCES [dbo].[User] ([ID])

ALTER TABLE [dbo].[Invitations_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Invitations_User-User_User1_ID] FOREIGN KEY([User1_ID])
REFERENCES [dbo].[User] ([ID])

ALTER TABLE [dbo].[Invitations_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Invitations_User-User_User2_ID] FOREIGN KEY([User2_ID])
REFERENCES [dbo].[User] ([ID])

ALTER TABLE [dbo].[Invitations_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_Invitations_User-User_room_ID] FOREIGN KEY([room_ID])
REFERENCES [dbo].[Room] ([ID])

ALTER TABLE [dbo].[BlackList_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_BlackList_User-User_User1_ID] FOREIGN KEY([User1_ID])
REFERENCES [dbo].[User] ([ID])

ALTER TABLE [dbo].[BlackList_User-User]  
WITH CHECK ADD  CONSTRAINT [FK_BlackList_User-User_User2_ID] FOREIGN KEY([User2_ID])
REFERENCES [dbo].[User] ([ID])

ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_weapon_ID] FOREIGN KEY([weapon_ID])
REFERENCES [dbo].[Weapon] ([ID])

ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_character_ID] FOREIGN KEY([character_ID])
REFERENCES [dbo].[Character] ([ID])

ALTER TABLE [dbo].[Character]  
WITH CHECK ADD  CONSTRAINT [FK_Character_characters_ID] FOREIGN KEY([characters_ID])
REFERENCES [dbo].[Characters] ([ID])

ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_role_ID] FOREIGN KEY([role_ID])
REFERENCES [dbo].[Role] ([ID])

ALTER TABLE [dbo].[Role]  
WITH CHECK ADD  CONSTRAINT [FK_Role_roles_ID] FOREIGN KEY([roles_ID])
REFERENCES [dbo].[Roles] ([ID])

ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_user_ID] FOREIGN KEY([user_ID])
REFERENCES [dbo].[User] ([ID])

ALTER TABLE [dbo].[User]  
WITH CHECK ADD  CONSTRAINT [FK_User_achievements_ID] FOREIGN KEY([achievements_ID])
REFERENCES [dbo].[Achievements] ([ID])

ALTER TABLE [dbo].[Player] 
WITH CHECK ADD  CONSTRAINT [FK_Player_room_ID] FOREIGN KEY([room_ID])
REFERENCES [dbo].[Room] ([ID])

ALTER TABLE [dbo].[Room]  
WITH CHECK ADD  CONSTRAINT [FK_Room_dropping_ID] FOREIGN KEY([dropping_ID])
REFERENCES [dbo].[Dropping] ([ID])

ALTER TABLE [dbo].[Room]  
WITH CHECK ADD  CONSTRAINT [FK_Room_deck_ID] FOREIGN KEY([deck_ID])
REFERENCES [dbo].[Deck] ([ID])

ALTER TABLE [dbo].[Card]  
WITH CHECK ADD  CONSTRAINT [FK_Card_player_ID] FOREIGN KEY([player_ID])
REFERENCES [dbo].[Player] ([ID])

ALTER TABLE [dbo].[Card]  
WITH CHECK ADD  CONSTRAINT [FK_Card_room_ID] FOREIGN KEY([room_ID])
REFERENCES [dbo].[Room] ([ID])

ALTER TABLE [dbo].[Card]  
WITH CHECK ADD  CONSTRAINT [FK_Card_cards_ID] FOREIGN KEY([cards_ID])
REFERENCES [dbo].[Cards] ([ID])

END
GO

exec Clear_bd

/*-----------------------END CLEAR ALL BD--------------------------*/


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

IF @CheckMail IS NOT NULL AND @CheckPassword IS NOT NULL
BEGIN
SELECT @massage = 0
END

RETURN @massage
END
GO


/*--------------------END AUTHORIZATION REQUEST--------------------*/


/*--------------------AVAILABLE ROOMS REQUEST----------------------*/


CREATE PROCEDURE  dbo.Available_rooms 
AS
BEGIN

SELECT [ID] 
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

/*
CREATE PROCEDURE  dbo.Creating_room (@owner_ID int, @max_count_of_player int)
AS
BEGIN


INSERT INTO [Room] ([status], [play_time], [count_of_players], [max_count_of_players])
VALUES (1, '00:00:00', 0, @max_count_of_player)

END
GO
*/

/*----------------------END CREATING ROOM--------------------------*/
