import chess
import gc

class State():
    def __init__(self):
        self.board = chess.Board()
    
    def serialize(self):
        # 257 bits according to readme
        pass

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        # TODO: add neural network here
        return 1

if __name__=='__main__':
    s = State()
    print(s.edges())
    del(s)
    del(State)
    gc.collect()
    exit()