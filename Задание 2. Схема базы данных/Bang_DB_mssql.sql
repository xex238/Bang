CREATE TABLE [User]
(
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
CREATE TABLE [Friends_User-User]
(
	ID integer NOT NULL,
	User1_ID integer NOT NULL,
	User2_ID integer NOT NULL,
  CONSTRAINT [PK_FRIENDS_USER-USER] PRIMARY KEY CLUSTERED
  (
  [ID] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)
GO
CREATE TABLE [Room]
(
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
CREATE TABLE [Invitations_User-User]
(
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
CREATE TABLE [BlackList_User-User]
(
	ID integer NOT NULL,
	User1_ID integer NOT NULL,
	User2_ID integer NOT NULL,
  CONSTRAINT [PK_BLACKLIST_USER-USER] PRIMARY KEY CLUSTERED
  (
  [ID] ASC
  ) WITH (IGNORE_DUP_KEY = OFF)

)