# Weather app
Knowing the weather of outside is a good idea. But what about the weather inside your home?. It is always good to know that what is the difference between the temperature of outside and inside and as well as humidity. So that we can be ready for the change in weather as soon as we step out of the home. At home, our body gets comfortable according to home temperature and humidity, but with knowing the difference, we can always prepare.
I did a small project in that direction where we are getting the temperature and humidity data of your zip code from open weather API and temperature and humidity data of your home from a DHT11 sensor using Arduino and understanding that in python using pyserial library. This project is a very minimal step, which has a lot of extensions. One such example is notifying the user when the difference between indoor and outdoor conditions is significant so that user can prepare. 
* Open weather is API is used to get the temperature and humidity of outside by providing zip code of your area.
* DHT11 sensor is used to get the inside temperature an humidity data.
* Flask has been used for the environment.
# App working 
* First of all user is asked to provide the zip code of the relevant area.
   ![](weather%20app/images/index.png)
   
* Than we render user to result  page, which shows the weather condition for outside and home
  
  ![](weather%20app/images/tempraturepng.png)

# Notes
* We are using US zip codes only, to use other country's zip codes please refer to the official documentation of open weather.
* temperature is provided in Celsius.

:copyright: Birender Veer Singh
