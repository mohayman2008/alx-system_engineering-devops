-- Configure MySQL Replication on the source server

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

-- Create a  replication user
CREATE USER IF NOT EXISTS
  'replica_user'@'%'
  IDENTIFIED BY 'replicate';

-- Grant 'replica_user' the required privilages to be able to replicate the primary database
GRANT REPLICATION SLAVE
  ON *.*
  TO 'replica_user'@'%';

-- Grant SELECT PRIVILAGES on `mysql`.`user` to 'holberton_user'
GRANT SELECT
  ON `mysql`.`user`
  TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;

-- Retrieving Binary Log Coordinates
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
