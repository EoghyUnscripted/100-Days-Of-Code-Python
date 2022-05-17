# Day 25 CSV Data, Pandas Library

## Exercise 25-1: Working With CSV - Weather Data

### Instructions

1. With the raw data in `weather_data.csv`, open the file and read each line
2. Create a new list that gets all of the temperatures in the file as integers
3. Get the average temperature
4. Get the highest temperature

### Example Input

`weather_data.csv`

    day,temp,condition
    Monday,12,Sunny
    Tuesday,14,Rain
    Wednesday,15,Rain
    Thursday,14,Cloudy
    Friday,21,Sunny
    Saturday,22,Sunny
    Sunday,24,Sunny

### Example Output

    Temperatures: [12, 14, 15, 14, 21, 22, 24]
    Average Temp: 17.428571428571427
    Max Temp: 24

### Hint

[Pandas 1.4.2 Documentation](https://pandas.pydata.org/docs/reference/index.html)

## Exercise 25-2: Working With CSV - Squirrel Census

### Instructions

1. With the raw data in `2018_squirrel_census.csv`, open the file and read each line
2. Using the `Primary Fur Color` Column, count the total numbers for:
   1. Squirrels with black fur
   2. Squirrels with cinnamon / red fur
   3. Squirrels with grey fur
3. Output results as a dataframe to a new csv file called `squirrel_counts.csv"

### Example Input

`2018_squirrel_census.csv`

    X,Y,Unique Squirrel ID,Hectare,Shift,Date,Hectare Squirrel Number,Age,Primary Fur Color,Highlight Fur Color,Combination of Primary and Highlight Color,Color notes,Location,Above Ground Sighter Measurement,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs from,Other Interactions,Lat/Long
    -73.9561344937861,40.7940823884086,37F-PM-1014-03,37F,PM,10142018,3,,,,+,,,,,false,false,false,false,false,,false,false,false,false,false,false,false,false,,POINT (-73.9561344937861 40.7940823884086)
    -73.9688574691102,40.7837825208444,21B-AM-1019-04,21B,AM,10192018,4,,,,+,,,,,false,false,false,false,false,,false,false,false,false,false,false,false,false,,POINT (-73.9688574691102 40.7837825208444)

### Example Output

`squirrel_counts.csv`

    ,Fur Color,Count
    0,Gray,2473
    1,Cinnamon,392
    2,Black,103

### Hint

[Pandas 1.4.2 Documentation](https://pandas.pydata.org/docs/reference/index.html)
