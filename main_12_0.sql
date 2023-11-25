-- Doc
USE hbnb_dev_db;
INSERT INTO users (id, email, password, first_name, last_name, created_at, updated_at) VALUES ("my_id_0", "email0@gmail.com", "pwd0", "John", "Doe", CURDATE(), CURDATE());
INSERT INTO users (id, email, password, first_name, created_at, updated_at) VALUES ("my_id_1", "email1@gmail.com", "pwd1", "Bob", CURDATE(), CURDATE());
INSERT INTO users (id, email, password, last_name, created_at, updated_at) VALUES ("my_id_2", "email2@gmail.com", "pwd2", "Did", CURDATE(), CURDATE());
INSERT INTO users (id, email, password, created_at, updated_at) VALUES ("my_id_3", "email3@gmail.com", "pwd3", CURDATE(), CURDATE());
