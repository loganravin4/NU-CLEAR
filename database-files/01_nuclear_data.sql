SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

USE `nu-clear-database`;

DROP TABLE IF EXISTS UserType;
INSERT INTO UserType (userType) VALUES
    ('SystemAdmin'),
    ('Advisor'),
    ('Student'),
    ('Employer'),
    ('DataAnalyst');

DROP TABLE IF EXISTS User;

