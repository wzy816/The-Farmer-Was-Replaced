
def heappush(heap, item):
	heap.append(item)
	_siftdown(heap, 0, len(heap) - 1)

def heappop(heap):
	last = heap.pop()
	if heap:
		return_item = heap[0]
		heap[0] = last
		_siftup(heap, 0)
		return return_item
	return last

def _siftdown(heap, startpos, pos):
	newitem = heap[pos]
	while pos > startpos:
		parentpos = (pos - 1) // 2
		parent = heap[parentpos]
		if newitem < parent:
			heap[pos] = parent
			pos = parentpos
			continue
		break
	heap[pos] = newitem

def _siftup(heap, pos):
	endpos = len(heap)
	startpos = pos
	newitem = heap[pos]
	childpos = 2 * pos + 1
	while childpos < endpos:
		rightpos = childpos + 1
		if rightpos < endpos and heap[childpos] > heap[rightpos]:
			childpos = rightpos
		heap[pos] = heap[childpos]
		pos = childpos
		childpos = 2 * pos + 1
	heap[pos] = newitem
	_siftdown(heap, startpos, pos)

if __name__ == '__main__':
	# heap = []
	# heappush(heap, 3)
	# heappush(heap, 1)
	# heappush(heap, 4)
	# heappush(heap, 1)
	# heappush(heap, 5)
	# print("Heap:", heap)  # Heap: [1, 1, 4, 3, 5]
	# poped = []
	# while heap:
	#     poped.append(heappop(heap))
	# print('Poped:', poped)



	heap = []
	heappush(heap, (1,'1'))
	heappush(heap, (2,'2'))
	heappush(heap, (2,'3'))
	heappush(heap, (4,'3'))
	heappush(heap, (2,'4'))
	print("Heap:", heap)
	poped = []
	while heap:
		poped.append(heappop(heap))
	print('Poped:', poped)

