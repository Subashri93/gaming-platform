CREATE DATABASE GameStatsDB;


USE GameStatsDB;


CREATE TABLE games (
    game VARCHAR(255) NOT NULL,
    number_of_times_played INT,
    PRIMARY KEY (game)
);


INSERT INTO games (game, number_of_times_played) VALUES
    ('caterpillar game', 0),
    ('color game', 0),
    ('egg catcher', 0),
    ('fidget spinner', 0),
    ('hangman', 0),
    ('rock paper scissors', 0),
    ('screen pet', 0),
    ('snake game', 0),
    ('brick breaker', 0),
    ('tic tac toe', 0);