# DataConcern
## Types of data needed to collect
* Dataset_FudanWiFi09[1]
* Weather data
* Number of bicycles

## source of data
* China Meteorological Administration
* Fudan Univeristy's Wi-Fi data
* Shared bicycle companies[2]

## Quality of data
* From the Wi-Fi data, we can get the latitude and longitude of each teaching buildings.
* The unit of time in Wi-Fi dataset is minute(s), so the data we got from shared bicycle companies' API should also be minute data.
* Weather data (daily).

## Data Usage
* The Wi-Fi dataset is a time series, so we should have a transformation on it.

## Quality of Service
* The Wi-Fi data have a high accuracy, as well as the GPS data of teaching buildings.
* Q: if we lose some data (like the situation in the real world), how should we deal with the time series data?

## Context
The URL for data source : http://www.cma.gov.cn/, https://can.fudan.edu.cn/data/fudanwifi09.

Reference
1. Y.-Q. Zhang, X. Li, J. Xu and A. V. Vasilakos, Human Interactive Patterns in Temporal Networks, IEEE Transcations on Systems, Man, and Cybernetics: Systems. vol. 45, pp.214-222, 2015
2. https://github.com/ubahnverleih/WoBike
