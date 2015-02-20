import sys
import pprint
def main(arg):
	args = len(arg)
	
	if(args<2):
		pprint.pprint("Enter input file name")
	else:
		
		try:
		#read input
			base=readInput(arg[1])
			pprint.pprint(base)
			output=solve(base)
		
		except Exception as exc:
			pprint.pprint(exc.args)


def readInput(fileName):

	inputFile=fileName
	base=[]
	with open(inputFile) as f:
		for line in f:
			row=[]
			lineElems=(line.splitlines()[0]).split(' ')
			
			for elem in lineElems:
				row.append(elem)
			base.append(row)
	return base

def solve(base):
	#create mapper
	#loop
		#update base if 0 present else break
		#update mapper
		
	mapper=[];
	
	for i in range (9):
		row=[]
		for j in range (9):
			row.append([])
			if base[i][j]==0:
				row.append(getPossibleValues(base,i,j))
			
				
	return base


def getPossibleValues(base,i,j):
	possibles=range(1,10)
	for x in range(9):
		if base[i][x] in possibles:
			possibles.remove(base[i][x])
		if base[x][j] in possibles:
			possibles.remove(base[x][i])
	return possibles



if __name__ == "__main__":
   main(sys.argv)
