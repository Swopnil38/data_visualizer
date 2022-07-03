import re
import numpy as np
import pandas as pd
import pycountry
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def read_yt_csv(name):
    
    list_alpha_2 = [i.alpha_2 for i in list(pycountry.countries)]
    list_alpha_3 = [i.alpha_3 for i in list(pycountry.countries)]    

    def country_flag(df):
        if (len(df)==2 and df in list_alpha_2):
            return pycountry.countries.get(alpha_2=df).name
        elif (len(df)==3 and df in list_alpha_3):
            return pycountry.countries.get(alpha_3=df).name
        else:
            return 'Invalid Code'
        
    geolocator = Nominatim(user_agent='your unique UA')
    def geolocate(country):
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(country)
            # And return latitude and longitude
            return [loc.latitude, loc.longitude]
        except GeocoderTimedOut:
            # Return missing value
            return geolocate(country)
        except:
            return 0,0
    
    data = pd.ExcelFile('data\{}.xlsx'.format(name))
    GenderAge = pd.read_excel(data,'GenderWiseAge')
    Geography = pd.read_excel(data,'Geography')
    view = pd.read_excel(data,'view')
    ages_yt =  []
    male_viewer_yt = []
    female_viewer_yt = []
    values = 0
    valuess = 0
    for i,j,k in zip(GenderAge['ageGroup'],GenderAge['Gender'],GenderAge['viewerPercentage']):
        if i[3:] not in ages_yt:
            if i == "age55-64" or i == "age65-" :
                continue
            else:
                ages_yt.append(i[3:])
        
        if j == "male":
            if i == "age55-64" or i == "age65-" :
                values = values + k
            else:
                male_viewer_yt.append(k)
            
        if j == "female":
            if i == "age55-64" or i == "age65-" :
                valuess = valuess + k
            else:
                female_viewer_yt.append(k)
        
    male_viewer_yt.append(values)
    female_viewer_yt.append(valuess)
    ages_yt.append("55+")

    country_name = []
    country_viewer_per = []
    for i in Geography['Country']:
        country_ = country_flag(i)
        country_name.append(country_)
    Geography['Country_Name'] = country_name
    
    country_lat = []
    country_lon = []
    
    
    for i in Geography['Country']:
        countrys_lat,countrys_long = geolocate(i)
        country_lat.append(countrys_lat)
        country_lon.append(countrys_long)
    Geography['Latitude'] = country_lat
    Geography['Longitude'] = country_lon
        
    print(Geography)
    
    
    total_views = 0
    for i in Geography['views']:
        total_views = total_views + i
    for i in Geography['views']:
        viewer_per = (i/total_views)*100
        country_viewer_per.append(viewer_per)
        
    view['year'] = pd.DatetimeIndex(view['date']).year
    view['month'] = pd.DatetimeIndex(view['date']).month
    view['date'] = pd.to_datetime(view['date'])
    
    year_month = []
    viewes = []
    avg_duration = []

        
    years = [2019,2020,2021,2022]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    for i in years:
        current_year = []
        current_year.append(i)
        year_df = view[view['year'].isin(current_year)]


        
        for j in months:
            monthss = str(i)+'/'+str(j)
            viewed = 0
            avg_durationed = 0
            month = []
            month.append(j)
            month_df = year_df[year_df['month'].isin(month)]
            
            for k in month_df['views']:
                viewed = viewed + k
            month_days = 0
            for l in month_df['avg.viewDuration']:
                avg_durationed = avg_durationed + l
                month_days = month_days + 1
            try:
                avg_durationed = avg_durationed/month_days
            except:
                avg_durationed = 0
            
            if viewed != 0 and avg_durationed != 0:
                viewes.append(viewed)
                avg_duration.append(avg_durationed/60)
                year_month.append(monthss)

    
    
        
    return ages_yt,male_viewer_yt,female_viewer_yt,country_name,country_viewer_per,country_lat,country_lon,viewes,avg_duration,year_month


