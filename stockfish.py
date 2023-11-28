import chess.engine

path = r'C:\Users\pulchihd\Desktop\PythonChess\stockfish-windows-x86-64-modern\stockfish\stockfish-windows-x86-64-modern'

engine = chess.engine.SimpleEngine.popen_uci(path)

board = chess.Board()

board.push(chess.Move.from_uci('e2e4'))

print(board)

# Let Stockfish analyze the position
limit = chess.engine.Limit(time=0.1)  # 0.1 seconds for analysis
best_move = engine.play(board, limit=limit)

print("Best move:", best_move.move)

board.push(chess.Move.from_uci('c7c5'))

print(board)

# Close the engine
engine.quit()