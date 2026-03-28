from alembic import context
from sqlalchemy import engine_from_config, pool
import os

from app.db.base import Base
from app.db import models  # noqa: F401

config = context.config

def run_migrations_offline():
    url = os.getenv("DATABASE_URL")
    context.configure(url=url, target_metadata=Base.metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    cfg = config.get_section(config.config_ini_section) or {}
    cfg["sqlalchemy.url"] = os.getenv("DATABASE_URL")
    connectable = engine_from_config(cfg, prefix="sqlalchemy.", poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=Base.metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
