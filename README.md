# AWS DeepRacer Autonomous Racing (PolyU)
A reinforcement learning (RL) project to train an AWS DeepRacer model for autonomous track navigation, developed to showcase machine learning skills for AeU’s BICT application, leveraging my PolyU Mechanical Engineering background.

## Purpose
Simulates autonomous vehicle control, applying RL to optimize lap times on a virtual track. Connects mechanical engineering (vehicle dynamics) with BICT’s data science modules for AI-resistant roles like data analyst.

## Features
- Trains an RL model using AWS DeepRacer’s 3D simulator.
- Custom reward function to prioritize track adherence, speed, and centering.
- Evaluates model performance (lap time, resets).
- Cloud-based training with AWS SageMaker/RoboMaker.

## Setup
1. Create an AWS account (free tier).
2. Access AWS DeepRacer Console.
3. Use `reward_function.py` in the console.
4. Train and evaluate on “re:Invent 2018” track.

## Files
- `reward_function.py`: RL reward function.
- `hyperparameters.json`: Training configuration (optional).
- `evaluation_results.txt`: Lap times and metrics (manual).

## Results
- Lap Time: [e.g., 15.5 seconds]
- Resets: [e.g., 1]
- Training Time: ~30 minutes

## Skills Demonstrated
- Reinforcement Learning (AWS DeepRacer, PPO)
- Python programming
- Cloud computing (AWS)
- Vehicle dynamics analysis
- Data analysis (model evaluation)