import booking


def test_success_delete_booking():
    # Arrange
    created_booking_id = booking.create_booking().json()["bookingid"]

    # Act
    deleted_booking_result = booking.delete_booking(created_booking_id)

    # Assert
    assert deleted_booking_result.status_code == 201
