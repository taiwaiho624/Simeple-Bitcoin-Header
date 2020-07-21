import hashlib

#return the root of the merkle tree of transactions
def merkle_root(txHashList,wholelist = []):
    wholelist.extend(txHashList)
    if(len(txHashList) == 1):          
        #the whole merkle tree in the form of list     
        return wholelist
    newHashList = []
    for i in range(0, len(txHashList)-1, 2):   
        newHashList.append(hash2(txHashList[i], txHashList[i+1]))
    #handle the case that the transaction is of odd number
    if(len(txHashList) % 2 == 1):
        newHashList.append(hash2(txHashList[-1], txHashList[-1]))  

    return merkle_root(newHashList,wholelist)

def hash2(txA, txB): 
    return hashlib.sha256(txA.encode('utf-8')+txB.encode('utf-8')).hexdigest()   

def merkle_proof(tx, txHashList, proof=[]):
    if (len(txHashList) == 1):
        return proof
    newHashList = []
    newTx = None
    for i in range(0, len(txHashList)-1, 2):   
        if(tx == txHashList[i]):
            proof.append({
                'hash':txHashList[i+1],
                'direction': 'left'
            })
        elif( tx == txHashList[i+1]):
            proof.append({
                'hash' :txHashList[i],
                'direction': 'right'
            })
        newHashList.append(hash2(txHashList[i], txHashList[i+1]))        
        newTx = hash2(txHashList[i], txHashList[i+1])
    
    if(len(txHashList) % 2 == 1):
        if(txHashList[-1] == tx):
            proof.append({
                'hash': txHashList[-1],
                'direction': 'left'
            })
        newHashList.append(hash2(txHashList[-1], txHashList[-1])) 
    
    return merkle_proof(newTx,newHashList,proof)





