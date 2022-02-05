# coding: utf-8

# In[39]:


from hashlib import sha256
import json
import time

from flask import Flask, request
import requests
import pyqrcode

def qr_code(s):
    
    d = pyqrcode.create(s)
    d.png('qrcode.png',scale=6)
    print('Code Executed properly')

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions=transactions
        # self.transactions = {"Product_name":"","Quantity":"0","Manufacturer":"Haris","Supplier":"ABC","Amount":1234}
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        
        
        

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


class Blockchain:
    # difficulty of our PoW algorithm
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        A function that adds the block to the chain after verification.
        Verification includes:
        * Checking if the proof is valid.
        * The previous_hash referred in the block and the hash of latest block
          in the chain match.
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def proof_of_work(self, block):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self,Desc):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof Of Work.
        """
        

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=Desc,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        return new_block.index


app = Flask(__name__)
blockchain = Blockchain()


# In[41]:


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
    

@app.route('/add',methods=['POST'])
def add_block_new():
    #  Quantity = request.form['Q']
    #  Manu = request.form['A']
    #  Name = request.form['B']
    #  sup = request.form['C']
    #  Amount = request.form['D']
    # previous_hash = blockchain.last_block.hash
    # new_index=blockchain.last_block.index+1
    # neew_block = Block(new_index, [], time.time(), previous_hash)
    # neew_block.hash = genesis_block.compute_hash()
    
    blockchain.mine(request.form)
    qr_code('http://127.0.0.1:5000/auth/'+blockchain.last_block.hash)
    imgPath='/qrcode.png'
    return json.dumps({'image_url': imgPath})

@app.route('/auth/<hash>')
def verification(hash):
    
    for block in blockchain.chain:
        print(block.hash)
        if hash == block.hash:
            return json.dumps({"status":"True"})
            
        
    return json.dumps({"status":"False"})


# In[45]:



app.run(debug=True, port=5000)
