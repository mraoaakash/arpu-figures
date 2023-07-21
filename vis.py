import os 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


fish_name = 'M2'


pre = pd.read_csv(f'./data/{fish_name}_pre.csv')
try:
    post = pd.read_csv(f'./data/{fish_name}_post.csv')
except:
    print(f'No post-intervention data for this {fish_name} fish')
print(pre.head())

# Plotting the distribution of the data

plt.figure(figsize=(5,3), dpi=300)
plt.title(f'Pre-intervention for fish {fish_name}', fontsize=16, fontweight='bold')
# plt.title('Post-intervention for fish {fish_name}', fontsize=16, fontweight='bold')
plt.plot(pre['Time.1'], pre['Readings'], '-', color='blue', label='Pre-intervention')
plt.xticks(np.arange(0,120,10),rotation=90, fontsize=8)
plt.ylim(0, 10)
plt.xlabel('Time (per minute)', fontsize=12, fontweight='bold')
plt.ylabel('DO Readings (ppm)', fontsize=12, fontweight='bold')
plt.tight_layout()
# plt.show()
plt.savefig(f'./vis/{fish_name}_pre.png')
try:
    plt.figure(figsize=(5,3), dpi=300)
    plt.title(f'Post-intervention for fish {fish_name}', fontsize=16, fontweight='bold')
    # plt.title('Post-intervention for fish {fish_name}', fontsize=16, fontweight='bold')
    plt.plot(post['Time.1'], post['Readings'], '-', color='red', label='Post-intervention')
    plt.xticks(np.arange(0,120,10),rotation=90, fontsize=8)
    plt.ylim(0, 10)
    plt.xlabel('Time (per minute)', fontsize=12, fontweight='bold')
    plt.ylabel('DO Readings (ppm)', fontsize=12, fontweight='bold')
    plt.tight_layout()
    # plt.show()
    plt.savefig(f'./vis/{fish_name}_post.png')
except:
    print(f'No post-intervention data for this {fish_name} fish')

plt.figure(figsize=(5,3), dpi=300)
plt.title(f'Pre/Post-intervention for fish {fish_name}', fontsize=16, fontweight='bold')
# plt.title('Post-intervention for fish {fish_name}', fontsize=16, fontweight='bold')
plt.plot(pre['Time.1'], pre['Readings'], '-', color='blue', label='Pre-intervention')
plt.xticks(np.arange(0,120,10),rotation=90, fontsize=8)
plt.ylim(0, 10)
plt.xlabel('Time (per minute)', fontsize=12, fontweight='bold')
plt.ylabel('DO Readings (ppm)', fontsize=12, fontweight='bold')
try:
    plt.plot(post['Time.1'], post['Readings'], '-', color='red', label='Post-intervention')
except:
    print(f'No post-intervention data for this {fish_name} fish')
plt.legend(loc='upper right', fontsize=8)

plt.tight_layout()
# plt.show()
plt.savefig(f'./vis/{fish_name}.png')