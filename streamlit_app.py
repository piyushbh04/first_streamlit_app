import streamlit
import pandas 
import requests


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

streamlit.header('Fruityvice Fruit Advice!')



fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)


