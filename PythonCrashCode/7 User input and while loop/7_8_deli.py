sandwich_orders = ['Tuna Sandwich', 'Chicken Sandwich', 'Beaf Sandwich', 'Fish Sandwich']
finished_sandwich_orders = []
for sandwich_order in sandwich_orders:
    print(f"I made your {sandwich_order.lower()}")
    finished_sandwich_orders.append(sandwich_order)
    sandwich_orders.remove(sandwich_order)
for sandwich_order in finished_sandwich_orders:
    print(sandwich_order)