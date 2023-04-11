CREATE DATABASE IF NOT EXISTS Tictag;

USE Tictag;

CREATE TABLE `employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL,
  `position` varchar(80) NOT NULL,
  `department` varchar(80) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `script_requests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `employee_id` int(11) NOT NULL,
  `project` varchar(120) NOT NULL,
  `request_description` varchar(600) NOT NULL,
  `impact` varchar(80) NOT NULL,
  `urgency` varchar(80) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_employee_id`
    FOREIGN KEY (`employee_id`)
    REFERENCES `employees` (`id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `scripts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `script_name` varchar(80) NOT NULL,
  `script_description` varchar(600) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `project` varchar(120) NOT NULL,
  `created_by` varchar(80) NOT NULL,
  `request_id` int(11) DEFAULT NULL,
  `script_link` varchar(400) NOT NULL,
  `comments` varchar(1000) DEFAULT "No Comments",
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO scripts values 

(1, 'Count Bounding Boxes (YOLO)', 'Counting the number of Bounding Boxes in a YOLO file', 'Chirag', 'Any Bounding Box Project', 'https://replit.com/join/qmcukdufdq-chiragnagpal1'),
(2, 'Count Bounding Boxes (XML)', 'Counting the number of Bounding Boxes in XML file', 'Chirag', 'Any Bounding Box Project', 'https://replit.com/join/znejwemvsr-chiragnagpal1'),
(3, 'Count Bounding Boxes in JSON', 'Counting the number of Bounding Boxes in a JSON file', 'Chirag', 'Any Bounding Box Project', ''),
(4, 'approve-all-coins', '[JOB-BOARD] - Mass approve all coins for the tasks on the job board. However, can only do a fixed number of coins to every user.', 'Yihang', 'No specific Project Has been used for CONVIN in the past', 'https://replit.com/join/kamkjblbzg-chiragnagpal1'),
(5, 'force-assign-user-to-subjob', '[JOB-BOARD] - To force assign a user to a few subjobs. Only subjobs which have exactly the number of items to be assigned will be considered.', 'Yihang', 'No specific Project', 'https://replit.com/join/vrqfluctrk-chiragnagpal1'),
(6, 'remove-all-from-job-board', '[JOB-BOARD] - To remove all items from job board for certain job IDs', 'Yihang', 'No specific Project', 'https://replit.com/join/ubnitooguo-chiragnagpal1'),
(7, 'Images-No-Bounding_Boxes', 'Count the number of images having no polygons tags (No bouding Boxes)', 'Chirag', 'TUV-SUD', 'https://replit.com/join/djvkhmectg-chiragnagpal1'),
(8, 'Folder-Categorisation', 'We have multiple scripts allowing for folder management - \n1. Move images/documents/files based on their tags (CSV) to different folders.', 'Chirag', 'TUV-SUD, Eyesee, Superbin, Convin', 'https://replit.com/join/uqbzumrlkt-chiragnagpal1');

--