#Import modules
import datetime
import json
import hashlib
from flask import   Flask, jsonify

class Blockchain:
    #This function is used to create the first block in the blockchain
    #Thus the previous block is of course 0 
    def __int__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash= '0')
    
    #This function adds additional blocks
    def create_block(self, proof, previous_hash):
        block = {'index':len(self.chain) + 1,
                 'timestamp': str(datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    #This function prints the previous hash
    def print_previous_block(self):
        return self.chain[-1]
    
    #This is the function for proof if work
    def proofwork(self, previous_hash):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_hash).encode()).hexdigest()
            if hash_operation[:4] == '00000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof