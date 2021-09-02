import pymysql

conn = pymysql.connect(
    host='frostborn.cqgqrihjywqc.ap-south-1.rds.amazonaws.com',
    user='romanti', 
    password = "FBdb5500",
    db='frostborndb',
    )

class MySQLDataFetch:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def fetch_column(self):
        with conn:
            with conn.cursor() as c:
                c.execute(
                    "SELECT %s FROM %s;"
                    %(self.c_name,self.t_name)
                    )
                
                output = sum(c.fetchall(),())
                return output

    def fetch_item(self):
        with conn:
            with conn.cursor() as c:
                c.execute(
                    "SELECT %s FROM %s WHERE %s = '%s';" 
                    %(self.c_name,self.t_name,self.w_1,self.w_2)
                    )
                
                output = sum(c.fetchall(),())
                return output

class MySQLDataInsert:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def register(username,gamename,email,password):
    with conn:
        with conn.cursor() as c:
            c.execute(
                "INSERT INTO %s (%s,%s,%s,%s)VALUES ('%s', '%s', '%s', '%s');"
                %(
                    'User',
                    'UserName',
                    'GameName',
                    'Email',
                    'UserPassword',
                    username,
                    gamename,
                    email,
                    password
                )
            )
        conn.commit()

def password(username):
    password = MySQLDataFetch(c_name='UserPassword',t_name='User',w_1='UserName',w_2=username).fetch_item()
    return password

def items_names():
    items_names = MySQLDataFetch(c_name='Itemname',t_name='Items').fetch_column()
    return items_names

if __name__ == "__main__" :
    pass