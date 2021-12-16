
# a block is stored as a tuple of 
# (parent_hash, transactions, hash_itself)

def get_parent_hash(block):
	return block[0]

def get_transactions(block):
	return block[1]

def get_hash_itself(block):
	return block[2]

# function to reate a block
def create_block(transactions, parent_hash):
	hash_itself = hash((transactions, parent_hash))
	return (parent_hash, transactions, hash_itself)

# function to create genesis block
def create_genesis_block(transactions):
	return create_block(transactions, 0)

# create the genesis block
genesis_block = create_genesis_block("Y paid $100 to X")

# print hash of genesis block
genesis_block_hash = get_hash_itself(genesis_block)
print("genesis_block_hash: ", genesis_block_hash)

# create another block
block1 = create_block("Y paid $20 to Z, X paid $10 to P", genesis_block_hash)

# print the hash of block1
block1_hash = get_hash_itself(block1)
print("block1_hash: ", block1_hash)