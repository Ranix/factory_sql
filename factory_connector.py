import configparser
from sql_connector import SqlConnector

class FactoryConnector:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        

    def _get_configuration(self, engine):
        """ Get the configuration of a specific engine.
        Args:
            engine (str): Engine name.

        Returns:
            dict: Engine configuration.
        """
        if engine in self.config:
            return self.config._sections[engine]
        else:
            return {'Error': "The engine doesn't exist in the configuration file."}


    def engine_list(self):
        """ Get the list of configurations in the config file.
        Returns:
            list: Engine configuration.
        """
        return [x for x in self.config._sections.keys()]


    def get_connection(self, engine):
        """ Get a specific engine object.
        Args:
            engine (str): Engine name.

        Returns:
            obj: Engine object.
        """
        configuration = self._get_configuration(engine)
        if engine == 'SQL':
            return SqlConnector(configuration)
        else:
            raise ValueError(configuration)


if __name__ == "__main__":
    Factory = FactoryConnector()
    
    #print(Factory.engine_list())

    sql_db = Factory.get_connection("SQL")

    sql_db.connect()
    tables = sql_db.engine_tables()
    # print(tables)

    employees = sql_db.read_table('employees')
    # print(type(employees))

    # Table operations
    # print(employees.columns.keys()) # return a list
    # print(employees.name)

    data = sql_db.get_data(employees)
    print(data, "Type:", type(data))

