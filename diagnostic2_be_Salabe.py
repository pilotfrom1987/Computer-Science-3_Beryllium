def calculate_total(topping_count):
     base_price = 10
     topping_price = 1.5
     total_price = base_price + (topping_count * topping_price)
     while response != "done":
          if response == "pepperoni":
               topping_count += 1
          elif response == "mushroom":
               topping_count += 1
          elif response == "extra cheese":
               topping_count += 1
          else:
               print("Invalid topping")

          response = input("type in toppings you want to add to your pizza (pepperoni, mushroom, extra cheese) or type 'done' when finished: ")
          