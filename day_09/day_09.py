import aocutils

# inspiration of using memory classes from Topaz
class Memory:
	def __init__(self, size, pos, idx):
		self.size = size
		self.pos = pos
		self.idx = idx
	
	def check(self):
		return (2 * self.pos + self.size - 1) * self.size // 2 * self.idx
	
	def __repr__(self):
		return f"Size: {self.size} | Pos: {self.pos} | Id: {self.idx}"

def rearrange(mems, freespaces):
	for mem in mems[::-1]:
		for freespace in freespaces:
			if mem.pos > freespace.pos and freespace.size >= mem.size:
				mem.pos = freespace.pos
				freespace.pos += mem.size
				freespace.size -= mem.size
	return mems

def checksum(mems):
	return sum(mem.check() for mem in mems)

@aocutils.timeFunction
def main():
	ref = list(map(int, aocutils.readFile(9)[0]))
	mems1, mems2, freespaces1, freespaces2, pos = [], [], [], [], 0

	idx = 0
	for p, r in enumerate(ref):
		if p % 2 == 0:
			mems2.append(Memory(r, pos, idx))
			for i in range(r):
				mems1.append(Memory(1, pos + i, idx))
			idx += 1
		else:
			freespaces2.append(Memory(r, pos, -1))
			for i in range(r):
				freespaces1.append(Memory(1, pos + i, -1))
		pos += r

	mems1, mems2 = rearrange(mems1, freespaces1), rearrange(mems2, freespaces2)
	total1, total2 = checksum(mems1), checksum(mems2)
	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()