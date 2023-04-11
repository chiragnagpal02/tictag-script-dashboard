-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Apr 10, 2023 at 09:23 AM
-- Server version: 5.7.34
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tictag_scripts`
--

-- --------------------------------------------------------

--
-- Table structure for table `script_package_1`
--

CREATE TABLE `script_package_1` (
  `script_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `location_link` varchar(900) DEFAULT NULL,
  `created_by` varchar(100) DEFAULT NULL,
  `specific_project` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `script_package_1`
--

INSERT INTO `script_package_1` (`script_id`, `name`, `description`, `location_link`, `created_by`, `specific_project`) VALUES
(1, 'Count Bounding Boxes (YOLO)', 'Counting the number of Bounding Boxes in a YOLO file', 'Chirag', 'Any Bounding Box Project', 'https://replit.com/join/qmcukdufdq-chiragnagpal1'),
(2, 'Count Bounding Boxes (XML)', 'Counting the number of Bounding Boxes in XML file', 'Chirag', 'Any Bounding Box Project', 'https://replit.com/join/znejwemvsr-chiragnagpal1'),
(3, 'Count Bounding Boxes in JSON', 'Counting the number of Bounding Boxes in a JSON file', 'Chirag', 'Any Bounding Box Project', ''),
(4, 'approve-all-coins', '[JOB-BOARD] - Mass approve all coins for the tasks on the job board. However, can only do a fixed number of coins to every user.', 'Yihang', 'No specific Project Has been used for CONVIN in the past', 'https://replit.com/join/kamkjblbzg-chiragnagpal1'),
(5, 'force-assign-user-to-subjob', '[JOB-BOARD] - To force assign a user to a few subjobs. Only subjobs which have exactly the number of items to be assigned will be considered.', 'Yihang', 'No specific Project', 'https://replit.com/join/vrqfluctrk-chiragnagpal1'),
(6, 'remove-all-from-job-board', '[JOB-BOARD] - To remove all items from job board for certain job IDs', 'Yihang', 'No specific Project', 'https://replit.com/join/ubnitooguo-chiragnagpal1'),
(7, 'Images-No-Bounding_Boxes', 'Count the number of images having no polygons tags (No bouding Boxes)', 'Chirag', 'TUV-SUD', 'https://replit.com/join/djvkhmectg-chiragnagpal1'),
(8, 'Folder-Categorisation', 'We have multiple scripts allowing for folder management - \n1. Move images/documents/files based on their tags (CSV) to different folders.', 'Chirag', 'TUV-SUD, Eyesee, Superbin, Convin', 'https://replit.com/join/uqbzumrlkt-chiragnagpal1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `script_package_1`
--
ALTER TABLE `script_package_1`
  ADD PRIMARY KEY (`script_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
