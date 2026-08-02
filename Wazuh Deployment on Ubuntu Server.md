# Wazuh Deployment on Ubuntu Server

1. I first installed the Ubuntu Server ISO and then set up a virtual machine in Oracle VirtualBox.
2. Username: jesus
3. Passcode: liebling

I set up the machine in unattended mode for fast results. It didn't install additional packages like `openssh-server` and `net-tools`, which are needed for the lab, so I installed them using:

```bash
sudo apt install openssh-server net-tools -y
```

I then created an SSH session from my main device to make the lab feel like it ran in the cloud. This also made it easy to copy clipboard content without needing the VirtualBox Guest Additions.

## After creating SSH session

![space](Images/Pasted%20image%2020260801112957.png)

Next I visited the Wazuh SIEM/EDR website and copied the one-liner installer that deploys Wazuh components (server, indexer, dashboard) on a single machine. I downloaded that script using `curl` and executed it.

Then I executed:

```bash
sudo ./wazuh-install.sh -a
```

The `-a` flag stands for "all-in-one".

After waiting 15–30 minutes the installation of Wazuh components finished and we received the dashboard access password shown here:

![space](Images/Pasted%20image%2020260801115550.png)

I used the same IP address I used for SSH and port `443` to access the dashboard in a browser:

![space](Images/Pasted%20image%2020260801115809.png)

After entering the credentials on the dashboard login page I gained access to the default dashboard.

