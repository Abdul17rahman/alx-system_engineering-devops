-- Setup replica on a slave for alx_web01

CHANGE REPLICATION SOURCE TO
SOURCE_HOST='3.80.18.141',
SOURCE_USER='replica_user',
SOURCE_PASSWORD='Abdulrahman_1',
SOURCE_LOG_FILE='mysql-bin.000001',
SOURCE_LOG_POS=899;
START REPLICA;
