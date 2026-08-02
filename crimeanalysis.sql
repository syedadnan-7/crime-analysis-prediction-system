-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2024 at 10:18 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crimeanalysis`
--

-- --------------------------------------------------------

--
-- Table structure for table `crimedetails`
--

CREATE TABLE `crimedetails` (
  `crimeid` int(5) NOT NULL,
  `userid` varchar(5) NOT NULL,
  `category` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `datetime` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `crimedetails`
--

INSERT INTO `crimedetails` (`crimeid`, `userid`, `category`, `fname`, `datetime`, `address`, `description`) VALUES
(1, '1', 'Theft', '', '2024-07-17T01:02', 'Online Mode', 'On July 15, 2024, at approximately 10:30 PM, a theft occurred at 123 Main Street. An unknown suspect forcefully entered the residence through a rear window and stole valuable electronics and jewelry. The homeowner reported hearing glass breaking and immed'),
(2, '1', 'Assault', '', '2024-07-17T01:02', 'Online Mode', 'The suspect is described as a male, approximately 6 feet tall, wearing a dark hoodie and jeans. Surveillance footage from neighboring houses captured a person matching this description fleeing the scene carrying a backpack.\n'),
(3, '1', 'Theft', '', '2024-07-17T01:02', 'Online Mode', 'The investigation is ongoing, and anyone with information about this incident is urged to contact the local police department at [phone number] or Crime Stoppers at [website or phone number].``\n'),
(4, '1', 'Theft', 'data.jpg', '2024-07-18 14:30:00', '123 Main St', 'Stolen electronics and jewelry from residence.'),
(5, '1', 'Assault', '', '2024-07-19 21:15:00', '456 Oak Ave', 'Physical altercation outside a bar.'),
(6, '1', 'Vandalism', 'graffiti.png', '2024-07-20 08:00:00', '789 Elm Rd', 'Public property vandalism with graffiti.'),
(7, '1', 'Robbery', 'mask.jpg', '2024-07-21 17:45:00', '321 Pine Blvd', 'Armed robbery at a convenience store.'),
(8, '1', 'Theft', 'data.jpg', '2024-07-18 14:30:00', '123 Main St', 'Stolen electronics and jewelry from residence.'),
(9, '1', 'Assault', '', '2024-07-19 21:15:00', '456 Oak Ave', 'Physical altercation outside a bar.'),
(10, '1', 'Vandalism', 'graffiti.png', '2024-07-20 08:00:00', '789 Elm Rd', 'Public property vandalism with graffiti.'),
(11, '1', 'Robbery', 'mask.jpg', '2024-07-21 17:45:00', '321 Pine Blvd', 'Armed robbery at a convenience store.'),
(12, '1', 'Burglary', '', '2024-07-22 10:00:00', '567 Cedar Ln', 'Residential break-in, valuables stolen.'),
(13, '1', 'Fraud', '', '2024-07-23 12:30:00', '890 Maple Dr', 'Credit card fraud reported by local businesses.'),
(14, '1', 'Drug Offense', '', '2024-07-24 16:20:00', '234 Birch Ave', 'Drug trafficking apprehended during routine patrol.'),
(15, '1', 'Kidnapping', '', '2024-07-25 09:45:00', '678 Walnut St', 'Child abduction attempt near local park.'),
(16, '1', 'Homicide', '', '2024-07-26 19:00:00', '901 Pinecrest Rd', 'Investigation underway following a fatal shooting.'),
(17, '1', 'Arson', 'fire.jpg', '2024-07-27 03:00:00', '345 Oakwood Ln', 'Suspected arson incident at abandoned warehouse.'),
(18, '1', 'Assault', '', '2024-07-28 13:15:00', '432 Elmwood Ave', 'Physical altercation between neighbors.'),
(19, '1', 'Theft', 'jewelry.jpg', '2024-07-29 18:30:00', '876 Oak Ridge Dr', 'Jewelry theft reported from a local store.'),
(20, '1', 'Burglary', '', '2024-07-30 22:00:00', '543 Cedar Ridge Rd', 'Residential burglary, entry through back door.'),
(21, '1', 'Fraud', '', '2024-07-31 11:45:00', '234 Maplewood Ln', 'Identity theft reported to local police.'),
(22, '1', 'Drug Offense', '', '2024-08-01 09:00:00', '789 Birchwood Ave', 'Drug possession arrest during traffic stop.'),
(23, '1', 'Arson', 'building_fire.jpg', '2024-08-02 04:30:00', '101 Pinehurst Ave', 'Suspicious fire incident at commercial building.'),
(24, '1', 'Kidnapping', '', '2024-08-03 20:20:00', '567 Oak Hill Rd', 'Attempted kidnapping of a child at local park.'),
(25, '1', 'Vandalism', 'broken_window.jpg', '2024-08-04 15:00:00', '890 Elmwood Blvd', 'Vandalism of public property, broken windows.'),
(26, '1', 'Robbery', 'masked_robber.jpg', '2024-08-05 12:45:00', '321 Pinecrest Ct', 'Armed robbery at a gas station.'),
(27, '1', 'Homicide', '', '2024-08-06 19:30:00', '654 Maple Ave', 'Investigation ongoing following a fatal stabbing.'),
(28, '1', 'Theft', 'stolen_car.jpg', '2024-08-07 08:00:00', '987 Oakwood Rd', 'Vehicle theft reported, stolen car.'),
(29, '1', 'Assault', '', '2024-08-08 10:15:00', '345 Cedar Blvd', 'Assault incident at a nightclub.'),
(30, '1', 'Burglary', '', '2024-08-09 23:00:00', '678 Birchwood Dr', 'Residential burglary, forced entry through window.'),
(31, '1', 'Fraud', '', '2024-08-10 14:30:00', '123 Maple Ridge Ave', 'Credit card fraud reported at a local store.'),
(32, '1', 'Drug Offense', '', '2024-08-11 07:45:00', '456 Elmwood Ave', 'Drug trafficking apprehended in a raid.'),
(33, '1', 'Arson', 'burned_car.jpg', '2024-08-12 02:00:00', '789 Pine Hill Rd', 'Arson incident involving a burned vehicle.'),
(34, '1', 'Kidnapping', '', '2024-08-13 21:00:00', '234 Oakwood Ln', 'Child abduction reported near school.'),
(35, '1', 'Vandalism', 'graffiti_wall.jpg', '2024-08-14 16:30:00', '567 Cedar Ave', 'Graffiti vandalism on public wall.'),
(36, '1', 'Robbery', 'masked_assailant.jpg', '2024-08-15 13:00:00', '890 Birch Ridge Dr', 'Robbery at a convenience store.'),
(37, '1', 'Homicide', '', '2024-08-16 18:00:00', '101 Pinecrest Rd', 'Fatal shooting incident under investigation.'),
(38, '1', 'Theft', 'shoplifting.jpg', '2024-08-17 09:30:00', '432 Maplewood Ave', 'Shoplifting reported at retail store.'),
(39, '1', 'Assault', '', '2024-08-18 11:45:00', '654 Elm Ridge Blvd', 'Physical assault outside a restaurant.'),
(40, '1', 'Burglary', '', '2024-08-19 22:30:00', '876 Cedar Hill Dr', 'Burglary at a warehouse, valuable items stolen.'),
(41, '1', 'Fraud', '', '2024-08-20 14:00:00', '543 Oakwood Ct', 'Fraudulent transactions reported by bank customers.'),
(42, '1', 'Drug Offense', '', '2024-08-21 06:15:00', '789 Maple Ridge Rd', 'Drug possession arrest during traffic stop.'),
(43, '1', 'Arson', 'building_fire2.jpg', '2024-08-22 03:45:00', '345 Birchwood Blvd', 'Fire incident at an abandoned building.'),
(44, '1', 'Kidnapping', '', '2024-08-23 19:45:00', '901 Oak Hill Rd', 'Attempted kidnapping of a teenager.'),
(45, '1', 'Vandalism', 'graffiti_park.jpg', '2024-08-24 17:15:00', '234 Cedar Ave', 'Graffiti vandalism in city park.'),
(46, '1', 'Robbery', 'masked_thief.jpg', '2024-08-25 12:00:00', '678 Pine Hill Ave', 'Robbery at a gas station, suspect wore a mask.'),
(47, '1', 'Homicide', '', '2024-08-26 20:00:00', '101 Elmwood Ln', 'Investigation underway following a homicide incident.'),
(48, '1', 'Theft', 'stolen_bike.jpg', '2024-08-27 08:45:00', '432 Oak Ridge Dr', 'Bicycle theft reported from residential area.'),
(49, '1', 'Assault', '', '2024-08-28 09:30:00', '876 Maple Ave', 'Assault incident at a sports event.'),
(50, '1', 'Burglary', '', '2024-08-29 21:00:00', '543 Cedar Ridge Rd', 'Residential burglary, intruder broke in through window.'),
(51, '1', 'Fraud', '', '2024-08-30 15:30:00', '234 Maplewood Ln', 'Identity theft and fraudulent charges reported.'),
(52, '1', 'Drug Offense', '', '2024-08-31 07:00:00', '789 Birchwood Ave', 'Drug trafficking operation dismantled by authorities.'),
(53, '1', 'Arson', 'burned_house.jpg', '2024-09-01 01:30:00', '101 Pinehurst Ave', 'Arson incident involving a residential property.'),
(54, '1', 'Kidnapping', '', '2024-09-02 18:30:00', '567 Oak Hill Rd', 'Attempted kidnapping of a child at local playground.'),
(55, '1', 'Vandalism', 'broken_statue.jpg', '2024-09-03 16:45:00', '890 Elmwood Blvd', 'Vandalism of public statue, significant damage.'),
(56, '1', 'Robbery', 'bank_robbery.jpg', '2024-09-04 13:15:00', '321 Pinecrest Ct', 'Bank robbery incident with multiple suspects.'),
(57, '1', 'Homicide', '', '2024-09-05 19:45:00', '654 Maple Ave', 'Fatal shooting in a residential area, investigation ongoing.'),
(58, '1', 'Theft', 'shoplifting2.jpg', '2024-09-06 10:30:00', '987 Oakwood Rd', 'Shoplifting reported at a local mall.'),
(59, '1', 'Assault', '', '2024-09-07 11:15:00', '345 Cedar Blvd', 'Assault outside a nightclub, altercation between groups.'),
(60, '1', 'Burglary', '', '2024-09-08 22:45:00', '678 Birchwood Dr', 'Burglary at a store, items stolen from the premises.'),
(61, '1', 'Fraud', '', '2024-09-09 14:15:00', '123 Maple Ridge Ave', 'Credit card fraud detected by financial institution.'),
(62, '1', 'Drug Offense', '', '2024-09-10 08:30:00', '456 Elmwood Ave', 'Drug seizure operation by law enforcement.'),
(63, '1', 'Arson', 'car_fire.jpg', '2024-09-11 04:00:00', '789 Pine Hill Rd', 'Car set on fire, suspected arson incident.'),
(64, '1', 'Kidnapping', '', '2024-09-12 20:15:00', '234 Oakwood Ln', 'Child abduction attempt foiled by bystanders.'),
(65, '1', 'Vandalism', 'graffiti_school.jpg', '2024-09-13 17:00:00', '567 Cedar Ave', 'Graffiti vandalism on school property.');

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

CREATE TABLE `userdetails` (
  `userid` int(5) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `usingfor` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userdetails`
--

INSERT INTO `userdetails` (`userid`, `name`, `email`, `phone`, `password`, `usingfor`, `address`, `created_at`) VALUES
(1, 'ppPrithiviraj', 'prithivirajk2503@gmail.com', '6381268718', '12345', 'Demo', '123', NULL),
(2, 'Vignesh', 'vig55549@gmail.com', '9098980989', '12345', 'Demo', '123', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `crimedetails`
--
ALTER TABLE `crimedetails`
  ADD PRIMARY KEY (`crimeid`);

--
-- Indexes for table `userdetails`
--
ALTER TABLE `userdetails`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `crimedetails`
--
ALTER TABLE `crimedetails`
  MODIFY `crimeid` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `userdetails`
--
ALTER TABLE `userdetails`
  MODIFY `userid` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
