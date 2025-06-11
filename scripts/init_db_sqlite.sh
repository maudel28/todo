#!/bin/bash

DB_FILE="./todo.db"

echo "Creating SQLite database at $DB_FILE..."

sqlite3 "$DB_FILE" <<EOF
CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    completed BOOLEAN DEFAULT 0,
    locked BOOLEAN DEFAULT 0
);
EOF

if [ $? -ne 0 ]; then
  echo "Failed!"
  exit 1
else
  echo "SQLite database initialized."
  exit 0
fi