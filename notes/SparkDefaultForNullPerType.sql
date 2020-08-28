-- SQL to create table and data for null replacement testing via Apache Spark SQL

DROP TABLE IF EXISTS tslp;
DROP TABLE IF EXISTS tetl;
CREATE TABLE tslp
(
	c_str VARCHAR(5),
	c_dt  date,
	c_ts  timestamp,
	c_num int,
	c_f float,
	n1 smallint,
	n2 integer,
	n3 bigint,
	n4 decimal,
	n5 numeric,
	b boolean,
	tx text,
	sr serial,
	bsr bigserial
);
CREATE TABLE tetl
(
	c_str VARCHAR(5) DEFAULT '-',
	c_dt  date DEFAULT('1900-01-01'),
	c_ts  timestamp DEFAULT ('1900-01-01 00:00:00'),
	c_num int DEFAULT 0,
	c_f float DEFAULT 0.0,
	n1 smallint DEFAULT 1,
	n2 integer DEFAULT 2, 
	n3 bigint DEFAULT 4,
	n4 decimal DEFAULT 8,
	n5 numeric DEFAULT 16,
	b boolean DEFAULT False,
	tx text DEFAULT 'Text',
	sr serial,
	bsr bigserial 
);

INSERT INTO tslp (c_dt, c_ts, c_num, c_f)  VALUES ('2020-03-31', '2020-03-31 00:00:00', 1, 1.0);
INSERT INTO tslp (c_str, c_ts, c_num,c_f) VALUES ('val', '2020-03-31 00:00:00', 1, 1.0);
INSERT INTO tslp (c_str, c_dt, c_num,c_f) VALUES ('val', '2020-03-31', 1, 1.0);
INSERT INTO tslp (c_str, c_dt, c_ts, c_f ) VALUES ('val', '2020-03-31', '2020-03-31 00:00:00', 1.0);
INSERT INTO tslp (c_str, c_dt, c_ts, c_num ) VALUES ('val', '2020-03-31', '2020-03-31 00:00:00', 1);

INSERT INTO tetl (c_dt, c_ts, c_num, c_f)  VALUES ('2020-03-31', '2020-03-31 00:00:00', 1, 1.0);
INSERT INTO tetl (c_str, c_ts, c_num,c_f) VALUES ('val', '2020-03-31 00:00:00', 1, 1.0);
INSERT INTO tetl (c_str, c_dt, c_num,c_f) VALUES ('val', '2020-03-31', 1, 1.0);
INSERT INTO tetl (c_str, c_dt, c_ts, c_f ) VALUES ('val', '2020-03-31', '2020-03-31 00:00:00', 1.0);
INSERT INTO tetl (c_str, c_dt, c_ts, c_num ) VALUES ('val', '2020-03-31', '2020-03-31 00:00:00', 1);

SELECT * FROM tslp;
SELECT * FROM tetl;
