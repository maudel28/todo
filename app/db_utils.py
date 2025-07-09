engine_type = None

def construct_db_uri(cfg):
    global engine_type
    engine_type = cfg.get("engine")
    engine = engine_type
    #engine = cfg.get("engine")

    if engine == "sqlite":
        sqlite_cfg = cfg["sqlite"]
        return f"sqlite:///{sqlite_cfg['database']}"

    elif engine == "mariadb":
        mdb = cfg["mariadb"]
        return f"mysql+pymysql://{mdb['user']}:{mdb['password']}@{mdb['host']}:{mdb['port']}/{mdb['database']}"

    elif engine == "postgresql":
        pg = cfg["postgresql"]
        return f"postgresql+psycopg2://{pg['user']}:{pg['password']}@{pg['host']}:{pg['port']}/{pg['database']}"

    else:
        raise ValueError(f"Unsupported engine: {engine}")

def get_engine_type():
    return engine_type
