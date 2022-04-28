# Elect-Trends
 
## Introduction:

Our project's goal is to depict our data using a map of the United States to demonstrate election trends and changes in people's preferences for parties in terms of count and percentage as well as to forecast the Presidential election in 2024. Visualization allows us to present data in a more human-friendly format, making it easier to see trends.

## Project Domain:

Visualization -  Social and Electoral Domain

## Team Members:
Nathan Griffith
<br/>
Ayushi Mundra
<br/>
Shreya Sekhar
<br/>
Akshay Srinivasan

## Data Resource:

https://electionlab.mit.edu/data

## Introduction to Datasets:

### Presidential Elections: 
Every four years, on the first Tuesday following the first Monday in November, presidential candidates are elected. Each state is allotted a particular number of electors based on its overall number of congressional members in the Electoral College system. This data is organized by county, resulting in a more accurate yes fluctuating United States map during visualization.

### House Elections: 
Representatives from all 435 congressional districts in each of the 50 U.S. states, as well as five non-voting delegates from the District of Columbia and four of the five inhabited U.S. territories, will be elected in the House Elections.

### Senate Elections: 
National Elections take place every even-numbered year. The president, vice president, one-third of the Senate, and the entire House of Representatives are all up for election every four years (on-year elections). When there isn't a presidential election in an even-numbered year, one-third of the Senate and the entire House are elected (off-year elections).

## Valid Parties:

We have a short list of valid parties that would be examined because there are many individual parties in addition to the mainstream parties. Democrat, Republican, Libertarian, Green, and other political parties are represented. All other parties are represented by the others, ensuring that no party is overlooked in the voting process.

## Visualization:

The presidential election comprises data by county, hence a county-by-county depiction of the dataset in both value and percentage changes with respect to the valid parties has been displayed.

With respect to the valid parties, the Senate election comprises state-by-state data, hence a state-by-state depiction of the data in both the value and percentage changes has been highlighted.

The House election data is cleaned up using total no, which will have the total votes by every county in the state. As a result, the value in percentage of each state is modified with respect to the total _no present and their voting pattern. In terms of the valid parties, the house election is finally reflected in state-by-state values and percentage changes.

The presidential election dataset spans the years 2000 to 2020, while the senate and house election datasets span the years 1976 to 2020. The streamlit app would allow the user to select the sort of election, such as Senate, House, or Presidential. After selecting the election type, the user can choose the party for whom they want to observe the trend, as well as the display in terms of numbers and percentages. The viewer is given a year range to choose the start and end year of visualization, and after selecting the needed parameters, they are presented with a visualization map of the United States with state/county election data exhibiting patterns by party and year showcasing the election trends.

## Visualization as a tool for answering questions:

1. Which states have had the largest change in opinion over time towards democrat?
  - With regards to the senate election, the state with the largest change in opinion regarding Democrats is Oregon with 56% of the voting shifting           towards the Democrats. As we can see from the map, there are a few more 50% + increase in other states too, but the highest is Oregon.
  <p align="center">
  <img width="220" alt="img 1" src="https://user-images.githubusercontent.com/51698822/165859285-7febc217-a9e7-4d7f-b4c9-66a07ce8ed6a.png">
  </p>
    
  - With regards to the house election, the state with the largest change in opinion regarding Democrats is Vermont and Maine with 100% of the voting         shifting towards the Democrats and in Wyoming and West Virginia with a 100% of the voting shifting against Democrats.
  <p align="center">
  <img width="220" alt="img2" src="https://user-images.githubusercontent.com/51698822/165860956-94c903d5-7eab-4005-858b-8b5c85d92188.png">
  </p>

2. Compare total votes based on Senate, House and Presidential based on party for year 1976/2000 and 2020.

 - House:
  <p align="center">
  <img width="336" alt="img3" src="https://user-images.githubusercontent.com/51698822/165861085-72dbb498-e27b-42c6-80a9-c1fc5faab1e8.png"> 
  &nbsp;
  <img width="286" alt="img4" src="https://user-images.githubusercontent.com/51698822/165861131-211ce793-4a48-4b40-a459-caef8dc6d7ba.png">
  </p>
  
  - Senate:
  <p align="center">
  <img width="336" alt="img5" src="https://user-images.githubusercontent.com/51698822/165861693-e40b4baa-729e-42f9-a019-7d1ebf078735.png">
  &nbsp;
  <img width="345" alt="img6" src="https://user-images.githubusercontent.com/51698822/165861709-ea771637-5488-493b-b16a-4503d99c4414.png">
  </p>
  
  - Presidential:
  <p align="center">
  <img width="349" alt="img7" src="https://user-images.githubusercontent.com/51698822/165862023-8e670f44-d832-4340-8dbf-1e2c9ead1d1a.png">
  &nbsp;
  <img width="282" alt="img8" src="https://user-images.githubusercontent.com/51698822/165862041-53ba96e9-8ae7-48e3-8ef7-e16e3aa4c283.png">
  </p>

 
