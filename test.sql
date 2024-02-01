create database test;

use test;

CREATE TABLE Registration (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    DateOfBirth DATE
);


INSERT INTO Registration VALUES (100 , 'John Doe', 'john.doe@example.com', '1990-01-15');
SELECT * FROM Registration;

UPDATE Registration SET Name='John Updated', Email='john.updated@example.com', DateOfBirth='1990-01-20' WHERE ID = 100;
SELECT * FROM Registration;

DELETE FROM Registration WHERE ID = 100;
SELECT * FROM Registration;
