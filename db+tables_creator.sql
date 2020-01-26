create database apartments;
use apartments;
CREATE TABLE `apartment_a` (
  `date` date NOT NULL,
  `water` int DEFAULT NULL,
  `electricity` int DEFAULT NULL,
  `total_water` varchar(45) DEFAULT NULL,
  `total_electricity` varchar(45) DEFAULT NULL,
  `total_payment` int DEFAULT NULL,
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
insert into apartment_a 
values('2000-01-01', 0,0,null,null,null);
CREATE TABLE `apartment_b` (
  `date` date NOT NULL,
  `water` int DEFAULT NULL,
  `electricity` int DEFAULT NULL,
  `total_water` varchar(45) DEFAULT NULL,
  `total_electricity` varchar(45) DEFAULT NULL,
  `total_payment` int DEFAULT NULL,
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
insert into apartment_b 
values('2000-01-01', 0,0,null,null,null);