# AppStatistics
##### 创建数据库
```
create database cmic_application_statistics;
```

##### 创建用户
```
create user 'test'@'%' identified by 'test123';
grant all on cmic_application_statistics.* to 'test'@'%';
```

##### 创建表application，对应“计费类型”sheet
```
create table application(app_id int not null,app_name varchar(20) not null,
AP_code int(11) not null,AP_name varchar(20) not null,billing_type enum('WEB','IAP') not null,
primary key(app_id));

```

##### 创建表m_amount，对应“流水金额”sheet
```
CREATE TABLE m_amount(date date NOT NULL,app_id int NOT NULL,
  time0 int(11) NOT NULL DEFAULT '0',
  time1 int(11) NOT NULL DEFAULT '0',
  time2 int(11) NOT NULL DEFAULT '0',
  time3 int(11) NOT NULL DEFAULT '0',
  time4 int(11) NOT NULL DEFAULT '0',
  time5 int(11) NOT NULL DEFAULT '0',
  time6 int(11) NOT NULL DEFAULT '0',
  time7 int(11) NOT NULL DEFAULT '0',
  time8 int(11) NOT NULL DEFAULT '0',
  time9 int(11) NOT NULL DEFAULT '0',
  time10 int(11) NOT NULL DEFAULT '0',
  time11 int(11) NOT NULL DEFAULT '0',
  time12 int(11) NOT NULL DEFAULT '0',
  time13 int(11) NOT NULL DEFAULT '0',
  time14 int(11) NOT NULL DEFAULT '0',
  time15 int(11) NOT NULL DEFAULT '0',
  time16 int(11) NOT NULL DEFAULT '0',
  time17 int(11) NOT NULL DEFAULT '0',
  time18 int(11) NOT NULL DEFAULT '0',
  time19 int(11) NOT NULL DEFAULT '0',
  time20 int(11) NOT NULL DEFAULT '0',
  time21 int(11) NOT NULL DEFAULT '0',
  time22 int(11) NOT NULL DEFAULT '0',
  time23 int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (date,app_id),
  CONSTRAINT m_amount_ibfk_1 FOREIGN KEY (app_id) REFERENCES application (app_id));
```

##### 创建m_order,对应“订单量”sheet
```
CREATE TABLE m_order(date date NOT NULL,app_id int NOT NULL,
  time0 int(11) NOT NULL DEFAULT '0',
  time1 int(11) NOT NULL DEFAULT '0',
  time2 int(11) NOT NULL DEFAULT '0',
  time3 int(11) NOT NULL DEFAULT '0',
  time4 int(11) NOT NULL DEFAULT '0',
  time5 int(11) NOT NULL DEFAULT '0',
  time6 int(11) NOT NULL DEFAULT '0',
  time7 int(11) NOT NULL DEFAULT '0',
  time8 int(11) NOT NULL DEFAULT '0',
  time9 int(11) NOT NULL DEFAULT '0',
  time10 int(11) NOT NULL DEFAULT '0',
  time11 int(11) NOT NULL DEFAULT '0',
  time12 int(11) NOT NULL DEFAULT '0',
  time13 int(11) NOT NULL DEFAULT '0',
  time14 int(11) NOT NULL DEFAULT '0',
  time15 int(11) NOT NULL DEFAULT '0',
  time16 int(11) NOT NULL DEFAULT '0',
  time17 int(11) NOT NULL DEFAULT '0',
  time18 int(11) NOT NULL DEFAULT '0',
  time19 int(11) NOT NULL DEFAULT '0',
  time20 int(11) NOT NULL DEFAULT '0',
  time21 int(11) NOT NULL DEFAULT '0',
  time22 int(11) NOT NULL DEFAULT '0',
  time23 int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (date,app_id),
  CONSTRAINT m_order_ibfk_1 FOREIGN KEY (app_id) REFERENCES application (app_id));
```

##### 创建表m_user，对应“人数”sheet
```
CREATE TABLE m_user(date date NOT NULL,app_id int NOT NULL,
  time0 int(11) NOT NULL DEFAULT '0',
  time1 int(11) NOT NULL DEFAULT '0',
  time2 int(11) NOT NULL DEFAULT '0',
  time3 int(11) NOT NULL DEFAULT '0',
  time4 int(11) NOT NULL DEFAULT '0',
  time5 int(11) NOT NULL DEFAULT '0',
  time6 int(11) NOT NULL DEFAULT '0',
  time7 int(11) NOT NULL DEFAULT '0',
  time8 int(11) NOT NULL DEFAULT '0',
  time9 int(11) NOT NULL DEFAULT '0',
  time10 int(11) NOT NULL DEFAULT '0',
  time11 int(11) NOT NULL DEFAULT '0',
  time12 int(11) NOT NULL DEFAULT '0',
  time13 int(11) NOT NULL DEFAULT '0',
  time14 int(11) NOT NULL DEFAULT '0',
  time15 int(11) NOT NULL DEFAULT '0',
  time16 int(11) NOT NULL DEFAULT '0',
  time17 int(11) NOT NULL DEFAULT '0',
  time18 int(11) NOT NULL DEFAULT '0',
  time19 int(11) NOT NULL DEFAULT '0',
  time20 int(11) NOT NULL DEFAULT '0',
  time21 int(11) NOT NULL DEFAULT '0',
  time22 int(11) NOT NULL DEFAULT '0',
  time23 int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (date,app_id),
  CONSTRAINT m_user_ibfk_1 FOREIGN KEY (app_id) REFERENCES application (app_id));
```

##### 创建表m_province,对应“分省分应用”sheet
```
CREATE TABLE `m_province` (
  date date NOT NULL,
  province varchar(20) NOT NULL,
  app_id int(11) NOT NULL,
  pre_user int(11) NOT NULL DEFAULT '0',
  pre_order int(11) NOT NULL DEFAULT '0',
  pre_amount int(11) NOT NULL DEFAULT '0',
  cur_user int(11) NOT NULL DEFAULT '0',
  cur_order int(11) NOT NULL DEFAULT '0',
  cur_amount int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (date,province,app_id),
  CONSTRAINT m_province_ibfk_1 FOREIGN KEY (app_id) REFERENCES application(app_id));
```

##### 创建表m_nationwide，对应“全国”sheet
```
 CREATE TABLE m_nationwide (
  date date NOT NULL,
  app_id int(11) NOT NULL,
  pre_user int(11) NOT NULL DEFAULT '0',
  pre_order int(11) NOT NULL DEFAULT '0',
  pre_amount int(11) NOT NULL DEFAULT '0',
  cur_user int(11) NOT NULL DEFAULT '0',
  cur_order int(11) NOT NULL DEFAULT '0',
  cur_amount int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (date,app_id),
  CONSTRAINT m_nationwide_ibfk_1 FOREIGN KEY (app_id) REFERENCES application (app_id));
```
