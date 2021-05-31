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
/*-----------------------FOREIGN KEYS END--------------------------*/
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
TRUNCATE TABLE [Players_range]


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

/*
-- "Идеальный запрос"
-- 3.22) Перемешивание карт из сброса и добавление их в колоду
CREATE PROCEDURE dbo.Shuffle_cards_in_Dropping(@room_ID int)
AS
BEGIN

-- Получение количества карт в сбросе
declare @max_index_number int =
(
	select max(index_number)
	from [Card]
	where (card_location = 1) and (room_ID = @room_ID)
)
declare @counter int = 1

WITH Series(a, b) AS
(
 SELECT 1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
 UNION ALL
 SELECT a+1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
 FROM Series
 WHERE a < @max_index_number
),
Helper(cards_ID, index_number) as
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
	order by a1
)

while (@counter <= @max_index_number)
	BEGIN
		UPDATE [Card]
		SET index_number = [Helper].index_number,
		card_location = 2
		WHERE (card_location = 1) and (room_ID = @room_ID) and ([Card].cards_ID = @counter)
	END

END
GO
*/

/*-------------------SHUFFLE_CARDS-----------------------*/

CREATE TABLE [dbo].[helper_Card](
	[cards_ID] [int] NOT NULL,
	[index_number] [int] NOT NULL
)
GO

-- 3.22) Перемешивание карт из сброса и добавление их в колоду
CREATE PROCEDURE dbo.Shuffle_cards_in_Dropping(@room_ID int)
AS
BEGIN

-- Получение количества карт в сбросе
declare @max_index_number int =
(
	select max(index_number)
	from [Card]
	where (card_location = 1) and (room_ID = @room_ID)
)
declare @counter int = 1

--truncate table [helper_Card]

WITH Series(a, b) AS
(
 SELECT 1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
 UNION ALL
 SELECT a+1,  cast ( rand( cast ( newid() as varbinary(16) ) ) * 1000000 + 1 as int )
 FROM Series
 WHERE a < @max_index_number
)
insert into [helper_Card]
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
	order by a1
)

while (@counter <= @max_index_number)
	BEGIN
		UPDATE [Card]
		SET index_number = [Helper].index_number,
		card_location = 2
		WHERE (card_location = 1) and (room_ID = @room_ID) and ([Card].cards_ID = @counter)
	END

END
GO

/*-------------------END SHUFFLE_CARDS-----------------------*/