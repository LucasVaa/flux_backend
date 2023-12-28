from typing import Union

from fastapi import FastAPI

import final_input

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/run/")
def run_model(P1_1_input: int = 0,
              P1_2_input: int = 0,
              P1_3_input: int = 0,
              W_input: float = 0,
              PRO_input: float = 0,
              M_input: float = 0,
              Re_input: float = 0,
              I_input: float = 0):
    return final_input.run_model(P1_1_input, P1_2_input, P1_3_input, W_input, PRO_input, M_input,
                                 Re_input, I_input)
