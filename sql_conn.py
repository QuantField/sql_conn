import pandas as pd
import sqlite3, os


class SqlConn:
    
    def __init__(self, dbname = "mylocalDB.db", save_db=False):
        """Setting up Sqlite Connection

        Args:
            dbname (str, optional): [Name of Database]. Defaults to "mylocalDB.db".
            save_db (bool, optional): [Whether to keep the database]. Defaults to False.
        """
        self.dbname    = dbname
        self.save_db   = save_db
        print("creating database {}...".format(self.dbname))
        if os.path.isfile(dbname) and self.save_db is False:
            os.remove(dbname)
        self.conn      = sqlite3.connect(self.dbname)
        self.cursor    = self.conn.cursor()

    
    def query(self, query):
        """ Runs queries
        For select queries a pandas dataframe is returned

        Args:
            query (str): sql query to run

        Returns:
            pandas dataframe (for select queries): result of the query
        """
        if query.strip().upper().find('SELECT')== 0 :
            return self.fetch(query)
        else:
            self.cursor.execute(query)

    
    def fetch(self,query):
        return pd.read_sql_query(query, self.conn)

    
    def upload(self,df, tablename):
        """Saving pandas dataframe to a table in the database

        Args:
            df (pandas dataframe): dataframe to upload to database
            tablename (str): name of table refereing to the uploaded dataframe 
        """
        df.to_sql(tablename,con=self.conn, index=None)
    
    
    def quit(self):
        """Cleaning up

        Closing database connection and an optional delete of the database 
        """
        try:
            self.conn.close()
        except:
            raise EnvironmentError(self.conn)
        print("database connection successfully closed")
        if self.save_db is False:
            print("deleting databse {}...".format(self.dbname))
            os.remove(self.dbname)





