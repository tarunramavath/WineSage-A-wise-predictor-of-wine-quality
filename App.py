import streamlit as st
import pickle

model=pickle.load(open("wine_model.pkl","rb"))

def predict(citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide):
    y_pred=model.predict([[citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide]])
    return y_pred

def main():
    citric_acid=st.text_input("citric_acid : ")
    residual_sugar=st.text_input("residual_sugar : ")
    chlorides=st.text_input("chlorides : ")
    free_sulfur_dioxide=st.text_input("free_sulfur_dioxide : ")
    total_sulfur_dioxide=st.text_input("total_sulfur_dioxide : ")
    
    if st.button("Submit"):
        y_prediction=predict(eval(citric_acid),eval(residual_sugar),eval(chlorides),eval(free_sulfur_dioxide),eval(total_sulfur_dioxide))
        st.success(f"Your output is {y_prediction}")

def ex():
    data=st.file_uploader("upload file",)


if __name__=="__main__":
    main()