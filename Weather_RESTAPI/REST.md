**RESTFUL WEBSERVICE for Weather Information**
----
  _REST API end points are used by GET or POST or DELETE requests with passing input parameters (if needed )to retrieve JSON data to the requested client ._
  
  _Web Service End Point 1_

* **URL**

  <http://gurramlearninglabs.com:8000/weather/historical/>

* **Method:**
  
  _The request type_

  `GET`
  
*  **URL Params**

   _No URL parameters are required for this operation._

   **Required:**
 
   `N/A`

   **Optional:**
 
   `N/A`

* **Data Params**

  _GET Request and NO data params are required._

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[
    {
        "DATE": "20130101"
    },
    {
        "DATE": "20130102"
    },
    {
        "DATE": "20130103"
    },
    {
        "DATE": "20130104"
    },]`
 
* **Error Response:**

  _Since the data is already present and sever is up running, there will be no error resposes from API._

* **Sample Call:**

  _Use Postman Software or Chrome Extension to send GET request using the end point URL._
  
  
 _Web Service End Point 2_
  
* **URL**

  <http://gurramlearninglabs.com:8000/weather/historical/>

* **Method:**
  
  _The request type_

  `GET`
  
*  **URL Params**

   **Required:**
   
   `DATE:[20130101]`

   **Optional:**
 
   `N/A`

* **Data Params**

  _GET Request and NO data params are required._

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
    "DATE": "20130101",
    "TMAX": 34,
    "TMIN": 26
}`
 
* **Error Response:**

  _If the DATE is not present there will be an error response from API._
  
  * **Code:** 404 <br />
    **Content:** `Bad Request - Date doesn't exist`

* **Sample Call:**

  _Use Postman Software or Chrome Extension to send GET request using the end point URL._
  
  
  
 _Web Service End Point 3_
  
* **URL**

  <http://gurramlearninglabs.com:8000/weather/historical/>

* **Method:**
  
  _The request type_

  `POST`
  
*  **URL Params**

   **Required:**
   
   `N/A`_ 

   **Optional:**
 
   `N/A`

* **Data Params**

  `{
    "DATE":"20180306",
    "TMAX":"25.0",
    "TMIN":"18.0"
   }`


* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{    
    "DATE": "20180306"
    }`
 
* **Error Response:**

  _If there is mismatch with data types while inserting new DATE then there will be an error response from API._
  
  * **Code:** 404 <br />
    **Content:** `Bad Request`

* **Sample Call:**

  _Use Postman Software or Chrome Extension to send POST request using the end point URL._
  _In the body menu and using raw data option, paste the below DATE information to get valid response_
  
  `{
    "DATE":"20180306",
    "TMAX":"25.0",
    "TMIN":"18.0"
  }`
  
  
  
_Web Service End Point 4_
  
* **URL**

  <http://gurramlearninglabs.com:8000/weather/historical/>

* **Method:**
  
  _The request type_

  `DELETE`
  
*  **URL Params**

   **Required:**
   
   `DATE:[20130106]`

   **Optional:**
 
   `N/A`

* **Data Params**

  _DELETE Request and NO data params are required._

* **Success Response:**

  * **Code:** 204 <br />
    **Content:** `No Content`
 
* **Error Response:**

  _If the DATE is not present there will be an error response from API._
  
  * **Code:** 404 <br />
    **Content:** `Bad Request - Date doesn't exist`

* **Sample Call:**

  _Use Postman Software or Chrome Extension to send GET request using the end point URL._
  
  
  
  _Web Service End Point 5_
  
* **URL**

  <http://gurramlearninglabs.com:8000/weather/forecast/>

* **Method:**
  
  _The request type_

  `GET`
  
*  **URL Params**

   **Required:**
   
   `DATE:[20130505]`

   **Optional:**
 
   `N/A`

* **Data Params**

  _GET Request and NO data params are required._

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ` [
    {
        "DATE": "20180506",
        "TMAX": 22,
        "TMIN": 16
    },
    {
        "DATE": "20180507",
        "TMAX": 23,
        "TMIN": 8
    },
    {
        "DATE": "20180508",
        "TMAX": 24,
        "TMIN": 5.333333333333333
    },
    {
        "DATE": "20180509",
        "TMAX": 25,
        "TMIN": 4
    },
    {
        "DATE": "20180510",
        "TMAX": 17,
        "TMIN": 3.2
    },
    {
        "DATE": "20180511",
        "TMAX": 18,
        "TMIN": 3.6666666666666665
    },
    {
        "DATE": "20180512",
        "TMAX": 19,
        "TMIN": 4.285714285714286
    }
]`
 
* **Error Response:**
  `N/A`

* **Sample Call:**

  _Use Postman Software or Chrome Extension to send GET request using the end point URL._
  
  
  
  
  
  
  
  


