import os

CREATE_BOOKING_BODY = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

AUTH_USER_BODY = {
    "username": "admin",
    "password": os.getenv("PASSWORD")
}
