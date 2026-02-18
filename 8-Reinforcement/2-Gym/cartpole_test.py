import sys
import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np
import random

env = gym.make("CartPole-v1", render_mode="human")
print(env.action_space)
print(env.observation_space)
print(env.action_space.sample())

obs, info = env.reset()

for _ in range(500):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()

env.close()