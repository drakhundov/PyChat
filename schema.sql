DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS users;

CREATE TABLE messages (
    username TEXT NOT NULL,
    receiver TEXT NOT NULL,
    text     TEXT   NOT NULL,
    time     NUMERIC   NOT NULL
);

CREATE TABLE users (
    username TEXT NOT NULL
                    UNIQUE,
    password TEXT NOT NULL
);

CREATE INDEX users_index ON users(username);
CREATE INDEX pw_index ON users(password);