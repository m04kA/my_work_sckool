-- Generation time: Mon, 04 May 2020 12:50:01 +0000
-- Host: mysql.hostinger.ro
-- DB name: u574849695_25
/*!40030 SET NAMES UTF8 */;
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP TABLE IF EXISTS `communities`;
CREATE TABLE `communities` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `communities_name_idx` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `communities` VALUES ('6','at'),
('8','consequatur'),
('15','culpa'),
('5','dolorum'),
('3','est'),
('13','explicabo'),
('1','iste'),
('10','libero'),
('7','magnam'),
('2','nam'),
('11','quasi'),
('12','quia'),
('4','quod'),
('14','repellat'),
('9','vel'); 


DROP TABLE IF EXISTS `friend_requests`;
CREATE TABLE `friend_requests` (
  `initiator_user_id` bigint(20) unsigned NOT NULL,
  `target_user_id` bigint(20) unsigned NOT NULL,
  `status` enum('requested','approved','unfriended','declined') COLLATE utf8_unicode_ci DEFAULT NULL,
  `requested_at` datetime DEFAULT current_timestamp(),
  `confirmed_at` datetime DEFAULT NULL ON UPDATE current_timestamp(),
  PRIMARY KEY (`initiator_user_id`,`target_user_id`),
  KEY `target_user_id` (`target_user_id`),
  CONSTRAINT `friend_requests_ibfk_1` FOREIGN KEY (`initiator_user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `friend_requests_ibfk_2` FOREIGN KEY (`target_user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `friend_requests` VALUES ('1','1','declined','1995-05-13 21:41:16','1985-10-06 09:44:57'),
('2','2','requested','1992-03-10 16:04:05','2010-07-16 06:44:28'),
('3','3','unfriended','1993-02-24 04:37:52','1978-10-20 11:33:02'),
('4','4','declined','1983-07-21 04:37:50','2004-06-30 15:13:15'),
('5','5','unfriended','1986-02-19 15:28:50','2001-12-14 15:26:07'),
('6','6','declined','1979-04-26 19:19:31','1978-04-19 21:46:31'),
('7','7','unfriended','1995-03-31 18:40:01','2003-12-09 20:28:17'),
('8','8','requested','2003-12-27 21:47:22','1988-08-20 12:52:01'),
('9','9','requested','1979-11-23 05:43:30','2006-06-16 10:40:04'),
('10','10','declined','1992-03-29 23:24:49','2008-08-08 23:24:19'); 


DROP TABLE IF EXISTS `likes`;
CREATE TABLE `likes` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `media_id` bigint(20) unsigned NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `media_id` (`media_id`),
  CONSTRAINT `likes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `likes_ibfk_2` FOREIGN KEY (`media_id`) REFERENCES `media` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `likes` VALUES ('1','1','1','1971-12-12 09:09:29'),
('2','2','2','2019-10-13 16:34:58'),
('3','3','3','2012-05-09 23:13:04'),
('4','4','4','2002-08-25 04:25:13'),
('5','5','5','2002-05-26 03:13:47'),
('6','6','6','1973-10-25 21:13:16'),
('7','7','7','2003-07-13 18:00:55'),
('8','8','8','1993-04-17 03:30:53'),
('9','9','9','1978-03-11 23:27:17'),
('10','10','10','2016-12-30 15:21:50'),
('11','1','11','1995-05-12 00:06:00'),
('12','2','12','2007-01-11 21:47:36'),
('13','3','13','1981-11-05 23:38:52'),
('14','4','14','2014-10-04 17:36:59'),
('15','5','15','1999-01-21 05:10:22'),
('16','6','16','2004-02-18 01:16:36'),
('17','7','17','1976-07-02 14:02:33'),
('18','8','18','2008-09-01 13:30:53'),
('19','9','19','1979-08-26 20:21:46'),
('20','10','20','1975-02-24 01:21:26'),
('21','1','21','1981-02-11 16:08:36'),
('22','2','22','1991-04-23 19:20:47'),
('23','3','23','1990-08-13 03:49:16'),
('24','4','24','1988-03-09 19:40:07'),
('25','5','25','1974-12-15 01:31:57'),
('26','6','26','2015-06-24 18:29:13'),
('27','7','27','2012-12-17 18:46:23'),
('28','8','28','1989-12-24 16:14:57'),
('29','9','29','2002-12-11 04:26:01'),
('30','10','30','1986-09-22 08:04:58'),
('31','1','31','2009-12-16 17:49:33'),
('32','2','32','2009-05-11 02:22:19'),
('33','3','33','2008-05-02 07:24:50'),
('34','4','34','1996-05-15 06:36:45'),
('35','5','35','2004-10-29 17:52:36'),
('36','6','36','2018-07-21 19:12:14'),
('37','7','37','1991-08-28 15:36:12'),
('38','8','38','1978-08-10 14:05:30'),
('39','9','39','1975-01-14 17:55:56'),
('40','10','40','2011-08-28 21:08:58'),
('41','1','41','1972-02-05 12:41:49'),
('42','2','42','1978-06-05 20:54:37'),
('43','3','43','1976-04-26 00:51:03'),
('44','4','44','1977-09-23 16:01:45'),
('45','5','45','2004-01-27 01:44:48'),
('46','6','46','2013-03-13 19:39:19'),
('47','7','47','1978-05-23 05:16:56'),
('48','8','48','1989-05-22 20:11:57'),
('49','9','49','1981-02-03 10:51:47'),
('50','10','50','1999-07-10 19:01:08'),
('51','1','1','2009-03-30 17:54:02'),
('52','2','2','2003-06-11 13:16:25'),
('53','3','3','2014-05-17 21:55:54'),
('54','4','4','2002-06-27 12:25:39'),
('55','5','5','1970-11-15 16:56:54'),
('56','6','6','2016-01-03 04:28:38'),
('57','7','7','2007-03-26 06:18:26'),
('58','8','8','2009-04-14 23:11:35'),
('59','9','9','1973-07-03 13:46:40'),
('60','10','10','1995-05-25 00:39:37'); 


DROP TABLE IF EXISTS `media`;
CREATE TABLE `media` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `media_type_id` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  `body` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `filename` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  `metadata` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `media_type_id` (`media_type_id`),
  CONSTRAINT `media_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `media_ibfk_2` FOREIGN KEY (`media_type_id`) REFERENCES `media_types` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `media` VALUES ('1','1','1','Molestiae enim blanditiis et est veritatis. Numquam consequatur in temporibus quidem nihil quaerat animi. Est esse similique ut eaque possimus.','autem','0',NULL,'1995-07-16 17:38:50','2002-05-20 22:28:33'),
('2','2','2','Molestiae quibusdam iure occaecati optio quo aut tempora neque. Aut provident totam consequatur. Dolorem dolor et molestiae magnam molestias eum delectus dicta. Laborum ipsa numquam numquam molestiae.','quibusdam','67064887',NULL,'1980-04-10 06:53:02','2014-01-15 00:10:54'),
('3','3','3','Et eos ad dolores qui autem nemo expedita. Sit ut architecto iste reiciendis accusamus reiciendis veritatis. Dolor qui aut non.','ut','201',NULL,'1987-12-06 00:38:51','1986-12-20 09:05:58'),
('4','4','4','Sed ad dicta architecto non labore nulla. Est porro tempore fugit blanditiis quia est. Voluptas sequi possimus blanditiis ducimus eum ipsa modi magnam. Dolorem sit eum est quia fugiat suscipit in.','magnam','154',NULL,'2005-04-03 01:40:50','1987-10-05 21:05:07'),
('5','5','5','Quaerat at tempora laudantium mollitia aut id voluptas. Itaque et perferendis vitae enim. Reiciendis porro est aut quis numquam. Delectus repellat quia similique cupiditate ipsum omnis voluptas.','est','9540794',NULL,'1971-01-15 07:03:19','1974-04-04 04:06:20'),
('6','6','6','Voluptatem beatae vel ut et error voluptate deserunt voluptas. Velit dolores eos eum quia. Magnam tempora voluptatum ea provident.','repellat','2692',NULL,'1978-08-26 15:12:37','2002-10-10 15:37:07'),
('7','7','7','Assumenda voluptas repudiandae quae dolorem. Culpa quisquam ut velit eos numquam non harum. Optio enim asperiores enim excepturi temporibus id voluptas. Saepe magnam quibusdam aliquam ut inventore officiis consequuntur.','illum','22041',NULL,'2005-06-06 20:54:27','2005-12-24 04:08:48'),
('8','8','8','Repudiandae nihil repudiandae temporibus et. Ut quis inventore consectetur aut voluptas. Saepe porro est voluptate ut quaerat eius officiis.','est','278333048',NULL,'1996-06-16 19:46:16','1984-08-01 04:50:36'),
('9','9','9','Pariatur facere est minus eius. Qui commodi qui et accusamus laborum rerum excepturi. Deleniti ut voluptatum consequatur at pariatur.','blanditiis','0',NULL,'1970-08-10 21:05:45','1978-04-13 06:06:37'),
('10','10','10','Voluptatum explicabo architecto vitae. Omnis necessitatibus voluptatem voluptatibus neque deleniti porro qui. Unde veniam eum id ut esse. Accusantium quia facere quis aliquid.','deleniti','818465',NULL,'1996-05-19 07:25:37','1997-02-01 20:01:11'),
('11','11','1','Vel culpa perferendis culpa. Blanditiis distinctio laudantium commodi id laboriosam error. Ea earum odio modi cupiditate.','adipisci','7',NULL,'2005-10-13 13:43:15','1984-10-14 02:16:03'),
('12','12','2','Molestiae ut eos non dolor ut. A sequi tenetur cum pariatur vero similique officiis. Illum natus voluptatibus hic dolorum reiciendis iusto debitis.','laboriosam','460720295',NULL,'2003-09-25 23:03:02','2000-12-17 03:55:13'),
('13','13','3','Sequi dignissimos ipsam expedita facilis rerum necessitatibus dolores. Deserunt quam nulla est eos maiores repellat quae. Eum qui maiores corporis eius quo eligendi.','nesciunt','64',NULL,'2000-06-11 15:02:50','1980-07-22 15:44:59'),
('14','14','4','Et ipsa sapiente culpa minima enim. Vero ut iste hic iusto sapiente et necessitatibus. Amet quasi sunt nesciunt magni error.','natus','52304074',NULL,'2005-06-06 01:15:12','1989-05-18 04:29:27'),
('15','15','5','Qui vel facilis aut harum eaque fugit incidunt. Repellat esse itaque officiis eveniet veritatis ut perferendis. Totam perferendis veritatis aut cupiditate quos eius. Eveniet non quidem odit facilis. Modi qui sunt amet rerum dolor dolores voluptate.','animi','209610105',NULL,'2013-04-20 06:06:00','1989-03-05 01:35:18'),
('16','16','6','Illum culpa veritatis quia aliquam aut. Ut pariatur aliquid molestiae ut. Illum optio eveniet molestiae alias nam maiores id. Dolore molestias sunt porro error distinctio et. In esse iusto sed distinctio magnam qui possimus.','est','719728528',NULL,'1994-01-11 17:57:07','1981-08-10 03:24:34'),
('17','17','7','Voluptatem repellat voluptatem rem quis. Consequatur unde impedit reiciendis sapiente corrupti pariatur nihil. Illo culpa ullam dolorem id ipsam tenetur aut. Velit qui et quibusdam.','in','339035',NULL,'1992-09-13 18:55:41','1981-12-21 05:52:39'),
('18','18','8','Quidem cumque praesentium commodi officiis sed. Voluptates ex culpa eum qui eum animi. In rem ratione nam quia fugiat et laborum ut. Dignissimos et quis sit natus amet odit laudantium eos.','quo','83493',NULL,'2002-02-02 15:45:30','1975-12-06 07:50:49'),
('19','19','9','Necessitatibus distinctio eveniet ipsum saepe voluptas sit. Sunt alias corporis occaecati voluptatem. Qui placeat et laudantium.','pariatur','8',NULL,'1984-03-19 04:25:31','1985-08-08 13:34:13'),
('20','20','10','Modi neque quibusdam quibusdam fuga sapiente qui vel. Doloribus voluptas numquam architecto et repudiandae. Perspiciatis quae error placeat et ipsa molestias.','nostrum','7352461',NULL,'1979-01-13 23:59:25','2006-02-01 01:42:53'),
('21','21','1','Dolores minima qui minima voluptates maiores id qui. Molestiae consectetur delectus tempora reiciendis quia id id. Voluptas non animi sapiente explicabo earum ut.','nihil','5',NULL,'2009-08-16 04:58:08','1994-08-29 00:43:00'),
('22','22','2','Qui delectus cupiditate necessitatibus rem enim corporis. Ut repellat mollitia aut ipsum iure asperiores ducimus.','qui','157',NULL,'1998-02-24 22:13:03','1981-10-09 12:52:23'),
('23','23','3','Maxime est deserunt repellat excepturi. Magni quo id nemo sit. Molestiae porro culpa temporibus sit praesentium. Qui voluptatem iusto eaque assumenda dolores officia. Quo qui amet aut corporis beatae commodi.','esse','646353405',NULL,'2002-10-15 14:29:36','2011-09-06 11:00:20'),
('24','24','4','Ipsum necessitatibus velit tenetur eaque. Qui vel est quam quia. Consectetur non dicta iure quia impedit dolores.','beatae','1',NULL,'2014-08-26 23:37:42','2000-04-13 01:10:20'),
('25','25','5','Recusandae autem voluptatem suscipit et blanditiis vero. Voluptatem est iste laborum rerum quod ea commodi. Eum fugit cumque voluptatem distinctio minima blanditiis. Voluptatibus voluptatum modi et molestiae quia.','ratione','2424041',NULL,'1998-05-20 19:28:28','2004-12-07 03:30:50'),
('26','26','6','Rerum sunt odio hic voluptas unde. Ab molestiae sit molestiae mollitia maiores quo. Debitis culpa recusandae culpa ea corrupti.','labore','14',NULL,'2008-03-17 13:29:29','1991-08-21 08:19:32'),
('27','27','7','Voluptas quas qui rem cum saepe qui ut quia. Optio expedita ipsa cupiditate qui odit temporibus. Dicta similique soluta id non est. Minus maxime praesentium vitae. Quo voluptatem sint tempora optio.','ratione','5538556',NULL,'1996-06-04 05:02:54','1990-12-20 17:54:31'),
('28','28','8','Non laboriosam voluptatem eos sint aut alias. Nisi et vero molestiae architecto est est. Iste necessitatibus eos beatae illo fugiat voluptate. Molestiae vero dolor nisi modi vel.','qui','8023192',NULL,'1992-06-01 13:14:54','1975-07-11 04:56:19'),
('29','29','9','Aut dignissimos recusandae praesentium est ex doloremque aut. Ex possimus ex officiis saepe. Consectetur sapiente aut animi omnis voluptatibus blanditiis.','ratione','427388',NULL,'2003-04-16 08:21:57','1987-04-23 19:54:00'),
('30','30','10','Recusandae eveniet expedita dolore sunt quo libero. Modi odio ut fugit illo minus. Fuga quo commodi vel saepe. Sunt quae est veritatis asperiores.','distinctio','88327',NULL,'2007-11-17 23:57:54','2006-01-18 12:21:26'),
('31','31','1','Vitae odit rerum et. Quia dignissimos quam quaerat temporibus consectetur aut. Voluptatem sapiente perferendis aut ea fugit provident. Numquam sapiente dolorem ut rem laudantium non.','nisi','0',NULL,'1989-06-08 06:36:36','2020-03-26 13:15:06'),
('32','32','2','Natus et doloribus est deleniti eius impedit qui. Pariatur sapiente ut modi non. Enim et commodi consequatur reiciendis earum aspernatur.','consectetur','43448039',NULL,'1979-10-17 12:19:59','2010-09-11 04:18:00'),
('33','33','3','Inventore et ducimus vel vitae. Nisi sunt non saepe veritatis. Consequatur voluptas molestiae reprehenderit corrupti quia molestiae. Aliquam aliquam ipsum ut et atque. Et nihil mollitia ut quo et.','cupiditate','53',NULL,'2018-06-07 23:18:07','1972-08-23 20:01:44'),
('34','34','4','Debitis mollitia optio ea vitae dolorum expedita. Qui minima omnis officia rerum velit accusantium.','dolor','89',NULL,'2013-11-25 12:37:29','2011-06-14 17:29:15'),
('35','35','5','Ut sunt odio nihil saepe. Dolores blanditiis commodi repudiandae saepe ipsum incidunt et. Quaerat veniam vitae perspiciatis officia iusto omnis. Aspernatur consequatur ut laboriosam dicta.','hic','3159',NULL,'2020-05-01 20:40:12','2000-09-03 19:21:02'),
('36','36','6','Voluptatum at voluptates sit magni doloremque. Rem minus at voluptates enim accusantium et. Dolor fuga et voluptatibus labore ut consequuntur dolorem. Qui perspiciatis magnam dolorem aut iste.','doloremque','498492',NULL,'2008-01-16 19:26:36','2006-07-11 16:22:23'),
('37','37','7','Est et nostrum quis ipsum ratione quia. Mollitia laboriosam sunt dignissimos quia. Voluptatem doloremque molestiae cupiditate cum rerum voluptas.','est','979219',NULL,'1997-09-21 06:34:19','1973-09-07 11:46:25'),
('38','38','8','Nobis fugiat maxime sunt illum in ducimus quia. Hic aut excepturi et ut dolor officia. Assumenda sit qui deserunt placeat aspernatur velit. Omnis praesentium vero sapiente nemo.','accusantium','7192916',NULL,'2013-08-23 18:49:27','2017-11-05 14:33:59'),
('39','39','9','Quo suscipit perferendis iusto enim. Ut provident sint quidem rerum dolore asperiores est. Voluptas quia autem et velit ullam suscipit. Consequuntur voluptate velit ea assumenda esse aut. Laborum fuga possimus voluptates sit aut.','neque','315234',NULL,'1987-07-15 03:32:36','2013-06-05 07:41:08'),
('40','40','10','Inventore aliquam impedit doloribus nobis quis optio. Accusamus iste maxime optio quo explicabo consequatur voluptas voluptatem. Eos est omnis optio et.','iste','6932720',NULL,'2000-05-29 11:19:17','2011-12-24 13:18:38'),
('41','41','1','Sit nam molestiae est. Placeat quae voluptatem quaerat maiores voluptas.','id','87',NULL,'1982-08-06 11:39:34','1978-04-04 19:10:24'),
('42','42','2','Autem perferendis corrupti et aliquid harum quos hic. Aut earum rerum quae tempora ipsam. Et doloremque enim quod sed molestias voluptatum perspiciatis porro.','quos','27',NULL,'1986-07-23 13:33:41','1998-11-01 07:38:39'),
('43','43','3','Aut possimus odit illo perferendis error. Dolor quia ea ullam quibusdam inventore distinctio non. Autem enim facilis voluptate sint doloribus.','et','302',NULL,'2012-11-09 18:52:50','1993-06-18 11:54:14'),
('44','44','4','Dolore labore non autem quidem et in rem. Nulla inventore consequuntur est occaecati necessitatibus occaecati eos. Voluptatem aut modi omnis et libero enim quidem. Numquam expedita debitis possimus quidem aut aliquid.','maiores','3469',NULL,'1978-12-12 01:36:15','1985-07-04 15:13:09'),
('45','45','5','Fuga ipsa veritatis hic explicabo voluptas. Aut recusandae qui delectus sit ipsum nihil est. Maiores et eius sint.','illum','4326483',NULL,'2010-03-31 01:41:53','1980-02-12 10:46:04'),
('46','46','6','Sed cum repellendus consequatur possimus ex. Quae cupiditate libero dolores voluptatibus iste harum quas et. Repudiandae vero similique repudiandae totam. Voluptatem ratione voluptates odit.','nulla','0',NULL,'1997-08-16 16:20:00','1992-08-23 02:55:15'),
('47','47','7','Minus qui officia iure quis quis nam. Omnis provident deleniti amet at. Consequuntur aut deserunt consequuntur ab omnis ut. Non totam aut praesentium.','nam','74940489',NULL,'1987-02-21 00:58:16','2014-12-06 19:56:34'),
('48','48','8','Voluptas qui atque commodi et similique. Nesciunt sapiente adipisci repudiandae deserunt et voluptas. Sapiente dolorem earum ea corrupti.','expedita','647123274',NULL,'1975-11-02 17:40:02','1988-09-29 12:12:05'),
('49','49','9','Odit quas nobis iure nam. In similique adipisci recusandae quis soluta qui impedit.','harum','964956899',NULL,'1993-07-25 22:25:43','2004-07-11 23:38:07'),
('50','50','10','Veniam et quia similique quia aperiam. Quia nesciunt voluptas amet aliquam et. Est ut vel sunt quibusdam.','quia','6464273',NULL,'1984-11-04 19:37:50','1992-03-17 07:01:36'); 


DROP TABLE IF EXISTS `media_types`;
CREATE TABLE `media_types` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `media_types` VALUES ('1','necessitatibus','1975-12-16 08:00:27','1978-02-20 07:22:44'),
('2','asperiores','2016-01-09 10:38:56','1970-08-17 05:55:37'),
('3','velit','2007-02-06 08:00:03','1977-04-03 23:17:38'),
('4','quis','1989-06-21 00:30:16','1992-07-21 01:26:54'),
('5','voluptatem','1997-09-22 15:32:26','1976-09-20 19:24:24'),
('6','quis','2016-12-11 19:27:46','1970-02-10 04:54:55'),
('7','fuga','1989-04-22 15:53:15','2003-01-24 07:14:05'),
('8','illo','2018-05-31 08:44:29','1976-01-10 00:07:10'),
('9','ratione','1999-09-19 23:41:19','2002-10-28 18:37:19'),
('10','suscipit','2014-09-27 20:24:01','1997-04-22 08:49:12'),
('11','voluptatem','1981-01-14 23:45:01','1992-05-14 21:35:04'),
('12','nesciunt','1977-07-24 01:23:11','1978-02-21 01:13:22'),
('13','rem','1979-10-17 14:21:55','1980-10-08 21:47:28'),
('14','rerum','1970-09-05 05:22:51','1980-09-11 00:40:25'),
('15','eius','2018-04-17 22:50:19','1977-04-13 00:58:18'),
('16','nulla','1984-04-12 23:19:55','1994-01-17 09:28:57'),
('17','suscipit','2016-05-02 10:07:48','2007-10-16 12:16:17'),
('18','eaque','1970-05-22 13:26:08','2003-06-27 15:16:07'),
('19','in','1998-06-01 03:49:16','2013-05-22 16:27:15'),
('20','consequuntur','2008-02-24 05:18:27','2002-02-12 07:15:54'),
('21','doloremque','1985-04-27 19:19:57','1971-09-30 11:14:30'),
('22','voluptate','1981-10-25 15:28:31','2000-06-05 03:29:43'),
('23','ipsa','1993-12-18 05:03:23','1993-08-11 17:52:03'),
('24','et','1998-09-10 20:45:16','2003-05-01 19:22:58'),
('25','saepe','1995-06-28 03:59:52','1998-10-02 21:48:26'),
('26','porro','2010-03-26 00:24:54','1984-03-27 03:30:03'),
('27','aliquid','2016-09-10 19:13:14','1988-09-26 17:24:30'),
('28','assumenda','1998-05-26 18:55:32','1983-03-29 17:34:40'),
('29','officiis','2018-05-04 21:02:24','2001-09-15 20:49:24'),
('30','quas','1995-01-10 21:51:09','2011-01-26 03:17:45'),
('31','blanditiis','1984-05-07 17:16:34','2019-04-20 07:27:09'),
('32','laboriosam','2007-09-07 21:34:34','1986-04-08 07:55:12'),
('33','qui','2012-09-24 19:14:09','1978-06-04 21:48:35'),
('34','aperiam','2009-01-23 12:37:00','1980-10-13 16:03:19'),
('35','facere','2000-03-06 07:00:42','2005-04-24 19:37:11'),
('36','repellendus','1997-10-29 05:54:18','1985-08-18 01:08:02'),
('37','ea','1981-07-09 06:30:27','1988-12-06 04:52:56'),
('38','pariatur','1995-01-27 02:36:07','1977-04-18 23:28:22'),
('39','vel','2005-12-25 02:00:22','1979-03-06 15:58:56'),
('40','nemo','2015-02-10 19:21:24','2008-11-30 00:56:55'),
('41','assumenda','1981-11-29 10:40:20','2010-03-24 03:17:53'),
('42','necessitatibus','2010-10-19 19:41:30','1970-09-26 05:34:24'),
('43','eveniet','2016-06-20 20:01:03','2014-09-26 04:18:29'),
('44','quos','1990-12-07 16:41:43','2006-03-23 17:43:35'),
('45','sint','1999-01-20 02:51:40','1988-10-07 07:53:42'),
('46','ut','2005-04-16 23:44:22','2017-11-05 14:16:32'),
('47','saepe','1981-05-20 18:11:36','2012-10-15 20:50:40'),
('48','in','2000-06-08 04:43:10','1974-05-31 02:20:21'),
('49','voluptatibus','2008-07-11 01:08:14','1994-07-14 20:30:36'),
('50','et','2013-11-02 09:47:04','2015-03-13 18:53:50'),
('51','iusto','1994-11-12 12:02:40','2010-09-20 06:52:10'),
('52','corporis','1989-06-10 23:13:21','1984-07-28 13:15:44'),
('53','aut','1980-05-17 12:24:24','1971-02-02 20:18:58'),
('54','et','2011-08-06 00:00:32','1989-03-30 07:19:37'),
('55','similique','2011-01-11 16:26:02','2009-08-06 14:56:31'),
('56','similique','2003-04-17 03:20:30','1993-12-27 11:26:41'),
('57','est','1976-02-24 14:07:31','1992-01-16 03:05:32'),
('58','blanditiis','1987-11-03 11:44:22','1983-03-13 21:35:08'),
('59','voluptas','1988-01-18 14:41:24','1993-11-28 05:55:31'),
('60','et','1987-04-11 22:52:13','2000-07-25 08:59:57'),
('61','suscipit','1993-11-24 20:08:13','1976-10-26 02:04:36'),
('62','blanditiis','1989-12-11 17:18:14','2000-05-15 14:42:45'),
('63','dolorem','1971-07-23 22:06:02','2004-04-29 11:29:30'),
('64','aut','1976-02-29 02:53:25','1970-05-01 15:02:51'),
('65','commodi','1971-03-25 22:35:17','2001-08-18 00:22:13'),
('66','doloribus','2000-11-18 02:47:44','2000-02-10 09:29:55'),
('67','laborum','1983-12-04 06:11:17','2003-06-18 16:05:36'),
('68','inventore','1992-08-31 17:44:18','2007-12-28 12:48:56'),
('69','ratione','2005-06-04 06:04:23','2005-02-08 02:03:04'),
('70','ea','1984-01-28 01:21:05','2016-05-31 15:07:53'); 


DROP TABLE IF EXISTS `messages`;
CREATE TABLE `messages` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `from_user_id` bigint(20) unsigned NOT NULL,
  `to_user_id` bigint(20) unsigned NOT NULL,
  `body` text COLLATE utf8_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `from_user_id` (`from_user_id`),
  KEY `to_user_id` (`to_user_id`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`from_user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `messages_ibfk_2` FOREIGN KEY (`to_user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `messages` VALUES ('1','1','1','Quaerat rerum est voluptate quae dolore esse. Autem alias voluptatibus odio voluptatem sapiente. Et accusamus fugiat ab ea.','1994-02-24 21:46:00'),
('2','2','2','Accusamus debitis repudiandae in iusto in facilis iusto nulla. Dolorum facilis nesciunt natus magnam. Dolores neque in dolores consequatur minima.','1996-07-06 15:23:27'),
('3','3','3','Voluptate voluptatem ut maiores architecto amet consequatur. Et consequuntur animi rerum sed eum numquam odio. Repellat molestiae sint quidem vel.','1988-08-13 00:14:00'),
('4','4','4','Aliquam rerum et beatae asperiores et qui at fuga. Earum asperiores nobis fuga ex. Error architecto consectetur perspiciatis totam non et non.','1991-09-22 05:08:22'),
('5','5','5','Et quo aspernatur quae. Voluptatem consequatur sequi sequi autem dolore velit fuga sed. Soluta quas qui eos non saepe dolor. Ut ut odit velit voluptatem.','1981-05-09 17:50:58'),
('6','6','6','Aperiam officia repellat sunt nostrum facilis culpa aut. Error aut nihil dolorem totam. Rerum omnis porro fugit qui sunt. Non molestiae id tenetur vel ut. Aliquid saepe et assumenda voluptatem est.','2002-01-12 17:28:55'),
('7','7','7','Esse explicabo cumque animi. Id sit iure et iste. Molestiae dignissimos debitis aut nihil nihil. Omnis sit repudiandae voluptatem.','2004-10-28 01:05:33'),
('8','8','8','Eveniet quo facere consequuntur et et ut. Iure facere sequi nostrum ipsa expedita nihil. Voluptatem quibusdam error omnis doloribus dolor quod. Omnis molestias modi est quod reprehenderit. Rerum quidem nihil culpa sed vero.','2013-01-11 00:21:00'),
('9','9','9','Et molestias quia vero dolorum porro velit. Quisquam debitis est sed nobis. Voluptate corporis quia quas occaecati in numquam rerum nam. Et velit et quaerat et quaerat occaecati.','1993-05-24 12:27:04'),
('10','10','10','Ut exercitationem sunt blanditiis pariatur dolore consequatur eligendi. Dolorum eos amet et possimus molestias voluptates. Cumque veritatis omnis in accusamus sed. Autem qui error nam.','2014-01-11 22:44:56'),
('11','1','1','Et voluptate ea quia ea soluta rerum dolores. Explicabo ut assumenda officia esse rerum.','1984-04-13 03:40:48'),
('12','2','2','Fugit et et beatae officiis dignissimos. Quis ratione maxime temporibus sequi non velit. Eveniet minima quidem rerum consequatur necessitatibus sed corrupti. Labore magni voluptas dolorem et.','2019-09-19 14:44:32'),
('13','3','3','Non tenetur incidunt aut dolorem sit laborum. Nobis est voluptatem inventore unde laboriosam eos quaerat.','1996-08-06 19:23:13'),
('14','4','4','Sit eos doloremque enim omnis ipsa nam. Ipsum nam libero fugit non quo. Saepe architecto nihil et sunt. Assumenda atque et quisquam fugit.','1970-08-14 13:22:49'),
('15','5','5','Et harum impedit reprehenderit ex est consequatur quia vero. Recusandae quia dignissimos iure et dicta tenetur quidem. Rerum quas blanditiis hic consequatur recusandae libero. Facilis qui facere suscipit sunt.','2001-08-02 21:46:09'),
('16','6','6','Dolores sed at qui et. Numquam sequi aut aut quia ut. Quasi enim et et atque libero sunt enim labore. Qui consectetur qui iusto ullam.','2018-02-23 00:53:30'),
('17','7','7','Cupiditate aliquam delectus libero deleniti. Non dolores doloribus magnam qui. Dolores rerum autem atque harum excepturi et.','1992-01-21 21:56:00'),
('18','8','8','Dolorem et rerum atque eligendi autem aliquam. Occaecati pariatur nemo molestiae ipsa at qui.','1973-09-25 20:03:35'),
('19','9','9','Magni ut est atque enim hic dolor ea. Vitae eum occaecati ab saepe qui. Eligendi quia totam similique voluptas accusantium.','1993-01-23 13:16:26'),
('20','10','10','Dolores ut doloribus nobis at et nemo repudiandae dolor. Sequi rerum sit aut voluptas.','1996-10-20 22:01:36'),
('21','1','1','Quibusdam et sit rerum fugiat. Et tenetur eos quod architecto delectus. Est dolor quibusdam rerum et consequatur.','2014-06-10 23:39:34'),
('22','2','2','Et ut nobis voluptatum amet. Molestias enim reiciendis nam dolorem reiciendis. Illo sequi repellendus sunt rerum. Aut provident perferendis ipsa.','1971-12-03 01:48:43'),
('23','3','3','Eum error et eveniet eos aut asperiores et. Voluptates sunt ut asperiores voluptates commodi eum quod.','1984-01-20 19:33:34'),
('24','4','4','Sit voluptas vel nam id et. Voluptatem in quaerat aut aliquam labore ad repellendus. Ipsa natus dolores deserunt eveniet in.','1978-01-10 19:38:49'),
('25','5','5','Distinctio est maiores ut ut earum laudantium sed. Voluptates voluptate quo non ad et sapiente voluptas. Dolor pariatur blanditiis odio nihil quidem repudiandae voluptatem reiciendis.','2001-11-01 12:15:24'),
('26','6','6','Dolor tempore ducimus alias soluta voluptatem necessitatibus quia. Veritatis pariatur nemo occaecati. Molestiae et in molestias explicabo est eum. Pariatur nobis asperiores distinctio.','2010-09-27 03:37:55'),
('27','7','7','Possimus possimus et deserunt explicabo. Corrupti similique ab voluptatem eius eaque. Qui ipsa recusandae pariatur illum saepe vero deserunt qui.','2006-08-06 20:23:02'),
('28','8','8','Delectus aspernatur praesentium labore tempora. Facere quae ea possimus doloremque tempora rerum. Culpa qui quia eligendi neque odit laboriosam dolore sequi.','1997-12-01 09:50:02'),
('29','9','9','Dicta ex saepe nemo esse qui a sit non. In eligendi atque cumque modi et. Eveniet id id eveniet rem labore dolores. Voluptates ut qui inventore.','1978-07-09 17:51:22'),
('30','10','10','Voluptas neque enim dolor animi. Voluptatem iusto laboriosam earum necessitatibus distinctio. Modi dolor itaque soluta magnam enim sint quidem. Consectetur itaque ad similique.','1998-02-05 09:04:59'),
('31','1','1','Nobis excepturi omnis rerum et qui sit et. Cumque sit aut maxime vel. Possimus aut voluptas inventore quis consequatur quo totam porro. Quo expedita minus tempore et enim quis.','1975-03-10 14:20:59'),
('32','2','2','Modi qui eius quis. Qui unde est quia voluptatibus cupiditate architecto consequatur. Exercitationem qui deserunt quis odit in ad.','2001-11-18 23:20:01'),
('33','3','3','Eveniet natus id cumque in. Dolores assumenda eligendi cum aliquid et adipisci. Aut voluptas quod corporis. Hic ad ea adipisci nihil neque in sed fugit.','2019-12-15 23:12:38'),
('34','4','4','Tenetur ea quia sed sed. Est accusantium sint dolorem debitis. Voluptas eveniet quibusdam dicta quia omnis veniam consectetur. Iste aut ad ea mollitia dignissimos est minus.','1974-07-13 05:47:59'),
('35','5','5','Voluptatum sequi non atque ipsa recusandae voluptas sed. Voluptatem iste eos voluptas perspiciatis cupiditate. Minima non veritatis quia dolores.','1988-12-10 15:18:24'),
('36','6','6','Asperiores tenetur facere neque nisi ut quibusdam. Nulla est placeat est sit ab architecto tempore. Nulla ratione velit rerum cupiditate est quia. Iure aut voluptas deserunt aut necessitatibus in minus non. Maiores expedita quasi reiciendis velit.','1989-06-18 20:44:42'),
('37','7','7','Sapiente at dolores ea a nihil consequuntur et. Dignissimos voluptatem aut incidunt nisi consectetur voluptas quia. Voluptates dolorem quo consequuntur ut aliquam eveniet. Facilis modi sit ex omnis minus delectus. Sapiente repudiandae accusantium impedit voluptatibus repellendus magni reprehenderit repellendus.','1984-02-29 22:49:52'),
('38','8','8','Voluptatem accusamus labore voluptatum facere ut mollitia. Distinctio ut aliquam doloremque quia excepturi doloremque aut. Atque temporibus ut ut.','1981-06-24 08:44:53'),
('39','9','9','Incidunt a possimus est aut et. Placeat distinctio quod voluptates. Sunt consequatur est repellat quos. Et ducimus error voluptatem aut architecto quo.','1984-03-18 15:17:35'),
('40','10','10','Vel odit debitis et sequi facilis nobis laborum. Beatae qui cupiditate repudiandae et voluptatem laboriosam corrupti. Laborum nihil voluptates odit veniam necessitatibus. Dolor architecto ducimus sequi.','1991-01-02 17:39:59'),
('41','1','1','Alias et recusandae iure sunt. Dolorum vitae harum fugit quidem rerum ducimus laboriosam. Distinctio rerum itaque quas aut natus optio. Qui quia corporis occaecati molestiae dignissimos.','1988-08-06 10:20:43'),
('42','2','2','Sint dolorem sed expedita ex corporis. Neque error rerum mollitia fuga quae. Distinctio ut recusandae eum quidem. Quo quae modi eaque necessitatibus perspiciatis sed. Omnis est corporis qui cumque unde.','1983-05-12 01:23:13'),
('43','3','3','Nostrum dolore debitis rerum eos libero nesciunt. Harum adipisci neque explicabo qui repudiandae blanditiis iste. Necessitatibus distinctio quia omnis. Voluptate qui quo voluptatem alias consequuntur est ut.','1996-12-20 05:33:12'),
('44','4','4','Nemo quas vitae reprehenderit in vel enim qui. Sit nobis illo consectetur sed culpa vel officiis est. Quaerat aut neque nemo est totam ipsum at ipsam. Sit vel et quasi a.','1992-01-27 22:43:25'),
('45','5','5','Facilis sed rerum explicabo dolore. Blanditiis dolorem distinctio id. Praesentium cum ab voluptatem illum voluptatibus dolore.','1970-03-25 11:29:58'),
('46','6','6','Incidunt expedita quaerat et omnis unde. Cupiditate optio velit occaecati illo tenetur repudiandae delectus. Cupiditate eos exercitationem enim et reiciendis eligendi sed neque. Fugiat expedita non velit voluptatem.','2013-12-14 20:50:47'),
('47','7','7','Atque et quisquam illo in. Non quia sint est quo adipisci quaerat.','2013-01-08 00:54:41'),
('48','8','8','Minus corrupti vitae et vel enim. Illum inventore optio consequatur possimus error non et.','2009-09-16 10:48:37'),
('49','9','9','Iste eligendi ut qui vero. Minima excepturi itaque voluptas quia. Facere est est ducimus tenetur nemo modi porro. Qui cupiditate et repellendus doloremque ipsa sed.','2012-07-03 00:29:45'),
('50','10','10','Quis eius nulla unde cumque ipsam nobis ullam. Atque perspiciatis reiciendis quia sunt. Veniam vero itaque velit quos accusamus vel qui at.','2019-07-08 03:54:07'); 


DROP TABLE IF EXISTS `photo_albums`;
CREATE TABLE `photo_albums` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `user_id` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `photo_albums_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `photo_albums` VALUES ('1','commodi','1'),
('2','quia','2'),
('3','ut','3'),
('4','quo','4'),
('5','et','5'),
('6','quibusdam','6'),
('7','et','7'),
('8','veritatis','8'),
('9','vero','9'),
('10','sunt','10'),
('11','qui','1'),
('12','blanditiis','2'),
('13','illum','3'),
('14','ratione','4'),
('15','repellat','5'),
('16','deleniti','6'),
('17','dolor','7'),
('18','et','8'),
('19','laudantium','9'),
('20','aut','10'),
('21','quae','1'),
('22','architecto','2'),
('23','totam','3'),
('24','laudantium','4'),
('25','eos','5'),
('26','est','6'),
('27','voluptatem','7'),
('28','minima','8'),
('29','et','9'),
('30','magnam','10'); 


DROP TABLE IF EXISTS `photos`;
CREATE TABLE `photos` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `album_id` bigint(20) unsigned NOT NULL,
  `media_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `album_id` (`album_id`),
  KEY `media_id` (`media_id`),
  CONSTRAINT `photos_ibfk_1` FOREIGN KEY (`album_id`) REFERENCES `photo_albums` (`id`),
  CONSTRAINT `photos_ibfk_2` FOREIGN KEY (`media_id`) REFERENCES `media` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=176 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `photos` VALUES ('151','1','1'),
('152','2','2'),
('153','3','3'),
('154','4','4'),
('155','5','5'),
('156','6','6'),
('157','7','7'),
('158','8','8'),
('159','9','9'),
('160','10','10'),
('161','11','11'),
('162','12','12'),
('163','13','13'),
('164','14','14'),
('165','15','15'),
('166','16','16'),
('167','17','17'),
('168','18','18'),
('169','19','19'),
('170','20','20'),
('171','21','21'),
('172','22','22'),
('173','23','23'),
('174','24','24'),
('175','25','25'); 


DROP TABLE IF EXISTS `profiles`;
CREATE TABLE `profiles` (
  `user_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `gender` char(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `photo_id` bigint(20) unsigned DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `hometown` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=231 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;



DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lastname` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'Фамиль',
  `email` varchar(120) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `users_firstname_lastname_idx` (`firstname`,`lastname`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `users` VALUES ('1','Dylan','Paucek','ella05@example.org','89348480196'),
('2','Rose','Conn','kailee.bergstrom@example.net','89059064932'),
('3','Ignacio','Mitchell','kendrick.lebsack@example.net','89864011718'),
('4','Fredy','Corkery','gail.crooks@example.com','89307784459'),
('5','Loma','Gusikowski','considine.kailey@example.org','89620497435'),
('6','Ron','Halvorson','stroman.zena@example.org','89210861881'),
('7','Josianne','Block','lori.lang@example.com','89860198630'),
('8','Joanny','Kovacek','erna03@example.com','89275962416'),
('9','Gust','Mosciski','osvaldo.lakin@example.net','89527219405'),
('10','Tristin','Langosh','rreichert@example.net','89275658225'); 


DROP TABLE IF EXISTS `users_communities`;
CREATE TABLE `users_communities` (
  `user_id` bigint(20) unsigned NOT NULL,
  `community_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`user_id`,`community_id`),
  KEY `community_id` (`community_id`),
  CONSTRAINT `users_communities_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `users_communities_ibfk_2` FOREIGN KEY (`community_id`) REFERENCES `communities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `users_communities` VALUES ('1','1'),
('2','2'),
('3','3'),
('4','4'),
('5','5'),
('6','6'),
('7','7'),
('8','8'),
('9','9'),
('10','10'); 




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

