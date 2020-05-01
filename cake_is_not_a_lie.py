
def solution(s):
    max_possible_equal_size_piece = 1
    length_of_cake = len(s)  

    for size_of_cake_piece in range(1, length_of_cake):
        cake_pieces = []
        if(length_of_cake % size_of_cake_piece == 0):
            for cake_piece in range(0, length_of_cake, size_of_cake_piece):
                cake_pieces.append(s[cake_piece:cake_piece+size_of_cake_piece])
            number_of_cake_pieces_divided = len(cake_pieces)

            max_possible_equal_size_piece = check(number_of_cake_pieces_divided, cake_pieces)
            if(max_possible_equal_size_piece != 1):
                return max_possible_equal_size_piece
    return max_possible_equal_size_piece

def check(number_of_cake_pieces_divided, cake_pieces):
    if cake_pieces.count(cake_pieces[0]) == number_of_cake_pieces_divided :
        return number_of_cake_pieces_divided
    else:
        return 1
