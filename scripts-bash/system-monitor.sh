#!/bin/bash

echo "==Monitor=="
echo "Date: $(date)"
echo "CPU usage: $(top -bn1)"
echo "Memory: $(free -h)"
echo "Disk usage: $(df -h /)"
echo "Top five processes: $(ps aux --sort=-%cpu)"







