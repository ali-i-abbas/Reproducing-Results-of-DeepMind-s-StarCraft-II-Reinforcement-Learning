# Effect of Feature Map Resolution on Reproducing Results of DeepMind’s StarCraft II Reinforcement Learning

Google’s DeepMind was hugely successful in applying
Reinforcement Learning (RL) techniques to solve Go and Atari
games, but StarCraft remained an open challenge due to its vast
action and state spaces with imperfect information. However,
DeepMind made some progress on StarCraft with their paper
“Starcraft II: A new challenge for reinforcement learning”, using
Asynchronous Advantage Actor Critic (A3C) RL. I reproduced
some of the results of DeepMind using a lower feature map
resolution of 32*32 pixels, using Reaver, a modular deep RL open
source framework, which uses Advantage Actor Critic (A2C) RL.
I compared my results with Reaver’s results which was obtained
by using 16*16 pixels feature map resolutions and DeepMind’s
results which was obtained with 64*64 pixels feature map
resolutions. I was able to get similar results to Reaver in most
cases and similar results to DeepMind in a few cases. I found that
the effect of increasing resolution was to make the algorithms
more sample efficient but generally did not lead to better results.


