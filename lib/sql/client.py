import sqlite3
import pandas as pd


trim_white_spaces = lambda value: ' '.join(value.split())



class SQLiteClient:    
    @staticmethod
    def inline_query(path, query):
        client = SQLiteClient(path)
        df = client.query(query)
        client.close()
        return df


    @staticmethod
    def inline_tables_definition(path, table=None):
        client = SQLiteClient(path)
        df = client.tables_definition(table)
        client.close()
        return df

    
    def __init__(self, path):
        self.__connection = sqlite3.connect(path)


    def close(self):
        self.__connection.close()


    def query(self, query):
        result = self.__connection.execute(query)
        return pd.DataFrame(
            data = [row for _, row in enumerate(result)],
            columns = [d[0] for d in result.description]
        )


    def tables_definition(self, table=None):
        where_table = f'AND name = \'{table}\'' if table else ''
        df = self.query(f'SELECT name, REPLACE (sql, "\'", \'"\') as SQL FROM sqlite_master WHERE type = \'table\' {where_table}')
        return [trim_white_spaces(r['SQL']) for r in df.to_dict('records')]
    
    
