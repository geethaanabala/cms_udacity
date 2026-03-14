import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('ac2df92a-66cf-4f47-875b-f5d027c33934') 

    BLOB_ACCOUNT = os.environ.get('images11') 
    BLOB_STORAGE_KEY = os.environ.get('gjnZ5s8WMq59un7FMwIusRF7PRudvxv36JHRkfvQZdyqhInaEHDB2jkuPbng920HcH4LXX5CMVvL+AStAaBIhQ==') 
    BLOB_CONTAINER = os.environ.get('images') 

    SQL_SERVER = os.environ.get('cms1.database.windows.net') 
    SQL_DATABASE = os.environ.get('cms')
    SQL_USER_NAME = os.environ.get('cmsadmin') 
    SQL_PASSWORD = os.environ.get('CMS4dmin') 
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "yDj8Q~1RUTTAois3IVM_tCPFt7icwjnhJvUbBbRd"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "83486ecb-fdc7-417d-80c2-6a5145a9ab15"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
