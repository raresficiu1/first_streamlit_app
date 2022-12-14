import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError

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


streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)


my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)


my_cur.execute("insert into fruit_load_list values ('from streamlit')")



fruit_choice = streamlit.text_input('What fruid would you like to add?','Kiwi')
streamlit.write('Thanks for adding', fruit_choice)
my_data_row.append([(fruit_choice)])
streamlit.dataframe(my_data_row)

