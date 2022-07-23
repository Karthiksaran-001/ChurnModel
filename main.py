"""
Created on Tue Jul  24 17:06:01 2019

@author: Karthik Saran
"""



import re
import streamlit as st
import pickle 
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity



def prediction(value):
    model = pickle.load(open('RetrainChurnModel.sav','rb'))
    output = model.predict(value)[0]
    score = model.predict_proba(value)
    conf_score = score[0][np.argmax(score)]
    conf_score = conf_score * 100 
    
    return [output , int(conf_score)]

def recommend(value):
    df = pickle.load(open("recommend_list.pkl" , "rb"))
    del df["Status"]
    X = df.iloc[: , :-1]
    cos_val = dict()
    for i in range(X.shape[0]): 
        val = cosine_similarity(value , [X.iloc[i].values])
        cos_val[str(i)] = val[0][0]
    max_val = max(cos_val.values())
    # print(max_val)
    for i , j in cos_val.items():
       
        if(j == max_val):
          recommendation  = df.iloc[int(i)]["Recommendation"]
    
    return recommendation





st.title("Churn Recommendation WebApp")
st.markdown("Predict the Customer is Churn or Active")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color: aqua;
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


with st.form('my_form'):
    age = st.text_input("Enter Your age")
   

    monthly_income = st.number_input("Enter Your Monthly Income")
    
    gender = st.radio('Pick your gender',['Male','Female'])
    if(gender == "Male"):
        gender = 0
    else:
        gender = 1

    relationship = st.radio('Pick your Relationship',['Maried','Single' , 'DIVORCE' , 'WIDOWED' , 'PARTNER' , 'OTHER'])

    if(relationship == "Maried"):
        relationship = 0
    elif(relationship =="Single"):
        relationship =1
    elif(relationship =="DIVORCE"):
        relationship = 2
    elif(relationship =="WIDOWED"):
        relationship = 3
    elif(relationship =="PARTNER"):
        relationship = 4
    else:
        relationship = 5

    ywu = st.number_input("How Long you are  Standard Bank Customer")
    tdt = st.number_input("How many Debited Transaction for Last Month")
    tct = st.number_input("How many Credited Transaction for Last Month")



    submitted = st.form_submit_button("Predict")

value = [[age , monthly_income , gender , relationship,ywu , tdt , tct ]]



if(submitted):
    predict = prediction(value)
    if(gender == 0):
        output = f"Based On Your Customer Activity HE is  : {predict[0]} State with {predict[1]}% Chance"
    else:
        output = f"Based On Your Customer Activity SHE is  : {predict[0]} State with {predict[1]}% Chance"

    st.write(output)

    # if(predict[0] == "CHURN"):
    Recommendation = recommend(value)
    st.write("Recommend Offer For You : \n" + Recommendation )
# print(prediction(value))
# print(recommend(value))





