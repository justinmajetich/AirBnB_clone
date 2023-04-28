-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: hbnb_dev_db
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Drop database
DROP DATABASE IF EXISTS hbnb_dev_db;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

USE hbnb_dev_db;

--
-- Table structure for table `amenities`
--

DROP TABLE IF EXISTS `amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amenities` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amenities`
--

LOCK TABLES `amenities` WRITE;
/*!40000 ALTER TABLE `amenities` DISABLE KEYS */;
/*!40000 ALTER TABLE `amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cities` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `state_id` varchar(60) NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `state_id` (`state_id`),
  CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES ('1f024cf1-7a07-47ed-8a39-52b07d3df3c6','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479549','Orlando'),('37de0299-f3ed-46ec-9ea6-21e977d8fc20','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479547','San Francisco'),('5d6f5de6-cdd4-4f9c-8f12-75417cfe7b6d','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479546','Phoenix'),('6e50f6a5-0d22-4f3d-9b39-0136a247e221','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479545','Montgomery'),('80f25c04-0b60-404e-bf16-cccbef1840c4','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479550','Savannah'),('9de4f140-ff63-4b92-9343-8a828c03e310','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479550','Atlanta'),('bbd1c8a3-48e3-48b6-b276-9438a01b390e','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479546','Tucson'),('c0549ab4-9564-4252-94a3-3a1b55f48c01','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479548','Denver'),('c7e18e3b-9d1f-4bb3-baa3-eb5a6f8e6d00','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479545','Birmingham'),('city100278524560015360','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479546','City in Arizona'),('city100278524560015361','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479550','City in Georgia'),('city100278524560015362','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479549','City in Florida'),('city100278524560015363','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479545','City in Alabama'),('city100278524560015364','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479555','City in Minnesota'),('city100278524560015365','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479557','City in Oregon'),('city100278524560015366','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479547','City in California'),('city100278524560015367','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479553','City in Indiana'),('city100278524560015368','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479548','City in Colorado'),('city100278524560015369','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479554','City in Louisiana'),('city100278524560015370','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479552','City in Illinois'),('city100278524560015371','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479556','City in Mississippi'),('city100278524560015372','2023-04-22 09:24:13','2023-04-22 09:24:13','421a55f4-7d82-47d9-b54c-a76916479551','City in Hawaii'),('db905277-b450-4952-883c-bf1fc6f56fc6','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479549','Miami'),('edfcb354-45ba-4478-bcc1-45e57c19cf35','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479547','Los Angeles'),('f16e21e7-7af2-4fbb-9dc4-25be36093e8d','2023-04-22 08:35:20','2023-04-22 08:35:20','421a55f4-7d82-47d9-b54c-a76916479548','Colorado Springs');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `place_amenity`
--

DROP TABLE IF EXISTS `place_amenity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `place_amenity` (
  `place_id` varchar(60) NOT NULL,
  `amenity_id` varchar(60) NOT NULL,
  PRIMARY KEY (`place_id`,`amenity_id`),
  KEY `amenity_id` (`amenity_id`),
  CONSTRAINT `place_amenity_ibfk_1` FOREIGN KEY (`place_id`) REFERENCES `places` (`id`),
  CONSTRAINT `place_amenity_ibfk_2` FOREIGN KEY (`amenity_id`) REFERENCES `amenities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `place_amenity`
--

LOCK TABLES `place_amenity` WRITE;
/*!40000 ALTER TABLE `place_amenity` DISABLE KEYS */;
/*!40000 ALTER TABLE `place_amenity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `places`
--

DROP TABLE IF EXISTS `places`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `places` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `city_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `name` varchar(128) NOT NULL,
  `description` varchar(128) DEFAULT NULL,
  `number_rooms` int NOT NULL,
  `number_bathrooms` int NOT NULL,
  `max_guest` int NOT NULL,
  `price_by_night` int NOT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `city_id` (`city_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `places_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`),
  CONSTRAINT `places_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `places`
--

LOCK TABLES `places` WRITE;
/*!40000 ALTER TABLE `places` DISABLE KEYS */;
/*!40000 ALTER TABLE `places` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `place_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `text` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `place_id` (`place_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`place_id`) REFERENCES `places` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `states`
--

DROP TABLE IF EXISTS `states`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `states` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `states`
--

LOCK TABLES `states` WRITE;
/*!40000 ALTER TABLE `states` DISABLE KEYS */;
INSERT INTO `states` VALUES ('421a55f4-7d82-47d9-b54c-a76916479545','2017-03-25 19:42:40','2017-03-25 19:42:40','Alabama'),('421a55f4-7d82-47d9-b54c-a76916479546','2017-03-25 19:42:40','2017-03-25 19:42:40','Arizona'),('421a55f4-7d82-47d9-b54c-a76916479547','2017-03-25 19:42:40','2017-03-25 19:42:40','California'),('421a55f4-7d82-47d9-b54c-a76916479548','2017-03-25 19:42:40','2017-03-25 19:42:40','Colorado'),('421a55f4-7d82-47d9-b54c-a76916479549','2017-03-25 19:42:40','2017-03-25 19:42:40','Florida'),('421a55f4-7d82-47d9-b54c-a76916479550','2017-03-25 19:42:40','2017-03-25 19:42:40','Georgia'),('421a55f4-7d82-47d9-b54c-a76916479551','2017-03-25 19:42:40','2017-03-25 19:42:40','Hawaii'),('421a55f4-7d82-47d9-b54c-a76916479552','2017-03-25 19:42:40','2017-03-25 19:42:40','Illinois'),('421a55f4-7d82-47d9-b54c-a76916479553','2017-03-25 19:42:40','2017-03-25 19:42:40','Indiana'),('421a55f4-7d82-47d9-b54c-a76916479554','2017-03-25 19:42:40','2017-03-25 19:42:40','Louisiana'),('421a55f4-7d82-47d9-b54c-a76916479555','2017-03-25 19:42:40','2017-03-25 19:42:40','Minnesota'),('421a55f4-7d82-47d9-b54c-a76916479556','2017-03-25 19:42:40','2017-03-25 19:42:40','Mississippi'),('421a55f4-7d82-47d9-b54c-a76916479557','2017-03-25 19:42:40','2017-03-25 19:42:40','Oregon');
/*!40000 ALTER TABLE `states` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-22  9:27:32
-- easy way to generate cities based on states
INSERT INTO cities (id, created_at, updated_at, state_id, name)
SELECT CONCAT('city', UUID_SHORT()), NOW(), NOW(), states.id, CONCAT('City in ', states.name)
FROM states
ORDER BY RAND()
LIMIT 15;
