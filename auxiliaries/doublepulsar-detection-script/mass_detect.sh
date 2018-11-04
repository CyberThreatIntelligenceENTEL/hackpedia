#!/bin/bash

echo "----"
echo "Bash script to detect 445 and 3389 ports Open. Uses masscan"
echo "It will create two files, smb.lst and rdp.lst"
echo "----"
echo ""
echo "Network segment/netmask (ie: 192.168.0.0/24): "
read network_segment

# Scan open ports
masscan -p445 $network_segment > smb.lst
masscan -p3389 $network_segment > rdp.lst

# Clean output
sed -i "s/^.* on //" smb.lst
sed -i "s/^.* on //" rdp.lst
