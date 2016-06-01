PRAGMA foreign_keys = OFF;
-- ----------------------------
DROP TABLE IF EXISTS "main"."memo";
CREATE TABLE "memo" (
"id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
"token"  TEXT,
"text"  TEXT
);