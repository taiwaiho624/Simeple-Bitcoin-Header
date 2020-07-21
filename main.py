from block import *
from blockchain import *
from transaction import *

def printProof(result):
    if(result == "error"):
        print("This transaction does not exist in the blockchain")
    else:
        string = ""
        for proof in result['proof']:
            string += "hash value: " + proof['hash'] + " | direction: " + proof['direction'] + '\n'
        print("This transaction is included in the block with id: " + result['block'].hash() + '\nwith merkle proof: \n' +  string )

def printVerify(result):
    if(result == True):
        print("The verification returns True")
    else:
        print("The verification returns False")


blockchain = Blockchain()

#[timestamp(t1)] Alice -> Bob: 10
transaction1a = Transaction(1589091527, "Alice", "Bob" , 10)
#[timestamp(t2)] Alice -> Bob: 1
transaction2a = Transaction(1589091627, "Alice", "Bob" , 1)
#[timestamp(t3)] Charlie -> Dan: 6
transaction2b = Transaction(1589091727, "Charlie", "Dan" , 6)
#[timestamp(t4)] Dan -> Bob: 2
transaction2c = Transaction(1589091827, "Dan", "Bob" , 2)
#[timestamp(t5)] Bob -> Alice: 4
transaction3a = Transaction(1589091927, "Bob", "Alice" , 4)
#[timestamp(t6)] Elle -> Alice: 9
transaction3b = Transaction(1589092027, "Elle", "Alice" , 9)
#[timestamp(t7)] Bob -> Alice: 5
transaction4a = Transaction(1589092127, "Bob", "Alice" , 5)
#[timestamp(t8)] Elle -> Alice: 3
transaction4b = Transaction(1589092227, "Elle", "Alice" , 3)

#first linked block
block1 = Block([transaction1a])
# #second linked block
block2 = Block([transaction2a, transaction2b, transaction2c])
# #third linked block
block3 = Block([transaction3a, transaction3b])
# #forth linked block
block4 = Block([transaction4a, transaction4b])

blockchain.append(block1)
blockchain.append(block2)
blockchain.append(block3)
blockchain.append(block4)
print(blockchain)

print ("-----------------------------------------------------")
print("The Merkle Proof for transaction 3a")
result = blockchain.generateMerkleProof(transaction3a)
printProof(result)
verification = blockchain.verifyProof(transaction3a, result['proof'], result['block'].merkle_root)
printVerify(verification)

print ("-----------------------------------------------------")
print("The Merkle Proof for transaction 4b")
result = blockchain.generateMerkleProof(transaction4b)
printProof(result)
verification = blockchain.verifyProof(transaction4b, result['proof'], result['block'].merkle_root)
printVerify(verification)

print ("-----------------------------------------------------")
print("Just show a testing case where the transaction does not exist in the blockchain")
result = blockchain.generateMerkleProof(Transaction(1589092227,"John", "Alce", 2))
printProof(result)



