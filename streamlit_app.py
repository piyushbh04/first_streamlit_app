import streamlit
import pandas 

streamlit.title('MY PARENTS NEW HEALTHY DINER')

streamlit.header('BREAKFAST MENU')

streamlit.text('1. Oats')
streamlit.text('2. Bananas')
streamlit.text('3. Peanut Butter')

streamlit.header('Build your own favorite Smoothie')
my_fruit_list=pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)




