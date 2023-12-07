import chess.engine

path = r'C:\Users\pulchihd\Desktop\PythonChess\stockfish-windows-x86-64-modern\stockfish\stockfish-windows-x86-64-modern'
engine = chess.engine.SimpleEngine.popen_uci(path)
board = chess.Board()

game = True
while game:
    print(board)
    try:
        print("White to play, please enter a move using the UCI protocol.")
        user_input = input("Move: ")
        move = chess.Move.from_uci(user_input)
        if move in board.legal_moves:
            if len(board.legal_moves) < 1:
                print("Game over")
                break
            board.push(move) 
        else:
            print("Illegal move, try again")
            continue
    except Exception as e:
        print("An error occurred:", e)
        continue

    try:
        limit = chess.engine.Limit(time=1.0)
        best_move = engine.play(board, limit=limit)
        board.push(chess.Move.from_uci(str(best_move.move)))
    except Exception as e:
        print("An error occurred:", e)
        print("ChessBot has resigned")
        break


# Let Stockfish analyze the position
  # 0.1 seconds for analysis


# Close the engine
engine.quit()