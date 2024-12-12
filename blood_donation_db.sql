-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2024 at 01:22 AM
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
-- Database: `blood_donation_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `adminID` int(11) NOT NULL,
  `admin_email` varchar(100) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`adminID`, `admin_email`, `username`, `password`) VALUES
(1, 'karlmrsgn05@gmail.com', 'Admin', 'imissyou'),
(2, 'minji@newjeans.com', 'Minji', 'minji123'),
(3, 'hanni@newjeans.com', 'Hanni', 'hanni2024'),
(4, 'danielle@newjeans.com', 'Danielle', 'dani456'),
(5, 'haerin@newjeans.com', 'Haerin', 'haerin789'),
(6, 'hyein@newjeans.com', 'Hyein', 'hyein567'),
(7, 'nayeon@twice.com', 'Nayeon', 'nayeonlove'),
(8, 'sana@twice.com', 'Sana', 'sanaforever'),
(9, 'momo@twice.com', 'Momo', 'momoqueen'),
(10, 'jihyo@twice.com', 'Jihyo', 'jihyo99');

-- --------------------------------------------------------

--
-- Table structure for table `donor_message`
--

CREATE TABLE `donor_message` (
  `donorMessID` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `donor_message` text DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `mess_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `donor_message`
--

INSERT INTO `donor_message` (`donorMessID`, `email`, `donor_message`, `user_id`, `mess_date`) VALUES
(1, 'karlmtsgn05@gmail.com', 'dadadadknjasFNJNFA', 19, '2024-12-07 02:03:15'),
(2, 'hehehe@gmail.com', 'dadadadaxcsa', 39, '2024-12-08 12:53:27'),
(3, 'hehehe@gmail.com', 'dadada', 39, '2024-12-08 12:53:30'),
(4, 'karlmrsgn000000@gmail.com', 'hello po', 23, '2024-12-07 02:03:15'),
(5, 'nicoleingco0@gmail.com', 'Kindly Process my application. thankyou!', 44, '2024-12-07 02:03:15'),
(6, 'jehoshuadimayuga@gmail.com', 'Process mo to boss\n', 45, '2024-12-07 02:03:15'),
(7, 'nicoleingco@gmail.com', 'annyeong\n', 21, '2024-12-07 02:03:15'),
(8, 'nicoleingco@gmail.com', 'hi', 21, '2024-12-07 02:03:15'),
(9, 'nicoleingco@gmail.com', 'dadadadada', 21, '2024-12-07 02:04:27'),
(10, 'nicoleingco@gmail.com', 'hehe', 21, '2024-12-07 04:35:58'),
(11, 'karlmarasigan0505050505@gmail.com', 'Process my application', 55, '2024-12-09 16:24:59'),
(12, 'karlmrsgn01234567@gmail.com', 'Please process my application', 56, '2024-12-09 16:31:11'),
(13, 'ingconicolee@gmail.com', 'Kindly process my application, thankyou!', 57, '2024-12-09 16:45:23'),
(14, 'jaspher@gmail.com', 'dadadada', 58, '2024-12-11 02:27:25');

-- --------------------------------------------------------

--
-- Table structure for table `donor_users`
--

