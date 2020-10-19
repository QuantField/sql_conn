import sys
sys.path.append("../")
from sqlconn import SqlConn
import pandas as pd


def _create_dataframe():
    data = [
    ['PITTSBURGH' ,160922],
    ['CORAOPOLIS' ,10359],
    ['MC KEESPORT' ,9104],
    ['GIBSONIA' ,6698],
    ['SEWICKLEY' ,6282],
    ['MC KEES ROCKS' ,6131],
    ['WEXFORD' ,6056],
    ['BETHEL PARK' ,5849],
    ['MONROEVILLE' ,5428],
    ['CARNEGIE' ,5209],
    ['CLAIRTON' ,4886],
    ['ALLISON PARK' ,4635],
    ['WEST MIFFLIN' ,4534],
    ['BRIDGEVILLE' ,4501],
    ['HOMESTEAD' ,4400],
    ['VERONA' ,4028],
    ['OAKDALE' ,3080],
    ['GLENSHAW' ,2941],
    ['ELIZABETH' ,2880]]
    df = pd.DataFrame(data, columns = ['PROPERTYCITY' ,'CNT'])
    return df 

def test_upload_dataframe():
    df = _create_dataframe()
    sql= SqlConn()
    sql.upload(df,'sales')
    res = sql.query("select min(CNT) as cnt from sales")
    assert res['cnt'][0] == 2880


def test_append_dataframe():
    df= pd.DataFrame([['DALLAS',1000]], columns = ['PROPERTYCITY' ,'CNT'])
    sql = SqlConn()
    sql.upload(df,'sales', append=True)
    res = sql.query("select min(CNT) as cnt from sales")
    assert res['cnt'][0] == 1000
    