def read_yt_csv_dately(name,yr,mo):
    data = pd.ExcelFile('data\{}.xlsx'.format(name))
    view = pd.read_excel(data,'view')
    view['year'] = pd.DatetimeIndex(view['date']).year
    view['month'] = pd.DatetimeIndex(view['date']).month
    view['date'] = pd.to_datetime(view['date'])
    view['day'] = view['date'].dt.date

    current_year = []
    current_year.append(yr)
    current_month = []
    current_month.append(mo)

    year_df = view[view['year'].isin(current_year)]

    month_df = year_df[year_df['month'].isin(current_month)]
    
    views = []
    for i in month_df['views']:
        views.append(i)
    date = []
    for j in month_df['date']:
        date.append(j)
    print(views)
    print(date)
    return views,date    
    
    
def read_fb_insta(name):

        
    geolocator = Nominatim(user_agent='your unique UA')
    def geolocate(country):
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(country)
            # And return latitude and longitude
            return [loc.latitude, loc.longitude]
        except GeocoderTimedOut:
            # Return missing value
            return geolocate(country)
        except:
            return 0,0
    data = pd.ExcelFile('data\{}.xlsx'.format(name))
    insta_age = pd.read_excel(data,'InstagramAge')
    fb_age = pd.read_excel(data,'FacebookAge')
    insta_Geography = pd.read_excel(data,'Instagram_Geography')
    fb_Geography = pd.read_excel(data,'Facebook_Geography')
    like_follow = pd.read_excel(data,'Fb_Insta')
    ages_fb =  []
    male_viewer_fb = []
    female_viewer_fb = []
    values = 0
    valuess = 0
    for i,j,k in zip(fb_age['ageGroup'],fb_age['Gender'],fb_age['viewerPercentage']):
        if i[3:] not in ages_fb:
            ages_fb.append(i[3:])
        
        if j == "male":
            male_viewer_fb.append(k)
            
        if j == "female":
            female_viewer_fb.append(k)
        


    ages_insta =  []
    male_viewer_insta = []
    female_viewer_insta = []
    values = 0
    valuess = 0
    for i,j,k in zip(insta_age['ageGroup'],insta_age['Gender'],insta_age['viewerPercentage']):
        if i[3:] not in ages_insta:
            ages_insta.append(i[3:])
        
        if j == "male":
            male_viewer_insta.append(k)
            
        if j == "female":
            female_viewer_insta.append(k)
    
    country_name = []
    country_viewer_per = []    
    country_lat = []
    country_lon = []

    for i in insta_Geography['Country']:
        countrys_lat,countrys_long = geolocate(i)
        country_lat.append(countrys_lat)
        country_lon.append(countrys_long)
        country_name.append(i)
    insta_Geography['Latitude'] = country_lat
    insta_Geography['Longitude'] = country_lon
        
    print(insta_Geography)
    total_views = 0
    for i in insta_Geography['Value']:
        total_views = total_views + i
    for i in insta_Geography['Value']:
        viewer_per = (i/total_views)*100
        country_viewer_per.append(viewer_per)
        
        
    country_name_fb = []
    country_viewer_per_fb = []    
    country_lat_fb = []
    country_lon_fb = []

    for i in fb_Geography['Country']:
        countrys_lat,countrys_long = geolocate(i)
        country_lat_fb.append(countrys_lat)
        country_lon_fb.append(countrys_long)
        country_name_fb.append(i)
    fb_Geography['Latitude'] = country_lat_fb
    fb_Geography['Longitude'] = country_lon_fb
        
    total_views = 0
    for i in fb_Geography['Value']:
        total_views = total_views + i
    for i in fb_Geography['Value']:
        viewer_per = (i/total_views)*100
        country_viewer_per_fb.append(viewer_per)   
        
    like_follow['year'] = pd.DatetimeIndex(like_follow['Date']).year
    like_follow['month'] = pd.DatetimeIndex(like_follow['Date']).month
    like_follow['date'] = pd.to_datetime(like_follow['Date'])
    
    year_month_fb_insta = []
    like_fb = []
    follower_insta = []

        
    years = [2019,2020,2021,2022]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    for i in years:
        current_year = []
        current_year.append(i)
        year_df = like_follow[like_follow['year'].isin(current_year)]


        
        for j in months:
            monthss = str(i)+'/'+str(j)
            viewed = 0
            avg_durationed = 0
            month = []
            month.append(j)
            month_df = year_df[year_df['month'].isin(month)]
            
            for k in month_df['Like']:
                viewed = viewed + k
            month_days = 0
            for l in month_df['Follower']:
                avg_durationed = avg_durationed + l

            like_fb.append(viewed)
            follower_insta.append(avg_durationed)
            year_month_fb_insta.append(monthss)
 
    
    
    return ages_fb,male_viewer_fb,female_viewer_fb,ages_insta,male_viewer_insta,female_viewer_insta,country_name,country_viewer_per,country_lat,country_lon,country_name_fb,country_viewer_per_fb,country_lat_fb,country_lon_fb,year_month_fb_insta,like_fb,follower_insta

