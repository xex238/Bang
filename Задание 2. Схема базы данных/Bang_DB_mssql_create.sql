CREATE TABLE [User] (
	ID integer NOT NULL UNIQUE,
	e-mail varchar NOT NULL UNIQUE,
	password varchar NOT NULL,
	nick varchar NOT NULL,
	room_ID integer NOT NULL,
  CONSTRAINT [PK_USER] PRIMARY KEY CLUSTERED
  (
  [ID] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [Friends_User-User] (
	ID integer NOT NULL,
	User1_ID integer NOT NULL,
	User2_ID integer NOT NULL,
  CONSTRAINT [PK_FRIENDS_USER-USER] PRIMARY KEY CLUSTERED
  (
  [ID] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [Room] (
	ID integer NOT NULL,
	status varchar NOT NULL,
	play_time time,
	owner_ID integer NOT NULL,
  CONSTRAINT [PK_ROOM] PRIMARY KEY CLUSTERED
  (
  [ID] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [Invitations_User-User] (
	ID integer NOT NULL,
	User1_ID integer NOT NULL,
	User2_ID integer NOT NULL,
	room_ID integer NOT NULL,
  CONSTRAINT [PK_INVITATIONS_USER-USER] PRIMARY KEY CLUSTERED
  (
  [ID] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [BlackList_User-User] (
	ID integer NOT NULL,
	User1_ID integer NOT NULL,
	User2_ID integer NOT NULL,
  CONSTRAINT [PK_BLACKLIST_USER-USER] PRIMARY KEY CLUSTERED
  (
  [ID] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
ALTER TABLE [User] WITH CHECK ADD CONSTRAINT [User_fk0] FOREIGN KEY ([room_ID]) REFERENCES [Room]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [User] CHECK CONSTRAINT [User_fk0]
GO

ALTER TABLE [Friends_User-User] WITH CHECK ADD CONSTRAINT [Friends_User-User_fk0] FOREIGN KEY ([User1_ID]) REFERENCES [User]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [Friends_User-User] CHECK CONSTRAINT [Friends_User-User_fk0]
GO
ALTER TABLE [Friends_User-User] WITH CHECK ADD CONSTRAINT [Friends_User-User_fk1] FOREIGN KEY ([User2_ID]) REFERENCES [User]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [Friends_User-User] CHECK CONSTRAINT [Friends_User-User_fk1]
GO

ALTER TABLE [Room] WITH CHECK ADD CONSTRAINT [Room_fk0] FOREIGN KEY ([owner_ID]) REFERENCES [User]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [Room] CHECK CONSTRAINT [Room_fk0]
GO

ALTER TABLE [Invitations_User-User] WITH CHECK ADD CONSTRAINT [Invitations_User-User_fk0] FOREIGN KEY ([User1_ID]) REFERENCES [User]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [Invitations_User-User] CHECK CONSTRAINT [Invitations_User-User_fk0]
GO
ALTER TABLE [Invitations_User-User] WITH CHECK ADD CONSTRAINT [Invitations_User-User_fk1] FOREIGN KEY ([User2_ID]) REFERENCES [User]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [Invitations_User-User] CHECK CONSTRAINT [Invitations_User-User_fk1]
GO
ALTER TABLE [Invitations_User-User] WITH CHECK ADD CONSTRAINT [Invitations_User-User_fk2] FOREIGN KEY ([room_ID]) REFERENCES [Room]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [Invitations_User-User] CHECK CONSTRAINT [Invitations_User-User_fk2]
GO

ALTER TABLE [BlackList_User-User] WITH CHECK ADD CONSTRAINT [BlackList_User-User_fk0] FOREIGN KEY ([User1_ID]) REFERENCES [User]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [BlackList_User-User] CHECK CONSTRAINT [BlackList_User-User_fk0]
GO
ALTER TABLE [BlackList_User-User] WITH CHECK ADD CONSTRAINT [BlackList_User-User_fk1] FOREIGN KEY ([User2_ID]) REFERENCES [User]([ID])
ON UPDATE CASCADE
GO
ALTER TABLE [BlackList_User-User] CHECK CONSTRAINT [BlackList_User-User_fk1]
GO

