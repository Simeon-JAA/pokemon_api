DROP DATABASE IF EXISTS pokemon_api; 

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
    in_current_team BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (user_pokemon_id)
);

CREATE TABLE pokemon_stats (
    pokemon_stats_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    pokemon_id SMALLINT UNIQUE NOT NULL,
    pokemon_type TEXT NOT NULL, --CREATE AN ENUM FOR THIS MAYBE
    health SMALLINT NOT NULL,
    attack SMALLINT NOT NULL,
    defense SMALLINT NOT NULL,
    special_attack SMALLINT NOT NULL,
    special_defense SMALLINT NOT NULL,
    pokemon_height SMALLINT NOT NULL,
    pokemon_weight SMALLINT NOT NULL,
    PRIMARY KEY (pokemon_stats_id),
    FOREIGN KEY (pokemon_id) REFERENCES user_pokemon (user_pokemon_id),
    CONSTRAINT check_attack CHECK (attack >= 0 AND attack <= 504),
    CONSTRAINT check_defense CHECK (defense >= 0 AND defense <= 504),
    CONSTRAINT check_special_attack CHECK (special_attack >= 0 AND special_attack <= 504),
    CONSTRAINT check_special_defense CHECK (special_defense >= 0 AND special_defense <= 504),
    CONSTRAINT check_health CHECK (health >= 0 AND health <= 255),
    CONSTRAINT check_height CHECK (pokemon_height > 0),
    CONSTRAINT check_weight CHECK (pokemon_weight > 0)
);

CREATE SCHEMA example;

SET SEARCH_PATH TO example;

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
    in_current_team BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY (user_pokemon_id)
);

CREATE TABLE pokemon_stats (
    pokemon_stats_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    pokemon_id SMALLINT UNIQUE NOT NULL,
    pokemon_type TEXT NOT NULL, --CREATE AN ENUM FOR THIS MAYBE
    attack SMALLINT NOT NULL,
    defense SMALLINT NOT NULL,
    special_attack SMALLINT NOT NULL,
    special_defense SMALLINT NOT NULL,
    health SMALLINT NOT NULL,
    pokemon_height SMALLINT NOT NULL,
    pokemon_weight SMALLINT NOT NULL,
    PRIMARY KEY (pokemon_stats_id),
    FOREIGN KEY (pokemon_id) REFERENCES user_pokemon (user_pokemon_id),
    CONSTRAINT check_attack CHECK (attack >= 0 AND attack <= 504),
    CONSTRAINT check_defense CHECK (defense >= 0 AND defense <= 504),
    CONSTRAINT check_special_attack CHECK (special_attack >= 0 AND special_attack <= 504),
    CONSTRAINT check_special_defense CHECK (special_defense >= 0 AND special_defense <= 504),
    CONSTRAINT check_health CHECK (health >= 0 AND health <= 255),     
    CONSTRAINT check_height CHECK (pokemon_height > 0),
    CONSTRAINT check_weight CHECK (pokemon_weight > 0)
);

INSERT INTO api_user 
(user_name)
VALUES 
('example_user_1'), ('example_user_2'),
('example_user_3'), ('example_user_4')
 RETURNING *;

INSERT INTO user_pokemon 
(user_id, pokemon_name, in_current_team)
VALUES 
(1, 'pikachu', TRUE), (1, 'charizard', TRUE), (1, 'diglett', TRUE),
(2, 'squirtle', TRUE), (2, 'pikachu', FALSE), 
(3, 'snorlax', TRUE)
 RETURNING *;

INSERT INTO pokemon_stats 
(pokemon_id, pokemon_type, attack, defense,
special_attack, special_defense, health, pokemon_height, pokemon_weight)
VALUES 
(1, 'thunder', 20, 20, 20, 20, 100, 5, 100),
(2, 'fire', 30, 50, 20, 20, 255, 100, 1500),
(3, 'earth', 10, 5, 20, 20, 50, 2, 77),
(4, 'water', 17, 10, 20, 20, 10, 9, 120),
(5, 'thunder', 20, 20, 20, 20, 100, 5, 100),
(6, 'earth', 200, 200, 20, 20, 255, 120, 2000)
 RETURNING *; 