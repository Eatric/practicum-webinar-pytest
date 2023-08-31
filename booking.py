import requests

import configuration
import data


def create_booking_with_body(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_BOOKING_API_PATH, json=body)


def create_booking():
    return create_booking_with_body(data.CREATE_BOOKING_BODY)


def get_token():
    return requests.post(configuration.BASE_URL + configuration.AUTH_API_PATH, json=data.AUTH_USER_BODY).json()["token"]


def delete_booking(id):
    return requests.delete(configuration.BASE_URL + configuration.DELETE_BOOKING_API_PATH + str(id), headers={
        "Cookie": "token=" + str(get_token())
    })
