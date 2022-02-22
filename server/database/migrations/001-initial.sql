CREATE TABLE readings(
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY,
  temperature REAL,
  humidity REAL,
);
