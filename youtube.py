import base64
import math
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from Value_Processing import read_fb_insta, read_yt_csv, read_yt_csv_dately, tiktok_data
from Visualizations import animatedline_chart, horizontal_bar, pie
from PIL import Image
from pydeck.types import String
import moviepy.editor as mp

st.set_page_config(layout="wide")

st.title('Social Media Data Visualization')



option = st.selectbox(
     'Which Channel Data you want to view?',
     ('Agrifo', 'Finance Factory', 'Generation of Nepal','Khulla Manch','The Doers','The Good Health','ViewFinders Production','Wedding Dreams'))
st.write('Data Visualization of :', option)
try:
    ages_yt,male_viewer_yt,female_viewer_yt,country_name,country_viewer_per,country_lat,country_lon,viewes,avg_duration,year_month = read_yt_csv(option)
except:
    st.title("No Data Found of Youtube")

figure = horizontal_bar(ages_yt,male_viewer_yt,female_viewer_yt,option)
st.pyplot(figure)

 
try:
    col,col2 = st.columns([3,2])
    with col:
        df = pd.DataFrame(list(zip(country_name,country_viewer_per,country_lat,country_lon)),columns = ['name','view','lat','lng'])
        df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
        
        layer = pdk.Layer(
            "ScatterplotLayer",
            df,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_min_pixels=10,
            radius_max_pixels=1000,
            get_position=['lng','lat'],
            get_radius="view",
            get_fill_color=[255, 140, 0],
            get_line_color=[0, 0, 0],
        )

        # Set the viewport location
        view_state = pdk.ViewState(
            longitude=84, latitude=28, zoom=6
        )

        # Combined all of it and render a viewport
        r = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "{view}\n{name}"}
        )
        
        st.pydeck_chart(r)
    with col2:
        df = pd.DataFrame(list(zip(country_name,country_viewer_per)),columns = ['Country Name','Country Viewer Percentage'])
        df.sort_values(by='Country Viewer Percentage')
        st.dataframe(df)
except:
    st.title("No Data Found of Youtube Geographical")
    
    
try:
    figure2 = animatedline_chart(year_month,viewes,option)

    clip = mp.VideoFileClip(figure2)
    clip.write_videofile("{}.mp4".format(option))

    video_file = open('{}.mp4'.format(option), 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
except:
    st.title("No Data Found of Youtube Views")
col1,col2,col3,col4,col5 = st.columns([4,1,2,1,4])

with col2:
    month_select = st.selectbox(
     'Select Month',
     ('1', '2', '3','4','5','6','7','8','9','10','11','12'))
with col4:
    year_select   = st.selectbox(
        'Select Year',
        ('2019','2020','2021','2022')
    )
data,labels = read_yt_csv_dately(option,int(year_select),int(month_select))
month_data = pd.DataFrame(data,index=labels)
if data == []:
    st.title("No Data Found")
else:
    st.area_chart(month_data)
try:
    ages_fb,male_viewer_fb,female_viewer_fb,ages_insta,male_viewer_insta,female_viewer_insta,country_name,country_viewer_per,country_lat,country_lon,country_name_fb,country_viewer_per_fb,country_lat_fb,country_lon_fb,year_month_fb_insta,like_fb,follower_insta = read_fb_insta(option)  
    

    figure = horizontal_bar(ages_fb,male_viewer_fb,female_viewer_fb,option)
    st.pyplot(figure)

    figure = horizontal_bar(ages_insta,male_viewer_insta,female_viewer_insta,option)
    st.pyplot(figure)
 
    col,col2 = st.columns([3,2])
    with col:
        df = pd.DataFrame(list(zip(country_name,country_viewer_per,country_lat,country_lon)),columns = ['name','view','lat','lng'])
        df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
        
        layer = pdk.Layer(
            "ScatterplotLayer",
            df,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_min_pixels=10,
            radius_max_pixels=1000,
            get_position=['lng','lat'],
            get_radius="view",
            get_fill_color=[255, 140, 0],
            get_line_color=[0, 0, 0],
        )

        # Set the viewport location
        view_state = pdk.ViewState(
            longitude=84, latitude=28, zoom=6
        )

        # Combined all of it and render a viewport
        r = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "{view}\n{name}"}
        )
        
        st.pydeck_chart(r)
    with col2:
        df = pd.DataFrame(list(zip(country_name,country_viewer_per)),columns = ['Country Name','Country Viewer Percentage'])
        df.sort_values(by='Country Viewer Percentage')
        st.dataframe(df)
        
    col,col2 = st.columns([3,2])
    with col:
        df = pd.DataFrame(list(zip(country_name_fb,country_viewer_per_fb,country_lat_fb,country_lon_fb)),columns = ['name','view','lat','lng'])
        df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
        
        layer = pdk.Layer(
            "ScatterplotLayer",
            df,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_min_pixels=10,
            radius_max_pixels=1000,
            get_position=['lng','lat'],
            get_radius="view",
            get_fill_color=[255, 140, 0],
            get_line_color=[0, 0, 0],
        )

        # Set the viewport location
        view_state = pdk.ViewState(
            longitude=84, latitude=28, zoom=6
        )

        # Combined all of it and render a viewport
        r = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "{view}\n{name}"}
        )
        
        st.pydeck_chart(r)
    with col2:
        df = pd.DataFrame(list(zip(country_name_fb,country_viewer_per_fb)),columns = ['Country Name','Country Viewer Percentage'])
        df.sort_values(by='Country Viewer Percentage')
        st.dataframe(df)

    like_data = pd.DataFrame(like_fb,index=year_month_fb_insta)
    if like_fb == []:
        st.title("No Data Found")
    else:
        st.area_chart(like_data)
    
    follower_data = pd.DataFrame(follower_insta,index=year_month_fb_insta)
    if follower_insta == []:
        st.title("No Data Found")
    else:
        st.area_chart(follower_data)
    
    
except:
    st.title("No Data Found of Facebook and Instagram")
    

tik_age,tik_age_label,tik_geo_label,tik_geo_value,follower_tiktok,year_month_tiktok,country_lat_fb,country_lon_fb = tiktok_data(option)
figure = pie(tik_age_label,tik_age,option)
st.pyplot(figure)


col,col2 = st.columns([3,2])
with col:
    df = pd.DataFrame(list(zip(tik_geo_label,tik_geo_value,country_lat_fb,country_lon_fb)),columns = ['name','view','lat','lng'])
    df['views'] = df['view'].apply(lambda viewed: math.pow(viewed,5))
    
    layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_min_pixels=10,
        radius_max_pixels=1000,
        get_position=['lng','lat'],
        get_radius="view",
        get_fill_color=[255, 140, 0],
        get_line_color=[0, 0, 0],
    )

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=84, latitude=28, zoom=6
    )

    # Combined all of it and render a viewport
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{view}\n{name}"}
    )
    
    st.pydeck_chart(r)
with col2:
    df = pd.DataFrame(list(zip(country_name_fb,country_viewer_per_fb)),columns = ['Country Name','Country Viewer Percentage'])
    df.sort_values(by='Country Viewer Percentage')
    st.dataframe(df)

follower_data = pd.DataFrame(follower_tiktok,index=year_month_tiktok)
if follower_tiktok == []:
    st.title("No Data Found")
else:
    st.area_chart(follower_data)

    
