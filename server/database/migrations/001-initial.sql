--------------------------------------------------------------------------------
-- Up
--------------------------------------------------------------------------------
CREATE TABLE readings(
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY,
  temperature REAL,
  humidity REAL
);
CREATE TABLE alarm (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  is_set BOOLEAN NOT NULL CHECK (is_set IN (0, 1))
);
INSERT INTO alarm (name, is_set)
VALUES ('default', 0);
--------------------------------------------------------------------------------
-- Down
--------------------------------------------------------------------------------
DROP TABLE readings;
DROP TABLE alarm;
