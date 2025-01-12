# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:27:02 2025

@author: mahyar
"""

import numpy as np
import matplotlib.pyplot as plt

def is_prime(num):
    prime = False
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                break
        else:
            prime = True
    else:
        pass
    return prime
nums = 50000
prime_nums = [i for i in range(nums) if is_prime(i)]

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(prime_nums, prime_nums, color='k', s=0.1)
ax.grid(False)
plt.savefig(f"Prime_Polar_{nums}_num.png", bbox_inches = 'tight', dpi=300)
plt.show()