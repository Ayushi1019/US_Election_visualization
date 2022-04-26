import pandas as pd
import numpy as np
from vega_datasets import data
import altair as alt
import streamlit as st

@st.cache(allow_output_mutation=True)

def load_df_county():

    df = pd.read_csv('County_President/countypres_2000-2020.csv',index_col="county_fips")
    df["county_fips"] = df.index

    # drop unused columns and nulls
    df = df.drop(columns=['mode', 'version', 'office'])
    df = df.dropna()
    df = df.loc[df['totalvotes'] != 0]
    temp = []
    for index, row in df.iterrows():
        temp.append(round(row['candidatevotes'] / row['totalvotes'], 4))
    df['percentage'] = temp

    #create new dataframe with desired data config
    curr_county = 'AUTAUGA'
    new_df = []
    temp_dict = {}
    for index, row in df.iterrows():
        
        if row['county_name'] == curr_county:
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
    new_df = new_df.set_index("county_fips")
    new_df["county_fips"] = new_df.index
    return new_df

def load_df_senate():

    df = pd.read_csv('Senate_dataset/1976-2020-senate.csv',index_col="state_fips")
    df["state_fips"] = df.index

    df = df.drop(columns=['mode', 'version', 'unofficial','writein','special','stage'])
    df = df.dropna()
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
        
        if row['state'] == curr_state:
            temp_dict['year'] = row['year']
            temp_dict['state'] = row['state']
            temp_dict['state_fips'] = int(row['state_fips'])
            temp_dict['total_no'] = row['totalvotes']
            curr_party = row['party_simplified'][0].lower()
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
            curr_party = row['party_simplified'][0].lower()

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
    new_df = new_df.set_index("state_fips")
    new_df["state_fips"] = new_df.index
    new_df = new_df.replace(np.nan, 0)
    return new_df

def load_df_house():
    df = pd.read_csv('House_dataset/1976-2020-house.csv')
    df = df.drop(columns=['writein','version','state_cen','state_ic','office','special','runoff','stage','mode','fusion_ticket','unofficial'])
    df = df.dropna()
    df = df.loc[df['totalvotes'] != 0]
    temp = []
    for index, row in df.iterrows():
        temp.append(round(row['candidatevotes'] / row['totalvotes'], 4))
    df['percentage'] = temp

    valid_parties = ['DEMOCRAT', 'REPUBLICAN', 'LIBERTARIAN', 'INDEPENDENT', 'GREEN', 'OTHER']

    for index, row in df.iterrows():
        if row['party'] not in valid_parties:
            df.loc[index,'party'] = 'OTHER'

    #create new dataframe with desired data config
    curr_dist = 'AL1'
    new_df = []
    temp_dict = {}
    for index, row in df.iterrows():
        if row['state_po'] + str(row['district']) == curr_dist:
            temp_dict['year'] = row['year']
            temp_dict['state'] = row['state_po']
            temp_dict['state_fips'] = int(row['state_fips'])
            temp_dict['district'] = row['district']
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
            elif curr_party == 'i':
                temp_dict['indep_no'] = row['candidatevotes']
                temp_dict['indep_pct'] = row['percentage']
            else:
                temp_dict['oth_no'] = row['candidatevotes']
                temp_dict['oth_pct'] = row['percentage']
        else:
            copy = temp_dict.copy()
            new_df.append(copy)
            temp_dict.clear()
        
            temp_dict['year'] = row['year']
            temp_dict['state'] = row['state_po']
            temp_dict['state_fips'] = int(row['state_fips'])
            temp_dict['district'] = row['district']
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
            elif curr_party == 'i':
                temp_dict['indep_no'] = row['candidatevotes']
                temp_dict['indep_pct'] = row['percentage']
            else:
                temp_dict['oth_no'] = row['candidatevotes']
                temp_dict['oth_pct'] = row['percentage']
            
        curr_dist = row['state_po'] + str(row['district'])
    

    new_df = pd.DataFrame(new_df)
    new_df = new_df.set_index("state_fips")
    new_df["state_fips"] = new_df.index
    new_df = new_df.replace(np.nan, 0)
    return new_df

