
import hashlib
from datetime import datetime

# BLOCK
class Block:
	def __init__(self, transactions, parent_hash):
		self.timestamp = datetime.utcnow()
		self.parent_hash = parent_hash
		self.transactions = transactions
		self.calculate_valid_hash()

	def is_hash_valid(self, calc_hash):
		return calc_hash.startswith('0' * 3)

	def calculate_valid_hash(self):
		calc_hash = ''
		nonce = 0

		while not self.is_hash_valid(calc_hash):
			temp = calc_hash + str(nonce)
			calc_hash = hashlib.sha256(temp.encode("utf-8")).hexdigest()
			nonce += 1

		self.hash_itself = calc_hash

	def to_string(self):
		return "{0}\t{1}\t{2}".format(self.transactions, self.timestamp, self.parent_hash)


# BLOCKCHAIN
class Blockchain:
	def __init__(self):
		self.blocks = []
		self.set_genesis_block()

	def set_genesis_block(self):
		genesis_block = Block("Genesis\t", '0'*64)
		self.blocks.append(genesis_block)

	def get_last_hash(self):
		last_block = self.blocks[-1]
		return last_block.hash_itself

	def add_new_block(self, transactions):
		prev_hash = self.get_last_hash()
		new_block = Block(transactions, prev_hash)
		self.blocks.append(new_block)

	def get_blocks(self):
		return self.blocks




def main():

	# creating a blockchain
	blockchain = Blockchain()
	blockchain.add_new_block("First block")
	blockchain.add_new_block("Second block")
	blockchain.add_new_block("Third block")
	blockchain.add_new_block("Fourth block")
	blockchain.add_new_block("Fifth block")

	for block in blockchain.get_blocks():
		print()
		print(block.to_string())




if __name__ == "__main__":
    main()



