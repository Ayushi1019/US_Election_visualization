import pandas as pd
import numpy as np
from vega_datasets import data
import altair as alt
import streamlit as st
from statsmodels.tsa.ar_model import AutoReg
import math

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
    new_df = new_df.replace(np.nan, 0)
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
            else:
                temp_dict['oth_no'] = row['candidatevotes']
                temp_dict['oth_pct'] = row['percentage']
        
        curr_dist = row['state_po'] + str(row['district'])

    new_df = pd.DataFrame(new_df)
    
    #create new dataframe with desired data config
    curr_state = 'AL'
    final_df = []
    temp_dict = {}
    for index, row in new_df.iterrows():
        if index >= len(new_df):
            break
        
        if row['state'] == curr_state:
            temp_dict['year'] = row['year']
            temp_dict['state'] = row['state']
            temp_dict['state_fips'] = int(row['state_fips'])
            curr_party = get_winning_party(new_df.loc[index])
            
            if curr_party == 'd':
                if 'dem_no' in temp_dict:
                    temp_dict['dem_no'] += 1
                else:
                    temp_dict['dem_no'] = 1
            elif curr_party == 'r':
                if 'rep_no' in temp_dict:
                    temp_dict['rep_no'] += 1
                else:
                    temp_dict['rep_no'] = 1
            elif curr_party == 'l':
                if 'lib_no' in temp_dict:
                    temp_dict['lib_no'] += 1
                else:
                    temp_dict['lib_no'] = 1
            elif curr_party == 'g':
                if 'grn_no' in temp_dict:
                    temp_dict['grn_no'] += 1
                else:
                    temp_dict['grn_no'] = 1
            elif curr_party == 'o':
                if 'oth_no' in temp_dict:
                    temp_dict['oth_no'] += 1
                else:
                    temp_dict['oth_no'] = 1
                    
                    
        else:
            total = 0
            if 'dem_no' in temp_dict:
                total += temp_dict['dem_no']
            else:
                temp_dict['dem_no'] = 0 
            if 'rep_no' in temp_dict:
                total += temp_dict['rep_no']
            else:
                temp_dict['rep_no'] = 0  
            if 'lib_no' in temp_dict:
                total += temp_dict['lib_no']
            else:
                temp_dict['lib_no'] = 0  
            if 'grn_no' in temp_dict:
                total += temp_dict['grn_no']
            else:
                temp_dict['grn_no'] = 0  
            if 'oth_no' in temp_dict:
                total += temp_dict['oth_no']
            else:
                temp_dict['oth_no'] = 0
                
            temp_dict['total_no'] = total
            
            temp_dict['dem_pct'] = round(temp_dict['dem_no'] / temp_dict['total_no'], 4)
            temp_dict['rep_pct'] = round(temp_dict['rep_no'] / temp_dict['total_no'], 4)
            temp_dict['lib_pct'] = round(temp_dict['lib_no'] / temp_dict['total_no'], 4)
            temp_dict['grn_pct'] = round(temp_dict['grn_no'] / temp_dict['total_no'], 4)
            temp_dict['oth_pct'] = round(temp_dict['oth_no'] / temp_dict['total_no'], 4)
                
            
            copy = temp_dict.copy()
            final_df.append(copy)
            temp_dict.clear()
            
            temp_dict['year'] = row['year']
            temp_dict['state'] = row['state']
            temp_dict['state_fips'] = int(row['state_fips'])
            curr_party = get_winning_party(new_df.loc[index])

            if curr_party == 'd':
                if 'dem_no' in temp_dict:
                    temp_dict['dem_no'] += 1
                else:
                    temp_dict['dem_no'] = 1
            elif curr_party == 'r':
                if 'rep_no' in temp_dict:
                    temp_dict['rep_no'] += 1
                else:
                    temp_dict['rep_no'] = 1
            elif curr_party == 'l':
                if 'lib_no' in temp_dict:
                    temp_dict['lib_no'] += 1
                else:
                    temp_dict['lib_no'] = 1
            elif curr_party == 'g':
                if 'grn_no' in temp_dict:
                    temp_dict['grn_no'] += 1
                else:
                    temp_dict['grn_no'] = 1
            elif curr_party == 'o':
                if 'oth_no' in temp_dict:
                    temp_dict['oth_no'] += 1
                else:
                    temp_dict['oth_no'] = 1
        
        curr_state = row['state']
        

    final_df = pd.DataFrame(final_df)
    final_df = final_df.set_index("state_fips")
    final_df["state_fips"] = final_df.index
    return final_df

def get_winning_party(row):
    max_val = 0
    winning_party = '#'
    if row['dem_no'] > max_val:
        max_val = row['dem_no']
        winning_party = 'd'
    if row['rep_no'] > max_val:
        max_val = row['rep_no']
        winning_party = 'r'
    if row['grn_no'] > max_val:
        max_val = row['grn_no']
        winning_party = 'g'
    if row['lib_no'] > max_val:
        max_val = row['lib_no']
        winning_party = 'l'
    if row['oth_no'] > max_val:
        max_val = row['oth_no']
        winning_party = 'o'
    return winning_party

def get_fips(state,data):
    for index, row in data.iterrows():
        if row[' stusps'].strip() == state:
            return row[' st']
    return -1

