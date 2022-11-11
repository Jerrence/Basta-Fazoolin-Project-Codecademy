# Making the Menus (lines 2 to 72)
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    if self.start_time < 1200:
      return self.name + " menu available from " + str(int(self.start_time / 100)) + 'am' + ' to ' + str(int(self.end_time / 100 - 12)) + 'pm'

    elif self.start_time >= 1200:
      return self.name + " menu available from " + str(int(self.start_time / 100 - 12)) + 'pm' + ' to ' + str(int(self.end_time / 100 - 12)) + 'pm'

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item, price in self.items.items():
      for purchased_item in purchased_items:
        if item in purchased_item:
          total_price += price

    return total_price

brunch_object = {
  'pancakes': 7.50,
  'waffles': 9.00,
  'burger': 11.00,
  'home fries': 4.50,
  'coffee': 1.50,
  'espresso': 3.00,
  'tea': 1.00,
  'mimosa': 10.50,
  'orange juice': 3.50
}

brunch = Menu("Brunch", brunch_object, 1100, 1600)

early_bird_object = {
  'salumeria plate': 8.00,
  'salad and breadsticks (serves 2, no refills)': 14.00,
  'pizza with quattro formaggi': 9.00,
  'duck ragu': 17.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 1.50,
  'espresso': 3.00,
}

early_bird = Menu("Early Bird", early_bird_object, 1500, 1800)

dinner_object = {
  'crostini with eggplant caponata': 13.00,
  'caesar salad': 16.00,
  'pizza with quattro formaggi': 11.00,
  'duck ragu': 19.50,
  'mushroom ravioli (vegan)': 13.50,
  'coffee': 2.00,
  'espresso': 3.00,
}

dinner = Menu("Dinner", dinner_object, 1700, 2300)

kids_object = {
  'chicken nuggets': 6.50,
  'fusilli with wild mushrooms': 12.00,
  'apple juice': 3.00
}

kids = Menu("Kids", kids_object, 1100, 2100)

print(brunch)
print(early_bird)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Creating the Franchises (lines 75 to 99)
class Franchises:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available_menus_list = []

    for menus in self.menus:
      if time >= menus.start_time and time <= menus.end_time:
        available_menus_list.append(menus)

    return available_menus_list

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchises("1232 West End Road", menus)
new_installment = Franchises("12 East Mulberry Street", menus)

print(flagship_store)

print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

# Creating Businesses! (lines 106 to 122)
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = {
  'arepa pabellon': 7.00,
  'pernil arepa': 8.50,
  'guayanes arepa': 8.00,
  'jamon arepa': 7.50
}

arepas_place = Franchises("189 Fitzgerald Avenue", menus)

take_a_arepa = Business("Take a' Arepa", arepas_place)

