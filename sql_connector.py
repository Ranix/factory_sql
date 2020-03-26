from connector import Connector
from sqlalchemy import Table, MetaData, engine, create_engine

from sqlalchemy.sql import select


class SqlConnector(Connector):
    
    def __init__(self, connection_parameters):
        url = self.create_url(connection_parameters)
        self.engine = create_engine(url)
        self.connection = None


    def create_url(self, connection_parameters):
        """ Create the configuration URL to connect to a specific engine,
        baso on a RFC-1738-style string.
        Args:
            connection_parameters (dic): Engine parameters.

        Returns:
            string : URL.
        """
        if 'sqlite' == connection_parameters["drivename"]:
            # Todo:
            # Check the OS to return a coorect path
            # Extract the path to create this string sqlite://<nohostname>/<path>
            # To use a SQLite :memory: database, specify an empty URL: 'sqlite://'
            return f'sqlite:///{connection_parameters["database"]}'
        url = engine.url.URL(
            connection_parameters["drivename"],
            username=connection_parameters["username"],
            password=connection_parameters["password"],
            host=connection_parameters["host"],
            port=connection_parameters["port"],
            database=connection_parameters["database"],
            query=None)
        return url


    def connect(self):
        self.engine.connect()
        # return print('connect to SQL')


    def disconnect(self):
        self.engine.close()
        # return print('disconnect from SQL')


    def engine_tables(self):
        """ Get all the tables inside the database.
        Returns:
            list: Tables in database.
        """
        return self.engine.table_names()
    

    def read_table(self, table_name=None):
        """Tranform a SQL table in to a python objet.
        Args:
            Table name (string): Name of the table.

        Returns:
            obj : Python table object.
        """
        if table_name:
            metadata = MetaData(self.engine)
            table_obj = Table(table_name, metadata, autoload=True)
            #print(table_obj.columns.keys())
            return table_obj

    def get_data(self, table_obj):
        query = select([table_obj])
        ResultProxy = self.engine.execute(query)
        return ResultProxy.fetchall()


    def create(self):
        return 'Insert'
    
 
    def update(self):
        return 'Update'


    def delete(self):
        return 'Delete'