CREATE TABLE `donor_users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `middle_initial` char(1) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `contact` varchar(15) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `blood_group` varchar(5) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `date_issued` date DEFAULT curdate()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `donor_users`
--

INSERT INTO `donor_users` (`id`, `first_name`, `middle_initial`, `last_name`, `contact`, `age`, `gender`, `blood_group`, `status`, `address`, `email`, `password`, `date_issued`) VALUES
(16, 'Kiko Battery', 'D', 'Marasigan', '09925265374', 19, 'Female', 'A+', 'Processed', 'Sta. Rita Karsada Batangas city, Batangas ', 'karlmrsgn000@gmail.com', 'nicole', NULL),
(18, 'Karl Matthew', 'D', 'Marasigan', '09454121330', 19, 'Male', 'O+', 'Done', 'Sta. Rita Krasada Batangas city', 'karlmrsgn1@gmail.com', '110923', NULL),
(19, 'Karl Matthew', 'D', 'Marasigan', '09999999999', 21, 'Male', 'A-', 'Processed', 'sta. Rita', 'karlmtsgn05@gmail.com', '12345', NULL),
(20, 'Karl Marasigan', 'D', 'Marasigan', '09454211330', 19, 'Male', 'O+', 'Done', 'Sta. Rita Karasada Batangas city, Batangas', '23-08160@gmail.com', 'karl12345', '2024-11-22'),
(21, 'Princess Nicole', 'C', 'Ingco', '09454211330', 20, 'Female', 'B-', 'Done', 'Banaba Apool Batangas city, Batangas', 'nicoleingco@gmail.com', '12345', '2024-11-22'),
(22, 'Karl Matthew', 'D', 'Marasigan', '09454211330', 19, 'Male', 'B-', 'Done', 'Sta. Rita Karsada Batangas city', 'Karlmatthew05@gmail.com', '12345', '2024-11-22'),
(23, 'Karl Matthew ', 'D', 'Marasigan', '09454211330', 23, 'Male', 'B+', 'Done', 'Sta. Rita Karsada batangas city, Batanagas', 'karlmrsgn000000@gmail.com', 'karl12345', '2024-11-23'),
(24, 'Karl Matthew', 'D', 'Marasigan', '099454211330', 23, 'Male', 'A-', 'Processed', 'Sta. Rita Karsada Batangas city, Batangas', 'okiksmarasigan@gmai.com', '12345', '2024-11-23'),
(25, 'Lance Edward', 'V', 'Dela Rosa', '09454211330', 21, 'Male', 'AB+', 'Done', 'Quezon', 'lanceedward@gmail.com', '12345', '2024-11-23'),
(27, 'Karl Matthew', 'D', 'Marasigan', '09454211330', 23, 'Male', 'B+', 'Processed', 'Sta. rita', 'kikobatttt@gmail.com', '12345', '2024-11-23'),
(30, 'karl', 'd', 'Marasigan', '09454211330', 23, 'Male', 'O+', 'Done', 'Sta. Rita Karsada', 'kikomarasigan05@gmail.com', '12345', '2024-11-24'),
(31, 'Karl Matthew', 'D', 'Marasigan', '09454211330', 23, 'Male', 'B-', 'Processed', 'Sta. Rita Karsada Batangas', 'karlkiko@gmail.com', '12345', '2024-11-25'),
(32, 'Karl Matthew', 'D', 'Marasigan', '09454211330', 23, 'Male', 'AB+', 'Done', 'Sta. Rita Karsada Batangas city', 'karlmarasigan1234567@gmail.com', '12345', '2024-11-25'),
(33, 'Karl', 'D', 'Marasigan', '09454211330', 32, 'Male', 'AB-', 'Done', 'Sta. RIta karsada', 'karlm050505@gmail.com', '12345', '2024-11-25'),
(34, 'Karl', 'D', 'Marasigan', '094542113392', 21, 'Male', 'AB-', 'Done', 'Sta. Rita Karsada Batangas city', '0kiks@gmail.com', '12345', '2024-11-25'),
(35, 'Karl Matthew', 'D', 'Marasigan', '09925265374', 19, 'Male', 'AB-', 'Done', 'Sta. Rita Karsada Batangas city', 'koki@gmail.com', '12345', '2024-11-25'),
(36, 'John Lex', 'D', 'Bacani', '09454211330', 21, 'Male', 'AB-', 'Done', 'Bonliw', 'johnlex@gmail.com', '12345', '2024-11-26'),
(37, 'Lair', 'M', 'Balmes', '09291604014', 19, 'Male', 'O+', 'Done', 'Mangilag Sur, Candelaria, Quezon', 'balmesbroz@gmail.com', 'titeko', '2024-11-26'),
(39, 'Paul Jehoshua', 'A', 'Dimayuga', '09454211330', 19, 'Male', 'B+', 'Processed', 'Bauan Batangas', 'hehehe@gmail.com', '12345', '2024-11-27'),
(40, 'ayelet', '', 'de castro', '09292261060', 19, 'Male', 'A+', 'Processed', 'pallocan east', 'ayelet@gmail.com', '123123', '2024-11-27'),
(41, 'Karl Matthew', 'M', 'Marasigan', '09454211330', 19, 'Male', 'O+', 'Processed', 'Sta. Rita Karsada Batangas city, Batangas', 'karlmrsgn1234567@gmail.com', '12345', '2024-12-01'),
(44, 'Princess Nicole', 'C', 'Ingco', '09925265374', 20, 'Female', 'AB+', 'Done', 'Sta. Rita Karsada Batangas city', 'nicoleingco0@gmail.com', '12345', '2024-12-02'),
(45, 'Paul Jehoshua', 'T', 'Dimayuga', '0999699999', 13, 'Male', 'AB+', 'Done', 'Bauan Batangas', 'jehoshuadimayuga@gmail.com', '12345', '2024-12-04'),
(46, 'Karl Matthew', 'D', 'Marasigan', '09454211330', 19, 'Male', 'O+', 'Processed', 'Sta. Rita Karsada Batangas city, Batangas', 'karlmrsgn05050505@gmail.com', '12345', '2024-12-08'),
(47, 'Cedric', 'E', 'Laja', '09123456789', 20, 'Male', 'AB+', 'Done', 'Hilltop Rd. Batangas city', 'cedriclaja@gmail.com', '12345', '2024-12-08'),
(48, 'Carlos Daniel', 'M', 'Sendin', '09123456789', 20, 'Female', 'AB+', 'Processed', 'Alangilan Batangas city, Batangas', 'carlosdaniel@gmail.com', '12345', '2024-12-08'),
(49, 'Lance Edward', 'V', 'Dela Rosa', '09123456789', 50, 'Male', 'A+', 'Processed', 'Quezon', 'delarosalance@gmail.com', '12345', '2024-12-08'),
(50, 'Karl', 'J', 'Catipan', '09123456789', 70, 'Female', 'O-', 'Pending', 'Tabangao Aplaya Batangas city, Batangas', 'catipays@gmail.com', '12345', '2024-12-08'),
(51, 'Lair Broz', 'D', 'Balmes', '09123456789', 20, 'Male', 'B-', 'Pending', 'Candelaria Quezon city', 'lairbrozkie@gmail.com', '12345', '2024-12-08'),
(52, 'John Paul', 'M', 'Arvesu', '09123456789', 20, 'Male', 'B-', 'Pending', 'Candelaria Quezon city', 'johnpaularvesu@gmail.com', '12345', '2024-12-08'),
(53, 'John Lex', 'P', 'Bacani', '09123456789', 20, 'Male', 'A+', 'Pending', 'bonliw', 'johnlexbacani@gmail.com', '12345', '2024-12-08'),
(54, 'Renz Fio', 'D', 'Magbojos', '09123456789', 24, 'Male', 'B-', 'Processed', 'Bauan Batangas', 'renzfio@gmail.com', '12345', '2024-12-08'),
(55, 'Karl Matthew', 'D', 'Marasigan', '09454211330', 20, 'Male', 'O+', 'Pending', 'Sta. Rita Karsada Batangas city', 'karlmarasigan0505050505@gmail.com', '12345', '2024-12-10'),
(56, 'Karl Matthew ', 'D', 'Marasigan', '09454211330', 19, 'Male', 'O+', 'Processed', 'Sta. Rita Karsada Batangas city', 'karlmrsgn01234567@gmail.com', '12345', '2024-12-10'),
(57, 'Princess Nicole', 'C', 'Ingco', '09123456789', 20, 'Female', 'AB+', 'Done', 'Sta. Rita Karsada Batangas city', 'ingconicolee@gmail.com', '12345', '2024-12-10'),
(58, 'Jaspher AndreI', 'A', 'Malabanan', '09123456789', 20, 'Male', 'B+', 'Processed', 'Lemery Batangas', 'jaspher@gmail.com', '12345', '2024-12-11');

-- --------------------------------------------------------

--
-- Table structure for table `requestor_message`
--

CREATE TABLE `requestor_message` (
  `messageID` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `req_message` text DEFAULT NULL,
  `requestorID` int(11) DEFAULT NULL,
  `mess_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `requestor_message`
