# Platform & Services
## Data sources
* sensors (weather data)
* stream data platforms (APIs of shared bicycle companies)
* our own database-as-a-service (Wi-Fi dataset)

## Analytics
* data visualization
* machine learning methods to help simulate missing data

## Data Services
* APIs: for some shared bicycle companies, they can visit our APIs and get Wi-Fi and weather data and then they can decide put more bicycles around the teaching buildings or not.

## Notification
~~TODO~~
> "new results are available"
>
> "new data sources are available"

## Human Services
* for **shared bicycle companies**: APIs
* for **students**: they can know the number of people in the teaching buildings, so that they can decide which teaching building should they go and self-study here.
* for **building administrators**: how many rooms should be open to students

## Elasticity Management
* APIs: return json data to programs
* data visualization: return map and pictures with data for human users
* TO BE CONTINUE...

## platform services in our scenario:

| Option | Technology/Framework
| --------   | -----
| Cloud Server |AWS
| Database | MongoDB
| Front-end | Javascript
| Back-end | Python
| Back-end Framework | flask
| Map APIs | baidu/Amap
| Bicycle APIs | ofo, mobike

### Why?
* We use docker's container technology.
* We can use AWS and MongoDB for free.
* The period of development by script programmming languages (Python & Javascript) is short.
* we find a project about flask & MongoDB on Github.
* baidu/Amap & ofo/mobike APIs -----> free.
