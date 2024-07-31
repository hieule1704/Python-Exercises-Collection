def make_car(manufacturer, model_name, **kwargs):
    car = {"manufacturer": manufacturer, "model_name": model_name}
    for key, value in kwargs.items():
        car[key] = value
    print(car)
    return car

make_car('Volvo', 'Grande Pluto', color="Red", option="Automatic")