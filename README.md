# DPS

# DPS AI CHALLENGE

## Description
This challenge for Artificial Intelligence Engineer Consists of 3 tasks.
- Mission 1: Create a AI Model
- Mission 2: Publish source code & Deploy
- Mission 3: Sending the URL of the task

## Demo link
View demo <a href="http://35.154.53.33:8501/"><b>Here!</b></a>.
Or use this API endpoint  `http://35.154.53.33:8501/` to returns your predictions.
#### Note
Category : alcohol accidents --> 0
           escape accidents  --> 1 
           traffic accidents --> 2 
           
Accident_Type : all in all           --> 0 
                injured and killed   --> 1 
                with personal injury --> 2
The endpoint accepts a POST request with a JSON body like this:
```
{
"Category":0,
"Accident_Type": "0",
"Year" : 2021,
"Month" : 01
}
```
It return prediction in the following format:
```
{
"prediction" : value
}
```
## DataFrame

Download the <a href="https://www.opengov-muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7"><b>Monatszahlen Verkehrsunfälle</b></a> Dataset from the München Open Data Portal. Here you see the number of accidents for specific categories per month.

## Packages:
- pandas
- matplotlib
- sklearn
- pickle

## Visualization:
visualization historically the number of accidents per category
### Accidents Category Visualization:

<img src="./images/download (2).png"/>
<img src="./images/download (3).png"/>
<img src="./images/download (4).png"/>
<img src="./images/download (5).png"/>

<br />

### Number of accidents per category
<img src="./images/download (6).png"/>

<br />

### Number of accidents per Accident Type
<img src="./images/download (7).png"/>
