#!/bin/bash

DB_NAME="todo_db"
USER="your_user"
PASSWORD="your_password"
HOST="localhost"
PORT="5432"

export PGPASSWORD="$PASSWORD"

echo "Initializing PostgreSQL schema..."

psql -U "$USER" -h "$HOST" -p "$PORT" -d "$DB_NAME" <<EOF
CREATE TABLE IF NOT EXISTS task (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    locked BOOLEAN DEFAULT FALSE
);
EOF

echo "PostgreSQL schema initialized."
