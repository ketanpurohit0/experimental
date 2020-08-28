DROP TABLE IF EXISTS foo_left;
CREATE TABLE foo_left
(
	name_left varchar(10),
	uid_left varchar(5)
);
DROP TABLE IF EXISTS foo_right;
CREATE TABLE foo_right
(
	name_right varchar(10),
	uid_right varchar(5)
);

TRUNCATE TABLE foo_left;
TRUNCATE TABLE foo_right;

INSERT INTO foo_left  VALUES ('ABC_1234','abcde'); -- This row should match in a join with the one below on 'name_left', the _1234 is an artefact of sequencing
INSERT INTO foo_right VALUES ('ABC_35', 'abcde') -- This row should match in a join with the one above on 'name_right', the _35 is an artefact of sequencing
INSERT INTO foo_left  VALUES ('DEF','def');
INSERT INTO foo_right VALUES ('DEF', 'def')
