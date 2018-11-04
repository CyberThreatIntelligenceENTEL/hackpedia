#!/bin/bash

# Args
if [ $# -eq 0 ] || [ $# -gt 1 ]; then
    echo ""
    echo "This scripts needs a file with network segments or IP list"
    echo " Usage: $0 example.lst"
    echo ""
    exit 1
fi

# Check Superuser
SUDO=''
if (( $EUID != 0 )); then
    SUDO='sudo'
fi

# File tracking
today=`date +%Y%m%d_%H%M%S`

# Start script
echo "--- Lets rumblee ---"
echo "Scanning $1"

# Scan for open ports
echo "~~~~~~~~~~ Running Masscan ~~~~~~~~~~~ "
$SUDO masscan -p445 -iL $1 > output/target_smb.lst

# Clean files
$SUDO sed -i "s/^.* on //" output/target_smb.lst

# nmap ms17-010 detection
echo "~~~~~~~~~~ Running NMAP ~~~~~~~~~~~ "
$SUDO nmap --script smb-vuln-ms17-010 --open -vv -p445 -oA output/nmap_$today -iL output/target_smb.lst

# Data parsing
echo "~~~~~~~~~~ Parsing Files ~~~~~~~~~~~ "
$SUDO python parse_files.py output/nmap_$today.xml

# Clean tempfiles
$SUDO rm output/target_smb.lst
echo "--- I'm done ---"
