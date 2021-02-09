import mysql.connector

class Mysql:
    def __init__(self, host, user, passwd, database):
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            passwd = passwd,
            database = database
        )

    def Close(self):
        self.db.close()

    def CallProc(self, proc_name, proc_param=[]):
        results = []

        cursor = self.db.cursor()
        print('Call Store Procedure: ' + proc_name)
        cursor.callproc(proc_name, proc_param)
        for result_args in cursor.stored_results():
            results = result_args.fetchall()
        cursor.close()
        return results
    
    def Insert(self, query, param):
        cursor = self.db.cursor()
        cursor.execute(query, param)
        self.db.commit()
        print('Execute: ' + query + ', ' + str(cursor.rowcount) + ' record inserted')
        cursor.close()

    def Select(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
		
    def Update(self, query):
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()
        return cursor.rowcount
	
