import pandas as pd

data = pd.read_csv("datasets/petrol_transport_data.csv")

avg_petrol_price = data['avg_petrol_price_naira_per_litre']
avg_bus_fare = data['avg_bus_fare_naira_per_drop']