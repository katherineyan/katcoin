
import hashlib

# UTILITY

def to_string(block):
	return "{0}\t{1}".format(block[2], block[0])

# function to see if hash is valid
def is_hash_valid(hash):
	return hash.startswith('0' * 3)

# function to find a valid hash
def calculate_valid_hash(start_hash):
	hash = str(start_hash)
	nonce = 0

	while not is_hash_valid(hash):
		temp = hash + str(nonce)
		hash = hashlib.sha256(temp.encode("utf-8")).hexdigest()
		nonce += 1
		print("nonce: " + str(nonce) + ", hash: " + hash)

	return hash


# BLOCKS

class Block:
	def __init__(self, transactions, parent_hash):
		hash_itself = hash((transactions, parent_hash))
		self.parent_hash = parent_hash
		self.transactions = transactions
		self.hash_itself = hash_itself


# MINING




def main():
	# create the genesis block
	genesis_block = Block("X paid $100 to Y", 0)

	# print hash of genesis block
	print("genesis_block_hash: ", genesis_block.hash_itself)

	# create another block
	block1 = Block("Y paid $20 to Z, X paid $10 to P", genesis_block.hash_itself)

	# print the hash of block1
	print("block1_hash: ", block1.hash_itself)

	# calculate a valid hash using the starting block
	if(False):
		valid_hash = calculate_valid_hash(genesis_block.hash_itself)
		print("valid_hash: ", valid_hash)


if __name__ == "__main__":
    main()



