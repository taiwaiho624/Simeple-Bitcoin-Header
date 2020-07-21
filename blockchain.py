from block import *
import hashlib

class Blockchain():

    def __init__(self):
        self.chain = []
        self.diff = 16
        self.maxNounce = 2**32
        self.target = 2 ** (256 - self.diff)

    def append(self,block):     
        #add previous block hash when appending new block
        if (len(self.chain) == 0):
            block.previous_block_hash = 0x0
        else:
            block.previous_block_hash = self.chain[-1].hash()
        
        #when the block hash is smaller than the threshold , append the block (16 leading zeros can be configured in the constructor)
        for i in range(self.maxNounce):
            if int(block.hash(), 16) <= self.target:
                self.chain.append(block)
                break
            else:
                block.nonce += 1

    def generateMerkleProof(self,tx):
       proof = []
       for block in self.chain:
           proof = block.generateMerkleProof(tx)
           if(len(proof) != 0):               
               return {
                   'block': block,
                   'proof': proof
               }
       if(len(proof) == 0):
           return "error"
    
    def verifyProof(self, tx, proofs, merkle_root):
        tempHash = tx.hash()
        for proof in proofs:
           if(proof['direction'] == 'left'):               
                tempHash =  hashlib.sha256(tempHash.encode('UTF-8') + proof['hash'].encode('UTF-8')).hexdigest()
           elif(proof['direction'] == 'right'):
                tempHash =  hashlib.sha256(proof['hash'].encode('UTF-8') + tempHash.encode('UTF-8') ).hexdigest()           
        if(tempHash == merkle_root):
            return True
        else:
            return False
    

    def __str__(self):
        result = ''
        for block in self.chain:
            result += block.__str__() + '\n'
        return result