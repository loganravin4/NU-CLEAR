SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

DROP DATABASE IF EXISTS `nu-clear-database`;
CREATE DATABASE `nu-clear-database`;
USE `nu-clear-database`;

-- Create tables
CREATE TABLE IF NOT EXISTS UserType (
    userType VARCHAR(255) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS User (
    userId INT PRIMARY KEY AUTO_INCREMENT,
    userType VARCHAR(255) NOT NULL,
    FOREIGN KEY (userType) REFERENCES UserType (userType)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS SystemAdmin (
    userId INT PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Module (
    moduleId INT PRIMARY KEY AUTO_INCREMENT,
    moduleName VARCHAR(255) NOT NULL,
    moduleStatus VARCHAR(255) NOT NULL,
    createdBy INT NOT NULL,
    updatedBy INT,
    FOREIGN KEY (createdBy) REFERENCES SystemAdmin (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (updatedBy) REFERENCES SystemAdmin (userId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Permission (
    permissionId INT PRIMARY KEY AUTO_INCREMENT,
    createdBy INT NOT NULL,
    userType VARCHAR(255) NOT NULL,
    canEditPerms BOOLEAN DEFAULT false,
    canEditModule BOOLEAN DEFAULT false,
    canEditAccSettings BOOLEAN DEFAULT false,
    canCreateReview BOOLEAN DEFAULT false,
    canCreateCoopListing BOOLEAN DEFAULT false,
    canCreateModule BOOLEAN DEFAULT false,
    canViewReview BOOLEAN DEFAULT false,
    canViewCoopListing BOOLEAN DEFAULT false,
    canViewModule BOOLEAN DEFAULT false,
    canDeleteReview BOOLEAN DEFAULT false,
    canDeleteCoopListing BOOLEAN DEFAULT false,
    canDeleteModule BOOLEAN DEFAULT false,
    FOREIGN KEY (createdBy) REFERENCES SystemAdmin (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (userType) REFERENCES UserType (userType)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS UserModule (
    userType VARCHAR(255),
    moduleId INT,
    PRIMARY KEY (userType, moduleId),
    FOREIGN KEY (userType) REFERENCES UserType (userType)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (moduleId) REFERENCES Module (moduleId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Advisor (
    userId INT PRIMARY KEY,
    nuId INT UNIQUE NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    department VARCHAR(255),
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Announcement (
    announcementId INT PRIMARY KEY AUTO_INCREMENT,
    createdBy INT NOT NULL,
    announcementText TEXT NOT NULL,
    FOREIGN KEY (createdBy) REFERENCES Advisor (userId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Student (
    userId INT PRIMARY KEY,
    nuId INT UNIQUE NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    major VARCHAR(255),
    coopLevel INT NOT NULL,
    year INT,
    advisor INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (advisor) REFERENCES Advisor (userId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Company (
    companyId INT PRIMARY KEY AUTO_INCREMENT,
    companyName VARCHAR(255) NOT NULL,
    size INT
);

CREATE TABLE IF NOT EXISTS Coop (
    coopId INT PRIMARY KEY AUTO_INCREMENT,
    locationCity VARCHAR(255),
    locationState VARCHAR(255),
    locationCountry VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    company INT NOT NULL,
    FOREIGN KEY (company) REFERENCES Company (companyId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Favorite (
    userId INT,
    coopId INT,
    PRIMARY KEY (userId, coopId),
    FOREIGN KEY (userId) REFERENCES Student (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (coopId) REFERENCES Coop (coopId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Review (
    reviewId INT PRIMARY KEY AUTO_INCREMENT,
    createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    createdBy INT NOT NULL,
    role INT NOT NULL,
    salary DECIMAL(6,2),
    rating FLOAT NOT NULL,
    summary TEXT,
    bestPart TEXT,
    worstPart TEXT,
    wouldRecommend BOOLEAN NOT NULL DEFAULT true,
    FOREIGN KEY (createdBy) REFERENCES Student (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (role) REFERENCES Coop (coopId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Employer (
    userId INT PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    role VARCHAR(255),
    department VARCHAR(255),
    company INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (company) REFERENCES Company (companyId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS DataAnalyst (
    userId INT PRIMARY KEY,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS Visualization (
    visualizationId INT PRIMARY KEY AUTO_INCREMENT,
    vizType VARCHAR(255) NOT NULL,
    filters VARCHAR(255) NOT NULL,
    company INT,
    createdBy INT NOT NULL,
    updatedBy INT,
    FOREIGN KEY (company) REFERENCES Company (companyId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (createdBy) REFERENCES DataAnalyst (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (updatedBy) REFERENCES DataAnalyst (userId)
        ON UPDATE cascade ON DELETE cascade
);

CREATE TABLE IF NOT EXISTS SummaryReport (
    summaryReportId INT PRIMARY KEY AUTO_INCREMENT,
    averageRating FLOAT NOT NULL,
    generatedSummary TEXT NOT NULL,
    company INT NOT NULL,
    generatedBy INT NOT NULL,
    updatedBy INT,
    FOREIGN KEY (company) REFERENCES Company (companyId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (generatedBy) REFERENCES DataAnalyst (userId)
        ON UPDATE cascade ON DELETE cascade,
    FOREIGN KEY (updatedBy) REFERENCES DataAnalyst (userId)
        ON UPDATE cascade ON DELETE cascade
);