# Host: localhost  (Version: 5.5.53-log)
# Date: 2020-02-08 14:52:31
# Generator: MySQL-Front 5.3  (Build 4.234)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "email"
#

DROP TABLE IF EXISTS `email`;
CREATE TABLE `email` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#
# Data for table "email"
#

/*!40000 ALTER TABLE `email` DISABLE KEYS */;
INSERT INTO `email` VALUES (1,'758682207@qq.com','test');
/*!40000 ALTER TABLE `email` ENABLE KEYS */;

#
# Structure for table "info"
#

DROP TABLE IF EXISTS `info`;
CREATE TABLE `info` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `sfz` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `iphone` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=2236570 DEFAULT CHARSET=utf8;

#
# Data for table "info"
#

/*!40000 ALTER TABLE `info` DISABLE KEYS */;
INSERT INTO `info` VALUES (1,'小陈','110000888899996658','河南','17896868563','758682207@qq.com');
/*!40000 ALTER TABLE `info` ENABLE KEYS */;

#
# Structure for table "qq"
#

DROP TABLE IF EXISTS `qq`;
CREATE TABLE `qq` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM AUTO_INCREMENT=11288 DEFAULT CHARSET=utf8;

#
# Data for table "qq"
#

/*!40000 ALTER TABLE `qq` DISABLE KEYS */;
INSERT INTO `qq` VALUES (1,'758682207','test1111');
/*!40000 ALTER TABLE `qq` ENABLE KEYS */;
