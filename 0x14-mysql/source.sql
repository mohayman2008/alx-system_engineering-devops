-- Configure MySQL Replication on the source server

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
