DROP TABLE IF EXISTS bookmarktable;

CREATE TABLE bookmarktable (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  link VARCHAR(255)
);
