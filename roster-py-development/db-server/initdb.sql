CREATE DATABASE roster;



-- other stuff

CREATE TABLE TEAMS (
    TEAM_ID INT,
    LEVEL VARCHAR(10),
    NAME VARCHAR(100),
    PRACTICE_TIME VARCHAR(50),
    LOCKED BOOLEAN,
    MAXIMUM_PICKS INT,
    PRACTICE_LOCATION VARCHAR(100),
    PRIMARY KEY (TEAM_ID)
); 

CREATE TABLE DANCERS (
    DANCER_ID INT, 
    TEAM_ID INT,
    NAME VARCHAR(100), 
    EMAIL VARCHAR(150), 
    PHONE VARCHAR(15), 
    GENDER VARCHAR(10), 
    YEAR VARCHAR(15), 
    DANCE_EXP VARCHAR(4),
    EXP_INTEREST VARCHAR(4), 
    TECH_INTEREST VARCHAR(4), 
    CAMP_INTEREST VARCHAR(4), 
    REACH_WORKSHOP_INTEREST VARCHAR(4),
    REACH_NEWS_INTEREST VARCHAR(4), 
    PRIMARY KEY (DANCER_ID),
    FOREIGN KEY (TEAM_ID) REFERENCES TEAMS(TEAM_ID)
);



CREATE TABLE USERS (
    USER_ID INT,
    ROLE VARCHAR(50),
    PRIMARY KEY (USER_ID)
);