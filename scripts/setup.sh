#!/bin/bash

echo "Setting up AI Pair Programming Tool..."

# Install Jac language
pip install jaclang

# Install other dependencies
pip install -r requirements.txt

echo "Setup complete! Run with: jac run ai_pair_programmer.jac"