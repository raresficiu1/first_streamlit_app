import streamlit
import requests
import pandas
variabile='kiwi'

streamlit.header("Fruityvice Fruit Advice!")



fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")
streamlit.text(fruityvice_response.json())


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
