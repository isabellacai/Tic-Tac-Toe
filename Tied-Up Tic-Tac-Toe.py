X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    print \
            """
            Welcome to Tied-Up Tic-Tac-Toe! In traditional human vs. human 
            Tic-Tac-Toe, the first player to move has doubled chances of winning
            if they know what they're doing. However, in this version, you will
            be playing against me, the computer, eliminating any unfair advantages 
            (the computer will always make the perfect move). Can you play
            beyond perfection? Or will you be stuck in a tie?
            

            You will make your move by entering a number, 0 - 8. The number
            will correspond to the board position as shown below:

                                         0 | 1 | 2
                                        -----------
                                         3 | 4 | 5
                                        -----------
                                         6 | 7 | 8

            
            """
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = raw_input(question).lower()
    return response
    
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(raw_input(question))
    return response
        
def pieces():
    go_first = ask_yes_no("Would you like the first move? (y/n): ")
    if go_first == "y":
        print "\nThen take the first move. You will need it."
        human = X
        computer = O
    else:
        print "\nYour bravery will be your undoing... I will go first."
        computer = X
        human = O
    return computer, human
    
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
    
def display_board(board):
    print "\n\t", board[0], "|", board[1], "|", board[2]
    print "\t", "---------"
    print "\t", board[3], "|", board[4], "|", board[5]
    print "\t", "---------"
    print "\t", board[6], "|", board[7], "|", board[8], "\n"
    
def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves    
    
def winner(board):
    WAYS_TO_WIN = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [0, 3, 6],
                   [1, 4, 7],
                   [2, 5, 8],
                   [0, 4, 8],
                   [2, 4, 6]]
    
    for row in WAYS_TO_WIN:
        
        if board[0]==X and board[1]==X and board[2]==X:
            winner=board[0]
            return winner
        
        if board[3]==X and board[4]==X and board[5]==X:
            winner=board[3]
            return winner 
        
        if board[6]==X and board[7]==X and board[8]==X:
            winner=board[6]
            return winner 
        
        if board[0]==X and board[3]==X and board[6]==X:
            winner=board[0]
            return winner 
        
        if board[1]==X and board[4]==X and board[7]==X:
            winner=board[1]
            return winner   
        
        if board[2]==X and board[5]==X and board[8]==X:
            winner=board[2]
            return winner 
        
        if board[0]==X and board[4]==X and board[8]==X:
            winner=board[0]
            return winner        
        
        if board[2]==X and board[4]==X and board[6]==X:
            winner=board[2]
            return winner        
        
        
        
        if board[0]==O and board[1]==O and board[2]==O:
                winner=board[0]
                return winner
               
        if board[3]==O and board[4]==O and board[5]==O:
                winner=board[3]
                return winner 
               
        if board[6]==O and board[7]==O and board[8]==O:
                winner=board[6]
                return winner 
               
        if board[0]==O and board[3]==O and board[6]==O:
                winner=board[0]
                return winner 
               
        if board[1]==O and board[4]==O and board[7]==O:
                winner=board[1]
                return winner   
               
        if board[2]==O and board[5]==O and board[8]==O:
                winner=board[2]
                return winner 
               
        if board[0]==O and board[4]==O and board[8]==O:
                winner=board[0]
                return winner        
               
        if board[2]==O and board[4]==O and board[6]==O:
                winner=board[2]
                return winner        
        
            
        if EMPTY not in board:
            return TIE            
        return None
    
def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print "\nThat square is already occupied, foolish human. Choose another.\n"
    print "Fine..."
    return move
    
def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print "I shall take square number",
    
    # if computer can win, take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print move
            return move
        board[move] = EMPTY
        
    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print move
            return move
        board[move] = EMPTY
        
    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print move
            return move
            
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X
        
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print the_winner, "won!\n"
    else:
        print "It's a tie!\n"
    if the_winner == computer:
        print "As I predicted, human, I am triumphant once more. \n" \
            "Proof that computers are superior to humans in all regards.\n"
            
    elif the_winner == human:
        print "No, no! It cannot be! Somehow you tricked me, human. \n" \
            "But never again! I, the computer, so swears it\n!"
            
    elif the_winner == TIE:
        print "You were most lucky, human, and somehow managed to tie me. \n" \
            "Celebrate today... for this is the best you will ever achieve.\n"
            
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    
    
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
        
main()