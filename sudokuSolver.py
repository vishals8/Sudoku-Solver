import sys
import pprint
import pdb
def main(arg):
	args = len(arg)
	
	if(args<2):
		pprint.pprint("Enter input file name")
	else:
		
		try:
		#read input
			base=readInput(arg[1])
			#pprint.pprint(base)
			#pdb.set_trace()
			output=solve(base)
			if output == 0:
				pprint.pprint("Could not solve")
				pprint.pprint("Either the input is incorrect or there are multiple solutions possible.")				
			else:
				pprint.pprint(base)
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
				row.append(int(elem))
			base.append(row)
	return base

def solve(base):
	#create mapper
	#loop
		#update base if 0 present else break
		#update mapper
		
	done=0
	counter= 1
	while  done!=1 and counter <= 81:
		done=1
		counter+=1
		mapper=[];
		for i in range (9):
			row=[]
			for j in range (9):
				cell=[]
				if base[i][j]==0:
					done=0
					cell=getPossibleValues(base,i,j)
				row.append(cell)
			mapper.append(row)
			
		for i in range (9):
			for j in range (9):
				if len(mapper[i][j])==1:
					base[i][j]=mapper[i][j][0]
	#pprint.pprint(mapper)
	
	if done!=1:
		return 0
	return 1


def getPossibleValues(base,i,j):
	possibles=range(1,10)
	validx=getCorrectRange(i)
	validy=getCorrectRange(j)
	for x in range(9):
		if base[i][x] in possibles:
			possibles.remove(base[i][x])
		if base[x][j] in possibles:
			possibles.remove(base[x][j])
	for x in validx:
		for y in validy:
			if base[x][y] in possibles:
				possibles.remove(base[x][y])	
	return possibles


def getCorrectRange(index):
	valid=[]
	if index<3:
		valid= range(3)
	elif index<6:
		valid= range(3,6)
	elif index<9:
		valid= range(6,9)
	return valid
		
if __name__ == "__main__":
   main(sys.argv)