--

INSERT INTO `requestor_message` (`messageID`, `email`, `req_message`, `requestorID`, `mess_date`) VALUES
(8, 'karlcatipan11@gmail.com', 'dadadas', 21, '2024-12-07 02:05:02'),
(9, 'kikobateriya@gmail.com', 'imissyou', 4, '2024-12-07 02:05:02'),
(10, 'karlcatipan11@gmail.com', 'dada', 21, '2024-12-07 02:05:02'),
(11, 'lanceedward@gmail.com', 'hi po hehehe', 13, '2024-12-07 02:05:02'),
(15, 'karlcatipan11@gmail.com', 'kindly process my request, thankyou!', 21, '2024-12-07 02:05:02'),
(16, 'kiko05555@gmail.com', 'Please process my request, thankyou!', 22, '2024-12-07 02:05:02'),
(17, 'kiko05555@gmail.com', 'thanks', 22, '2024-12-07 02:05:02'),
(18, 'ingcoprincessnicole@gmail.com', 'Please proccess my request, thank you!', 23, '2024-12-08 01:34:32'),
(19, 'juan.dc@gmail.com', 'can you process my request immediately? it\'s emergency, thankyou', 24, '2024-12-08 13:04:49'),
(20, 'miguel.flores@gmail.com', 'thankyou', 28, '2024-12-08 13:05:25'),
(21, 'jasmine.bautista@yahoo.com', 'process this request thankyou', 29, '2024-12-08 13:07:06'),
(22, 'donateme@gmail.com', 'hi', 19, '2024-12-08 13:07:30'),
(23, 'donateme@gmail.com', 'imissyou', 19, '2024-12-08 13:07:35'),
(24, 'donateme@gmail.com', 'donate po thankyou', 19, '2024-12-08 13:07:46'),
(25, 'donateme@gmail.com', 'thanks', 19, '2024-12-08 13:07:53'),
(26, 'nicoleingcoo@gmail.com', 'Please process my request', 34, '2024-12-09 16:26:36'),
(27, 'nicoleingcooo@gmail.com', 'Please process my request, thankyou!', 35, '2024-12-09 16:34:43'),
(28, 'karlmarasigan123456@gmail.com', 'Please process my request, thankyou!', 36, '2024-12-09 16:47:13'),
(29, 'karlmarasigan123456@gmail.com', 'thankyou!', 36, '2024-12-09 16:53:03');

