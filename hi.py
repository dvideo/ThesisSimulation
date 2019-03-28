'''
def main():
	# dict = {'Emily':30,'John':40}
	# print(dict['Emily'])
	# dict['Joshua'] = 22
	# print("After adding Joshua: ",dict['Joshua'])


	# if 'Joshua' in dict:
	# 	print('Found him')
	# else:
	# 	print("Not Found")


	dict = ['Josh', 'Chris', 'Jake', 'Dwayne', 'Maria' , 'Maria']
	# print(nameAppearsTwice(dict))
	num_array = [3,4,1,2,9]



def nameAppearsTwice(dict):
	dict_check = {}
	for i in dict:
		if i in dict_check:
			return i
		else:
			dict_check[i] = 1
	return ''


def adds_up_to_ten(num_array):
	

main()
'''
'''
def main():
	print(factorial(4))

def factorial(n):
	if n==0:
		return 1
	elif n<0:
		return -1
	else:
		return n * factorial(n-1)

'''
'''
def main():
	primeNumber(11)

def primeNumber(n):
	for i in range(2,n):
		print(i)
		if n%i==0:
			print("not prime ",i)
			return

	print("prime")


'''
'''
def main():
	num = 1221
	temp = num
	rev =0

	while temp!=0:
		rev = (temp%10) + rev*10
		print(rev, temp)
		temp = temp//10

	print(rev, num)
		

	# while num>0:
	# 	num = num // 10
	# 	print(num)



'''
'''
class Person:
	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age


# 	def main():

josh = Person("Josh", "Gitter", 22)
print(josh.first)


def main():
	list = [3,4,1,2,9]
	print(pair(list))


def pair(list):
	for i in range(0,len(list)):
		for j in range(0,len(list)):
			if list[i]+list[j] ==10:
				return list[i],list[j]
	return('no pair')

def pair(list):
	nums_seen = { }
	for i in list:
		if 10-i in nums_seen:
			return 10-i, i
		else:
			nums_seen[i] = 1



main()

'''
'''

class Node:
	def __init__(self,value=None):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	# def insert(self, ):
	# 	print ("hi")


def removeDuplicates(list):
	currentNode= list.head
	duplicateCheck = currentNode.value
	if currentNode.next is None:
		return
	else:
		currentValue = currentNode.next.value
		while currentNode is not None:
			# prevNode = currentNode
			# currentNode=currentNode.next
			if duplicateCheck== currentValue:
				# prevNode.next = currentNode.next
				currentNode.next = current.next.next
			else:
				duplicateCheck = currentNode.value

list1 = LinkedList()
josh = Node(1)
chris = Node(1)
jake = Node(1)
mom = Node(0)
list1.head = josh
josh.next=chris
chris.next = jake
jake.next = mom

removeDuplicates(list1)
currentNode=list1.head
while currentNode is not None:
	print("value",currentNode.value)
	currentNode=currentNode.next

'''

# print(chris.next.value)



# main()


'''

def main():
	n1 = "2"
	n2 = "3"
	print(multiply(n1,n2))
	# n3 = str("1")*str("2")
	# print(n3)
	array = [[]]
	array[0] = [1,2,3]
	array2 = ['ate','car', 'bar', 'zit', 'bit', 'fit']
	# print(array[0])
	for i in range(0,len(array2)):
		array2[i] = ''.join(sorted(array2[i]))
	trying = 'sadfdfds'

	print('bye',''.join(sorted(trying)))
	array2.sort()
	print('hi',array2)

	matrix=[]
	matrix.append(['hi','bye'])
	matrix.append(['here','i','am'])
	print('matrix',matrix)


def multiply(n1,n2):
	n1 = int(n1)
	n2 = int(n2)
	return str(n1*n2)

'''
'''
def main():
	array = ['ate','the','tea', 'hte','nug']
	# get_anagrams(array)
	string = "hereIam"
	string = string[::-1]
	# print(string)

	print(validParenthesis("()"))




def validParenthesis(string):
	if len (string) <0:
		return False
	if len(string)==0:
		return True
	else:
		tempString = string[::-1]
		print (tempString, 'string', string)
		if tempString == string:
			return True
		else:
			return False		




def get_anagrams(array):
	anagrams = []
	dict1 = {}
	if len(array) < 1:
		return -1
	elif len(array) == 1:
		return array
	else:
		for i in range(0,len(array)):
			dict1[array[i]] = ''.join(sorted(array[i]))
	
	# Anagram_check = array[0]
	# For i in array:
	print(dict1)



main()
'''
'''
def main():
	s= '()()[]{{{}[]}}'
	print(isValid(s))

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
'''
'''
def main():
	n=-1290
	print(reverseInt(n))


def reverseInt(n):
	string = str(n)
	cont = True
	neg = False
	while cont:
		if string[len(string)-1] == '0':
			n = n//10
			string = str(n)
		else:
			cont=False
	if n < 0:
		neg = True
		n = abs(n)
	string = str(n)
	string = string[::-1]
	if neg:
		string = '-'+ string
	return string

'''

'''

def main():
	dictionary = {}
	string = 'LL'
	count = 0
	dictionary['L'] = 10
	dictionary['M'] = 20
	for i in string:
		count += dictionary[i]
	print(count)


	for i in dictionary:
		print (i)

'''
'''
def main():
	string = 'LLLM'
	print(convertRomanNumeral(string))

def convertRomanNumeral(string):
	dictionary = { }
	dictionary['I'] = 1
	dictionary['V'] = 5
	dictionary['X'] = 10	
	dictionary['L'] = 50
	dictionary['C'] = 100
	dictionary['D'] = 500
	dictionary['M'] = 1000
	count =0

	for i in string:
		count += dictionary[i]

	return count

 
main()
'''

'''
array = [10]
def main():
	print(array)
	function1()
	print(array)



def function1():
	array[0] = 3
'''


def main():
	trial = {}
	trial[10]=[2,1,2,12]
	for i in trial:
		print (trial[i])
main()