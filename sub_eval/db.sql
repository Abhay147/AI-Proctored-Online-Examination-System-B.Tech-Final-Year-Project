/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - se
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`se` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `se`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add assign_sub_table',7,'add_assign_sub_table'),
(26,'Can change assign_sub_table',7,'change_assign_sub_table'),
(27,'Can delete assign_sub_table',7,'delete_assign_sub_table'),
(28,'Can view assign_sub_table',7,'view_assign_sub_table'),
(29,'Can add courses_table',8,'add_courses_table'),
(30,'Can change courses_table',8,'change_courses_table'),
(31,'Can delete courses_table',8,'delete_courses_table'),
(32,'Can view courses_table',8,'view_courses_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add notification_table',10,'add_notification_table'),
(38,'Can change notification_table',10,'change_notification_table'),
(39,'Can delete notification_table',10,'delete_notification_table'),
(40,'Can view notification_table',10,'view_notification_table'),
(41,'Can add question_table',11,'add_question_table'),
(42,'Can change question_table',11,'change_question_table'),
(43,'Can delete question_table',11,'delete_question_table'),
(44,'Can view question_table',11,'view_question_table'),
(45,'Can add subject_table',12,'add_subject_table'),
(46,'Can change subject_table',12,'change_subject_table'),
(47,'Can delete subject_table',12,'delete_subject_table'),
(48,'Can view subject_table',12,'view_subject_table'),
(49,'Can add students_table',13,'add_students_table'),
(50,'Can change students_table',13,'change_students_table'),
(51,'Can delete students_table',13,'delete_students_table'),
(52,'Can view students_table',13,'view_students_table'),
(53,'Can add staff_table',14,'add_staff_table'),
(54,'Can change staff_table',14,'change_staff_table'),
(55,'Can delete staff_table',14,'delete_staff_table'),
(56,'Can view staff_table',14,'view_staff_table'),
(57,'Can add result_table',15,'add_result_table'),
(58,'Can change result_table',15,'change_result_table'),
(59,'Can delete result_table',15,'delete_result_table'),
(60,'Can view result_table',15,'view_result_table'),
(61,'Can add notes_table',16,'add_notes_table'),
(62,'Can change notes_table',16,'change_notes_table'),
(63,'Can delete notes_table',16,'delete_notes_table'),
(64,'Can view notes_table',16,'view_notes_table'),
(65,'Can add feedback_table',17,'add_feedback_table'),
(66,'Can change feedback_table',17,'change_feedback_table'),
(67,'Can delete feedback_table',17,'delete_feedback_table'),
(68,'Can view feedback_table',17,'view_feedback_table'),
(69,'Can add exam_table',18,'add_exam_table'),
(70,'Can change exam_table',18,'change_exam_table'),
(71,'Can delete exam_table',18,'delete_exam_table'),
(72,'Can view exam_table',18,'view_exam_table'),
(73,'Can add complaint_table',19,'add_complaint_table'),
(74,'Can change complaint_table',19,'change_complaint_table'),
(75,'Can delete complaint_table',19,'delete_complaint_table'),
(76,'Can view complaint_table',19,'view_complaint_table'),
(77,'Can add chat_table',20,'add_chat_table'),
(78,'Can change chat_table',20,'change_chat_table'),
(79,'Can delete chat_table',20,'delete_chat_table'),
(80,'Can view chat_table',20,'view_chat_table'),
(81,'Can add previous_question',21,'add_previous_question'),
(82,'Can change previous_question',21,'change_previous_question'),
(83,'Can delete previous_question',21,'delete_previous_question'),
(84,'Can view previous_question',21,'view_previous_question');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'SE','assign_sub_table'),
(20,'SE','chat_table'),
(19,'SE','complaint_table'),
(8,'SE','courses_table'),
(18,'SE','exam_table'),
(17,'SE','feedback_table'),
(9,'SE','login_table'),
(16,'SE','notes_table'),
(10,'SE','notification_table'),
(21,'SE','previous_question'),
(11,'SE','question_table'),
(15,'SE','result_table'),
(14,'SE','staff_table'),
(13,'SE','students_table'),
(12,'SE','subject_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'SE','0001_initial','2024-02-19 05:44:54.841927'),
(2,'contenttypes','0001_initial','2024-02-19 05:44:54.887111'),
(3,'auth','0001_initial','2024-02-19 05:44:55.161243'),
(4,'admin','0001_initial','2024-02-19 05:44:55.222202'),
(5,'admin','0002_logentry_remove_auto_add','2024-02-19 05:44:55.235501'),
(6,'admin','0003_logentry_add_action_flag_choices','2024-02-19 05:44:55.250153'),
(7,'contenttypes','0002_remove_content_type_name','2024-02-19 05:44:55.298280'),
(8,'auth','0002_alter_permission_name_max_length','2024-02-19 05:44:55.346187'),
(9,'auth','0003_alter_user_email_max_length','2024-02-19 05:44:55.361314'),
(10,'auth','0004_alter_user_username_opts','2024-02-19 05:44:55.378555'),
(11,'auth','0005_alter_user_last_login_null','2024-02-19 05:44:55.411796'),
(12,'auth','0006_require_contenttypes_0002','2024-02-19 05:44:55.411796'),
(13,'auth','0007_alter_validators_add_error_messages','2024-02-19 05:44:55.411796'),
(14,'auth','0008_alter_user_username_max_length','2024-02-19 05:44:55.461316'),
(15,'auth','0009_alter_user_last_name_max_length','2024-02-19 05:44:55.492417'),
(16,'auth','0010_alter_group_name_max_length','2024-02-19 05:44:55.504928'),
(17,'auth','0011_update_proxy_permissions','2024-02-19 05:44:55.535767'),
(18,'auth','0012_alter_user_first_name_max_length','2024-02-19 05:44:55.567655'),
(19,'sessions','0001_initial','2024-02-19 05:44:55.599704'),
(20,'SE','0002_previous_question','2024-02-19 11:18:52.515434'),
(21,'SE','0003_rename_answer_previous_question_year','2024-02-19 12:01:13.839123'),
(22,'SE','0004_auto_20240221_1044','2024-02-21 05:14:28.724180'),
(23,'SE','0005_alter_previous_question_question','2024-03-10 04:07:21.352187');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('2d5yinar2x2qclv4cshpmhrl3fecqr46','eyJsaWQiOjJ9:1rscUk:18GHt80VX9gR9wT7TiEJebIUU5QdKM4cKFea9BM2zQ4','2024-04-19 05:52:10.888646'),
('34o3tyhhdwhtfb6xia30yj1c7h2d8ktg','eyJsaWQiOjJ9:1rsdOF:Ui6gcju5CAjnuSvi1Ty1vubH9Oc5tm3eTOlI0aKSrSI','2024-04-19 06:49:31.281653'),
('6capc7vu986dzwmz7j2qdmh6egisbirt','.eJyrVsrJTFGyMtNRKi4pTUnNK4lPzi8tKk5VsjJFCBWn5oL5JSCl5jpKyXklSlbGtQBoFROK:1rjtMo:Qm0IdkbWU0nRUcebgWk_x7jf1hStoaveIPRbGVvutPw','2024-03-26 04:03:54.831929'),
('uxf05358te8hglfxdwn02g1bgy37g5ur','eyJsaWQiOjYsIm9vIjoiMiIsInNpZCI6IjEiLCJwcCI6NH0:1rdkaO:Y-e0rRwebmDRA0QExx9FPQAwZ3eEEg3w21HkMIRLbZU','2024-03-09 05:28:32.537333'),
('wwp5r7nf4urj1szyjdmm54k0y2rm96w1','.eJyrVsrJTFGyMtNRys9XslIyUdJRSgYJGOooFYNosEhxSWlKal5JfHJ-aVFxqpKVKUKoODUXzE8uAOtJLgFTJSCt5kBuHpBvUAsAzb8dVA:1rjeD5:Z8kUuaOWCqnJJRrHSYKIfUcXkFN9-mbxWHzrNRco7ow','2024-03-25 11:52:51.527872');

/*Table structure for table `se_assign_sub_table` */

DROP TABLE IF EXISTS `se_assign_sub_table`;

CREATE TABLE `se_assign_sub_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `STAFF_id` bigint NOT NULL,
  `SUBJECT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_assign_sub_table_STAFF_id_b5ab92a7_fk_SE_staff_table_id` (`STAFF_id`),
  KEY `SE_assign_sub_table_SUBJECT_id_6e8ea521_fk_SE_subject_table_id` (`SUBJECT_id`),
  CONSTRAINT `SE_assign_sub_table_STAFF_id_b5ab92a7_fk_SE_staff_table_id` FOREIGN KEY (`STAFF_id`) REFERENCES `se_staff_table` (`id`),
  CONSTRAINT `SE_assign_sub_table_SUBJECT_id_6e8ea521_fk_SE_subject_table_id` FOREIGN KEY (`SUBJECT_id`) REFERENCES `se_subject_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_assign_sub_table` */

insert  into `se_assign_sub_table`(`id`,`STAFF_id`,`SUBJECT_id`) values 
(5,1,8),
(6,1,10),
(7,1,11),
(8,1,6),
(9,1,7),
(10,1,7),
(11,1,9),
(14,3,6);

/*Table structure for table `se_attend_exam` */

DROP TABLE IF EXISTS `se_attend_exam`;

CREATE TABLE `se_attend_exam` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `answer` longtext NOT NULL,
  `mark` double NOT NULL,
  `QUESTION_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_attend_exam_STUDENT_id_e63731ce_fk_SE_students_table_id` (`STUDENT_id`),
  CONSTRAINT `SE_attend_exam_STUDENT_id_e63731ce_fk_SE_students_table_id` FOREIGN KEY (`STUDENT_id`) REFERENCES `se_students_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_attend_exam` */

insert  into `se_attend_exam`(`id`,`answer`,`mark`,`QUESTION_id`,`STUDENT_id`) values 
(1,'cascading style sheet',20.000000000000004,10,1),
(2,'hypertext markup language',0,11,1),
(3,'programing lang',0,12,1);

/*Table structure for table `se_chat_table` */

DROP TABLE IF EXISTS `se_chat_table`;

CREATE TABLE `se_chat_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `FROM_id` bigint NOT NULL,
  `TO_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_chat_table_FROM_id_49084ee6_fk_SE_login_table_id` (`FROM_id`),
  KEY `SE_chat_table_TO_id_fd30a840_fk_SE_login_table_id` (`TO_id`),
  CONSTRAINT `SE_chat_table_FROM_id_49084ee6_fk_SE_login_table_id` FOREIGN KEY (`FROM_id`) REFERENCES `se_login_table` (`id`),
  CONSTRAINT `SE_chat_table_TO_id_fd30a840_fk_SE_login_table_id` FOREIGN KEY (`TO_id`) REFERENCES `se_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_chat_table` */

insert  into `se_chat_table`(`id`,`message`,`date`,`time`,`FROM_id`,`TO_id`) values 
(1,'hi','2024-02-21','10:30:25.000000',2,6),
(2,'hlo','2024-02-21','10:42:25.000000',6,2),
(3,'hiiii','2024-02-21','10:30:25.000000',2,6),
(4,'jiii','2024-02-21','10:30:25.000000',2,6),
(5,'ghgh','2024-02-21','10:30:45.000000',6,2),
(6,'hi','2024-02-21','10:30:25.000000',6,6),
(7,'hlo','2024-02-21','10:30:25.000000',6,6),
(8,'hi','2024-02-24','10:30:25.000000',6,6),
(9,'hi','2024-02-24','10:30:25.000000',2,13),
(10,'hi','2024-03-10','10:30:25.000000',6,8);

/*Table structure for table `se_complaint_table` */

DROP TABLE IF EXISTS `se_complaint_table`;

CREATE TABLE `se_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(100) NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_complaint_table_STUDENT_id_eb828f03_fk_SE_students_table_id` (`STUDENT_id`),
  CONSTRAINT `SE_complaint_table_STUDENT_id_eb828f03_fk_SE_students_table_id` FOREIGN KEY (`STUDENT_id`) REFERENCES `se_students_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_complaint_table` */

insert  into `se_complaint_table`(`id`,`complaint`,`date`,`reply`,`STUDENT_id`) values 
(1,'guhihi','2024-02-20','pending',1),
(2,'ooooo','2024-02-20','pending',1),
(3,'admin@123','2024-02-21','pending',1);

/*Table structure for table `se_courses_table` */

DROP TABLE IF EXISTS `se_courses_table`;

CREATE TABLE `se_courses_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `course` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_courses_table` */

insert  into `se_courses_table`(`id`,`course`,`description`) values 
(2,'btech ce','jhxkskj'),
(3,'btech bm','sjkdgawjdbc'),
(5,'btech cs','fsytgfsdh'),
(6,'btech mech','erfghjk');

/*Table structure for table `se_exam_table` */

DROP TABLE IF EXISTS `se_exam_table`;

CREATE TABLE `se_exam_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `subject_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_exam_table_subject_id_6224b25c_fk_SE_subject_table_id` (`subject_id`),
  CONSTRAINT `SE_exam_table_subject_id_6224b25c_fk_SE_assign_sub_table_id` FOREIGN KEY (`subject_id`) REFERENCES `se_assign_sub_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_exam_table` */

insert  into `se_exam_table`(`id`,`date`,`time`,`subject_id`) values 
(7,'2024-03-20','12:08:00.000000',7);

/*Table structure for table `se_feedback_table` */

DROP TABLE IF EXISTS `se_feedback_table`;

CREATE TABLE `se_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `STAFF_id` bigint NOT NULL,
  `STUDENT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_feedback_table_STAFF_id_dea313c6_fk_SE_staff_table_id` (`STAFF_id`),
  KEY `SE_feedback_table_STUDENT_id_b13b7e76_fk_SE_students_table_id` (`STUDENT_id`),
  CONSTRAINT `SE_feedback_table_STAFF_id_dea313c6_fk_SE_staff_table_id` FOREIGN KEY (`STAFF_id`) REFERENCES `se_staff_table` (`id`),
  CONSTRAINT `SE_feedback_table_STUDENT_id_b13b7e76_fk_SE_students_table_id` FOREIGN KEY (`STUDENT_id`) REFERENCES `se_students_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_feedback_table` */

insert  into `se_feedback_table`(`id`,`feedback`,`date`,`STAFF_id`,`STUDENT_id`) values 
(1,'great class','2024-02-19',1,1),
(2,'wonderful class','2024-02-07',1,2),
(3,'jgwqfdf','2024-02-20',1,1),
(4,'VHK','2024-02-20',1,1),
(5,'great','2024-02-21',1,1),
(6,'admin@123','2024-03-10',1,1);

/*Table structure for table `se_login_table` */

DROP TABLE IF EXISTS `se_login_table`;

CREATE TABLE `se_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_login_table` */

insert  into `se_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin@123','1234','admin'),
(2,'anu@123','1234','staff'),
(3,'drishya@123','1234','staff'),
(4,'athulya@123','1234','staff'),
(6,'sahla@123','1234','student'),
(7,'anshi@123','12345','student'),
(8,'dilu@123','1234','student'),
(9,'fidha@123','1234','student'),
(10,'naveen','naveen','staff'),
(13,'anshi@123','1234','student'),
(14,'last.png','1234','student'),
(15,'last.png','1234','student'),
(16,'fidha@123','1234','student'),
(17,'fidha@123','1234','student'),
(18,'fidha@123','1234','reject'),
(19,'nahla@123','1234','staff');

/*Table structure for table `se_notes_table` */

DROP TABLE IF EXISTS `se_notes_table`;

CREATE TABLE `se_notes_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `NOTES` varchar(100) NOT NULL,
  `DATE` date NOT NULL,
  `SUBJECT_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_notes_table_SUBJECT_id_d5ccb6b5_fk_SE_subject_table_id` (`SUBJECT_id`),
  CONSTRAINT `SE_notes_table_SUBJECT_id_d5ccb6b5_fk_SE_subject_table_id` FOREIGN KEY (`SUBJECT_id`) REFERENCES `se_subject_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_notes_table` */

insert  into `se_notes_table`(`id`,`NOTES`,`DATE`,`SUBJECT_id`) values 
(6,'new systm arch_MqhKLp5.png','2024-02-20',10),
(10,'DSC07532_rB2mzym.JPG','2024-03-10',8),
(11,'Screenshot (20)_mqd4tM8.png','2024-02-21',8),
(13,'WhatsApp Image 2024-02-23 at 10.42.38 AM.jpeg','2024-02-24',10),
(14,'WhatsApp Image 2024-02-23 at 10.42.38 AM_FXTHP4F.jpeg','2024-02-24',7),
(15,'WhatsApp Image 2024-02-23 at 10.42.38 AM_U6yanbc.jpeg','2024-02-24',6);

/*Table structure for table `se_notification_table` */

DROP TABLE IF EXISTS `se_notification_table`;

CREATE TABLE `se_notification_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_notification_table` */

/*Table structure for table `se_previous_question` */

DROP TABLE IF EXISTS `se_previous_question`;

CREATE TABLE `se_previous_question` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL,
  `assign_sub_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_previous_question_assign_sub_id_46912d32_fk_SE_assign` (`assign_sub_id`),
  CONSTRAINT `SE_previous_question_assign_sub_id_46912d32_fk_SE_assign` FOREIGN KEY (`assign_sub_id`) REFERENCES `se_assign_sub_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_previous_question` */

insert  into `se_previous_question`(`id`,`question`,`year`,`assign_sub_id`) values 
(4,'DSC07532.JPG','2020',5);

/*Table structure for table `se_question_table` */

DROP TABLE IF EXISTS `se_question_table`;

CREATE TABLE `se_question_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `EXAMID_id` bigint NOT NULL DEFAULT '-10089',
  `mark` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_question_table_EXAMID_id_f3913199_fk_SE_exam_table_id` (`EXAMID_id`),
  CONSTRAINT `SE_question_table_EXAMID_id_f3913199_fk_SE_exam_table_id` FOREIGN KEY (`EXAMID_id`) REFERENCES `se_exam_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_question_table` */

insert  into `se_question_table`(`id`,`question`,`answer`,`EXAMID_id`,`mark`) values 
(10,'what is css','cascading style sheet',7,'20'),
(11,'what is html','hypertext markup language',7,'10'),
(12,'what is python','programing lang',7,'5');

/*Table structure for table `se_result_table` */

DROP TABLE IF EXISTS `se_result_table`;

CREATE TABLE `se_result_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `STUDENT_id` bigint NOT NULL,
  `EXAM_id` bigint NOT NULL DEFAULT '-9999',
  `result` bigint NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_result_table_STUDENT_id_48410d10_fk_SE_students_table_id` (`STUDENT_id`),
  KEY `SE_result_table_EXAM_id_83e3403e_fk_SE_exam_table_id` (`EXAM_id`),
  CONSTRAINT `SE_result_table_EXAM_id_83e3403e_fk_SE_exam_table_id` FOREIGN KEY (`EXAM_id`) REFERENCES `se_exam_table` (`id`),
  CONSTRAINT `SE_result_table_STUDENT_id_48410d10_fk_SE_students_table_id` FOREIGN KEY (`STUDENT_id`) REFERENCES `se_students_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_result_table` */

insert  into `se_result_table`(`id`,`STUDENT_id`,`EXAM_id`,`result`,`status`) values 
(2,1,7,20,'pending'),
(3,1,7,0,'pending'),
(4,1,7,0,'pending');

/*Table structure for table `se_staff_table` */

DROP TABLE IF EXISTS `se_staff_table`;

CREATE TABLE `se_staff_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `experience` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_staff_table_LOGIN_id_9ac1ee58_fk_SE_login_table_id` (`LOGIN_id`),
  CONSTRAINT `SE_staff_table_LOGIN_id_9ac1ee58_fk_SE_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `se_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_staff_table` */

insert  into `se_staff_table`(`id`,`firstname`,`lastname`,`qualification`,`experience`,`place`,`phone`,`email`,`gender`,`LOGIN_id`,`image`) values 
(1,'Anu','k s','MTech','6','kozhikode',9824386437,'anuks@gmail.com','female',2,'last.png'),
(2,'drishya','s g','MTech','6','kozhikode',9824386437,'drishya@gmail.com','female',3,'last.png'),
(3,'athulya','j s','MTech','3','kozhikode',9828246437,'athulyaa@gmail.com','female',4,'last.png'),
(4,'naveen','john','M Tech','3','kkm',9876543210,'naveen@gmail','male',10,'Screenshot (19).png');

/*Table structure for table `se_students_table` */

DROP TABLE IF EXISTS `se_students_table`;

CREATE TABLE `se_students_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) NOT NULL,
  `Lname` varchar(100) NOT NULL,
  `Sem` int NOT NULL,
  `place` varchar(100) NOT NULL,
  `phone` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `COURSE_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_students_table_COURSE_id_4e40588e_fk_SE_courses_table_id` (`COURSE_id`),
  KEY `SE_students_table_LOGIN_id_d0520429_fk_SE_login_table_id` (`LOGIN_id`),
  CONSTRAINT `SE_students_table_COURSE_id_4e40588e_fk_SE_courses_table_id` FOREIGN KEY (`COURSE_id`) REFERENCES `se_courses_table` (`id`),
  CONSTRAINT `SE_students_table_LOGIN_id_d0520429_fk_SE_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `se_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_students_table` */

insert  into `se_students_table`(`id`,`firstname`,`Lname`,`Sem`,`place`,`phone`,`email`,`gender`,`COURSE_id`,`LOGIN_id`,`image`) values 
(1,'sahla','ek',5,'mukkam',8747426837,'sahla@gmail.com','female',5,6,'last.png'),
(2,'dilshana','vv',3,'nadapuram',8923648246,'dilshana@gmail.com','female',5,8,'last.png'),
(3,'anshi','p',1,'kallanthode',9087654321,'anship@gmail.com','Female',2,13,'Screenshot (18)_JYZF4gh.png'),
(4,'fidha','p p',4,'puthiyedath purayil',8921776200,'fidhasalampp23@gmail.com','Female',3,18,'new systm arch_6iVj7st.png');

/*Table structure for table `se_subject_table` */

DROP TABLE IF EXISTS `se_subject_table`;

CREATE TABLE `se_subject_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) NOT NULL,
  `Sem` int NOT NULL,
  `COURSE_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SE_subject_table_COURSE_id_eeaad681_fk_SE_courses_table_id` (`COURSE_id`),
  CONSTRAINT `SE_subject_table_COURSE_id_eeaad681_fk_SE_courses_table_id` FOREIGN KEY (`COURSE_id`) REFERENCES `se_courses_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `se_subject_table` */

insert  into `se_subject_table`(`id`,`subject`,`Sem`,`COURSE_id`) values 
(6,'civil',1,2),
(7,'bce',2,2),
(8,'maths',1,5),
(9,'graphics',2,5),
(10,'lsd',3,2),
(11,'cgip',5,5),
(13,'mechanics',1,6);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
