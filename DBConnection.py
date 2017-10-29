import _mysql

def ConnectDB(host, user, password, dbName):
    return _mysql.connect(host, user, password, dbName)

def InsertRating(cnx, questionID, questionText, rating, customerID):
    cnx.query("INSERT INTO Test VALUES ('TEst text lol');")
    print("InsertRating in DB succeeded");

def InsertKeyPhrase(cnx, customerID, keyPhrase):
    cnx.query("INSERT INTO Test VALUES ('TEst text lol');")
    print("InsertKeyPhrase in DB succeeded");

def CloseDB(cnx):
    cnx.close() 
