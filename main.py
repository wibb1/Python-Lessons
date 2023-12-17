import pandas

df_hotels = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df_hotels.loc[df_hotels["id"] == self.hotel_id, "name"].squeeze()
        self.city = df_hotels.loc[df_hotels["id"] == self.hotel_id, "city"].squeeze()
        self.spa = df_hotels.loc[df_hotels["id"] == self.hotel_id, "spa"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"] = "no"
        df_hotels.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel has a vacancy"""
        availability = df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"].squeeze()
        return availability == 'yes'


class HotelReservation:
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


class SpaReservation:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        return f"""
Thank you for your spa reservation!
Here is your spa booking information:
    Name: {self.customer_name}
    Hotel: {self.hotel.name}
"""


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration, "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        return False


class SecureCreditCard(CreditCard):
    def authenticate(self, user_entry):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        return password == user_entry


if __name__ == '__main__':
    print(df_hotels)
    hotel_ID = input("Enter the id of the hotel: ")
    hotel = Hotel(hotel_ID)

    if hotel.available():
        # assume credit card data
        card_type = input("What type of card: \n regular card(1) or secure card(2)")

        credit_card = CreditCard(number="1234") if card_type == 1 else SecureCreditCard(number="1234")
        if (
                (isinstance(credit_card, CreditCard) and
                 credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"))
                or
                (isinstance(credit_card, SecureCreditCard) and
                 credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123") and
                 credit_card.authenticate("mypass"))
        ):
            hotel.book()
            name = input("Enter your name: ")
            reservation = HotelReservation(name, hotel)
            print(reservation.generate())
            if hotel.spa == 'yes':
                spa_question = input("Do your want to book a spa package?")
                if spa_question.lower() == 'yes':
                    spa_reservation = SpaReservation(name, hotel)
                    print(spa_reservation.generate())
            print("Thank you have a nice day")
        else:
            print("There was a problem with your card")
    else:
        print("No Vacancy")
