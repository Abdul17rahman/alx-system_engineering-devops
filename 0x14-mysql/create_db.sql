-- Creates a database tyrell_corp
-- Creates a table nexus6
-- Add atleast one row.
-- Grant holberton_user privileges to select

CREATE DATABASE
	IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE
	IF NOT EXISTS nexus6
	(id INT, name VARCHAR(256));
INSERT INTO nexus6(id, name)
	VALUES(1, "Abdul");
GRANT SELECT
	ON tyrell_corp.*
	TO 'holberton_user'@'localhost';
