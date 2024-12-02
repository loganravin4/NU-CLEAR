DROP DATABASE IF EXISTS `nu-clear-database`;
CREATE DATABASE `nu-clear-database`;
USE `nu-clear-database`;


CREATE TABLE `User` (
  `userId` integer PRIMARY KEY,
  `userType` varchar(255) NOT NULL,
  `managedBy` integer
);

CREATE TABLE `SystemAdmin` (
  `userId` integer PRIMARY KEY,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255)
);

CREATE TABLE `Module` (
  `moduleId` integer PRIMARY KEY,
  `moduleName` varchar(255) NOT NULL,
  `moduleStatus` varchar(255) NOT NULL,
  `createdBy` integer NOT NULL
);

CREATE TABLE `Permission` (
  `permissionId` integer PRIMARY KEY,
  `editedBy` integer NOT NULL,
  `canEditPerms` bool DEFAULT false,
  `canEditModule` bool DEFAULT false,
  `canEditAccSettings` bool DEFAULT false,
  `canCreateReview` bool DEFAULT false,
  `canCreateCoopListing` bool DEFAULT false,
  `canCreateModule` bool DEFAULT false,
  `canViewReview` bool DEFAULT false,
  `canViewCoopListing` bool DEFAULT false,
  `canViewModule` bool DEFAULT false,
  `canDeleteReview` bool DEFAULT false,
  `canDeleteCoopListing` bool DEFAULT false,
  `canDeleteModule` bool DEFAULT false
);

CREATE TABLE `UserPermission` (
  `userType` varchar(255),
  `permissionId` integer,
  PRIMARY KEY (`userType`, `permissionId`)
);

CREATE TABLE `UserModule` (
  `userType` varchar(255),
  `moduleId` integer,
  PRIMARY KEY (`userType`, `moduleId`)
);

CREATE TABLE `Advisor` (
  `nuId` integer PRIMARY KEY,
  `userId` integer,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255),
  `department` varchar(255)
);

CREATE TABLE `Student` (
  `nuId` integer PRIMARY KEY,
  `userId` integer,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `major` varchar(255),
  `coopLevel` integer NOT NULL,
  `year` integer,
  `advisor` integer NOT NULL
);

CREATE TABLE `Company` (
  `companyId` integer PRIMARY KEY,
  `companyName` varchar(255) NOT NULL,
  `size` integer
);

CREATE TABLE `Coop` (
  `jobId` integer PRIMARY KEY,
  `locationCity` varchar(255),
  `locationState` varchar(255),
  `locationCountry` varchar(255),
  `title` varchar(255),
  `description` varchar(255),
  `company` integer
);

CREATE TABLE `Review` (
  `reviewId` integer PRIMARY KEY,
  `createdAt` timestamp DEFAULT (now()),
  `createdBy` integer,
  `role` varchar(255) NOT NULL,
  `salary` decimal(6,2),
  `rating` varchar(255) NOT NULL,
  `summary` varchar(255),
  `bestPart` varchar(255),
  `worstPart` varchar(255)
);

CREATE TABLE `Employer` (
  `userId` integer PRIMARY KEY,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255),
  `role` varchar(255),
  `department` varchar(255),
  `company` integer NOT NULL
);

CREATE TABLE `DataAnalyst` (
  `userId` integer PRIMARY KEY,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL
);

CREATE TABLE `Visualization` (
  `visualizationId` integer PRIMARY KEY,
  `type` varchar(255) NOT NULL,
  `filters` varchar(255) NOT NULL,
  `company` integer,
  `createdBy` integer
);

CREATE TABLE `SummaryReport` (
  `summaryReportId` integer PRIMARY KEY,
  `averageRating` varchar(255) NOT NULL,
  `generatedSummary` varchar(255) NOT NULL,
  `company` integer,
  `generatedBy` integer
);

ALTER TABLE `User` ADD FOREIGN KEY (`managedBy`) REFERENCES `SystemAdmin` (`userId`);

ALTER TABLE `SystemAdmin` ADD FOREIGN KEY (`userId`) REFERENCES `User` (`userId`);

ALTER TABLE `Module` ADD FOREIGN KEY (`createdBy`) REFERENCES `SystemAdmin` (`userId`);

ALTER TABLE `Permission` ADD FOREIGN KEY (`editedBy`) REFERENCES `SystemAdmin` (`userId`);

ALTER TABLE `UserPermission` ADD FOREIGN KEY (`userType`) REFERENCES `User` (`userType`);

ALTER TABLE `UserPermission` ADD FOREIGN KEY (`permissionId`) REFERENCES `Permission` (`permissionId`);

ALTER TABLE `UserModule` ADD FOREIGN KEY (`userType`) REFERENCES `User` (`userType`);

ALTER TABLE `UserModule` ADD FOREIGN KEY (`moduleId`) REFERENCES `Module` (`moduleId`);

ALTER TABLE `Advisor` ADD FOREIGN KEY (`userId`) REFERENCES `User` (`userId`);

ALTER TABLE `Student` ADD FOREIGN KEY (`userId`) REFERENCES `User` (`userId`);

ALTER TABLE `Student` ADD FOREIGN KEY (`advisor`) REFERENCES `Advisor` (`userId`);

ALTER TABLE `Coop` ADD FOREIGN KEY (`company`) REFERENCES `Company` (`companyId`);

ALTER TABLE `Review` ADD FOREIGN KEY (`createdBy`) REFERENCES `Student` (`userId`);

ALTER TABLE `Review` ADD FOREIGN KEY (`role`) REFERENCES `Coop` (`jobId`);

ALTER TABLE `Employer` ADD FOREIGN KEY (`userId`) REFERENCES `User` (`userId`);

ALTER TABLE `Employer` ADD FOREIGN KEY (`company`) REFERENCES `Company` (`companyId`);

ALTER TABLE `DataAnalyst` ADD FOREIGN KEY (`userId`) REFERENCES `User` (`userId`);

ALTER TABLE `Visualization` ADD FOREIGN KEY (`company`) REFERENCES `Company` (`companyId`);

ALTER TABLE `Visualization` ADD FOREIGN KEY (`createdBy`) REFERENCES `DataAnalyst` (`userId`);

ALTER TABLE `SummaryReport` ADD FOREIGN KEY (`company`) REFERENCES `Company` (`companyId`);

ALTER TABLE `SummaryReport` ADD FOREIGN KEY (`generatedBy`) REFERENCES `DataAnalyst` (`userId`);
