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
    hp SMALLINT NOT NULL,
    attack SMALLINT NOT NULL,
    defense SMALLINT NOT NULL,
    speed SMALLINT NOT NULL,
    special_attack SMALLINT NOT NULL,
    special_defense SMALLINT NOT NULL,
    height SMALLINT NOT NULL,
    pokemon_weight SMALLINT NOT NULL,
    PRIMARY KEY (pokemon_stats_id),
    FOREIGN KEY (pokemon_id) REFERENCES user_pokemon (user_pokemon_id),
    CONSTRAINT check_attack CHECK (attack >= 0 AND attack <= 504),
    CONSTRAINT check_defense CHECK (defense >= 0 AND defense <= 504),
    CONSTRAINT check_speed CHECK (speed >= 0 AND speed <= 504),
    CONSTRAINT check_special_attack CHECK (special_attack >= 0 AND special_attack <= 504),
    CONSTRAINT check_special_defense CHECK (special_defense >= 0 AND special_defense <= 504),
    CONSTRAINT check_hp CHECK (hp >= 0 AND hp <= 255),
    CONSTRAINT check_height CHECK (height > 0),
    CONSTRAINT check_pokemon_weight CHECK (pokemon_weight > 0)
);

CREATE TABLE pokemon_types (
    pokemon_types_id INT GENERATED ALWAYS AS IDENTITY,
    pokemon_id INT UNIQUE NOT NULL,
    pokemon_type TEXT NOT NULL, --potentially make an ENUM TYPE
    PRIMARY KEY (pokemon_types_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon_stats(pokemon_id)
);

CREATE TABLE pokemon_abilities (
    pokemon_ability_id INT GENERATED ALWAYS AS IDENTITY,
    ability_name TEXT NOT NULL,
    PRIMARY KEY (pokemon_ability_id)
);

CREATE TABLE pokemon_abilities_flavor_text (
    pokemon_abilities_flavor_text_id INT GENERATED ALWAYS AS IDENTITY,
    pokemon_ability_id INT NOT NULL,
    flavor_text TEXT NOT NULL,
    version_group TEXT NOT NULL, -- possibly make ENUM?
    PRIMARY KEY (pokemon_abilities_flavor_text_id),
    FOREIGN KEY (pokemon_ability_id) REFERENCES pokemon_abilities (pokemon_ability_id)
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
    attack SMALLINT NOT NULL,
    defense SMALLINT NOT NULL,
    speed SMALLINT NOT NULL,
    special_attack SMALLINT NOT NULL,
    special_defense SMALLINT NOT NULL,
    hp SMALLINT NOT NULL,
    height SMALLINT NOT NULL,
    pokemon_weight SMALLINT NOT NULL,
    PRIMARY KEY (pokemon_stats_id),
    FOREIGN KEY (pokemon_id) REFERENCES user_pokemon (user_pokemon_id),
    CONSTRAINT check_attack CHECK (attack >= 0 AND attack <= 504),
    CONSTRAINT check_defense CHECK (defense >= 0 AND defense <= 504),
    CONSTRAINT check_speed CHECK (speed >= 0 AND speed <= 504),
    CONSTRAINT check_special_attack CHECK (special_attack >= 0 AND special_attack <= 504),
    CONSTRAINT check_special_defense CHECK (special_defense >= 0 AND special_defense <= 504),
    CONSTRAINT check_hp CHECK (hp >= 0 AND hp <= 255),     
    CONSTRAINT check_height CHECK (height > 0),
    CONSTRAINT check_pokemon_weight CHECK (pokemon_weight > 0)
);

CREATE TABLE pokemon_types (
    pokemon_types_id INT GENERATED ALWAYS AS IDENTITY,
    pokemon_id INT UNIQUE NOT NULL,
    pokemon_type TEXT NOT NULL,
    PRIMARY KEY (pokemon_types_id),
    FOREIGN KEY (pokemon_id) REFERENCES pokemon_stats(pokemon_id)
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
(pokemon_id, attack, defense, speed,
special_attack, special_defense, hp, height, pokemon_weight)
VALUES 
(1, 20, 20, 50, 20, 20, 100, 5, 100),
(2, 30, 50, 50, 20, 20, 255, 100, 1500),
(3, 10, 5, 50, 20, 20, 50, 2, 77),
(4, 17, 10, 50, 20, 20, 10, 9, 120),
(5, 20, 20, 50, 20, 20, 100, 5, 100),
(6, 200, 200, 50, 20, 20, 255, 120, 2000)
RETURNING *; 

INSERT INTO pokemon_types
(pokemon_id, pokemon_type)
VALUES
(1, 'electric'),
(2, 'fire'),
(3, 'ground'),
(4, 'water'),
(5, 'thunder'),
(6, 'normal')
RETURNING *;
