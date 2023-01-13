import streamlit
import pandas 
import requests
from urllib.error import URLError



import snowflake.connector



streamlit.title('MY PARENTS NEW HEALTHY DINER')

streamlit.header('BREAKFAST MENU')

streamlit.text('1. Oats')
streamlit.text('2. Bananas')
streamlit.text('3. Peanut Butter')

streamlit.header('Build your own favorite Smoothie')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index("Fruit")
fruits_selected=streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index))
fruits_toshow=my_fruit_list.loc[fruits_selected]



streamlit.dataframe(fruits_toshow)

def get_fruityvice_data(this_fruit_choice):
 fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
 fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 return fruityvice_normalized


  


streamlit.header('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
        back_from_function=get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
  
  



streamlit.text("The fruit load list contains:")
def get_fruit_load_list():
 my_cur = my_cnx.cursor()
 my_cur.execute("select * from fruit_load_list")
 return my_cur.fetchall()
 
if streamlit.button('Get Fruit Load List'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 my_data_rows=get_fruit_load_list()
 streamlit.dataframe(my_data_rows)
 
 
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
   my_cur.execute("insert into fruit_load_list values('test')")
   return "Thanks for adding " + new_fruit
  
   
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
 my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
 back_from_function=insert_row_snowflake(add_my_fruit)
 streamlit.text(back_from_function)






