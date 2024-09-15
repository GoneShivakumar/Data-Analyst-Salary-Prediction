import streamlit as st

import Prediction as pdt

def main():

    st.header("Salary Prediction for Data Analyst")
    with st.form(key='my_form'):
        age = st.number_input('Select Age',min_value=0,max_value=100,key='age')
        YOE = st.number_input('Select Years of Experience',min_value=0,max_value=60,key='yoe')
        GF = st.radio('Gender',['Female','Male'],horizontal=True,key='gf')
        st.write(GF)
        # GM = st.radio('Gender',['Female','Male'],horizontal=True,key='gm')
        Edu = st.radio('Education Level',['Bachelors','Masters'],horizontal=True,key='b')
        # EduM = st.radio('Education Level',['Bachelors','Masters'],horizontal=True,key='m')
        button= st.form_submit_button(label="Submit")

    if button:
        if GF == 'Female':
            valgf = 1
            valgm = 0
        else:
            valgf = 0
            valgm = 1

        if Edu == 'Bachelors':
            valed = 1
            vale = 0
        else:
            valed = 0
            vale = 1

        prdval = pdt.predict(age,YOE,valgf,valgm,valed,vale)
        prdctval = prdval[0].round()
        st.subheader(f"Your Salary could be $ {prdctval}")

if __name__ =='__main__':
    main()
