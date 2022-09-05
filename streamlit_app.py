import streamlit
import requests
import pandas
variabile='kiwi'

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{variabile}")
streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
