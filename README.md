## ✅ Flask ToDo App

A minimalist ToDo web application built with **Flask**, **SQLAlchemy**, and configurable to work with **SQLite**, **MariaDB**, or **PostgreSQL**.

---

### 📦 Requirements

* Python 3.9+
* Virtual environment (recommended)
* One of the following database engines:

  * SQLite
  * MariaDB (10+)
  * PostgreSQL (12+)

---

### 🔧 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/maudel28/todo.git
cd flask-todo-app
```

2. **Create a virtual environment and install dependencies:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Create your configuration files:**

> ❗ Both `config.yaml` and `db-config.yaml` are required.

#### `db-config.yaml`

```yaml
engine: sqlite

sqlite:
  database: /full/path/to/todo.db

mariadb:
  user: root
  password: mariadbpass
  host: localhost
  port: 3306
  database: todo_db

postgresql:
  user: postgres
  password: pgpass
  host: localhost
  port: 5432
  database: todo_db
```

#### `config.yaml`

```yaml
database_config_path: "/full/path/to/db-config.yaml"

style:
  background_color: "#ffffff"
  text_color: "#000000"
  button_color: "#007bff"
  button_text_color: "#ffffff"
  completed_text_color: "#888888"
```

4. **Initialize your database:**

Use one of the provided scripts inside `scripts/`:

```bash
# For SQLite
./scripts/init_db_sqlite.sh

# For MariaDB
./scripts/init_db_mariadb.sh

# For PostgreSQL
./scripts/init_db_postgres.sh
```

---

### 🚀 Run the App

```bash
python run.py
```

Visit `http://localhost:8080` in your browser.

---

### 📌 Notes

* All tasks can be added, completed, and deleted — unless **locked**, in which case they cannot be deleted from the UI.
* Task lock status can only be changed directly via database access.
* The UI is styled dynamically using values from `config.yaml`.

---

### 📎 About `requirements.txt`

This project installs support for all three database engines:

```txt
Flask
SQLAlchemy
PyYAML
pymysql
psycopg2-binary
```

> ⚠️ Note:
>
> * If using **SQLite**, neither `pymysql` nor `psycopg2-binary` will be used.
> * If using **MariaDB**, `psycopg2-binary` is not required.
> * If using **PostgreSQL**, `pymysql` is not required.
>
> You may omit unused drivers from your environment manually if desired.
