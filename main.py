import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print ('start')
sphere_pack_length = 4


input_file = pd.read_csv("test.csv")

print ('calculating sphere volume')
sphere_count_df = input_file.groupby('d').count()
small_sphere_d, big_sphere_d = sphere_count_df.index 

small_sphere_count, big_sphere_count = sphere_count_df.iat[0, 0], sphere_count_df.iat[1, 0]
total_sphere_count = small_sphere_count + big_sphere_count

small_sphere_r = small_sphere_d/2
big_sphere_r = big_sphere_d/2

small_sphere_volume = small_sphere_count*4/3*np.pi*math.pow(small_sphere_r,3)
big_sphere_volume = big_sphere_count*4/3*np.pi*math.pow(big_sphere_r,3)
average_sphere_volume = ( small_sphere_count*small_sphere_volume + big_sphere_count*big_sphere_volume ) / total_sphere_count


sphere_volume_diff_sum = np.zeros(18*sphere_pack_length)
sphere_volume = np.zeros(total_sphere_count)
frequency = np.zeros(18*sphere_pack_length)
gamma = np.zeros(18*sphere_pack_length)
distance = np.zeros(18*sphere_pack_length)
sphere_variance_line = np.ones(18*sphere_pack_length)

print ('calculating sphere distances and volume differences')

for i in range(0,total_sphere_count):
    x_i = input_file.iat[i, 0]
    y_i = input_file.iat[i, 1]
    z_i = input_file.iat[i, 2]
    r_i = input_file.iat[i, 3]
    sphere_i_volume = 4/3*np.pi*math.pow(r_i,3)

    
    sphere_volume[i]=sphere_i_volume

    for j in range(i+1,total_sphere_count):
        x_j = input_file.iat[j, 0]
        y_j = input_file.iat[j, 1]
        z_j = input_file.iat[j, 2]
        r_j = input_file.iat[j, 3]
        sphere_j_volume = 4/3*np.pi*math.pow(r_j,3)
       
        sphere_distance = math.sqrt(math.pow((x_i - x_j), 2) + math.pow((y_i - y_j), 2) +math.pow((z_i - z_j), 2))
        sphere_volume_diff = math.pow((sphere_i_volume - sphere_j_volume), 2)

        for k in range(0,18*sphere_pack_length):
            if (sphere_distance < (k*0.2) ) and (sphere_distance > ( (k*0.2) - 0.2)):
                sphere_volume_diff_sum[k] += sphere_volume_diff
                frequency[k] += 1
                break


sphere_variance = np.var(sphere_volume)


# print(sphere_variance)

print ('calculating sphere pack variogram')

for k in range(0,18*sphere_pack_length):    
    if sphere_volume_diff_sum [k] > 0:
        gamma[k] = sphere_volume_diff_sum[k]/(2*frequency[k]*sphere_variance)
        distance[k] = k/10

print ('plotting sphere pack variogram')

plt.plot(distance, gamma, distance, sphere_variance_line, label='Variogram')
plt.xlabel("Distance", fontsize=16)
plt.ylabel("Gamma", fontsize=16)
plt.ylim([0,1.5])
plt.xlim([0,4])
plt.title('Grain Volume Variogram', fontsize=19)
plt.show()
