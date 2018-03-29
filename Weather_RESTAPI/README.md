Implemented REST API from weather information using the below end points. Please look for REST.md file for detailed description about REST APIs.

The root URL is "http://gurramlearninglabs.com:8000/weather" and data file is already migrated using sqllite.

Instructions:
Please use POSTMAN software or chrome extension for validating the service requests. The GET requests can also be validated using browser but for POST and DELETE requests, it requires software.

Sample POST request procedure:

1. Open POSTMAN software and paste the below url and select option "POST" in the drop down
http://gurramlearninglabs.com:8000/weather/historical/

2. Go to Body(Highlighted with Blue Dot) and paste the input data 
{
"DATE":"20180404",
"TMAX":"25.0",
"TMIN":"18.0"
}

3. Click Send and response will be shown at the botton of the screen.

4. For DELETE request, select DELETE option and paste the below url
http://gurramlearninglabs.com:8000/weather/historical/20180404


Note:
Also, I would like to inform you that validate_hw2.py execution is having inconsistent behavior and gets hung in the middle due to time out error. The screen shot explains the score for the assigment after successful execution

<img width="441" alt="aditya_assign2_output" src="https://github.uc.edu/storage/user/3795/files/b97bb50a-1c05-11e8-9972-d0750e04042d">





