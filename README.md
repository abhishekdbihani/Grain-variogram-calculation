# Grain variogram calculation

Investigation of correlated spatial heterogeneity is important for reservoir characterization in the petroleum industry. To examine if there are spatial correlations between the different spherical grain sizes in a grain pack (Figure 1) and the distances between them, we can construct variograms for measuring the spatial distribution of grain volume. The inputs for the code are the co-ordinates of all the spherical grains and their radii (refer.csv file), and the output is a variogram. 

<img src="https://github.com/abhishekdbihani/Grain-variogram-calculation/blob/master/imgs/bidisperse%20grain%20pack1.png" align="middle" width="400" height="400" alt="bidisperse grain pack">
 
Figure 1- Grain pack of two different sized spheres

The variogram (γ) for the lag distance H is defined as,

<img src="https://github.com/abhishekdbihani/Grain-variogram-calculation/blob/master/imgs/eq1.PNG" align="middle" width="300" height="50" alt="eq1">			(1)

where N(H) is the number of possible pairs of data for lag H, and z(u) is the stationary function corresponding to the grain volume (Pyrcz and Deutsch, 2014). The lag distance is the distance between data pairs for which the variogram is calculated. It is selected in order to get the maximum data in each lag and usually coincides with the data spacing. The minimum lag distance was considered 0.1 for all simulations. The stationary function grain volume (V) calculated by equation (2) where r is grain radius, is the scalar variable associated with a location u and was used to calculate the variogram, 

<img src="https://github.com/abhishekdbihani/Grain-variogram-calculation/blob/master/imgs/eq2.PNG" align="middle" width="150" height="50" alt="bidisperse grain pack">						(2)

The variograms were normalized with respect to the variance (var) given in equation (3), where n are the total number of grains and z(avg) is the average grain volume,

<img src="https://github.com/abhishekdbihani/Grain-variogram-calculation/blob/master/imgs/eq3.PNG" align="middle" width="250" height="50" alt="bidisperse grain pack">	 (3)

# Example: 
A sample input to test the code has been provided (test1.csv). It is a grain pack of 2663 spheres, out of which 5 are large (r=0.5 unit) and 2658 are small (r=0.1 unit). The length of the grain-pack is 3 in all directions. 
An example of the expected output of the code is given in Figure 2. 

<img src="https://github.com/abhishekdbihani/Grain-variogram-calculation/blob/master/imgs/expected%20code%20output.PNG" align="middle" width="600" height="400" alt="expected code output">

Figure 2- Expected code output: Variogram of the grain pack

The blue line represents the variogram and the red line represents the variance (sill) with a constant value of one. When the variogram is lower than the variance, there are positive correlations between the different grains and when the variogram is higher than the variance, there are negative correlations between the grains. Figure 2 shows that while there is a positive correlation at low distances, due to smaller grains in close proximity with each other, the variogram begins approaching the variance value which signifies random distribution. At distances near the sample length, due to fewer number of data points, some deviation from variance may be observed

# Contributors: 
Abhishek Bihani & Anurag Bihani

# References:
Pyrcz, M. J., & Deutsch, C. V. (2014). Geostatistical reservoir modeling. Oxford university press.

# Citation: 
If you use this workflow please cite as: [A. Bihani, H. Daigle (2019). On the Role of Spatially Correlated Heterogeneity in Determining Mudrock Sealing Capacity for CO2 Sequestration. Marine and Petroleum Geology, 106(106), 116–127.](https://www.sciencedirect.com/science/article/abs/pii/S0264817219301886)


