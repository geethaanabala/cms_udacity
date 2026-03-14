import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "ac2df92a-66cf-4f47-875b-f5d027c33934"

    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT") or "images11"
    BLOB_STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY") or "gjnZ5s8WMq59un7FMwIusRF7PRudvxv36JHRkfvQZdyqhInaEHDB2jkuPbng920HcH4LXX5CMVvL+AStAaBIhQ=="
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER") or "images"

    SQL_SERVER = os.environ.get("SQL_SERVER") or "cms.database.windows.net"
    SQL_DATABASE = os.environ.get("SQL_DATABASE") or "cms"
    SQL_USER_NAME = os.environ.get("SQL_USER_NAME") or "cmsadmin"
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD") or "CMS4dmin"
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET") or "wN48Q~SVo5ecjrNs-Fac1wvs9cRVgXVYPxEmjc.r"
    CLIENT_ID = os.environ.get("CLIENT_ID") or "1660e7a3-74ae-4945-aea0-5bd962871c33"
    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"
