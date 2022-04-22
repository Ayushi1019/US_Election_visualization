from tracemalloc import start
import pandas as pd
import numpy as np
from vega_datasets import data
import altair as alt
import streamlit as st


@st.cache(allow_output_mutation=True)

def load_df():

    df = pd.read_csv('County_President/countypres_2000-2020.csv')

    # drop unused columns and nulls
    df = df.drop(columns=['mode', 'version', 'office'])
    df = df.dropna()
    df = df.reset_index()
    df = df.loc[df['totalvotes'] != 0]
    temp = []
    for index, row in df.iterrows():
        temp.append(round(row['candidatevotes'] / row['totalvotes'], 4))
    df['percentage'] = temp

    #create new dataframe with desired data config
    #create new dataframe with desired data config
    curr_county = 'AUTAUGA'
    new_df = []
    temp_dict = {}
    for index, row in df.iterrows():
        temp_dict['year'] = row['year']
        temp_dict['county'] = row['county_name']
        temp_dict['state'] = row['state_po']
        temp_dict['county_fips'] = int(row['county_fips'])
        temp_dict['total_no'] = row['totalvotes']
        curr_party = row['party'][0].lower()
        
        if row['county_name'] == curr_county:
            if curr_party == 'd':
                temp_dict['dem_no'] = row['candidatevotes']
                temp_dict['dem_pct'] = row['percentage']
            elif curr_party == 'r':
                temp_dict['rep_no'] = row['candidatevotes']
                temp_dict['rep_pct'] = row['percentage']
            elif curr_party == 'l':
                temp_dict['lib_no'] = row['candidatevotes']
                temp_dict['lib_pct'] = row['percentage']
            elif curr_party == 'g':
                temp_dict['grn_no'] = row['candidatevotes']
                temp_dict['grn_pct'] = row['percentage']
            else:
                temp_dict['oth_no'] = row['candidatevotes']
                temp_dict['oth_pct'] = row['percentage']
        else:
            copy = temp_dict.copy()
            new_df.append(copy)
            temp_dict.clear()
            
            temp_dict['year'] = row['year']
            temp_dict['county'] = row['county_name']
            temp_dict['state'] = row['state_po']
            temp_dict['county_fips'] = int(row['county_fips'])
            temp_dict['total_no'] = row['totalvotes']
            curr_party = row['party'][0].lower()

            if curr_party == 'd':
                temp_dict['dem_no'] = row['candidatevotes']
                temp_dict['dem_pct'] = row['percentage']
            elif curr_party == 'r':
                temp_dict['rep_no'] = row['candidatevotes']
                temp_dict['rep_pct'] = row['percentage']
            elif curr_party == 'l':
                temp_dict['lib_no'] = row['candidatevotes']
                temp_dict['lib_pct'] = row['percentage']
            elif curr_party == 'g':
                temp_dict['grn_no'] = row['candidatevotes']
                temp_dict['grn_pct'] = row['percentage']
            else:
                temp_dict['oth_no'] = row['candidatevotes']
                temp_dict['oth_pct'] = row['percentage']
        
        curr_county = row['county_name']
        

    new_df = pd.DataFrame(new_df)
    new_df = new_df.replace(np.nan, 0)
    return new_df

df = load_df()

county = alt.topo_feature(data.us_10m.url, 'counties')

col3,col4 = st.columns(2)

col1, col2 = st.columns(2)
years = tuple(df["year"].unique())

with col3:
    
    party = st.radio(
            "Choose party",
            ('Democrat', 'Republican', 'Libertarian','Green'))

    value = st.radio(
            "Choose to display # or '%' change",
            ('# values', "'%' change"))

with col1:
    
    start_year = st.selectbox(
        'Select Start year',years)

with col2:
    end_year = st.selectbox(
     'Select End year',years)

curr_party = "dem_no"
if party == 'Democrat' and value == "# values":
     curr_party = "dem_no"
elif party == 'Democrat' and value == "'%' change":
     curr_party = "dem_pct"
elif party == 'Republican' and value == "# values":
     curr_party = "rep_no"
elif party == 'Republican' and value == "'%' change":
     curr_party = "rep_pct"
elif party == 'Libertarian' and value == "# values":
     curr_party = "lib_no"
elif party == 'Libertarian' and value == "'%' change":
     curr_party = "lib_pct"
elif party == 'Green' and value == "# values":
     curr_party = "grn_no"
elif party == 'Green' and value == "'%' change":
     curr_party = "grn_pct"

fig = alt.Chart(county).mark_geoshape().project(
            type='albersUsa'
        ).encode(
            color=curr_party+':Q',
            tooltip=['county:N', curr_party+':Q']
        ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(df.loc[df["year"] == start_year], 'county_fips', [curr_party, 'county'])
        ).properties(
            width=300,
            height=400
        )
fig2 = alt.Chart(county).mark_geoshape(
        stroke='black',
            strokeWidth=1
        ).project(
            type='albersUsa'
        ).encode(
            color=curr_party+':Q',
            tooltip=['county:N', curr_party+':Q']
        ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(df.loc[df["year"] == end_year], 'county_fips', [curr_party, 'county'])
        ).properties(
            width=300,
            height=400
        )

if start_year != end_year:

    with col1:
        st.write(fig)

    with col2:
        st.write(fig2)

