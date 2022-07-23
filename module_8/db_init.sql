<<<<<<< HEAD
DROP USER IF EXISTS 'pysports_user'@'localhost';

CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password by '#dontBreakMe1';

GRANT ALL PRIVILEGES ON pysports. * TO 'pysports_user'@'localhost';


DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


CREATE TABLE team (
    team_id     INT            NOT NULL,       AUTO_INCREMENT,
    team_name   VARCHAR(75)    NOT NULL,
    mascot      VARCHAR(75)    NOT NULL,
    PRIMARY KEY(team_id)
);


CREATE TABLE player (
    player_id     INT          NOT NULL        AUTO_INCREMENT,
    first_name    VARCHAR(75)  NOT NULL,
    last_name     VARCHAR(75)  NOT NULL,
    team_id       INT          NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINTS fk_team
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


INSERT INTO team(team_name, mascot)
    VALUES('Team Rein', 'Bee');

INSERT INTO team(team_name, mascot)
    VALUES('Team Shur', 'Shark');


INSERT INTO player(first_name, last_name, team_id)
    VALUES('John', 'Smith', (SELECT team_id FROM team WHERE team_name = 'Team Rein'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Tim', 'Walker', (SELECT team_id FROM team WHERE team_name = 'Team Rein'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Cris', 'Dur', (SELECT team_id FROM team WHERE team_name = 'Team Rein'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jane', 'Huss', (SELECT team_id FROM team WHERE team_name = 'Team Shur'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Lis', 'Mye', (SELECT team_id FROM team WHERE team_name = 'Team Shur'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Ric', 'Dre', (SELECT team_id FROM team WHERE team_name = 'Team Shur'));
=======

>>>>>>> 97be1e19a1237ec4b0acf441109891622316bb78
