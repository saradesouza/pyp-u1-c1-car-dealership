class Vehicle(object):
  def __init__(self, maker, model, year, base_price, miles):
    self.maker = maker
    self.model = model
    self.year = year
    self.base_price = base_price
    self.miles = miles

  def sale_price(self, base_price):
    sale_price = base_price * SALE_PRICE_MULTIPLIER 
    return self.sale_price

  def purchase_price(self, base_price):
    purchase_price = base_price * PURCHASE_PRICE_MULTIPLIER 
    return self.purchase_price

class Car(Vehicle):
  SALE_PRICE_MULTIPLIER = 1.2
  PURCHASE_PRICE_MULTIPLIER = 0.004

class Motorcycle(Vehicle):
  SALE_PRICE_MULTIPLIER = 1.1
  PURCHASE_PRICE_MULTIPLIER = 0.009

class Truck(Vehicle):
  SALE_PRICE_MULTIPLIER = 1.6
  PURCHASE_PRICE_MULTIPLIER = 0.02