#!/bin/bash

echo "Deploying AI Pair Programming Tool to cloud..."

# Build the application
jac build ai_pair_programmer.jac

# Deploy as service
jac serve ai_pair_programmer.jac --port 8000 --host 0.0.0.0

echo "Deployment complete! API available at http://localhost:8000"