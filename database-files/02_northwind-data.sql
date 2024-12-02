#
# Converted from MS Access 2010 Northwind database (northwind.accdb) using
# Bullzip MS Access to MySQL Version 5.1.242. http://www.bullzip.com
#
# CHANGES MADE AFTER INITIAL CONVERSION
# * column and row names in CamelCase converted to lower_case_with_underscore
# * space and slash ("/") in table and column names replaced with _underscore_
# * id column names converted to "id"
# * foreign key column names converted to xxx_id
# * variables of type TIMESTAMP converted to DATETIME to avoid TIMESTAMP
#   range limitation (1997 - 2038 UTC), and other limitations.
# * unique and foreign key checks disabled while loading data
#
#------------------------------------------------------------------
#

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

USE `nu-clear-database`;

#
# Dumping data for table 'User'
#

INSERT INTO `User` (`userId`, `userType`) VALUES (1, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (2, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (3, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (4, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (5, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (6, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (7, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (8, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (9, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (10, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (11, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (12, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (13, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (14, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (15, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (16, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (17, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (18, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (19, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (20, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (21, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (22, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (23, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (24, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (25, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (26, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (27, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (28, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (29, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (30, 'SystemAdmin');
INSERT INTO `User` (`userId`, `userType`) VALUES (31, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (32, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (33, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (34, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (35, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (36, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (37, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (38, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (39, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (40, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (41, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (42, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (43, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (44, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (45, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (46, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (47, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (48, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (49, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (50, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (51, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (52, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (53, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (54, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (55, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (56, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (57, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (58, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (59, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (60, 'Student');
INSERT INTO `User` (`userId`, `userType`) VALUES (61, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (62, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (63, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (64, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (65, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (66, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (67, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (68, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (69, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (70, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (71, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (72, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (73, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (74, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (75, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (76, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (77, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (78, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (79, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (80, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (81, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (82, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (83, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (84, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (85, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (86, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (87, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (88, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (89, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (90, 'Advisor');
INSERT INTO `User` (`userId`, `userType`) VALUES (91, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (92, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (93, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (94, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (95, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (96, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (97, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (98, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (99, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (100, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (101, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (102, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (103, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (104, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (105, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (106, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (107, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (108, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (109, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (110, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (111, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (112, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (113, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (114, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (115, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (116, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (117, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (118, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (119, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (120, 'Data Analyst');
INSERT INTO `User` (`userId`, `userType`) VALUES (121, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (122, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (123, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (124, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (125, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (126, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (127, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (128, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (129, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (130, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (131, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (132, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (133, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (134, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (135, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (136, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (137, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (138, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (139, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (140, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (141, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (142, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (143, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (144, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (145, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (146, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (147, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (148, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (149, 'Employer');
INSERT INTO `User` (`userId`, `userType`) VALUES (150, 'Employer');



# _ records

#
# Dumping data for table 'SystemAdmin'
#

# _ records

#
# Dumping data for table 'Employees'
#

# _ records

#
# Dumping data for table 'Module'
#

# _ records

#
# Dumping data for table 'UserModule'
#


# _ records

#
# Dumping data for table 'Permssion'
#


# _ records

#
# Dumping data for table 'UserPermission'
#


# _ records

#
# Dumping data for table ''
#


# _ records

#
# Dumping data for table ''
#


# _ records
 
#
# Dumping data for table ''
#


# _ records

#
# Dumping data for table ''
#

#  _ records

#
# Dumping data for table ''
#

# _ records

#
# Dumping data for table ''
# 

# _ records

#
# Dumping data for table ''
#



#
# Dumping data for table ''
#


# 4 records

#
# Dumping data for table ''
#


# _ records

#
# Dumping data for table ''
#


# _ records

#
# Dumping data for table ''
#


# _ records

#
# Dumping data for table ''
#


# _ records

#
# Dumping data for table 'suppliers'
#

# _ records

SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS; 