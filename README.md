# Experimentation load simulator

This tool simulates flag evaluations for the purposes of running an experiment in LaunchDarkly. Work in progress.

To use:

1. Install dependencies

2. Copy the contents of `.env.example` to a file called `.env`. Fill in the new file with your SDK key.

3. Modify values in the `helpers/claim.py` file to affect randomness of the simulation
