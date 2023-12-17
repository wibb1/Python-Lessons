import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.city = df.loc[df["id"] == self.hotel_id, "city"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel has a vacancy"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        return availability == 'yes'


class Reservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        return f"""
Thank you for your reservation!
Here is your booking information:
    Name: {self.customer_name}
    Hotel: {self.hotel.name}
    City: {self.hotel.city}
"""


if __name__ == '__main__':
    print(df)
    hotel_ID = input("Enter the id of the hotel: ")
    hotel = Hotel(hotel_ID)

    if hotel.available():
        hotel.book()
        name = input("Enter your name: ")
        reservation = Reservation(name, hotel)
        print(reservation.generate())
    else:
        print("No Vacancy")
