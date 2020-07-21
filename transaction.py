import datetime
import hashlib

class Transaction():
    def __init__(self,timestamp,payer,payee,amount):
        self.timestamp = timestamp
        self.data = "[" + str(timestamp) + "]" + payer + "->" + payee + ":" + str(amount)

    #transaction_id
    def hash(self):
        return hashlib.sha256(self.data.encode('UTF-8')).hexdigest()

    def __str__(self):
        return self.data


    