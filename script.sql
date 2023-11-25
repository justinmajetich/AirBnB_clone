-- Doc
USE hbnb_dev_db;
SELECT 
    a.name, p.name 
FROM 
    place_amenity AS pa JOIN places AS p ON pa.place_id = p.id 
    JOIN amenities AS a ON pa.amenity_id = a.id
ORDER BY a.name, p.name DESC;
