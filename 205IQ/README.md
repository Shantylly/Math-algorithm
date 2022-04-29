# 205IQ

This algorithm is a new IQ test, which is supposed to be better suited to the current population than the classical tests from previous centuries.

This algorithm need to be calibrate and we are asked to provide the following tasks:

1. given u and s, plot the density function of the IQ for every integer between 0 and 200,
2. given u, s and one IQ value, print the percentage of people with an IQ inferior to this value,
3. given u, s and two IQ values, print the percentage of people with an IQ in between those values.

* USAGE
	- ./205IQ u s \[IQ1] \[IQ2]

* DESCRIPTION
	u	population  
	s	standard deviation  
	IQ1	minimum IQ  
	IQ2	maximum IQ  

## Bonus

To use the bonus you need the dependencies "gnuplot".
Open a command prompt and type :

>apt install gnuplot

Once it is installed, start the program and redirect the result in a file call "data" :

>./205IQ X Y > data

Then you just need to execute :

> cat drawer.gnu | gnuplot

And a new image.png is created with a graphical display of our results.