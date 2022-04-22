from tracemalloc import start
import pandas as pd
import numpy as np
from vega_datasets import data
import altair as alt
import streamlit as st
import requests


@st.cache

def load_df():

    df = pd.read_csv('Senate_dataset/1976-2020-senate.csv', encoding = "ISO-8859-1")

    df = df.drop(columns=['mode', 'version', 'unofficial','writein','special','stage'])
    df = df.dropna()
    df = df.reset_index()
    df = df.loc[df['totalvotes'] != 0]
    temp = []
    for index, row in df.iterrows():
        temp.append(round(row['candidatevotes'] / row['totalvotes'], 4))
    df['percentage'] = temp

    #create new dataframe with desired data config
    curr_state = 'ARIZONA'
    new_df = []
    temp_dict = {}
    for index, row in df.iterrows():
        temp_dict['year'] = row['year']
        temp_dict['state'] = row['state']
        temp_dict['state_fips'] = int(row['state_fips'])
        temp_dict['total_no'] = row['totalvotes']
        curr_party = row['party_detailed'][0].lower()
        
        
        if row['state'] == curr_state:
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
            temp_dict['state'] = row['state']
            temp_dict['state_fips'] = int(row['state_fips'])
            temp_dict['total_no'] = row['totalvotes']
            curr_party = row['party_detailed'][0].lower()

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
        
        curr_state = row['state']
        

    new_df = pd.DataFrame(new_df)
    new_df = new_df.replace(np.nan, 0)
    return new_df

df = load_df()
st.write(df)

states = alt.topo_feature(data.us_10m.url, 'states')

party = st.radio(
     "Choose party",
     ('Democrat', 'Republican', 'Libertarian','Green'))

value = st.radio(
     "Choose to display # or '%' change",
     ('# values', "'%' change"))

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

print(curr_party)

years = tuple(df["year"].unique())

start_year = st.selectbox(
     'Select Start year',years)
end_year = st.selectbox(
     'Select End year',years)

st.write(df.loc[df["year"] == start_year])
print(len(df.loc[df["year"] == start_year]))

fig = alt.Chart(states).mark_geoshape().project(
        type='albersUsa'
    ).encode(
        color=curr_party+':Q',
        tooltip=['state:N', curr_party+':Q']
    ).transform_lookup(
    lookup='id',
    from_=alt.LookupData(df.loc[df["year"] == start_year], 'state_fips', [curr_party, 'state'])
    ).properties(
        width=400,
        height=400
    )

fig2 = alt.Chart(states).mark_geoshape(
    stroke='black',
        strokeWidth=1
    ).project(
        type='albersUsa'
    ).encode(
        color=curr_party+':Q',
        tooltip=['state:N', curr_party+':Q']
    ).transform_lookup(
    lookup='id',
    from_=alt.LookupData(df.loc[df["year"] == end_year], 'state_fips', [curr_party, 'state'])
    ).properties(
        width=400,
        height=400
    )

st.write(fig)
st.write(fig2)



