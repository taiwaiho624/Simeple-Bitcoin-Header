from transaction import *
from merkle import *
import datetime
import hashlib
import math  



class Block():
    previous_block_hash = None
    timestamp = None
    nonce = 0
    merkle_root = None
    transactions = []
    def __init__(self, transactions):  
        now = datetime.datetime.now()
        self.timestamp = int(datetime.datetime.timestamp(now))
        self.transactions = transactions

        transactions_hash_list = []
        for transaction in transactions:
            transactions_hash_list.append(transaction.hash())    

        merkle_root_list = merkle_root(transactions_hash_list)        #parse the transactions_hash to find the merkle root 
        self.merkle_tree = merkle_root_list                           #the whole merkle tree
        self.merkle_root = merkle_root_list[-1]                       #the merkle root


    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') + 
            str(self.timestamp).encode('utf-8') + 
            str(self.previous_block_hash).encode('utf-8') + 
            str(self.merkle_root).encode('utf-8')
        )
        return h.hexdigest()

    def generateMerkleProof(self,tx):
        transactions_hash_list = []
        for transaction in self.transactions:
            transactions_hash_list.append(transaction.hash())
        if(tx.hash() not in transactions_hash_list):
            return []
        return merkle_proof(tx.hash(), transactions_hash_list, [])

    def __str__(self):
        transacations_string = ''
        for transaction in self.transactions:
            transacations_string += "  Transaction_id: " + transaction.hash() + " " + transaction.__str__() + " | " + datetime.datetime.fromtimestamp(transaction.timestamp).strftime("%m/%d/%Y, %H:%M:%S") + "\n"
        return  "Block Hash:       " + str(self.hash()) +"\n" +  "Previous Hash:    " + str(self.previous_block_hash) + "\n" + "nonce: "+ str(self.nonce) + "\n"+ "Merkle root hash: "+ self.merkle_root + "\n"+ "Transaction list: \n" + transacations_string +   "Timestamp: "+ str(self.timestamp) + " " + datetime.datetime.fromtimestamp(self.timestamp).strftime("%m/%d/%Y, %H:%M:%S")  + "\n--------------"

   
   

        


