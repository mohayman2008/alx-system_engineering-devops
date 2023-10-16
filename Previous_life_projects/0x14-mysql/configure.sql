-- Configure SQL on the servers

-- Create a user for the checker
CREATE USER IF NOT EXISTS
  'holberton_user'@'localhost'
  IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant the access to the replication status to holberton_user
GRANT REPLICATION CLIENT
  ON *.*
  TO 'holberton_user'@'localhost';

-- Create A new database and activate it
CREATE DATABASE IF NOT EXISTS `tyrell_corp`;
USE `tyrell_corp`;

-- Create A new table 'nexus6'
CREATE TABLE IF NOT EXISTS `nexus6`
  (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `name` CHAR(128) DEFAULT NULL);

-- Insert a dummy row
INSERT INTO `nexus6` (`name`) VALUE ('No Body');

-- Grant SELECT PRIVILAGES on the new database to 'holberton_user'
GRANT SELECT
  ON `tyrell_corp`.*
  TO 'holberton_user'@'localhost';
