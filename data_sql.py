import pymysql


class MySQLDataFetch:
    def __init__(self, item_for_fetch, table_name, where_1, where_2):
        self.item_for_fetch = item_for_fetch
        self.table_name = table_name
        self.where_1 = where_1
        self.where_2 = where_2

    def fetch_column(self):
        conn = pymysql.connect(
            host='frostborn.cqgqrihjywqc.ap-south-1.rds.amazonaws.com',
            user='romanti', 
            password = "FBdb5500",
            db='frostborndb',
            )
        
        
        with conn.cursor() as c:
            c.execute("SELECT %s FROM %s;" %(self.item_for_fetch,self.table_name))
            output = sum(c.fetchall(),())
            return output

        conn.close()

    def fetch_item(self):
        conn = pymysql.connect(
            host='frostborn.cqgqrihjywqc.ap-south-1.rds.amazonaws.com',
            user='romanti', 
            password = "FBdb5500",
            db='frostborndb',
            )
        


        with conn.cursor() as c:
            c.execute("SELECT %s FROM %s WHERE %s = %s;" %(self.item_for_fetch,self.table_name,self.where_1,self.where_2))
            output = c.fetchall()
            return output
        
        conn.close()

def password(username):
    password = MySQLDataFetch('UserPassword','User', 'UserName', username).fetch_item()
    return password
def items_names():
    items_names = MySQLDataFetch('Itemname','Items','','').fetch_column()
    return items_names

if __name__ == "__main__" :
    password('Rom')