import external as ext
class player:
    def __init__(self,turn,side,pieces,name):
        self.turn = turn
        self.side = side
        self.pieces = pieces
        self.name = name
class piece:
    def __init__(self,side,alive,position,first_move):
        self.side = side
        self.alive = alive
        self.position = position
        self.first_move = first_move

class bishop(piece):
    def __init__(self,side,alive,position,first_move):
        super().__init__(side,alive,position,first_move)

    def determine_valid_squares(self,init_position,side,all_pieces,enemy_pieces,board):
        x = 0
        y = 0
        squares = board.copy()
        removed_squares = []

        for i in squares:
            delta_x = abs(i[0] - init_position[0])
            delta_y = abs(i[1] - init_position[1])

            if delta_x != delta_y:
                removed_squares.append(i)
            else:
                if i in all_pieces:
                    removed_squares.append(i.position)
            
                    
        for i in removed_squares:
            squares.remove(i)
        return squares

class knight(piece):
    def __init__(self,side,alive,position,first_move):
        super().__init__(side,alive,position,first_move)

    def determine_valid_squares(self,init_position,side,all_pieces,enemy_pieces,board):
        x = 0
        y = 0
        squares = board.copy()
        removed_squares = []

        all_positions = []
        for i in all_pieces:
            all_positions.append(i.position)

        for i in squares:
            delta_x = abs(i[0] - init_position[0])
            delta_y = abs(i[1] - init_position[1])

            if (not(delta_x == 1 and delta_y ==2)) and (not(delta_x == 2 and delta_y == 1)) and not i in removed_squares:
                removed_squares.append(i) 
            else:
                if i in all_positions and not i in removed_squares:
                    removed_squares.append(i)
            
                    
        for i in removed_squares:
            squares.remove(i)
        return squares        

class rook(piece):
    def __init__(self,side,alive,position,first_move):
        super().__init__(side,alive,position,first_move)

    def determine_valid_squares(self,init_position,side,all_pieces,enemy_pieces,board):
        x = 0
        y = 0
        squares = board.copy()
        removed_squares = []

        all_positions = []
        for i in all_pieces:
            all_positions.append(i.position)

        for i in squares:
            delta_x = abs(i[0] - init_position[0])
            delta_y = abs(i[1] - init_position[1])

            if (not(delta_x > 0 and delta_y == 0)) and (not(delta_x == 0 and delta_y > 0)) and (not i in removed_squares):
                removed_squares.append(i) 
            else:
                if i in all_positions:
                    removed_squares.append(i)
            
                    
        for i in removed_squares:
            squares.remove(i)
        return squares        

class queen(piece):
    def __init__(self,side,alive,position,first_move):
        super().__init__(side,alive,position,first_move)

    def determine_valid_squares(self,init_position,side,all_pieces,enemy_pieces,board):
        x = 0
        y = 0
        squares = board.copy()
        removed_squares = []

        all_positions = []
        for i in all_pieces:
            all_positions.append(i.position)

        for i in squares:
            delta_x = abs(i[0] - init_position[0])
            delta_y = abs(i[1] - init_position[1])

            if (not(delta_x > 0 and delta_y == 0)) and (not(delta_x == 0 and delta_y > 0)) and (delta_x != delta_y):
                if not i in removed_squares:
                    removed_squares.append(i) 
            else:
                if i in all_positions and not i in removed_squares:
                        removed_squares.append(i)
            
                    
        for i in removed_squares:
            squares.remove(i)
        return squares     

class pawn(piece):
    def __init__(self,side,alive,position,first_move):
        super().__init__(side,alive,position,first_move)

    def determine_valid_squares(self,init_position,side,all_pieces,enemy_pieces,board):
        '''
        "all" here indicates the player making the move
        '''
        x = 0
        y = 0
        squares = board.copy()
        removed_squares = []

        all_positions = []
        for i in all_pieces:
            all_positions.append(i.position)

        enemy_positions = []
        for i in enemy_pieces:
            enemy_positions.append(i.position)

        for i in squares:
            delta_x = abs(i[0] - init_position[0])
            if side == "white":
                delta_y = i[1] - init_position[1]
            elif side == "black":
                delta_y = init_position[1] - i[1]

            if i in enemy_positions:
                if not(delta_y == 1 and delta_x == 1) and not i in removed_squares:
                    removed_squares.append(i)
            else:
                if self.first_move:
                    if not(delta_y == 1 and delta_x == 0) and not(delta_y == 2 and delta_x == 0) and not i in removed_squares:
                        removed_squares.append(i)
                else:
                    if not(delta_y == 1 and delta_x == 0) and not i in removed_squares:
                        removed_squares.append(i)
            
                if i in all_positions and not i in removed_squares:
                    removed_squares.append(i)
                               
        for i in removed_squares:
            squares.remove(i)
        
        
        return squares     

