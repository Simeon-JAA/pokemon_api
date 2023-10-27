DROP DATABASE IF EXISTS pokemon_api ; 

CREATE DATABASE pokemon_api;

\c pokemon_api;

CREATE TABLE api_user (
    user_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    user_name TEXT NOT NULL,
    PRIMARY KEY (user_name), 
    CONSTRAINT check_user_name CHECK (LENGTH(user_name) > 4 AND LENGTH(user_name) < 20)
);

CREATE TABLE user_pokemon (
    user_pokemon_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    user_id SMALLINT NOT NULL,
    pokemon_name TEXT NOT NULL,
    pokemon_type TEXT NOT NULL, --CREATE AN ENUM FOR THIS MAYBE
    pokemon_height SMALLINT NOT NULL,
    pokemon_weight SMALLINT NOT NULL,
    PRIMARY KEY (user_pokemon_id),
    CONSTRAINT check_height CHECK (pokemon_height > 0),
    CONSTRAINT check_weight CHECK (pokemon_weight > 0)
);

CREATE TABLE pokemon_stats (
    pokemon_stats_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    pokemon_id SMALLINT UNIQUE NOT NULL,
    attack SMALLINT NOT NULL,
    defense SMALLINT NOT NULL,
    health SMALLINT NOT NULL,
    PRIMARY KEY (pokemon_stats_id),
    FOREIGN KEY (pokemon_id) REFERENCES user_pokemon (user_pokemon_id),
    CONSTRAINT check_attack CHECK (attack >= 0 AND attack <= 504),
    CONSTRAINT check_defense CHECK (defense >= 0 AND defense <= 504),
    CONSTRAINT check_health CHECK (health >= 0 AND health <= 255)
);