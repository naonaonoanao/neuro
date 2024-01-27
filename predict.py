import chess
import keras.src.saving
import numpy as np


board = chess.Board()
model = keras.models.load_model('model')

PIECE_SYMBOLS_NEW = ['.', 'P', 'R', 'N', 'B', 'Q', 'K', 'p', 'n', 'b', 'r', 'q', 'k']


def piece(cell): return str(board.piece_at(cell)) if str(board.piece_at(cell)) != 'None' else '.'


def clear_board():
    global board
    board = chess.Board()


def make_user_move(this_move):
    print([str(move) for move in board.legal_moves])
    board.push_san(this_move)
    print(board)


def get_legal_moves():
    print(board)
    leg_moves = [str(move) for move in board.legal_moves]
    return leg_moves


def make_neuro_move():
    legals = []
    recom = []

    # первый слой доступных ходов
    for key in board.legal_moves:
      legals.append(str(key))

    # перебираем доступные ходы
    for index, legal_move in enumerate(legals):

      board.push_san(legal_move)
      combination_code = [PIECE_SYMBOLS_NEW.index(piece(cell)) for cell in range(64)]
      x_analised = np.array([ int(key) for key in combination_code ])
      x = np.expand_dims(x_analised, axis=0)

      res = model.predict(x, verbose=0)
      recom.append([legal_move, res[0][0]])

      board.pop()

    print()

    # печатаем ход и оценку
    ind = np.argmax([ key[1] for key in recom ])
    print(recom[ind])
    print()

    for key in reversed(np.argsort([ key[1] for key in recom  ] )):
      print(recom[key])

    # делаем ход
    board.push_san(recom[ind][0])
    print(board)
    return recom[ind][0]
