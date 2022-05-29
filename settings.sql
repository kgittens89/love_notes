DROP DATABASE love_notes;
DROP USER love_notes_user;

CREATE DATABASE love_notes;
CREATE USER love_notes_user WITH PASSWORD 'love_notes_password';
GRANT ALL PRIVILEGES ON DATABASE love_notes TO love_notes_user