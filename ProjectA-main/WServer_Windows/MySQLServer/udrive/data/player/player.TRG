TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`localhost` TRIGGER `MakeCharacter` BEFORE INSERT ON `player` FOR EACH ROW BEGIN\n	IF(new.`name` REGEXP \'[^A-Za-z0-9]\')THEN\n		SET new.`name`=NULL;\n	END IF;\nEND'
sql_modes=0
definers='root@localhost'
