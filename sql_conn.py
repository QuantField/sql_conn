import pandas as pd
import sqlite3, os


class SqlConn:
    
    def __init__(self, dbname = None , save_db=False):
        """Setting up Sqlite Connection

        Args:
            dbname (str, optional): [Name of Database]. Defaults to in memory if is None
            save_db (bool, optional): [Whether to keep the database]. Defaults to False.
        """                        
        self.in_memory = False
        self.dbname    = dbname
        if self.dbname is None:
            self.in_memory = True
        self.save_db   = save_db
        if self.in_memory == False:
            print("creating database {}...".format(self.dbname))
            if os.path.isfile(dbname) and self.save_db is False:
                os.remove(dbname)
            self.conn      = sqlite3.connect(self.dbname)
            print("Database Connection established successfully")
        else:            
            self.conn = sqlite3.connect(":memory:")
            print("In memory Connection established successfully")
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
            return pd.read_sql_query(query, self.conn)
        else:
            self.cursor.execute(query)
            self.conn.commit()


    def save_table(self, table_name, csv_file_name):
        df = self.query("select * from {table}".format(table=table_name))
        df.to_csv(csv_file_name, index=False)

    
    def upload(self,df, tablename):
        """Saving pandas dataframe to a table in the database

        Args:
            df (pandas dataframe): dataframe to upload to database
            tablename (str): name of table refereing to the uploaded dataframe 
        """
        try:
            df.to_sql(tablename,con=self.conn, index=None)
        except:
            print("Dataframe upload failed")
        else:
            print("Upload succsessful")
    
    
    def quit(self):
        """Cleaning up

        Closing database connection and an optional delete of the database 
        """
        try:
            self.conn.close()
        except:
            raise EnvironmentError(self.conn)
        print("database connection successfully closed")
        if self.in_memory == False:
            if self.save_db is False:
                print("deleting database {}...".format(self.dbname))
                os.remove(self.dbname)
