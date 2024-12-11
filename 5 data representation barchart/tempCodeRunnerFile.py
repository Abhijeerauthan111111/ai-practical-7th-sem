import numpy as np
import matplotlib.pyplot as plt
# Data for the bar chart
games = ['Pubg', 'Free Fire', 'Mine Craft', 'GTA-V']
ratings = [8.5, 7.8, 4.5, 9.7]

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(games, ratings)

# Customize the chart
plt.title('Mobile Games Ratings', fontsize=14)
plt.xlabel('Games', fontsize=12)
plt.ylabel('Ratings', fontsize=12)

# Add rating values on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}',
             ha='center', va='bottom')

# Set y-axis limit to make it look better
plt.ylim(0, 12)

# Display the chart
plt.show()