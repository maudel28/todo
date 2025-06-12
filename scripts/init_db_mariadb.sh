#!/bin/bash

DB_NAME="todo_db"
USER="your_user"
PASSWORD="your_password"
HOST="localhost"
PORT="3306"

echo "Initializing MariaDB schema..."

mysql -u"$USER" -p"$PASSWORD" -h "$HOST" -P "$PORT" "$DB_NAME" <<EOF
CREATE TABLE IF NOT EXISTS task (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    locked BOOLEAN DEFAULT FALSE
);
EOF

if [ $? -ne 0 ]; then
  echo "Failed!"
  exit 1
else
  echo "MariaDB schema initialized."
  exit 0
fi
