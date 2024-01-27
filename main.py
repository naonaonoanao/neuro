from fastapi import FastAPI
import uvicorn

import predict

app = FastAPI()


@app.post("/clear-board")
async def clear_board_chess():
    predict.clear_board()
    return {"message": "Board cleaned!"}


@app.get("/get-legal-moves")
async def legal_moves():
    return {"legal_moves": predict.get_legal_moves()}


@app.post("/make-user-move")
async def user_move_chess(move: str):
    predict.make_user_move(move)
    return {"message": "Move made!"}


@app.post("/make-neuro-move")
async def neuro_move_chess():
    return {"neuro_move": predict.make_neuro_move()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
