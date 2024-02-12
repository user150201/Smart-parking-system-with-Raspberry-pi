# Smart Car Parking System with Image Processing and Artificial Intelligence
## This Project is Built with just Using a Raspberry pi 4b and a 720p web camera with a Adminitration control panel using a website.
Inorder to run the project the Programmes shold be excecuted in order
1. loops_draw.py needs to be run repeatedly upto total number of parking lot by changing the file name in the file on line number 33 and 35.Each time while running the file draw the regoin of intrest for each of the parking slots indepentendly. A series of text files will be formed. These represents the coordinates the parking slots.
2. Run the program loops.py to obtain a surveilence of the whole whole footage with diffent slots labellled each other. Detection of car parked at each slot can be tested here.
3. Run the park_app1.py to deploy a website at localhost which will provide the real time monitoring of parking slot with calculated parking time and parking fee.
