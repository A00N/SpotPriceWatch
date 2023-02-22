import requests
from datetime import datetime


def parse_datetime(datetime):
    date, time = datetime.split("T")
    hour = time.split(":")[0]
    return hour


class ElectricSpotPrices:

    def __init__(self):
        self.data = {}
        self.__fetch_data()

    def __fetch_data(self):
        url = "https://api.spot-hinta.fi/Today"
        response = requests.get(url)
        self.data = response.json()

    def date(self):
        date = datetime.now()
        hour = date.hour
        date = date.strftime("%Y-%m-%d")
        return date, hour

    def current_price(self):
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:00:00+02:00")
        for date in self.data:
            if date['DateTime'] == current_time:
                time = parse_datetime(date["DateTime"])
                return time, round(date['PriceWithTax']*100,3)
        # If no data with the current time was found, return None
        return None

    def current_day_prices(self):
        prices = []
        for data in self.data:
            time = parse_datetime(data["DateTime"])
            prices.append(tuple((time, round(data["PriceWithTax"]*100,3))))
        return prices

    def min_price(self):
        rank = 1
        for data in self.data:
            if data['Rank'] == rank:
                time = parse_datetime(data["DateTime"])
                return time, round(data['PriceWithTax']*100, 3)

    def max_price(self):
        rank = 24
        for data in self.data:
            if data['Rank'] == rank:
                time = parse_datetime(data["DateTime"])
                return time, round(data['PriceWithTax']*100, 3)




