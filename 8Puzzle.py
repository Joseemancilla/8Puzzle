

#####  8 puzzle  ######
#### Jose Mancilla ####
######### AI ##########


#Start class
class Board:

#Function to initialize class objects
    def __init__(s,board,depth,value):

        s.board = board
        s.depth = depth
        s.value = value


#Function find_cero
#Takes the board a puzzle and the cero to find
    def find_cero(s,bor,cero):
        #Loop throught the board to find the 0 in our board
        for i in range(0,len(s.board)):
            for j in range(0,len(s.board)):
                if bor[i][j] == cero:
                    return i,j #return the 0



#Function to move the board in directions and create the corresponding nodes
    def nodes(s):
    #Find in the board our 0
        row,col = s.find_cero(s.board,'0')
#pos val has the values of our 0 to move to one of the directions according to the puzzle
        pos_val = [[row,col-1],[row,col+1],[row-1,col],[row+1,col]]
        # initialize all_child array
        all_child = []
        #i holds the values of the moves of 0
        for i in pos_val:
            c = s.move(s.board,row,col,i[0],i[1])
            #if the returnd value of move is not none depth+1 and apend the node
            if c is not None:
                child_node = Board(c,s.depth+1,0)
                all_child.append(child_node) #append the node

        #return the all_child array
        return all_child




# Funciton move takes the board and moves our 0 in the position
    def move(s,bor,row1,col1,row2,col2):

    #if out of board return none to nodes funtion
        if row2 >= 0 and row2 < len(s.board) and col2 >= 0 and col2 < len(s.board):
            cur_board = [] #initilaize cur_board
            cur_board = s.new(bor) #call to new funtion that send the chunks of the function
            cur = cur_board[row2][col2]
            cur_board[row2][col2] = cur_board[row1][col1]
            cur_board[row1][col1] = cur
            return cur_board #return the board
        else:
            #return none to nodes
            return None




#Function new
    def new(s,numbers):
        num = []
        #i holds the the first three values of [] and moves on tothe next three
        #[1,2,3] ->
        #loop through numbers
        for i in numbers:
            n = [] #initzialize array n
            for j in i: #Loop through the 3 numbers
                n.append(j) #send those numbers to n
            num.append(n)#apend the chunk of 3
        return num #send the chunks





#class game
class game:
#Function init initialize the size and open and close the list
    def __init__(s,n):


        s.open = []
        s.closed = []
        s.size = n


#Function to recieve the input puzzle from the player
    def read_puzzle(s):
        bor = []
        #loop from 0 to size
        for i in range(0,s.size):
        #tul holds the input of the board
            tul = input()
            bor.append(tul)#append the input board
        return bor #return the board



#function to calculate the heuristic of moves
    def fvalue(s,initial,goal):
        #return hvalue functio with the intiial board and the goal
        return s.hvalue(initial.board,goal)+initial.depth



#Function to calculate the how many moves to the goal state of boards
    def hvalue(s,initial,goal):
        count = 0 #start the count
        for i in range(0,s.size):
            for j in range(0,s.size):
                #if our initial  pos is not our goal and is not the cero we are looking for
                if initial[i][j] != '0' and initial[i][j] != goal[i][j]:
                    #increment the count
                    count += 1
        return count #return the count of moves



#Funciton Apuzzle to print board and send puzzle
    def Apuzzle (s):
        print("Enter the initial state of the 8 puzzle: \n")
        #intiial is the call to inpur our initila board
        initial = s.read_puzzle()
        print("Enter the goal state of your 8 puzzle: \n")
        #the goal state read
        goal = s.read_puzzle()

        initial = Board(initial,0,0)
        #send intial fvaluefunction  with the initl and the goal
        initial.value = s.fvalue(initial,goal)

        #append the first node
        s.open.append(initial)

#While
        while True:
            cur = s.open[0]
            #print the division between the boards
            print("")
            print("  | ")
            print ("   ")

     #loop though the current boards and print it
            for i in cur.board:
                for j in i:
                    print(j,end=" ") #end parameter print each number separately
                print("")#chucks of 3

    #if the goal node is 0 then we have our state goal and break
            if(s.hvalue(cur.board,goal) == 0):
                break
        #loop though the cur board.nodes
            for i in cur.nodes():
                i.value = s.fvalue(i,goal) #send the fvalue with curent i and our goal
                s.open.append(i) #append each one
            s.closed.append(cur) #close when done
            del s.open[0] # delete s[0]

    #sort the list on the f value
    #key lambda sorts by paramters
            s.open.sort(key = lambda x:x.value,reverse=False)#set reversea argumnet to false





#Main
#bor is our game class with 3
bor = game(3)
#call bor3 with Apuzzle function
bor.Apuzzle()
