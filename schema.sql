drop table if EXISTS login_log;
create table login_log (
	`id` bigint(20) not null auto_increment comment 'id, auto increment',
	`user_id` bigint(20) not null default -1 comment 'user id',
	`phone_num` varchar(64) not null default '' comment '',
	`time` bigint(20) not null default 0 comment 'unix time',
	`raw_imei` varchar(18) not null default '' comment 'lowcase raw imei',
	`md5_imei` varchar(32) not null default '' comment 'md5 imei, raw imei is lowcase',
	`android_id` varchar(36) not null default '' comment 'android id',
	`raw_idfa` varchar(36) not null default '' comment 'idfa',
	`os` varchar(10) not null default '' comment 'os type, eg: ios,android',
	`phone_model` varchar(30) not null default '' comment '机型，eg: huawei,vivo',
	primary key(`id`)
);

drop table if EXISTS t_user;
CREATE TABLE `t_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `nick_name` varchar(128) NOT NULL DEFAULT '' COMMENT '昵称',
  `user_name` varchar(128) NOT NULL DEFAULT '' COMMENT '用户名',
  `phone_num` varchar(64) NOT NULL DEFAULT '' COMMENT '电话号码',
  `email` varchar(128) NOT NULL DEFAULT '' COMMENT '邮箱',
  `password` varchar(128) NOT NULL DEFAULT '' COMMENT '密码',
  `gender` int(2) NOT NULL DEFAULT 0 COMMENT '性别 0:male 1:female',
  `birthday` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '生日时间戳',
  `longitude` double NOT NULL DEFAULT 0 COMMENT '注册时经度',
  `lattitude` double NOT NULL DEFAULT 0 COMMENT '注册时纬度',
  `address` varchar(128) NOT NULL DEFAULT '0' COMMENT '注册时地址',
  `default_pet` bigint(20) NOT NULL DEFAULT -1 COMMENT '默认的宠物id',
  `head_portrait` varchar(128) NOT NULL DEFAULT '' COMMENT '头像',
  `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_phone_num` (`phone_num`),
  UNIQUE KEY `uk_email` (`email`),
  UNIQUE KEY `uk_user_name` (`user_name`),
  KEY `idx_create_time` (`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8_bin COMMENT='用户信息表'