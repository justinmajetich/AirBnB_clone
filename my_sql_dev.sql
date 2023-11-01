IF NOT EXISTS hbnb_dev_db
CREATE hbnb_dev_db
GRANT ALL *.* TO hbnb_dev_db IDENTIFIED BY 'hbnb_dev_pwd'
GRANT SELECT *.* TO preformace_schema IDENTIFIED BY 'hbnb_dev_pwd';
