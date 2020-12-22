<h1>My Hiking Buddy ReadMe</h1>
[![microbit rotunda](ETR107_Projects/Final_Project/hikingbuddy.jpg)]
<br>
<strong>Features:</strong>
<ul>
  <li>Pedometer</li>
  <li>Temp Tracker</li>
  <li>Humitiy Tracker</li>
</ul>
<p>With Covid Times upon us, I have been  doing a lot more hiking and walking (away from other humans of course). I thought it would be a great idea for my project to be a tracker of these walks and hikes. My ideas in the first place were very ambitious, and perhaps a bit too far above my skill level of combining coding and electronics. It was fun to attempt regardless.</p>
  
<p>Originally, I wanted to store multiple data using various sensors on the Microbit, as well as using an AM2320. The goal was to record temperature and humidity using the AM2320, and to record direction and steps using the Microbit sensors. Upon being connected to a computer (my first idea was to use BlueTooth) the Microbit would write a file containing all the data to the computer to be saved. One part of the data was intended to be a dictionary. The idea for that was to have the key be a number of 0 though 3. 0 would mean North, 1 would mean West, 2 South, and 3 East. The code would use the compass, record the steps in a direction, and add it to the dictionary when the compass read a new direction. These dictionary entries would then be taken and used to map out the hike using turtles.</p>

<p>
