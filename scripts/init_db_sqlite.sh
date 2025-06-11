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

echo "SQLite database initialized."
