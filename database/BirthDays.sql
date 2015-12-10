DROP TABLE IF EXISTS BirthDays CASCADE;
CREATE TABLE BirthDays (
  chatID        BIGINT,
  full_name     TEXT NOT NULL,
  age           BIGINT,
  last_modified BIGINT,
  already_asked BOOLEAN,
  PRIMARY KEY (full_name, chatID)
);

DROP FUNCTION IF EXISTS add_birthday(chat_idInput BIGINT, nameInput TEXT, ageInput BIGINT,
last_modifiedInput BIGINT, already_askedInput BOOLEAN ) CASCADE;
CREATE OR REPLACE FUNCTION add_BirthDay(chat_idInput       BIGINT, nameInput TEXT, ageInput BIGINT,
                                        last_modifiedInput BIGINT, already_askedInput BOOLEAN)
    RETURNS void AS $$
    BEGIN
      INSERT INTO BirthDays(chatID, full_name, age, last_modified, already_asked)
      VALUES (chat_idInput, nameInput, ageInput, last_modifiedInput, already_askedInput);
    END;
    $$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS get_birthday(nameInput TEXT, chat_idInput BIGINT) CASCADE ;
CREATE OR REPLACE FUNCTION get_birthday(nameInput TEXT, chat_idInput BIGINT)
    RETURNS TABLE(chat_id             BIGINT,
                  name                TEXT,
                  age                 BIGINT,
    last_modified BIGINT,
                  already_asked       BOOLEAN) AS $$
    BEGIN
      RETURN QUERY
        SELECT * FROM BirthDays
        WHERE full_name = nameInput and
              chatID = chat_idInput;
    END;
    $$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS update_birthday(nameInput TEXT, chat_idInput BIGINT, increment_by INT) CASCADE;
CREATE OR REPLACE FUNCTION update_birthday(nameInput TEXT, chat_idInput BIGINT, increment_by INT)
   RETURNS TABLE(_chat_id             BIGINT,
                  _name                TEXT,
                  _age                 BIGINT,
   _last_modified BIGINT,
                  _already_asked       BOOLEAN) AS $$
    BEGIN
      UPDATE BirthDays
        SET age = age + increment_by
        WHERE full_name = nameInput and
              chatID = chat_idInput;
        RETURN QUERY SELECT * FROM get_birthday(nameInput, chat_idInput);
    END;
    $$ LANGUAGE plpgsql;


DROP FUNCTION IF EXISTS remove_birthday(nameInput TEXT, chat_idInput BIGINT) CASCADE;
CREATE OR REPLACE FUNCTION remove_birthday(nameInput TEXT, chat_idInput BIGINT)
   RETURNS TABLE(_chat_id             BIGINT,
                  _name                TEXT,
                  _age                 BIGINT,
   _last_modified BIGINT,
                  _already_asked       BOOLEAN) AS $$
    BEGIN
    RETURN QUERY SELECT * FROM get_birthday(nameInput, chat_idInput);
      DELETE FROM BirthDays
      WHERE full_name = nameInput and
            chatID = chat_idInput;

    END;
    $$ LANGUAGE plpgsql; 