def tiktok_data(name):
    geolocator = Nominatim(user_agent='your unique UA')
    def geolocate(country):
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(country)
            # And return latitude and longitude
            return [loc.latitude, loc.longitude]
        except GeocoderTimedOut:
            # Return missing value
            return geolocate(country)
        except:
            return 0,0
    
    data = pd.ExcelFile('data\{}.xlsx'.format(name))
    tiktok_age = pd.read_excel(data,'Tiktok_Age')
    tiktok_Geography = pd.read_excel(data,'Tiktok_Geography')
    tiktok_follower = pd.read_excel(data,'Tiktok_Follower')
    
    tik_age = []
    tik_age_label = []
    tik_geo_label = []
    tik_geo_value = []

    
    for i in tiktok_age['Gender']:
        tik_age_label.append(i)
    for i in tiktok_age['Views']:
        tik_age.append(i)
    
    
    country_lat_fb = []
    country_lon_fb = []

    for i in tiktok_Geography['Country']:
        countrys_lat,countrys_long = geolocate(i)
        country_lat_fb.append(countrys_lat)
        country_lon_fb.append(countrys_long)
        tik_geo_label.append(i)
    tiktok_Geography['Latitude'] = country_lat_fb
    tiktok_Geography['Longitude'] = country_lon_fb
        
    total_views = 0
    for i in tiktok_Geography['Value']:
        total_views = total_views + i
    for i in tiktok_Geography['Value']:
        viewer_per = (i/total_views)*100
        tik_geo_value.append(viewer_per)   

    
    

        
    year_month_tiktok = []
    follower_tiktok = []
    
    tiktok_follower['year'] = pd.DatetimeIndex(tiktok_follower['Date']).year
    tiktok_follower['month'] = pd.DatetimeIndex(tiktok_follower['Date']).month
    tiktok_follower['date'] = pd.to_datetime(tiktok_follower['Date'])

        
    years = [2019,2020,2021,2022]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    for i in years:
        current_year = []
        current_year.append(i)
        year_df = tiktok_follower[tiktok_follower['year'].isin(current_year)]


        
        for j in months:
            monthss = str(i)+'/'+str(j)
            viewed = 0
            avg_durationed = 0
            month = []
            month.append(j)
            month_df = year_df[year_df['month'].isin(month)]
            

            for l in month_df['Followers']:
                avg_durationed = avg_durationed + l


            follower_tiktok.append(avg_durationed)
            year_month_tiktok.append(monthss)
            
    return tik_age,tik_age_label,tik_geo_label,tik_geo_value,follower_tiktok,year_month_tiktok,country_lat_fb,country_lon_fb
 