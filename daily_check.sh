#!/bin/bash

# Get today's date
today=$(date +\%Y-\%m-\%d)

# Create a backup folder for today's date if it doesn't exist
mkdir -p "Backup/$today"

# Define the site suffixes (you can modify this array daily)
Site_suffix=("uno" "sale" "legal" "re" "com" "pm" "app" "bike" "tel")  # Add more suffixes if needed

# Loop over each site suffix
for suffix in "${Site_suffix[@]}"; do
    # Ping output
    ping -c 4 "www.1tamilmv.$suffix" | tee "Backup/$today/ping_output_${suffix}_$today.txt"
    
    # Nslookup output
    nslookup "www.1tamilmv.$suffix" | tee "Backup/$today/nslookup_output_${suffix}_$today.txt"
    
    # Nmap output
    nmap -v -A "www.1tamilmv.$suffix" | tee "Backup/$today/nmap_output_${suffix}_$today.txt"
done

echo "Daily check complete. Outputs stored in the Backup/$today folder."

