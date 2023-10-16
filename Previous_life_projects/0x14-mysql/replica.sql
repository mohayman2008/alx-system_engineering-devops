-- Configure MySQL Replication on the source server

-- Set the master server
CHANGE MASTER TO
MASTER_HOST='54.90.15.29',
MASTER_USER='replica_user',
MASTER_PASSWORD='replicate',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=154;

# Start the replication
START SLAVE;
