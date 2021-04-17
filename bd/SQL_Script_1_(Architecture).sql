USE [Test_1]
GO
/*-----------------------------------------------------------------*/
/*---------------------------“¿¡À»÷€-------------------------------*/
/*-----------------------------------------------------------------*/
CREATE TABLE [dbo].[User](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[e-mail] [nvarchar](50) NOT NULL,
	[nick] [nvarchar](50) NOT NULL,
	[room_ID] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[User]
ADD CONSTRAINT [PK_User_ID] PRIMARY KEY CLUSTERED ([ID])
GO


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

CREATE TABLE [dbo].[Player](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[user_ID] [int] NOT NULL,
	[role_ID] [int] NOT NULL,
	[character_ID] [int] NOT NULL,
	[weapon_ID] [int] NOT NULL,
	[player_move] [bit] NOT NULL,
	[win] [bit] NOT NULL
)
GO
ALTER TABLE [dbo].[Player]
ADD CONSTRAINT [PK_Player_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Role](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[name] [int] NOT NULL,
	[status] [bit] NOT NULL
)
GO
ALTER TABLE [dbo].[Role]
ADD CONSTRAINT [PK_Role_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Roles](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[card_image] [bit] NOT NULL,
	[card_back] [bit] NOT NULL,
	[description] [nvarchar](500) NOT NULL

)
GO
ALTER TABLE [dbo].[Roles]
ADD CONSTRAINT [PK_Roles_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Player_Cards](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[player_ID] [int] NOT NULL,
	[card_ID] [int] NOT NULL

)
GO
ALTER TABLE [dbo].[Player_Cards]
ADD CONSTRAINT [PK_Player_Cards_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Card](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[on_the_table] [bit] NOT NULL,
	[on_the_dropping] [bit] NOT NULL,
	[dropping_order] [int] NOT NULL

)
GO
ALTER TABLE [dbo].[Card]
ADD CONSTRAINT [PK_Card_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Cards](
	[ID] [int] IDENTITY(1,1) NOT NULL,
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

CREATE TABLE [dbo].[Room](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[status] [nvarchar](50) NOT NULL,
	[play_time] [time] NOT NULL,
	[count_of_players] [int] NOT NULL,
	[owner_ID] [int] NOT NULL,
	[dropping_ID] [int] NOT NULL,
	[deck_ID] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Room]
ADD CONSTRAINT [PK_Room_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Dropping](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[count_of_cars] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Dropping]
ADD CONSTRAINT [PK_Dropping_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Deck](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[count_of_cars] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Deck]
ADD CONSTRAINT [PK_Deck_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Character](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](50) NOT NULL,
	[alive] [bit] NOT NULL,
	[lives][int] NOT NULL

)
GO
ALTER TABLE [dbo].[Character]
ADD CONSTRAINT [PK_Character_ID] PRIMARY KEY CLUSTERED ([ID])
GO

CREATE TABLE [dbo].[Characters](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[card_image] [bit] NOT NULL,
	[caed_back] [bit] NOT NULL,
	[description][nvarchar](500) NOT NULL,
	[max_lives] [int] NOT NULL
)
GO
ALTER TABLE [dbo].[Characters]
ADD CONSTRAINT [PK_Characters_ID] PRIMARY KEY CLUSTERED ([ID])
GO

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
/*-----------------------¬Õ≈ÿÕ»≈  Àﬁ◊»-----------------------------*/
/*-----------------------------------------------------------------*/



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

ALTER TABLE [dbo].[User]  
WITH CHECK ADD  CONSTRAINT [FK_User_room_ID] FOREIGN KEY([room_ID])
REFERENCES [dbo].[Room] ([ID])
GO

ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_weapon_ID] FOREIGN KEY([weapon_ID])
REFERENCES [dbo].[Weapon] ([ID])
GO

ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_user_ID] FOREIGN KEY([user_ID])
REFERENCES [dbo].[User] ([ID])
GO

ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_role_ID] FOREIGN KEY([role_ID])
REFERENCES [dbo].[Role] ([ID])
GO

ALTER TABLE [dbo].[Player]  
WITH CHECK ADD  CONSTRAINT [FK_Player_character_ID] FOREIGN KEY([character_ID])
REFERENCES [dbo].[Character] ([ID])
GO

ALTER TABLE [dbo].[Role]  
WITH CHECK ADD  CONSTRAINT [FK_Role_ID] FOREIGN KEY([ID])
REFERENCES [dbo].[Roles] ([ID])
GO

ALTER TABLE [dbo].[Player_Cards]  
WITH CHECK ADD  CONSTRAINT [FK_Player_Cards_player_ID] FOREIGN KEY([player_ID])
REFERENCES [dbo].[Player] ([ID])
GO

ALTER TABLE [dbo].[Player_Cards]  
WITH CHECK ADD  CONSTRAINT [FK_Player_Cards_card_ID] FOREIGN KEY([card_ID])
REFERENCES [dbo].[Card] ([ID])
GO

ALTER TABLE [dbo].[Card]  
WITH CHECK ADD  CONSTRAINT [FK_Card_ID] FOREIGN KEY([ID])
REFERENCES [dbo].[Cards] ([ID])
GO

ALTER TABLE [dbo].[Room]  
WITH CHECK ADD  CONSTRAINT [FK_Room_owner_ID] FOREIGN KEY([owner_ID])
REFERENCES [dbo].[User] ([ID])
GO

ALTER TABLE [dbo].[Room]  
WITH CHECK ADD  CONSTRAINT [FK_Room_dropping_ID] FOREIGN KEY([dropping_ID])
REFERENCES [dbo].[Dropping] ([ID])
GO

ALTER TABLE [dbo].[Room]  
WITH CHECK ADD  CONSTRAINT [FK_Room_deck_ID] FOREIGN KEY([deck_ID])
REFERENCES [dbo].[Deck] ([ID])
GO

ALTER TABLE [dbo].[Character]  
WITH CHECK ADD  CONSTRAINT [FK_Character_ID] FOREIGN KEY([ID])
REFERENCES [dbo].[Characters] ([ID])
GO


ALTER TABLE [dbo].[Friends_User-User]   
DROP CONSTRAINT [FK_Friends_User-User_User2_ID];   
GO  

/*-----------------------------------------------------------------*/
/*--------------------------- ÓÌÂˆ-------------------------------*/
/*-----------------------------------------------------------------*/
