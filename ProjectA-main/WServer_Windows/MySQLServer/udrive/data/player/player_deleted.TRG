TYPE=TRIGGERS
triggers='CREATE DEFINER=`root`@`localhost` TRIGGER `MakeCharacter_copy` BEFORE INSERT ON `player_deleted` FOR EACH ROW BEGIN\n	IF(new.`name` REGEXP \'[^A-Za-z0-9]\')THEN\n		SET new.`name`=NULL;\n	END IF;\nEND'
sql_modes=0
definers='root@localhost'
