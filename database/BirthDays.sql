DROP TABLE IF EXISTS BirthDays CASCADE;
CREATE TABLE BirthDays (
  id                  SERIAL,
  name                TEXT NOT NULL,
  age            BIGINT,
  PRIMARY KEY (id)

);

DROP FUNCTION IF EXISTS add_birthday(nameInput TEXT, ageInput BIGINT) CASCADE ;
CREATE OR REPLACE FUNCTION add_BirthDay(nameInput TEXT, ageInput BIGINT)
    RETURNS void AS $$
    BEGIN
      INSERT INTO BirthDays(name, age) VALUES (nameInput, ageInput);
    END;
    $$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS get_birthday(nameInput TEXT) CASCADE ;
CREATE OR REPLACE FUNCTION get_birthday(nameInput TEXT)
    RETURNS TABLE(name TEXT, age BIGINT) AS $$
    BEGIN
      RETURN QUERY
        SELECT b.name, b.age FROM BirthDays b;
    END;
    $$ LANGUAGE plpgsql;
