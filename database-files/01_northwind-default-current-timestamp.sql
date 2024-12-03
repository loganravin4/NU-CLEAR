DROP DATABASE IF EXISTS `nu-clear-database`;
CREATE DATABASE `nu-clear-database`;
USE `nu-clear-database`;

-- Create tables
CREATE TABLE IF NOT EXISTS UserType (
    userType varchar(255) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS User (
    userId integer PRIMARY KEY,
    userType varchar(255) NOT NULL,
    FOREIGN KEY (userType) REFERENCES UserType (userType)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS SystemAdmin (
    userId integer PRIMARY KEY,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    email varchar(255),
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS Module (
    moduleId integer PRIMARY KEY,
    moduleName varchar(255) NOT NULL,
    createdBy integer NOT NULL,
    updatedBy integer,
    FOREIGN KEY (createdBy) REFERENCES SystemAdmin (userId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (updatedBy) REFERENCES SystemAdmin (userId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS UserModule (
  userId int NOT NULL,
  moduleId int NOT NULL,
  moduleStatus varchar(255) NOT NULL,
  CONSTRAINT userId_fk
        FOREIGN KEY (userId) REFERENCES User (userId)
            ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT moduleId_fk
        FOREIGN KEY (moduleId) REFERENCES Module (moduleId)
            ON UPDATE CASCADE ON DELETE CASCADE,
  PRIMARY KEY (userId, moduleId)
)

CREATE TABLE IF NOT EXISTS Permission (
    permissionId integer PRIMARY KEY,
    editedBy integer NOT NULL,
    canEditPerms bool DEFAULT false,
    canEditModule bool DEFAULT false,
    canEditAccSettings bool DEFAULT false,
    canCreateReview bool DEFAULT false,
    canCreateCoopListing bool DEFAULT false,
    canCreateModule bool DEFAULT false,
    canViewReview bool DEFAULT false,
    canViewCoopListing bool DEFAULT false,
    canViewModule bool DEFAULT false,
    canDeleteReview bool DEFAULT false,
    canDeleteCoopListing bool DEFAULT false,
    canDeleteModule bool DEFAULT false,
    FOREIGN KEY (editedBy) REFERENCES SystemAdmin (userId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS UserPermission (
    userType varchar(255),
    permissionId integer,
    PRIMARY KEY (userType, permissionId),
    FOREIGN KEY (userType) REFERENCES UserType (userType)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (permissionId) REFERENCES Permission (permissionId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS UserModule (
    userType varchar(255),
    moduleId integer,
    PRIMARY KEY (userType, moduleId),
    FOREIGN KEY (userType) REFERENCES UserType (userType)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (moduleId) REFERENCES Module (moduleId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS Advisor (
    nuId integer PRIMARY KEY,
    userId integer UNIQUE NOT NULL,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    email varchar(255),
    department varchar(255),
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS Student (
    nuId integer PRIMARY KEY,
    userId integer UNIQUE NOT NULL,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    major varchar(255),
    coopLevel integer NOT NULL,
    year integer,
    advisor integer NOT NULL,
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (advisor) REFERENCES Advisor (nuId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS Company (
    companyId integer PRIMARY KEY,
    companyName varchar(255) NOT NULL,
    size integer
);

CREATE TABLE IF NOT EXISTS Coop (
    jobId integer PRIMARY KEY,
    locationCity varchar(255),
    locationState varchar(255),
    locationCountry varchar(255),
    title varchar(255),
    description varchar(255),
    company integer,
    FOREIGN KEY (company) REFERENCES Company (companyId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS Review (
    reviewId integer PRIMARY KEY,
    createdAt timestamp DEFAULT (now()),
    createdBy integer,
    role integer NOT NULL,
    salary decimal(6,2),
    rating varchar(255) NOT NULL,
    summary varchar(255),
    bestPart varchar(255),
    worstPart varchar(255),
    isAnonymous bool NOT NULL DEFAULT FALSE,
    FOREIGN KEY (createdBy) REFERENCES Student (userId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (role) REFERENCES Coop (jobId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS Employer (
    userId integer PRIMARY KEY,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    email varchar(255),
    role varchar(255),
    department varchar(255),
    company integer NOT NULL,
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (company) REFERENCES Company (companyId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS DataAnalyst (
    userId integer PRIMARY KEY,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    FOREIGN KEY (userId) REFERENCES User (userId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS Visualization (
    visualizationId integer PRIMARY KEY,
    type varchar(255) NOT NULL,
    filters varchar(255) NOT NULL,
    company integer,
    createdBy integer NOT NULL,
    updatedBy integer,
    FOREIGN KEY (company) REFERENCES Company (companyId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (createdBy) REFERENCES DataAnalyst (userId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (updatedBy) REFERENCES DataAnalyst (userId)
        ON UPDATE cascade ON DELETE restrict
);

CREATE TABLE IF NOT EXISTS SummaryReport (
    summaryReportId integer PRIMARY KEY,
    averageRating varchar(255) NOT NULL,
    generatedSummary varchar(255) NOT NULL,
    company integer,
    generatedBy integer NOT NULL,
    updatedBy integer,
    FOREIGN KEY (company) REFERENCES Company (companyId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (generatedBy) REFERENCES DataAnalyst (userId)
        ON UPDATE cascade ON DELETE restrict,
    FOREIGN KEY (updatedBy) REFERENCES DataAnalyst (userId)
        ON UPDATE cascade ON DELETE restrict
);

/*
INSERT INTO UserType (userType)
    VALUES ('SystemAdmin'), ('Advisor'), ('Student'), ('Employer'), ('DataAnalyst');

INSERT INTO User (userId, userType)
    VALUES
        (5, 'SystemAdmin'),
        (101, 'Advisor'),
        (102, 'Advisor'),
        (103, 'Advisor'),
        (201, 'Student'),
        (202, 'Student'),
        (203, 'Student'),
        (301, 'Employer'),
        (302, 'Employer'),
        (303, 'Employer'),
        (401, 'DataAnalyst'),
        (402, 'DataAnalyst'),
        (403, 'DataAnalyst');

INSERT INTO SystemAdmin (userId, firstName, lastName, email)
    VALUES
        (5, 'Ariana', 'Duke', 'ariana.duke@clearplatform.com');

INSERT INTO Module (moduleId, moduleName, moduleStatus, createdBy)
    VALUES
    (1, 'How to compare company ratings', 'Active', 5),
    (2, 'Seeing your students dashboards', 'Active', 5),
    (3, 'Company profile management', 'Active', 5);

INSERT INTO UserModule (userType, moduleId)
    VALUES
        ('Student', 1),
        ('Advisor', 2),
        ('Employer', 3);

INSERT INTO Permission (permissionId, editedBy, canEditPerms, canEditModule, canEditAccSettings,
                        canCreateReview, canCreateCoopListing, canCreateModule, canViewReview,
                        canViewCoopListing, canViewModule, canDeleteReview, canDeleteCoopListing, canDeleteModule)
    VALUES
        (1, 5, true, true,
         true, true, true,
         true, true, true, true,
         true, true, true),
        (2, 5, false, false, false, true, false, false, true, false, true, false, false, false);

INSERT INTO UserPermission (userType, permissionId)
    VALUES
        ('Student', 2),
        ('SystemAdmin', 1);

INSERT INTO Advisor (nuId, userId, firstName, lastName, email, department)
    VALUES
        (1, 101, 'Quinn', 'Aldridge',
         'quinn.aldridge@northeastern.edu', 'Counseling'),
        (2, 102, 'Sophia', 'Brown',
         'sophia.brown@northeastern.edu', 'Computer Science'),
        (3, 103, 'James', 'Smith',
         'james.smith@northeastern.edu', 'Data Science');

INSERT INTO Student (nuId, userId, firstName, lastName, major, coopLevel, year, advisor)
    VALUES
        (2239281, 201, 'Amelia', 'Fordham', 'CS', 1, 3, 1),
        (2234928, 202, 'Jordan', 'Kim', 'DSBA', 2, 4, 2),
        (2234193, 203, 'Maya', 'Patel', 'BSCS', 0, 2, 2);

INSERT INTO Company (companyId, companyName, size)
    VALUES
        (1, 'BarkTree Bank', 5000),
        (2, 'Tech Spark Solutions', 200),
        (3, 'Google', 150000),
        (4, 'Innovate Labs', 50);

INSERT INTO Coop (jobId, locationCity, locationState, locationCountry, title, description, company)
    VALUES
        (1, 'Boston', 'MA', 'USA', 'QA Engineering Intern',
         'Assist in software quality assurance testing, writing test cases, and debugging applications.',
         1);

INSERT INTO Review (reviewId, createdAt, createdBy, role, salary, rating, summary, bestPart, worstPart)
    VALUES
        (1, DEFAULT, 201, 1, 25.00,
         '4/5', 'Great learning experience with some challenges.',
         'Learned a lot about QA and testing methodologies.',
         'Limited mentorship and guidance at times.');

INSERT INTO Employer (userId, firstName, lastName, email, role, department, company)
    VALUES
        (301, 'Crystal', 'Cooper', 'crystal.cooper@barktreebank.com', 'Hiring Manager', 'Fintech', 1),
        (302, 'Marcus', 'Taylor', 'marcus.taylor@techspark.com', 'Director of Engineering', 'Software Development', 2),
        (303, 'Emma', 'Reed', 'emma.reed@google.com', 'Senior Recruiter', 'Data Science', 3);

INSERT INTO DataAnalyst (userId, firstName, lastName)
    VALUES
        (401, 'Sabrina', 'Johnson'),
        (402, 'Daniel', 'Green'),
        (403, 'Olivia', 'Clark');

INSERT INTO Visualization (visualizationId, type, filters, company, createdBy)
    VALUES
        (1, 'Bar Chart', 'Year: 3, Role: QA Engineering Intern', 1, 401),
        (2, 'Pie Chart', 'Rating: 4/5 and above, Location: USA', 3, 401),
        (3, 'Line Chart', 'Year: 2, Role: Data Analyst', 2, 402),
        (4, 'Heatmap', 'Demographics: Gender, Year', 1, 403);

INSERT INTO SummaryReport (summaryReportId, averageRating, generatedSummary, company, generatedBy)
    VALUES
        (1, '4.2/5', 'BarkTree Bank offers strong mentorship but limited guidance for juniors.', 1, 401),
        (2, '4.5/5', 'Google excels in supporting students with structured programs and clear goals.', 3, 401),
        (3, '3.8/5', 'Tech Spark Solutions is great for hands-on experience but has long hours.', 2, 402),
        (4, '4.0/5', 'Innovate Labs provides creative freedom but lacks formal training.', 4, 403);
*/