# server-allocator
Module to optimize server allocation 

Python 2.7

<h3>Usage:</h3>
<code>import allocator</code></br>
<b>For scenario where min no of cpus, max amount given.</b></br>
<code>allocator.get_costs(instances,hours,cpus,price)</code></br></br>

<b>For scenario where max no of servers for a given amount is to be calculated</b></br>
<code>allocator.get_costs(instances,hours,<em>None</em>,price)</code></br></br>

<b>For scenario where min no of cpus is to be calculated at the most profitable rate</b></br>
<code>allocator.get_costs(instances,hours,price)</code>
