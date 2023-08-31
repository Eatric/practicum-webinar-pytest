import pytest

import booking
import helper


def test_success_creating_booking():
    # Arrange
    # Act
    booking_create_result = booking.create_booking()

    # Assert
    assert booking_create_result.status_code == 200


def test_success_creating_booking_with_custom_firstname():
    # Arrange
    booking_body = helper.modify_create_booking_body("Andrey")

    # Act
    booking_create_result = booking.create_booking_with_body(booking_body)

    # Assert
    assert booking_create_result.status_code == 201,\
        f"Expected 201, but Actual is {booking_create_result.status_code}"
    assert booking_create_result.json()["booking"]["firstname"] == "Andrey"

@pytest.mark.parametrize("totalprice", [
    pytest.param(
        999999, id="Check TotalPrice High Border"
    ),
    pytest.param(
        1, id="Check TotalPrice Low Border"
    ),
    pytest.param(
        0, id="Check TotalPrice Zero"
    ),
])
def test_success_creating_booking_with_different_totalprice(totalprice):
    # Arrange
    booking_body = helper.modify_booking_body("totalprice", totalprice)

    # Act
    booking_create_result = booking.create_booking_with_body(booking_body)

    # Assert
    assert booking_create_result.status_code == 200
    assert booking_create_result.json()["booking"]["totalprice"] == totalprice

