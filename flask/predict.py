import streamlit as st
import pickle
import mongo

lin_model = pickle.load(open('model1.pkl','rb'))
log_model = pickle.load(open('model2.pkl','rb'))
svc_model = pickle.load(open('model3.pkl','rb'))

def classify(num):
    if num < 0.5:
        return 'Dengue'
    
    elif num < 1.5:
        return 'Typhoid'
    
    else :
        return 'Anemia'
    
# df = mongo.getDisease()
# X = df[['lymphocytes', 'platelets','RBCs', 'haemoglobin']].values
# output = classify(log_model.predict(X))
# print(log_model.predict(X))
# print(output)



   


# def main():
#     st.title("Disease Prediction")

#     html_temp = """
#     <div style="background-color:cyan ;padding:10px">
#     <h2 style="color:blue;text-align:center;">Disease Classification</h2>
#     </div>
#     """

#     st.markdown(html_temp, unsafe_allow_html=True)

#     activities = ['Linear Regression','Logistic Regression','SVM']

#     options = st.sidebar.selectbox('Which model would you choose ? ',activities)

#     st.subheader(options)


#     sl = st.slider('Lymphocytes',20.0,50.0)
#     sw=st.slider('Platelete', 0.0, 450.0)
#     pl=st.slider('RBC',3.0 , 6.0)
#     pw=st.slider('Hemoglobin', 0.0, 18.0)
 
#     inputs =[[sl,sw,pl,pw]]

#     if st.button('Classify'):

#         if options=='Linear Regression':
#             st.success(classify(lin_model.predict(inputs)))
#         elif options=='Logistic Regression':
#             st.success(classify(log_model.predict(inputs)))
#         else:
#            st.success(classify(svc_model.predict(inputs)))


# if __name__=='__main__':
#     main()





