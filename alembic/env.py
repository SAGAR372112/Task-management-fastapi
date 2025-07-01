from sqlalchemy import engine_from_config
from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
import os
import sys

# Add app to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import Base  # or your correct models import
from app.database import DATABASE_URL  # if DATABASE_URL is defined in code

config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata

def run_migrations_online():
    connectable = create_engine(DATABASE_URL)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()
