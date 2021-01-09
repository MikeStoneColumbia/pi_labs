echo "******** System Info ********"
echo
echo "Current Raspberry Pi Version: "
cat /proc/version | grep "Linux"

echo "Current Directory:"
pwd
echo
echo "IP address: "
hostname -I
echo
echo "Disk Usage:"
df -h --total
echo
echo "Memory:"
cat /proc/meminfo | grep "MemTotal"
cat /proc/meminfo | grep "MemFree"
echo
echo "CPU Temp:"
vcgencmd measure_temp
echo
echo "******** End ***************"
