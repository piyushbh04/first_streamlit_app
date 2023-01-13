import streamlit
import pandas 

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



import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
