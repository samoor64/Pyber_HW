
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# File to Load (Remember to change these)
city_df = pd.read_csv("data/city_data.csv")
ride_df = pd.read_csv("data/ride_data.csv")

# Read the City and Ride Data

# Combine the data into a single dataset
cr_df = pd.merge(city_df, ride_df, how='outer', on='city' )
# Display the data table for preview

cr_df.head()

urban = cr_df[cr_df["type"] == "Urban"]

rural = cr_df[cr_df["type"] == "Rural"]

suburban = cr_df[cr_df["type"] == "Suburban"]
cr_df.head()



# In[4]:


city_type = cr_df.type.unique()
city_type


# In[5]:


group_type = cr_df.groupby(['type']).count()



# ## Bubble Plot of Ride Sharing Data

# In[6]:


#average fare per type
#type_group = cr_df.groupby(["type"]).mean()


#y-axis
y_urban = urban.groupby(["city"])["fare"].mean()
y_rural = rural.groupby(["city"])["fare"].mean()
y_suburban = suburban.groupby(["city"])["fare"].mean()

#x_axis
x_urban = urban.groupby(["city"])["fare"].count()
x_rural = rural.groupby(["city"])["fare"].count()
x_suburban = suburban.groupby(["city"])["fare"].count()


z_urban = urban.groupby(["city"])["driver_count"].mean()
z_rural = rural.groupby(["city"])["driver_count"].mean()
z_suburban = suburban.groupby(["city"])["driver_count"].mean()

#ride_id count
#grouping_count = cr_df.groupby('city').count()
#ride_count = grouping_count['ride_id']

#Average Fare and Rides per city
#ride_group = cr_df.groupby(["city"]).mean()

#avg_fare = ride_group['fare']

#avg_drive = ride_group['driver_count']


# In[7]:


# Obtain the x and y coordinates for each of the three city types
#x_axis = np.arange(len(ride_count))

#y_axis = np.arange(len(avg_drive))
#ticks = [value for value in x_axis] 

# Build the scatter plots for each city types


# Incorporate the other graph properties

urban_plt = plt.scatter(x_urban, y_urban, s=10*z_urban, marker="o", facecolors="blue", edgecolors="black", label="Urban")
rural_plt = plt.scatter(x_rural, y_rural, s=10*z_rural, marker="o", facecolors="red", edgecolors="black", label="Rural")
suburban_plt = plt.scatter(x_suburban, y_suburban, s=10*z_suburban, marker="o", facecolors="yellow", edgecolors="black", label="Suburban")

# Create a legend
plt.xlabel('Total Number of Rides (Per City)')
plt.ylabel('Average Fare($)')
plt.legend(title="City Types")
plt.grid(True)
# Incorporate a text label regarding circle size
plt.show()

# Save Figure


# In[6]:


# Obtain the x and y coordinates for each of the three city types

# Build the scatter plots for each city types

# Incorporate the other graph properties

# Create a legend

# Incorporate a text label regarding circle size

# Save Figure


# In[7]:


# Show plot
plt.show()


# ## Total Fares by City Type

# In[32]:


# Calculate Type Percents
num_fare = cr_df.groupby(['type']).sum()['fare']/cr_df['fare'].sum()

colors = ["yellow", "lightskyblue", "lightcoral"]
labels = ["Rural", "Suburban", "Urban"]
explode = (0, 0 ,.2)
# Build Pie Chart

# Save Figure
num_rides


# In[46]:


# Calculate Type Percents
plt.pie(num_fare, explode=explode,labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
# Build Pie Chart

# Save Figure
plt.title("Total Fares by City Type")


# In[10]:


# Show Figure
plt.show()


# ## Total Rides by City Type

# In[45]:


# Calculate Ride Percents
num_ride = cr_df.groupby(['type']).count()['ride_id']/cr_df['ride_id'].count()

# Build Pie Chart
plt.pie(num_ride, explode=explode,labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
# Save Figure
plt.title("Total Rides by City Type")


# In[12]:


# Show Figure
plt.show()


# ## Total Drivers by City Type

# In[44]:


# Calculate Driver Percents
num_drive = cr_df.groupby(['type']).sum()['driver_count']/cr_df['driver_count'].sum()

# Build Pie Charts
plt.pie(num_drive, explode=explode,labels=labels, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)
# Save Figure
plt.title("Drivers by City Type")


# In[14]:


# Show Figure
plt.show()

