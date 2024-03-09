# mypy: ignore-errors
from django.conf import settings
from langchain.indexes import SQLRecordManager
from langchain.indexes.base import RecordManager


def get_default_db_connection_string():
    default_db = settings.DATABASES["default"]
    db_name = default_db["NAME"]
    db_user = default_db["USER"]
    db_password = default_db["PASSWORD"]
    db_host = default_db["HOST"]
    db_port = default_db["PORT"]

    connection_string = (
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    print("CONNECTION STRING: ", connection_string)
    return connection_string


RESOURCES_NAMESPACE = "qdrant/resources"

RESOURCES_RECORD_MANAGER = None


def get_resources_record_manager() -> RecordManager:
    # pylint: disable=global-statement
    global RESOURCES_RECORD_MANAGER
    if RESOURCES_RECORD_MANAGER is not None:
        return RESOURCES_RECORD_MANAGER

    RESOURCES_RECORD_MANAGER = SQLRecordManager(
        RESOURCES_NAMESPACE, db_url=get_default_db_connection_string()
    )
    RESOURCES_RECORD_MANAGER.create_schema()
    return RESOURCES_RECORD_MANAGER
