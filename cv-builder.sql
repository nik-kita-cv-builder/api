CREATE TYPE "auth_provider" AS ENUM (
  'google'
);

CREATE TABLE "users" (
  "id" int PRIMARY KEY,
  "auth_provider" auth_provider NOT NULL,
  "auth_id" varchar NOT NULL
);

CREATE TABLE "profiles" (
  "id" int PRIMARY KEY,
  "name" varchar NOT NULL,
  "summary" varchar,
  "user_id" int
);

CREATE TABLE "contacts" (
  "title" varchar NOT NULL,
  "value" varchar NOT NULL,
  "user_id" int,
  "profile_id" int
);

CREATE UNIQUE INDEX ON "users" ("auth_provider", "auth_id");

ALTER TABLE "profiles" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;

ALTER TABLE "contacts" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE;

ALTER TABLE "contacts" ADD FOREIGN KEY ("profile_id") REFERENCES "profiles" ("id") ON DELETE SET NULL;
