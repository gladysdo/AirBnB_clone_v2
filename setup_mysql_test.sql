-- create a database  MySQL server for the project
CREATE database IF NOT EXISTS hbnb_test_db;
-- create a user
CREATE user IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant privillage
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
