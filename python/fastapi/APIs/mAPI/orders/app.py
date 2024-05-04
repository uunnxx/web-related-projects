from fastapi import FastAPI

from orders import api


app = FastAPI(debug=True)
