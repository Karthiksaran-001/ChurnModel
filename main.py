import streamlit as st
import pickle 
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import math


def prediction(value):
    model = pickle.load(open('FinalChurnModel.sav','rb'))
    output = model.predict(value)[0]
    score = model.predict_proba(value)
    conf_score = score[0][np.argmax(score)]
    conf_score = conf_score * 100 
    
    return [output , int(conf_score)]

def recommend(value):
    df = pickle.load(open("recommend_list.pkl" , "rb"))
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




with st.form('my_form'):
    age = st.text_input("Enter Your age")
   

    monthly_income = st.text_input("Enter Your Monthly Income")
    
    gender = st.radio('Pick your gender',['Male','Female'])
    if(gender == "Male"):
        gender = 0
    else:
        gender = 1

    tda = st.text_input("Total Debit Amount")
    tdt = st.text_input("Total Debit Transaction")
    tca = st.text_input("Total credit Amount")
    tct = st.text_input("Total credit Transaction")
    targ_desc = st.radio('Pick your gender',['LOW','MIDDLE' ,'EXECUTIVE' , 'PLATINUM'])
    if(targ_desc == "PLATINUM"):
        targ_desc= 3
    elif(targ_desc == "EXECUTIVE"):
        targ_desc = 2
    elif(targ_desc == "MIDDLE"):
        targ_desc = 1
    else:
        targ_desc = 0 

    submitted = st.form_submit_button("Predict")

value = [[int(age) , float(monthly_income) , int(gender) , float(tda) , int(tdt) , float(tca) , int(tct) , int(targ_desc)]]



if(submitted):
    predict = prediction(value)
    if(gender == 0):
        output = f"Based On Your Customer Activity HE is  : {predict[0]} State with {predict[1]}% Chance"
    else:
        output = f"Based On Your Customer Activity SHE is  : {predict[0]} State with {predict[1]}% Chance"

    st.write(output)

    if(predict[0] == "CHURN"):
        Recommendation = recommend(value)
        st.write("Recommend Offer For You : \n" + Recommendation )
# print(prediction(value))
# print(recommend(value))





