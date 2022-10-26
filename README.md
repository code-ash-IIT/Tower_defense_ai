Tower-Defense-AI
=============

A fresh take on the classic tower defense game and AI to play it. Made in Python. 
The game contains 2 modes:
1. Manual
2. AI mode (genetic Algorithm mode)

Player can choose to use the game in any of given modes.
```bash
Implemented Genetic Algorithm from scratch whose performance matches human level performance.
```

Alternative RL Algorithms
-------------------

Model-Free RL
1. <a href="https://arxiv.org/abs/1602.01783#" target="_blank">Asynchronous Advantage Actor-Critic (A2C/A3C)</a>
2. <a href="https://arxiv.org/abs/1707.06347" target="_blank">Proximal Policy Optimization (PPO)</a>
3. <a href="https://arxiv.org/abs/1502.05477" target="_blank">Trust Region Policy Optimization (TRPO)</a>
4. <a href="https://arxiv.org/abs/1509.02971" target="_blank">Deep Deterministic Policy Gradient (DDPG)</a>
5. <a href="https://arxiv.org/abs/1802.09477" target="_blank">Twin Delayed DDPG (TD3)</a>
6. <a href="https://arxiv.org/abs/1801.01290" target="_blank">Soft Actor-Critic (SAC)</a>
7. <a href="https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf" target="_blank">Deep Q-Networks (DQN)</a>
8. <a href="https://arxiv.org/abs/1707.06887" target="_blank">Categorical 51-Atom DQN (C51)</a>
9. <a href="https://arxiv.org/abs/1710.10044" target="_blank">Quantile Regression DQN (QR-DQN)</a>
10. <a href="https://arxiv.org/abs/1707.06887" target="_blank">Hindsight Experience Replay (HER)</a>

Model-Baded RL
1. <a href="https://arxiv.org/abs/1707.06887" target="_blank">World Models </a>
2. <a href="https://arxiv.org/abs/1707.06887" target="_blank">Imagination-Augmented Agents (I2A)</a>
3. <a href="https://arxiv.org/abs/1707.06887" target="_blank">Model-Based RL with Model-Free Fine-Tuning (MBMF)</a>
4. <a href="https://arxiv.org/abs/1707.06887" target="_blank">Model-Based Value Expansion (MBVE)</a>
5. <a href="https://arxiv.org/abs/1707.06887" target="_blank">AlphaZero</a>


Usage
-----

The objective of the game is to stop enemy from crossing a map by building towers that slow them down and eventually destroy them. Players must manage their money and strategically place towers on the map to stop waves of enemy creeps that gain health and speed as the game progresses. Towers have varying characteristics such as dealing splash damage and slowing down creeps within a certain radius. The interface is largely intuitive as shown below

<p align="center">
  <img src="/Images/gif.gif" alt="gameplay" />
</p>

Installation
------------

Clone the git repo into a local directory and run on the desktop
```bash
$ git clone git@github.com:code-ash-IIT/Tower_defense_ai.git localDir/
$ cd localDir/code
$ python main.py
```

Shots from Gameplay
-------------------

<p align="center">
<img src="/Images/1.png">
</p>
<p align="center">
<img src="/Images/2.png">
</p>
<p align="center">
<img src="/Images/3ai.png">
</p>


 
