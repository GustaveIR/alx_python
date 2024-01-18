-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;

-- Use the database
USE hbtn_0e_6_usa;

-- Create the 'states' table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);
