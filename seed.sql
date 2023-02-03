TRUNCATE TABLE BOOKMARKTABLE;

ALTER SEQUENCE bookmarktable_id_seq RESTART WITH 1;

INSERT INTO bookmarktable(name, link) VALUES ('Google', 'https://www.google.com/');
INSERT INTO bookmarktable(name, link) VALUES ('LinkedIn', 'https://www.linkedin.com/');
INSERT INTO bookmarktable(name, link) VALUES ('GitHub', 'https://github.com/');
INSERT INTO bookmarktable(name, link) VALUES ('Reddit', 'https://www.reddit.com/');
INSERT INTO bookmarktable(name, link) VALUES ('Discord', 'https://discord.com/');
INSERT INTO bookmarktable(name, link) VALUES ('LeetCode', 'https://leetcode.com/');
INSERT INTO bookmarktable(name, link) VALUES ('Facebook', 'https://www.facebook.com/');
INSERT INTO bookmarktable(name, link) VALUES ('The Odin Project', 'https://www.theodinproject.com/');