def prediction_df_pres():
    df = load_df_county()

    tmp_df = df.drop(columns=['lib_no', 'lib_pct', 'grn_no', 'grn_pct', 'oth_no', 'oth_pct', 'dem_pct', 'rep_pct'])
    final_df = []
    temp_dict = {}
    curr_state = 'AL'
    for index, row in tmp_df.iterrows():
        if row['state'] == curr_state:
            temp_dict['year'] = row['year']
            temp_dict['state'] = row['state']
            temp_dict['state_fips'] = get_fips(row['state'],state_data)
            if 'total_no' in temp_dict:
                temp_dict['total_no'] += row['total_no']
                temp_dict['dem_no'] += row['dem_no']
                temp_dict['rep_no'] += row['rep_no']
            else:
                temp_dict['total_no'] = row['total_no']
                temp_dict['dem_no'] = row['dem_no']
                temp_dict['rep_no'] = row['rep_no']
        else:
            copy = temp_dict.copy()
            final_df.append(copy)
            temp_dict.clear()
            
            temp_dict['year'] = row['year']
            temp_dict['state'] = row['state']
            temp_dict['state_fips'] = get_fips(row['state'],state_data)
            if 'total_no' in temp_dict:
                temp_dict['total_no'] += row['total_no']
                temp_dict['dem_no'] += row['dem_no']
                temp_dict['rep_no'] += row['rep_no']
            else:
                temp_dict['total_no'] = row['total_no']
                temp_dict['dem_no'] = row['dem_no']
                temp_dict['rep_no'] = row['rep_no']
                
            curr_state = row['state']
            
            
    final_df = pd.DataFrame(final_df)
    final_df = final_df.set_index("state_fips")
    final_df["state_fips"] = final_df.index

    duplicate = []
    counter = {}
    for index, row in final_df.iterrows():
        k = str(row['year'])+row['state']
        if k in counter:
            counter[k]+=1
            duplicate.append(index)
        else:
            counter[k]=1
    final_df.drop(duplicate)

    return final_df

dataset = st.sidebar.selectbox(
        "Choose the dataset",
        ("Senate", "House", "Presidential","Presidential Prediction for 2024")
    )

df = load_df_senate()
state_data = pd.read_csv('us-state-ansi-fips.csv')

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
elif dataset == "Presidential Prediction for 2024":
    st.write("Presidential Election Prediction Analysis for 2024")

alt.data_transformers.enable('default', max_rows=None)

if dataset != "Presidential Prediction for 2024":
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
    
    if start_year != end_year :

        df2 = pd.DataFrame(df,columns=[curr_col])
        df_end_year = pd.DataFrame(df.loc[df["year"] == end_year],columns=[curr_col,curr_party])
        df_start_year = pd.DataFrame(df.loc[df["year"] == start_year],columns=[curr_col,curr_party])

        df2.columns = df2.columns.str.replace(' ', '')
        df_end_year.columns = df_end_year.columns.str.replace(' ', '')
        df_start_year.columns = df_start_year.columns.str.replace(' ', '')

        df2 = (df2.reset_index()
            .drop_duplicates(subset=p_key, keep='first')
            .set_index(p_key).sort_index())
        df_end_year = (df_end_year.reset_index()
            .drop_duplicates(subset=p_key, keep='first')
            .set_index(p_key).sort_index())
        df_start_year = (df_start_year.reset_index()
            .drop_duplicates(subset=p_key, keep='first')
            .set_index(p_key).sort_index())

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
else:
    df = prediction_df_pres()
    features = alt.topo_feature(data.us_10m.url, 'states')
    forecasts = {}
    
    for group, values in df.groupby("state").dem_no:
        model = AutoReg(values, lags=0)
        result = model.fit()
        prediction = result.forecast(steps=1)
        forecasts[group] = prediction

        
    dem_predictions = pd.DataFrame(forecasts)
    forecasts = {}
    
    for group, values in df.groupby("state").rep_no:
        model = AutoReg(values, lags=0)
        result = model.fit()
        prediction = result.forecast(steps=1)
        forecasts[group] = prediction
   
    rep_predictions = pd.DataFrame(forecasts)
    final_df = []
    temp_dict = {}

    for col in dem_predictions.columns:
        a=0
        b=0
        
        temp_dict['year'] = 2024
        temp_dict['state'] = col
        temp_dict['state_fips'] = get_fips(col,state_data)
        
        for item in dem_predictions[col]:
            if not math.isnan(item):
                a = item
                temp_dict['dem_no'] = item
        for item in rep_predictions[col]:
            if not math.isnan(item):
                b = item
                temp_dict['rep_no'] = item
            
        copy = temp_dict.copy()
        final_df.append(copy)
        temp_dict.clear()
    final_df = pd.DataFrame(final_df)
    final_df = final_df.set_index("state_fips")
    final_df["state_fips"] = final_df.index

    final_df['winner'] = np.where((final_df['dem_no'] <= final_df['rep_no']), 0, 1)
    final_df['winning_party'] = np.where((final_df['winner'] == 0), "Republican", "Democrat")

    fig = alt.Chart(features).mark_geoshape(
            stroke='black',
                strokeWidth=1
            ).project(
                type='albersUsa'
            ).encode(
                color= alt.Color('winner:Q',scale=alt.Scale(scheme='redblue')),
                tooltip=['state:N', 'winning_party:N'],
                
            ).transform_lookup(
            lookup='id',
            from_=alt.LookupData(final_df, 'state_fips', ['state','winner','winning_party'])
            ).properties(
                width=1000,
                height=500
            )
    st.write(fig)
    


