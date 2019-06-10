-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 10 Cze 2019, 17:41
-- Wersja serwera: 10.1.38-MariaDB
-- Wersja PHP: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `testowa`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `dane`
--

CREATE TABLE `dane` (
  `id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `programs`
--

CREATE TABLE `programs` (
  `id` int(11) NOT NULL,
  `program_name` varchar(128) NOT NULL,
  `code_text` varchar(4096) NOT NULL,
  `date_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `programs`
--

INSERT INTO `programs` (`id`, `program_name`, `code_text`, `date_added`) VALUES
(9, 'test.py', 'import sys\n\ndef fibonacci(n : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 1\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 17:48:46'),
(10, 'test.py', 'import sys\n\ndef fibonacci(n : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 1\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 18:33:29'),
(11, 'test.py', 'import sys\n\ndef fibonacci(n : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 1\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 18:39:15'),
(12, 'test.py', 'import sys\nabcd\ndef fibonacci(n : int, x : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 2\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 18:44:01'),
(13, 'test.py', 'import sys2\n\ndef fibonacci(n : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 1\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 18:44:35'),
(26, 'test.py', 'import sys\n\ndef fibonacci(n : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 1\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 20:08:28'),
(27, 'test.py', 'import sys\n\ndef fibonacci(n : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 1\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 20:13:36'),
(28, 'test.py', 'import sys\n\ndef fibonacci(n : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 1\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 20:19:04');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `programs2`
--

CREATE TABLE `programs2` (
  `id` int(11) NOT NULL,
  `program_name` varchar(128) NOT NULL,
  `code2` varchar(4096) NOT NULL,
  `date_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `programs2`
--

INSERT INTO `programs2` (`id`, `program_name`, `code2`, `date_added`) VALUES
(1, 'test.py', 'import sys\n\ndef fibonacci(n : int):\n        if n == 1:\n            return 0\n        elif n == 2:\n            return 1\n        else:\n            pom2 = 1\n            result = 1\n\n            for i in range(n-2):\n                pom1 = result\n                result = pom1 + pom2\n                pom2 = pom1\n\n            return result\n\nif __name__ == \"__main__\":\n    n = int(sys.argv[1])\n    i = fibonacci(n)\n    print(str(i))\n    sys.exit(i)', '2019-06-09 17:23:21');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `programs3`
--

CREATE TABLE `programs3` (
  `id` int(11) NOT NULL,
  `program_name` varchar(128) NOT NULL,
  `code` varchar(4096) NOT NULL,
  `date_added` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `programs_diffs`
--

CREATE TABLE `programs_diffs` (
  `id` int(11) NOT NULL,
  `program1_id` int(11) NOT NULL,
  `program2_id` int(11) NOT NULL,
  `similarity` float NOT NULL DEFAULT '0',
  `diff` varchar(4096) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Zrzut danych tabeli `programs_diffs`
--

INSERT INTO `programs_diffs` (`id`, `program1_id`, `program2_id`, `similarity`, `diff`) VALUES
(13, 11, 9, 1, ''),
(14, 11, 10, 1, ''),
(15, 11, 12, 0.997722, '--- \n+++ \n@@ -172,7 +172,7 @@\n   =  -1+2 \n \n  '),
(16, 11, 13, 1, ''),
(17, 11, 14, 1, ''),
(18, 11, 15, 1, ''),
(19, 11, 16, 1, ''),
(20, 11, 17, 1, ''),
(21, 11, 18, 1, ''),
(22, 11, 19, 1, ''),
(23, 11, 20, 1, ''),
(24, 11, 21, 1, ''),
(25, 11, 22, 1, ''),
(26, 11, 9, 1, ''),
(27, 11, 10, 1, ''),
(28, 11, 12, 0.997722, '--- \n+++ \n@@ -172,7 +172,7 @@\n   =  -1+2 \n \n  '),
(29, 11, 13, 0.998862, '--- \n+++ \n@@ -8,6 +8,7 @@\n s y s+2 \n \n d'),
(30, 11, 14, 1, ''),
(31, 11, 15, 1, ''),
(32, 11, 16, 1, ''),
(33, 11, 17, 1, ''),
(34, 11, 18, 1, ''),
(35, 11, 19, 1, ''),
(36, 11, 20, 1, ''),
(37, 11, 21, 1, ''),
(38, 11, 22, 1, ''),
(39, 11, 23, 1, ''),
(40, 11, 9, 1, ''),
(41, 11, 10, 1, ''),
(42, 11, 12, 0.997722, '*** \n--- \n***************\n*** 172,178 ****\n     =   ! 1  \n  \n   --- 172,178 ----\n     =   ! 2  \n  \n   '),
(43, 11, 13, 0.998862, '*** \n--- \n***************\n*** 8,13 ****\n--- 8,14 ----\n  s  y  s+ 2  \n  \n  d'),
(44, 11, 14, 1, ''),
(45, 11, 15, 1, ''),
(46, 11, 16, 1, ''),
(47, 11, 17, 1, ''),
(48, 11, 18, 1, ''),
(49, 11, 19, 1, ''),
(50, 11, 20, 1, ''),
(51, 11, 21, 1, ''),
(52, 11, 22, 1, ''),
(53, 11, 23, 1, ''),
(54, 11, 24, 1, ''),
(55, 11, 9, 1, ''),
(56, 11, 10, 1, ''),
(57, 11, 12, 0.997722, '--- \n+++ \n@@ -172,7 +172,7 @@\n   =  -1+2 \n \n  '),
(58, 11, 13, 0.998862, '--- \n+++ \n@@ -8,6 +8,7 @@\n s y s+2 \n \n d'),
(59, 11, 14, 1, ''),
(60, 11, 15, 1, ''),
(61, 11, 16, 1, ''),
(62, 11, 17, 1, ''),
(63, 11, 18, 1, ''),
(64, 11, 19, 1, ''),
(65, 11, 20, 1, ''),
(66, 11, 21, 1, ''),
(67, 11, 22, 1, ''),
(68, 11, 23, 1, ''),
(69, 11, 24, 1, ''),
(70, 11, 25, 1, ''),
(71, 11, 9, 1, ''),
(72, 11, 10, 1, ''),
(73, 11, 12, 0.983165, '--- \n+++ \n@@ -9,6 +9,10 @@\n y s \n+a+b+c+d \n d e@@ -31,6 +35,15 @@\n i n t+,+ +x+ +:+ +i+n+t ) : \n@@ -172,7 +185,7 @@\n   =  -1+2 \n \n  '),
(74, 11, 13, 0.998862, '--- \n+++ \n@@ -8,6 +8,7 @@\n s y s+2 \n \n d'),
(75, 11, 26, 1, ''),
(76, 11, 9, 1, ''),
(77, 11, 10, 1, ''),
(78, 11, 12, 0.983165, '--- \n+++ \n@@ -9,6 +9,10 @@\n y s \n+a+b+c+d \n d e@@ -31,6 +35,15 @@\n i n t+,+ +x+ +:+ +i+n+t ) : \n@@ -172,7 +185,7 @@\n   =  -1+2 \n \n  '),
(79, 11, 13, 0.998862, '--- \n+++ \n@@ -8,6 +8,7 @@\n s y s+2 \n \n d'),
(80, 11, 26, 1, ''),
(81, 11, 27, 1, ''),
(82, 11, 9, 1, ''),
(83, 11, 10, 1, ''),
(84, 11, 12, 0.983165, '--- \n+++ \n@@ -9,6 +9,10 @@\n y s \n+a+b+c+d \n d e@@ -31,6 +35,15 @@\n i n t+,+ +x+ +:+ +i+n+t ) : \n@@ -172,7 +185,7 @@\n   =  -1+2 \n \n  '),
(85, 11, 13, 0.998862, '--- \n+++ \n@@ -8,6 +8,7 @@\n s y s+2 \n \n d'),
(86, 11, 26, 1, ''),
(87, 11, 27, 1, ''),
(88, 11, 28, 1, '');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `dane`
--
ALTER TABLE `dane`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `programs`
--
ALTER TABLE `programs`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `programs2`
--
ALTER TABLE `programs2`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `programs3`
--
ALTER TABLE `programs3`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `programs_diffs`
--
ALTER TABLE `programs_diffs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `dane`
--
ALTER TABLE `dane`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `programs`
--
ALTER TABLE `programs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT dla tabeli `programs2`
--
ALTER TABLE `programs2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `programs_diffs`
--
ALTER TABLE `programs_diffs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
