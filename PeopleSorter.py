import sys
from Person import Person


def bubbleSort(L):
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j].age > L[j+1].age:
                L[j].age, L[j+1].age = L[j+1].age, L[j].age
                L[j].fName, L[j+1].fName = L[j+1].fName, L[j].fName
                L[j].lName, L[j+1].lName = L[j+1].lName, L[j].lName
    return L

def load(inputFilePath):
	try:
	    inputFile = open(inputFilePath)
	except Exception, e:
	    print >>sys.stderr, 'Cannot open', inputFilePath
	    exit()

	numberOfPeople = 0
	personList = []
	for line in inputFile:
	    personTraits = line.split(",")
	    numberOfPeople += 1
	    person = Person(personTraits[1], personTraits[0], int(personTraits[4]), int(personTraits[3]), int(personTraits[2]))
	    personList.append(person)
	return personList

def main():
    if len(sys.argv)!= 1:
        inputFilePath = sys.argv[1]
        personList = load(inputFilePath)

    	bubbleSort(personList)
    	for i in range(len(personList)):
    		print personList[i].lName+ " "+ str(personList[i].age)+ "hello"
    else:
        print "Usage -- python PeopleSorter input.txt"



main()
