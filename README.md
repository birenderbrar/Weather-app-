# Weather app
Knowing weather of outside is good idea. but what about the weather of inside your home?. It is always good to know that what is the difference between temprature of outside and inside and as well as humidity. So that we can be ready for the change in weather as soon as we step out of home. At home our body gets comfortable according to home temprature and humidity but with knowing differnce we can always prepare.
I did a small project in that direction where we are getting temprature and humidity data of your zip code from open weather api and temorature and humidity data of your home from DHT11 sensor using arduino and getting that in python using pyserial library. This project is very minimal step, which has lot of extensions one such example is notfying user when diffrence between indoor and outdoor conditions is significant so that user can prepare. 
* Open weather is api is used to get the temprature and humidity of outside by providing zipcode of your area.
* DHT11 sensor is used to get the inside temprature an dhumidity data.
* Flask has been used for the environment.
# App working 
* First of all user is asked to provide the zipcode of the relevant area.
   ![](weather app/images/index.png)
   
* Than we render user to result page, which shows the weather condion for outside and home
  
  ![](weather app/images/temprature.png)

# Notes
* we are using us zip codes only, in order to use other counry's zip codes please refer to the offial documentationof open weather.
* temprature is provided in Celsuis.

:copyright:Birender Veeer Singh
