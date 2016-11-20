<h3>Project 2 Data Collection.</h3>

I have scraped together two datasets: <ul>
<li><a href="https://github.com/ekivolowitz/p2/blob/master/baseball_birthdays.txt">baseball_birthdays.txt</a> 1935 Baseball players.</li>
<li><a href="https://github.com/ekivolowitz/p2/blob/master/football_birthdays.txt">football_birthdays.txt</a> 4104 Football players.</li>
<li><a href="https://github.com/ekivolowitz/p2/blob/master/combined.txt">combined.txt</a> 6039 Football and Baseball players combined.</li> 
</ul>
<strong> Note the schema of all three files follows "Month/Day/Year".</strong>
Each of these files contain the birthday information on the entire population of athletes in the respective sports in no particular order.

<h3> Combining Data </h3>
For combining the populations, we should get the same answer from running an analysis on the combined data, or by manipulating the data individually and combining it. By this, I mean Xc = Xf + Xb where X means mean, and c,f,b mean combined, football, baseball. and S^2c = S^2f + S^2b.



<h3>Moving Forward</h3>
Either we take random samples from both populations and compare them individually, or we use both of the entire populations as our samples. My vote is for using the combined populations as we have access to the data and they are computational equivalent in code and price. The process of analyzing these would be a binomial hypothesis test where <ul><li>H0: proportion of athletes born in months 1-6 = proportion of athletes born in months 7-12.</li><li>HA: proportion of athletes born in months 1-6 != proportion of athletes born in months 7-12.</li></ul>