class king(piece):
    def __init__(self,side,alive,position,first_move):
        super().__init__(side,alive,position,first_move)
    
    def determine_valid_squares(self,init_position,side,all_pieces,enemy_pieces,board):
        x = 0
        y = 0
        squares = board.copy()
        removed_squares = []

        all_positions = []
        for i in all_pieces:
            all_positions.append(i.position)

        for i in squares:
            delta_x = abs(i[0] - init_position[0])
            delta_y = abs(i[1] - init_position[1])

            #if not one space away
            if delta_x > 1 or delta_y > 1:
                if not i in removed_squares:
                    removed_squares.append(i)
            # if not(delta_x == 1 and delta_y == 0) and not(delta_x == 0 and delta_y == 1)or (delta_x == 1 and delta_y ==1):
            #     if not i in removed_squares:
            #         removed_squares.append(i) 
            else:
                if i in all_positions and not i in removed_squares:
                        removed_squares.append(i)
            
                    
        for i in removed_squares:
            squares.remove(i)
        return squares    


def get_array(stage,valid_squares):  
    valid_coord = False
    while valid_coord == False:
        valid_coord = True
        letters = input(f"enter {stage} position: ")
        coord = ext.convert_to_coordinates(letters)
        
        if coord not in valid_squares:
            print(f"Try again.\nEnter first value for {stage} position: ")
            valid_coord = False

    return coord

def pieces_between(start,end,player,enemy):
    delta_x = end[0] - start[0]
    delta_y = end[1] - start[1]

    if delta_x > 0:
        sign_x = 1
    elif delta_x < 0:
        sign_x = -1
    elif delta_x == 0: #doing this instead of else incase it messes up soomething
        sign_x = 0
    else:
        raise Exception("Error. start position or end position dont have numbers for x??")


    if delta_y > 0:
        sign_y = 1
    elif delta_y < 0:
        sign_y = -1
    elif delta_y == 0: #doing this instead of else incase it messes up soomething
        sign_y = 0
    else:
        raise Exception("Error. start position or end position dont have numbers for y??")

    coord = start
    coord[0] += sign_x
    coord[1] += sign_y

    all_positions = []
    for i in player.pieces:
        all_positions.append(i.position)
    for i in enemy.pieces:
        all_positions.append(i.position)

    while coord != end:
        if coord in all_positions:
            return True
        coord[0] += sign_x
        coord[1] += sign_y
    
    return False

def find_piece(active_player,position):
    for i in active_player.pieces:
        if position == i.position:
            return i    
    return "PieceNotFoundError"

def move(piece, position, enemy_player):
    for enemy_piece in enemy_player.pieces:
        if position == enemy_piece.position:
            enemy_piece.alive = False
            enemy_player.pieces.remove(enemy_piece)
            break
    
    piece.position = position
    if piece.first_move == True:
        piece.first_move = False
