## 创建库hupu
	create database hupu  DEFAULT CHARSET utf8;
## 创建表
	create table hupu ( 
		id INT(11) PRIMARY KEY AUTO_INCREMENT,
		titles TINYTEXT,titles_urls VARCHAR(255),
		author VARCHAR(255),author_url TINYBLOB,
		stick_time TINYBLOB,
		reply TINYBLOB,
		Last_reply_time TINYBLOB,
		Finally_reply_author TINYBLOB )
