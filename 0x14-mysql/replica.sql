-- Configure MySQL Replication on the source server

-- Set the master server
CHANGE MASTER TO
MASTER_HOST='52.91.120.176',
MASTER_USER='replica_user',
MASTER_PASSWORD='replicate',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=4227;

# Start the replication
START SLAVE;