def play():  
    #define full board
    board = []
    for y in range(8):
        for x in range(8):
            board.append([y+1,x+1])

    white_bishop_1 = bishop("white",True,[3,1],True)
    white_bishop_2 = bishop("white",True,[6,1],True)
    white_knight_1 = knight("white",True,[2,1],True)
    white_knight_2 = knight("white",True,[7,1],True)
    white_rook_1 = rook("white",True,[1,1],True)
    white_rook_2 = rook("white",True,[8,1],True)
    white_queen = queen("white",True,[4,1],True)
    white_king = king("white",True,[5,1],True)
    white_pawn_1 = pawn("white",True,[1,2],True)
    white_pawn_2 = pawn("white",True,[2,2],True)
    white_pawn_3 = pawn("white",True,[3,2],True)
    white_pawn_4 = pawn("white",True,[4,2],True)
    white_pawn_5 = pawn("white",True,[5,2],True)
    white_pawn_6 = pawn("white",True,[6,2],True)
    white_pawn_7 = pawn("white",True,[7,2],True)
    white_pawn_8 = pawn("white",True,[8,2],True)

    white_pieces = [white_bishop_1,white_bishop_2,white_knight_1,white_knight_2,white_rook_1,white_rook_2,white_queen,white_king,white_pawn_1,white_pawn_2,white_pawn_3,white_pawn_4,white_pawn_5,white_pawn_6,white_pawn_7,white_pawn_8]

    black_bishop_1 = bishop("black",True,[3,8],True)
    black_bishop_2 = bishop("black",True,[6,8],True)
    black_knight_1 = knight("black",True,[2,8],True)
    black_knight_2 = knight("black",True,[7,8],True)
    black_rook_1 = rook("black",True,[1,8],True)
    black_rook_2 = rook("black",True,[8,8],True)
    black_queen = queen("black",True,[4,8],True)
    black_king = king("black",True,[5,8],True)
    black_pawn_1 = pawn("black",True,[1,7],True)
    black_pawn_2 = pawn("black",True,[2,7],True)
    black_pawn_3 = pawn("black",True,[3,7],True)
    black_pawn_4 = pawn("black",True,[4,3],True)
    black_pawn_5 = pawn("black",True,[5,7],True)
    black_pawn_6 = pawn("black",True,[6,7],True)
    black_pawn_7 = pawn("black",True,[7,7],True)
    black_pawn_8 = pawn("black",True,[8,7],True)
    black_pieces = [black_rook_1,black_rook_2,black_bishop_1,black_bishop_2,black_knight_1,black_knight_2,black_queen,black_king,black_pawn_1,black_pawn_2,black_pawn_3,black_pawn_4,black_pawn_5,black_pawn_6,black_pawn_7,black_pawn_8]

    player1 = player(True,"white",white_pieces,"player1")
    player2 = player(False, "black",black_pieces,"player2")

    #player1.name = input("Enter player1's name: ")
    player1.name = "Player1"
    #player2.name = input("Enter player2's name: ")
    player2.name = "Player2"

    active_player = player1
    enemy_player = player2
    #while game not over

    all_pieces = []
    for i in white_pieces:
        all_pieces.append(i)
    for i in black_pieces:
        all_pieces.append(i)

    while True:
        print(f"{active_player.name} is going now.")

        active_positions = []
        for i in active_player.pieces:
            active_positions.append(i.position)

        piece_valid = False
        while piece_valid == False: #see extras.txt "attribution"
            start_position = get_array("start",active_positions) #get_array("start",all_pieces for colour)
            chosen_piece = find_piece(active_player,start_position)

            piece_valid = True
            if chosen_piece == "PieceNotFoundError":
                piece_valid = False
                print("Try Again. NO piece here.")

            valid_squares = chosen_piece.determine_valid_squares(chosen_piece.position,active_player.side, active_player.pieces,enemy_player.pieces,board)
            
            if chosen_piece.__class__.__name__ != "knight":
                removed_squares = []
                for i in valid_squares:
                    if pieces_between(start_position.copy(),i,active_player,enemy_player):
                        removed_squares.append(i)
                
                for i in removed_squares:
                    valid_squares.remove(i)
                valid_coords = []

            
            for i in valid_squares:
                for active_piece in active_player.pieces:
                    if i == active_piece.position:
                        removed_squares.append(i)

            for i in valid_squares:
                valid_coords.append(ext.convert_to_letters(i))

            if len(valid_squares) > 0:
                print(f"the squares your {chosen_piece.__class__.__name__} can move to are {valid_coords}.")
            
            else:
                print(f"The {chosen_piece.__class__.__name__} you chose cannot move to any squares ")
                piece_valid = False
        square_valid = False

        while square_valid == False:
            end_position = get_array("end",valid_squares)
            square_valid = True
            if end_position not in valid_squares:
                square_valid = False
                print("sorry, no squares found here.")
            if pieces_between(start_position,end_position,active_player,enemy_player):
                square_valid = False
                print("Sorry, piece in between.")
        
        move(chosen_piece, end_position, enemy_player)
        print(f"The {chosen_piece.__class__.__name__} which was on {ext.convert_to_letters(start_position)} is now on {ext.convert_to_letters(chosen_piece.position)}. It should be on {ext.convert_to_letters(end_position)}.")

        if active_player == player1 and enemy_player == player2:
            active_player = player2
            enemy_player = player1
        elif active_player == player2 and enemy_player == player1:
            active_player = player1
            enemy_player = player2
        else: 
            raise Exception("Neither player is playing rn????")


    return "placeholder won","by winning."

def start():
    winner,reason = play()
    print(f"Game over. {winner}{reason}")
start()