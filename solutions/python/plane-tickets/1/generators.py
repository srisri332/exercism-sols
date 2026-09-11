"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B
    """

    letters = ["A", "B", "C", "D"]
    i = 0
    while i < number:
        yield letters[i%4]
        i+=1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    letters = generate_seat_letters(number)
    
    seat_number = 1

    for letter in  letters:
        yield f"{seat_number}{letter}"
        seat_number = seat_number + 1 if letter == "D" else seat_number
        if seat_number == 13:
            seat_number += 1

    

def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    seats = generate_seats(len(passengers))
    passengers = iter(passengers)
    mapping = {}

    for seat in seats:
        passenger = next(passengers, None)
        if passenger:
            mapping[passenger] = seat
    return mapping        


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        yield f"{seat}{flight_id}".ljust(12, "0")
