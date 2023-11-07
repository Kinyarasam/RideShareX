-- This script prepares a MySQL servr for the project
-- Create project deving database with the name : ride_share_x_dev_db
CREATE DATABASE IF NOT EXISTS ride_share_x_dev_db ;
-- Create a new user named : ride_share_x_dev with all priveledges on the db ride_share_x_dev_db
-- with the password : ride_share_x_dev_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'ride_share_x_dev'@'localhost' IDENTIFIED BY 'ride_share_x_dev_pwd';
-- Granting all priviledges to the new user
GRANT ALL PRIVILEGES ON ride_share_x_dev_db.* TO 'ride_share_x_dev'@'localhost';
FLUSH PRIVILEGES;
-- Granting the SELECT priviledge for the user ride_share_x_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'ride_share_x_dev'@'localhost';
FLUSH PRIVILEGES;
