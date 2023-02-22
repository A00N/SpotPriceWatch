from flask import render_template, request, redirect, abort
from app import app
from services import spot_price_data

spot = spot_price_data.ElectricSpotPrices()


@app.route("/index", methods=["GET"])
def data():
    date, hour = spot.date()
    current_time, current_price = spot.current_price()
    current_time_plus = int(current_time) + 1
    min_time, min_price = spot.min_price()
    min_time_plus = int(min_time) + 1
    max_time, max_price = spot.max_price()
    max_time_plus = int(max_time) + 1
    day_prices = spot.current_day_prices()
    return render_template("index.html",
                           date=date,
                           hour=hour,
                           current_time=current_time,
                           current_time_plus=current_time_plus,
                           current_price=current_price,
                           min_time=min_time,
                           min_time_plus=min_time_plus,
                           min_price=min_price,
                           max_time=max_time,
                           max_time_plus=max_time_plus,
                           max_price=max_price,
                           day_prices=day_prices)
