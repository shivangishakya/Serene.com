DROP TABLE IF EXISTS "users";

CREATE TABLE "users" (
	"username"	varchar(255),
	"password"	varchar(255),
	"recipient"	varchar(255),
	"level" int,
	"prevlevel" int,
	"name"	varchar(255),
	"phone"	varchar(255),
	"address" varchar(255),
	PRIMARY KEY("username")
);