dataset = st.sidebar.selectbox(
        "Choose the dataset",
        ("Senate", "House", "Presidential")
    )
df = load_df_senate()

valid_party = ['DEMOCRAT', 'REPUBLICAN', 'LIBERTARIAN', 'GREEN', 'OTHER']
if dataset == "Senate":
    st.write("Senate Election Analysis")
    df = load_df_senate()
    features = alt.topo_feature(data.us_10m.url, 'states')
    curr_col = "state"
    p_key = "state_fips"

elif dataset == "House":
    st.write("House Election Analysis")
    df = load_df_house()
    features = alt.topo_feature(data.us_10m.url, 'states')
    curr_col = "state"
    p_key = "state_fips"
    valid_party = ['DEMOCRAT', 'REPUBLICAN', 'LIBERTARIAN', 'INDEPENDENT', 'GREEN', 'OTHER']

elif dataset == "Presidential":
    st.write("Presidential Election Analysis")
    df = load_df_county()
    features = alt.topo_feature(data.us_10m.url, 'counties')
    curr_col = "county"
    p_key = "county_fips"
    valid_party = ['DEMOCRAT', 'REPUBLICAN', 'LIBERTARIAN', 'GREEN', 'OTHER']

party = st.radio(
    "Choose party",
    tuple(valid_party))

value = st.radio(
    "Choose to display # or '%' change",
    ('# values', "'%' change"))

curr_party = ""
if party == 'DEMOCRAT' and value == "# values":
    curr_party = "dem_no"
elif party == 'DEMOCRAT' and value == "'%' change":
    curr_party = "dem_pct"
elif party == 'REPUBLICAN' and value == "# values":
    curr_party = "rep_no"
elif party == 'REPUBLICAN' and value == "'%' change":
    curr_party = "rep_pct"
elif party == 'LIBERTARIAN' and value == "# values":
    curr_party = "lib_no"
elif party == 'LIBERTARIAN' and value == "'%' change":
    curr_party = "lib_pct"
elif party == 'OTHER' and value == "# values":
    curr_party = "oth_no"
elif party == 'OTHER' and value == "'%' change":
    curr_party = "oth_pct"
elif party == 'INDEPENDENT' and value == "# values":
    curr_party = "ind_no"
elif party == 'INDEPENDENT' and value == "'%' change":
    curr_party = "ind_pct"
elif party == 'GREEN' and value == "# values":
    curr_party = "grn_no"
elif party == 'GREEN' and value == "'%' change":
    curr_party = "grn_pct"

years = tuple(df["year"].unique())

start_year = st.selectbox(
    'Select Start year',years)
end_year = st.selectbox(
    'Select End year',years)


alt.data_transformers.enable('default', max_rows=None)

if start_year != end_year and dataset != "House":
    df2 = pd.DataFrame(df,columns=[curr_col])
    df_end_year = pd.DataFrame(df.loc[df["year"] == end_year],columns=[curr_col,curr_party])
    df_start_year = pd.DataFrame(df.loc[df["year"] == start_year],columns=[curr_col,curr_party])
    df2["end_year"] = df_end_year[curr_party]
    df2["start_year"] = df_start_year[curr_party]
    df2[p_key] = df2.index

    df2 = df2.replace(np.nan, 0)
    df2["diff"] = df2["end_year"] - df2["start_year"]
    df2 = df2.loc[df2[curr_col] != 0]

    fig = alt.Chart(features).mark_geoshape(
        stroke='black',
            strokeWidth=1
        ).project(
            type='albersUsa'
        ).encode(
            color=alt.Color('diff:Q',scale=alt.Scale(scheme='turbo')),
            tooltip=[curr_col+':N', 'diff:Q'],
            
        ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(df2, p_key, ['diff', curr_col])
        ).properties(
            width=800,
            height=400
        )
    
    st.write(fig)



