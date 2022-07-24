import json
import csv
import requests
from pathlib import Path
import streamlit as st
from train_info import *
from utils import findkey, sortkey
import datetime, time
#parking_url = "http://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2"


def api_call(select):
    lta_url = "http://datamall2.mytransport.sg/ltaodataservice/PCDRealTime?TrainLine="

    headers = {"AccountKey":  st.secrets["LTA_APIKEY"],
               "accept": "application/json"}

    if select in list(trainline.keys())[1:]:

        query_param = trainline.get(select)
        url = f"{lta_url}{query_param}"
        response = requests.request(method="get", url=url, headers=headers)
        data = response.json()
        #st.write(data["value"])
        crowd_data = sortkey(data["value"])
        for info in crowd_data:
            if info["Station"] in traindict.keys():
                line = traindict.get(info["Station"])
                info["Station"] = line[0]
                if info["CrowdLevel"] == "l":
                    info["CrowdLevel"] = "\U0001F41F Light"
                elif info["CrowdLevel"] == "h":
                    info["CrowdLevel"] = "\U0001F41F \U0001F41F \U0001F41F Crowded"
                elif info["CrowdLevel"] == "m":
                    info["CrowdLevel"] = "\U0001F41F \U0001F41F Moderate"
                else:
                    info["CrowdLevel"] = "\U0001F937 Check Later"
        
            with st.container():
                c1, c2 = st.columns((1, 3))
                with c1:
                    
                    st.write("\U0001F686",info["Station"])
                with c2:
                
                    st.write(info["CrowdLevel"]-)

