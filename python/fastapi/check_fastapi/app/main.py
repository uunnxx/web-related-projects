from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date

from pydantic import BaseModel


app = FastAPI()


class HotelSchema(BaseModel):
    address: str
    name: str
    stars: int


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        # date_from: date,
        # date_to: date,
        date_from: int,
        date_to: int,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5)
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


# @app.get('/hotels', response_model=list[HotelSchema])
# @app.get('/hotels')
# def get_hotels(
#     location: str,
#     date_from: date,
#     date_to: date,
#     has_spa: Optional[bool] = None,
#     stars: Optional[int] = Query(None, ge=1, le=5)
# ) -> list[HotelSchema]:
#     hotels = [
#         {
#             'address': 'Hotel address',
#             'name': 'Hotel Name',
#             'stars': 5
#         }
#     ]
#     return hotels

@app.get('/hotels')
def get_hotels(search_args: HotelsSearchArgs = Depends()):
    return search_args


class BookingSchema(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post('/bookings')
def add_booking(booking: BookingSchema):
    pass