3. Which states have had the largest change in opinion over time towards republicans?
  - With regards to the senate election, the state with the largest change in opinion regarding Republicans is Oregon with 62% of the voting shifting         towards the Republicans.
    <p align="center">
     <img width="220" alt="img9" src="https://user-images.githubusercontent.com/51698822/165862396-4765fabe-8f6e-478a-9953-c14d1183b035.png">
    </p>

  - With regards to the house election, the state with the largest change in opinion regarding Republicans is West Verginia with 100% of the voting           shifting towards the Republicans and in Vermount and Maine with 100% of the voting shifting against the Republicans.
    <p align = "center">
    <img width="220" alt="img10" src="https://user-images.githubusercontent.com/51698822/165862413-e26a41e6-7a55-45e8-8797-48d35b247240.png">
    </p>

4. When were periods where majority changed from red to blue/blue to red in house elections?

  - There hasn’t been a significant change in this timeframe in presidential elections except in states like ohio turned into a blue state in 2008, and        wisconsin turned into a red state in 2016. There were a few other changes but nothing too significant.
   <p align = "center">
   <img width="405" alt="img11" src="https://user-images.githubusercontent.com/51698822/165862842-6633707b-4498-4776-85ef-e049df60d3dc.png">
    </p>

5. Comparison between 2016-2020 regarding democrats, republicans group by the senate, president, house.

  - Presidential:
  <p align="center">
  <img width="449" alt="img12" src="https://user-images.githubusercontent.com/51698822/165862903-ea9c7c6c-8ef0-41c0-8f4b-34e6bf5e8687.png">
  </p>
    <figcaption align = "center">   <b>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DEMOCRATS &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; REPUBLICANS</b></figcaption>
  <p align="center">
  <img width="340" alt="img13" src="https://user-images.githubusercontent.com/51698822/165862982-409c4574-8d01-4466-9cc6-5e7327bdb0ac.png">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img width="340" alt="img14" src="https://user-images.githubusercontent.com/51698822/165863019-ce969796-ee30-4ccf-9e24-f39d201629ff.png">
  </p>
  
  - House:
  <p align="center">
  <img width="449" alt="img15" src="https://user-images.githubusercontent.com/51698822/165863247-9c544748-dead-4901-bd41-21bdd2703033.png">
  </p> 
  <figcaption align = "center"><b>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DEMOCRATS &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; REPUBLICANS</b></figcaption>
  </p> 
  <p align="center">
  <img width="340" alt="img16" src="https://user-images.githubusercontent.com/51698822/165863810-1b97fa2d-2c4e-43fc-9531-a7ee808932ed.png">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img width="340" alt="img17" src="https://user-images.githubusercontent.com/51698822/165863819-ce60a416-ddcd-4931-a5c8-b2e46618bf5b.png">
           
  - Senate:
  <p align="center">
  <img width="360" alt="img18" src="https://user-images.githubusercontent.com/51698822/165864510-85f94571-3d4d-46e6-a9fe-c12fe3bd70d9.png">
  </p>
  
  <figcaption align = "center">   <b>&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;DEMOCRATS &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; REPUBLICANS</b></figcaption>
   <p align="center">
  <img width="340" alt="img19" src="https://user-images.githubusercontent.com/51698822/165864531-50e7ce1a-4c0c-4436-a903-73d803da48e9.png">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img width="340" alt="img20" src="https://user-images.githubusercontent.com/51698822/165864547-1dff8401-1d99-460d-a2b4-a31e59da82f5.png">
  </p>
  
## Prediction:

<br/>
The presidential dataset from year 2000-2020 is used for the prediction of the 2024 presidential elections. The whole span of twenty years consisting of six elections are considered and analyzed to predict the upcoming 2024 elections. A linear regression model is used to predict the 2024 elections which gives us the final count of 271 for the Democrats and 267 for the Republicans, showing that the Democrats win the presidential election for the year 2024.This prediction is not based on every election happened o far but only on the years which our dataset comprises of hence, may not be 100% accurate but with respect to our dataset, the chances for the democrats winning the election of the year 2024 is high as predicted and shown using the visualization plot showcasing the counts per each state.

