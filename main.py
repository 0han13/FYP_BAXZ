#!/usr/bin/env python3
"""
SILRAD — Feature Interaction Analysis of Sysmon Event Values for Early
Ransomware Detection Using Deep Reinforcement Learning.

Run the full reproducible pipeline:

    python main.py

Fast smoke test (smaller data + fewer DRL steps):

    python main.py --max-rows 8000 --drl-timesteps 5000 --dl-epochs 2
"""

from src.pipeline import main

if __name__ == "__main__":
    main()
