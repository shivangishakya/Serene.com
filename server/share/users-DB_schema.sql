DROP TABLE IF EXISTS "users";

CREATE TABLE "users" (
	"username"	varchar(255),
	"password"	varchar(255),
	"recipient"	varchar(255),
	"level" int,
	"prevlevel" int,
	PRIMARY KEY("username")
);

