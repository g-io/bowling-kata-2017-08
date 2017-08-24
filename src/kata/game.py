class Game:
    def __init__(self):
        self.score_board = []
        pass

    def roll(self, pins):
        self.score_board.append(pins)
        return False

    def score(self):
        total = 0
        throws_this_frame = []
        frame_no = 1
        score_for_this_frame=0
        for i in range(0, len(self.score_board)):
            pins_this_throw = self.score_board[i]

            throws_this_frame.append(pins_this_throw)
            if pins_this_throw == 10 and len(throws_this_frame) == 1:
                frame_no+=1
                throws_this_frame = []
                score_for_this_frame=10+self.score_board[i+1]+self.score_board[i+2]
            elif score_for_this_frame+pins_this_throw==10:
                frame_no+=1
                throws_this_frame = []
                score_for_this_frame=10+self.score_board[i+1]
            else:
                

            total += pins_this_throw
        return total