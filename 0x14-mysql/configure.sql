-- Configure SQL on the servers

-- Create a user for the checker
CREATE USER IF NOT EXISTS
  'holberton_user'@'localhost'
  IDENTIFIED BY 'projectcorrection280hbtn';

-- Grant the access to the replication status to holberton_user
GRANT REPLICATION CLIENT
  ON *.*
  TO 'holberton_user'@'localhost';

FLUSH PRIVILEGES;
