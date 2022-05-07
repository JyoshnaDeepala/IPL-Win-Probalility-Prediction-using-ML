import streamlit as st
import pickle
import pandas as pd
teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']
cities= ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe= pickle.load(open('pipe.pkl','rb'))

st.title('IPL Win Probability Predictor')



col1,col2 =st.columns(2)

with col1:
    batting_team=st.selectbox('Select the batting team',sorted(teams))
    if batting_team=='Sunrisers Hyderabad':
        st.image("srhf1.jpg",width=350)
    elif batting_team=='Mumbai Indians':
        st.image("mif.jpg",width=350)
    elif batting_team=='Royal Challengers Bangalore':
        st.image("rcbf1.jpg",width=350)
    elif batting_team=='Kolkata Knight Riders':
        st.image("kkrf2.jpg",width=350)
    elif batting_team =='Kings XI Punjab':
        st.image("kxpf.jpg", width=350)
    elif batting_team=='Chennai Super Kings':
        st.image("cskf.jpg",width=350)
    elif batting_team =='Rajasthan Royals':
        st.image("rrf1.jpg", width=350)
    elif batting_team =='Delhi Capitals':
        st.image("dcf.jpg", width=350)


with col2:
    bowling_team= st.selectbox('Select the bowling team',sorted(teams))
    if  bowling_team=='Sunrisers Hyderabad':
        st.image("srhf1.jpg",width=350)
    elif bowling_team=='Mumbai Indians':
        st.image("mif.jpg",width=350)
    elif bowling_team=='Royal Challengers Bangalore':
        st.image("rcbf1.jpg",width=350)
    elif bowling_team=='Kolkata Knight Riders':
        st.image("kkrf2.jpg",width=350)
    elif bowling_team =='Kings XI Punjab':
        st.image("kxpf.jpg", width=350)
    elif bowling_team=='Chennai Super Kings':
        st.image("cskf.jpg",width=350)
    elif bowling_team =='Rajasthan Royals':
        st.image("rrf1.jpg", width=350)
    elif bowling_team =='Delhi Capitals':
        st.image("dcf.jpg", width=350)


col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17=st.columns(12)
with col6:
    st.write(" ")
with col7:
    st.write(" ")
with col8:
    st.write(" ")
with col9:
    st.write(" ")
with col10:
    st.write(" ")
with col11:
    st.title("VS")
with col12:
    st.write(" ")
with col13:
    st.write(" ")
with col14:
    st.write(" ")
with col15:
    st.write(" ")
with col16:
    st.write(" ")
with col17:
    st.write(" ")


selected_city = st.selectbox('Select host city',sorted(cities))


target =st.number_input('Target')


col3,col4,col5= st.columns(3)
with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wicket out')

if st.button('Pridict probability'):
    runs_left = target - score
    balls_left = 120 -(overs*6)
    wickets = 10-wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [selected_city],
                             'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets': [wickets],
                             'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")






