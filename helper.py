import data


def modify_create_booking_body(name):
    return modify_booking_body("firstname", name)


def modify_booking_body(key, value):
    body = data.CREATE_BOOKING_BODY.copy()
    body[key] = value

    return body
