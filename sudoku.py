def solution(nodes, color):
	for X in nodes:
		for Y in nodes[X]:
			if color[X] == color[Y] or color[X] is None:
				return False
	return True

##########################################


def recur2(nodes, color):
	if solution(nodes, color):
		return True
	n = "Handy"
	best = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	presto = "Handy"
	for Q in names:
		if color[Q] is None:
			avail = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			for L in nodes[Q]:
				if color[L] in avail:
					avail.remove(color[L])
			if len(avail) == 0:
				return False
			elif len(avail) == 1:
				best = avail
				presto = Q
				break
			elif len(avail) < len(best):
				best = avail
				presto = Q

	if presto == "Handy":
		return False
	n = presto
	for X in best:
		color[n] = X
		if recur(nodes, color):
			return True
		color[n] = None
	return False


nodes = {}
color = {}
names = []

#Sudoku neighbors
for X in range(81):
	names.append(str(X))
	color[str(X)] = None
	nodes[str(X)] = []
	for Y in range(X - (X % 9), X - (X % 9) + 9):
		if Y == X:
			continue
		nodes[str(X)].append(str(Y))
	for Y in range(X % 9, X % 9 + 80, 9):
		if Y == X:
			continue
		nodes[str(X)].append(str(Y))
	
	if X in [0, 1, 2, 9, 10, 11, 18, 19, 20]:
		for Y in [0, 1, 2, 9, 10, 11, 18, 19, 20]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))
	if X in [3, 4, 5, 12, 13, 14, 21, 22, 23]:
		for Y in [3, 4, 5, 12, 13, 14, 21, 22, 23]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))
	if X in [6, 7, 8, 15, 16, 17, 24, 25, 26]:
		for Y in [6, 7, 8, 15, 16, 17, 24, 25, 26]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))
	if X in [27, 28, 29, 36, 37, 38, 45, 46, 47]:
		for Y in [27, 28, 29, 36, 37, 38, 45, 46, 47]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))
	if X in [30, 31, 32, 39, 40, 41, 48, 49, 50]:
		for Y in [30, 31, 32, 39, 40, 41, 48, 49, 50]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))
	if X in [33, 34, 35, 42, 43, 44, 51, 52, 53]:
		for Y in [33, 34, 35, 42, 43, 44, 51, 52, 53]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))
	if X in [54, 55, 56, 63, 64, 65, 72, 73, 74]:
		for Y in [54, 55, 56, 63, 64, 65, 72, 73, 74]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))
	if X in [57, 58, 59, 66, 67, 68, 75, 76, 77]:
		for Y in [57, 58, 59, 66, 67, 68, 75, 76, 77]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))
	if X in [60, 61, 62, 69, 70, 71, 78, 79, 80]:
		for Y in [60, 61, 62, 69, 70, 71, 78, 79, 80]:
			if str(Y) not in nodes[str(X)] and X != Y:
				nodes[str(X)].append(str(Y))


	game = list("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......")
	
	for X in range(len(game)):
		if game[X] != ".":
			color[str(X)] = int(game[X])
	recur2(nodes, color)

	print(" ")
	for Y in range(0, 81, 9):
		print(color[str(Y)], color[str(Y + 1)], color[str(Y + 2)], color[str(Y + 3)], color[str(Y + 4)], color[str(Y + 5)], color[str(Y + 6)], color[str(Y + 7)], color[str(Y + 8)])
	print("")