-- --------------------------------------------------------

--
-- Table structure for table `req_users`
--

CREATE TABLE `req_users` (
  `requestorID` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `middle_initial` char(2) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `contact_number` varchar(15) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `blood_needed` varchar(5) DEFAULT NULL,
  `urgency_level` varchar(30) DEFAULT NULL,
  `status_req` varchar(20) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `req_users`
--

INSERT INTO `req_users` (`requestorID`, `first_name`, `middle_initial`, `last_name`, `contact_number`, `age`, `gender`, `blood_needed`, `urgency_level`, `status_req`, `address`, `email`, `password`) VALUES
(1, 'Marasigan', 'D.', 'Marasigan', '09454211330', 19, 'Male', 'O+', 'Critical/Emergency', 'Processed/Ready', 'Sta. Rita Karasda Batangas city, Batangas', 'karlmrsgn1109@gmail.com', '12345'),
(2, 'Karl Matthew', 'D.', 'Marasigan', '09454211330', 19, 'Female', 'O+', 'Critical/Emergency', 'Processed/Ready', 'Sta. Rita Karsada Batangas city, Batangas', 'Karlmrsgn1109@gmail.com', '123456'),
(3, 'kiko', 'd', 'mars', '0999', 19, 'Male', 'O+', 'Critical/Emergency', 'Processed/Ready', 'statatata', 'Karlmrsgn1109@gmail.com', '123451234567'),
(4, 'Kiko', 'D.', 'Bateriya', '09454211330', 19, 'Male', 'O+', 'Critical/Emergency', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'kikobateriya@gmail.com', 'nicsy'),
(5, 'Princess Nicole', 'C.', 'Ingco', '09708272147', 20, 'Female', 'AB+', 'Urgent', 'Processed/Ready', 'Sitio Apool, Sta. Rita Karsada Batangas city, Batangas', '23-01801@g.batstate-u.edu.ph', 'kikomybaby'),
(6, 'Okiks', 'D', 'Bateriya', '09454211330', 19, 'Male', 'AB+', 'Moderate', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'karlmrsgn0123@gmail.com', '12345'),
(7, 'Karl Matthew', 'D.', 'Marasigan', '09454211330', 19, 'Male', 'O+', 'Critical/Emergency', 'Processed/Ready', 'Sta. Rita Karsada Batangas city, Batangas', '23-08160@g.batstate-u.edu.ph', 'karl12345'),
(8, 'Kiko', 'D.', 'Marasigan', '09454211330', 19, 'Male', 'O+', 'Moderate', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'kikobateriya@gmail.com', 'okok'),
(9, 'John Lex', 'D.', 'Bacani', '09380628243', 19, 'Male', 'O-', 'Moderate', 'Processed/Ready', 'San Luis Batangas', 'johnlex@gmail.com', '12345'),
(10, 'Princess Nicole', 'D', 'Ingco', '09454211330', 20, 'Female', 'AB+', 'Urgent', 'Processed/Ready', 'Sitio Banaba Apool, Sta. Rita Batangas city, Batangas', 'nicoleingco0@gmail.com', '12345'),
(12, 'Karl Matthew', 'D.', 'Marasigan', '09454211330', 32, 'Male', 'AB+', 'Urgent', 'Processed/Ready', 'Batangas', 'karlmarasigan28@gmail.com', 'karl1345'),
(13, 'Lancelot', 'V.', 'Dela Rosa', '09454211330', 21, 'Male', 'AB+', 'Moderate', 'Processed/Ready', 'Quezon', 'lanceedward@gmail.com', '12345'),
(14, 'Karl Matthew', 'D', 'Marasigan', '09454211330', 59, 'Male', 'B-', 'Low Priority', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'kikobatteryhehe@gmail.com', '12345'),
(15, 'Karl Matthew', 'D', 'Marasigan', '09454211330', 32, 'Male', 'O+', 'Critical/Emergency', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'mamamamam@gmail.com', '12345'),
(16, 'Karl Matthew', 'D', 'Marasuigan', '0945123313131', 21, 'Male', 'B-', 'Urgent', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'kikookis@gmail.com', '12345'),
(17, 'karl amtthew', 'd', 'marasigan', '09454211330', 23, 'Male', 'AB-', 'Urgent', 'Processed/Ready', 'Sta. Rita karasdada', 'karlkikokarl@gmail.com', '12345'),
(18, 'karl matthew', 'd', 'Marasigan', '1233455666', 21, 'Male', 'AB-', 'Moderate', 'Processed/Ready', 'Sta. rita', 'oksksksks@gmail.com', '12345'),
(19, 'Karl', 'D', 'Marasigan', '12345', 12, 'Male', 'AB+', 'Moderate', 'Processed/Ready', 'Sta. Rita Karsada', 'donateme@gmail.com', '12345'),
(20, 'Karl', 'D.', 'Catipan', '09454211330', 19, 'Male', 'AB-', 'Critical/Emergency', 'Pending request', 'Tabangao Aplaya', 'catipay@gmail.com', '12345'),
(21, 'Karl', 'J', 'Catipan', '09272915995', 19, 'Male', 'B+', 'Low Priority', 'Pending request', 'Tabangao Bagong Lipunan, Batangas City', 'karlcatipan11@gmail.com', 'Sa12345!'),
(22, 'Karl Matthew', 'D.', 'Marasigan', '09454211330', 19, 'Male', 'AB+', 'Moderate', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'kiko05555@gmail.com', '12345'),
(23, 'Princess Nicole', 'C.', 'Ingco', '09925265374', 20, 'Female', 'AB+', 'Low Priority', 'Processed/Ready', 'Sta. Rita Karsada Batangas city, Batangas', 'ingcoprincessnicole@gmail.com', '12345'),
(24, 'Juan', 'A.', 'Dela Cruz', '09171234567', 24, 'Male', 'A+', 'Critical/Emergency', 'Pending Request', 'Manila, Philippines', 'juan.dc@gmail.com', 'pass123'),
(25, 'Maria', 'B.', 'Santos', '09182345678', 30, 'Female', 'B+', 'Routine', 'Processed/Ready', 'Quezon City, Philippines', 'maria.santos@yahoo.com', 'secret456'),
(26, 'Lito', 'E.', 'Reyes', '09271234568', 42, 'Male', 'B-', 'Urgent', 'Pending Request', 'Batangas City, Philippines', 'lito.reyes@gmail.com', 'lito789'),
(27, 'Rosa', 'I.', 'Cruz', '09281122334', 26, 'Female', 'O+', 'Routine', 'Pending Request', 'Davao City, Philippines', 'rosa.cruz@gmail.com', 'cruz123'),
(28, 'Miguel', 'C.', 'Flores', '09193334455', 38, 'Male', 'AB+', 'Urgent', 'Processed/Ready', 'Laguna, Philippines', 'miguel.flores@gmail.com', 'miguel321'),
(29, 'Jasmine', 'D.', 'Bautista', '09345556677', 29, 'Female', 'O-', 'Critical/Emergency', 'Pending Request', 'Cavite, Philippines', 'jasmine.bautista@yahoo.com', 'jazzy456'),
(30, 'Alex', 'F.', 'Mendoza', '09128889900', 35, 'Male', 'A-', 'Routine', 'Processed/Ready', 'Cebu City, Philippines', 'alex.mendoza@hotmail.com', 'alexpass'),
(31, 'Katrina', 'G.', 'Ramirez', '09227778899', 27, 'Female', 'B-', 'Critical/Emergency', 'Pending Request', 'Iloilo City, Philippines', 'kat.ramirez@gmail.com', 'katrina12'),
(32, 'Roberto', 'H.', 'Villanueva', '09361112233', 40, 'Male', 'AB-', 'Urgent', 'Processed/Ready', 'Baguio City, Philippines', 'roberto.v@gmail.com', 'robert456'),
(33, 'Angelica', 'J.', 'Perez', '09236667788', 31, 'Female', 'O+', 'Routine', 'Pending Request', 'Quezon City, Philippines', 'angelica.perez@gmail.com', 'angie123'),
(34, 'Princess Nicole', 'C.', 'Ingco', '09123456789', 20, 'Female', 'AB+', 'Critical/Emergency', 'Pending request', 'Sta. Rita Karsada Batangas city', 'nicoleingcoo@gmail.com', '12345'),
(35, 'Princess Nicole', 'C.', 'Ingco', '09123456789', 20, 'Male', 'AB+', 'Moderate', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'nicoleingcooo@gmail.com', '12345'),
(36, 'Karl Matthew', 'D.', 'Marasigan', '09454211330', 19, 'Male', 'AB+', 'Urgent', 'Processed/Ready', 'Sta. Rita Karsada Batangas city', 'karlmarasigan123456@gmail.com', '12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`adminID`);

--
-- Indexes for table `donor_message`
--
ALTER TABLE `donor_message`
  ADD PRIMARY KEY (`donorMessID`),
  ADD KEY `fk_donor_user_id` (`user_id`);

--
-- Indexes for table `donor_users`
--
ALTER TABLE `donor_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `requestor_message`
--
ALTER TABLE `requestor_message`
  ADD PRIMARY KEY (`messageID`),
  ADD KEY `fk_requestor_id` (`requestorID`);

--
-- Indexes for table `req_users`
--
ALTER TABLE `req_users`
  ADD PRIMARY KEY (`requestorID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `adminID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `donor_message`
--
ALTER TABLE `donor_message`
  MODIFY `donorMessID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `donor_users`
--
ALTER TABLE `donor_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT for table `requestor_message`
--
ALTER TABLE `requestor_message`
  MODIFY `messageID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `req_users`
--
ALTER TABLE `req_users`
  MODIFY `requestorID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `donor_message`
--
ALTER TABLE `donor_message`
  ADD CONSTRAINT `fk_donor_user_id` FOREIGN KEY (`user_id`) REFERENCES `donor_users` (`id`);

--
-- Constraints for table `requestor_message`
--
ALTER TABLE `requestor_message`
  ADD CONSTRAINT `fk_requestor_id` FOREIGN KEY (`requestorID`) REFERENCES `req_users` (`requestorID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
