Why: this agent is going to be main log source for our indexer in wazuh. 

I clicked "Deploy new agent" option in Wazuh Dashboard and there selected agent machine as Windows and server IP address as 192.168.100.88 which is IP adress of machine Wazuh server is deployed on. Additionally I set agent name "Windows" to new agent. Wazuh automatically created a powershell command for me to copy and paste to powershell on my Windows machine. Command is like this:
`Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.14.7-1.msi -OutFile $env:tmp\wazuh-agent; msiexec.exe /i $env:tmp\wazuh-agent /q WAZUH_MANAGER='192.168.100.88' WAZUH_AGENT_NAME='Windows'`
Which basically installs an exe and sets up our agent.

Then after installation finished I wrote this command:
`NET START Wazuh`
to powershell and it starts the agent and now our windows logs are being sent to our Ubuntu Wazuh server deployment.

![space]("/VirtualBox_Windows_01_08_2026_12_39_17.png")

But I also want to send sysmon logs to server. For this I set up sysmon like this.

From this link:
> https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

I downloaded Sysmon in a zip archive. 

I also need a sysmonconfig.xml file which is a configuration file for Sysmon applet. I installed Olaf Hartong's sysmonconfig.xml file which can be found on his github account. This is the standard choice for me. and It is more detailed for detection engineering
![space]("/VirtualBox_Windows_01_08_2026_12_50_39.png")
This is what I have in hand after also unzipping sysmon.zip and installing sysmonconfig.xml. 

In an elevated Powershell I ran this command for setting up Sysmon. And my sysmon is up and running. 
![space]("/VirtualBox_Windows_01_08_2026_12_54_04.png")
But currently the sysmon logs aren't sent to server. For this I need to edit C:\Program Files (x86)\ossec-agent\ossec.conf.

I add this config block under Log Analysis part of config file using elevated Notepad.
```
<localfile> 
	<location>Microsoft-Windows-Sysmon/Operational</location> <log_format>eventchannel</log_format> 
</localfile>
```
![space]("/VirtualBox_Windows_01_08_2026_12_59_48.png")

and then I restarted Wazuh agent service using this command:
`Restart-Service -Name wazuh`

Now as we can see I have an active wazuh agent and a wazuh server to investigate and analyze logs.
![space]("/Pasted image 20260801130446.png")

I also tested if the sysmon works correctly in Event Viewer snap-in. and it works correctly like in this picture 
![space]("/VirtualBox_Windows_01_08_2026_13_12_02.png")
Sysmon events are being generated and can be viewed at windows machine but we need all events to be shown in Wazuh not just alerts. By default most events are just being archived and not turns into alerts. For troubleshooting this we need to enable logall and logall_json flags in ossec.conf file and also enable /etc/filebeat/filebeat.yml archived option. after editing both files I restarted wazuh-manager service using `sudo systemctl restart wazuh-manager` command. 
I also restart filebeat service and check if it works and talks to server using 
```
sudo systemctl restart filebeat
sudo systemctl status filebeat
sudo filebeat test config
sudo filebeat test output
```
commands output is like this
![space]("/Pasted image 20260801134256.png")After this I still can't see wazuh-archives option in the Discover data selector menu. So I should create a wazuh index pattern in dashboard. 
I come to Dashboard Management-Index Patterns-Create Index Pattern and write down wazuh-archives-* in Index Pattern name text box and then select Next Step.
![space]("/Pasted image 20260801140407.png")
I select timefield as @timestamp and click Create index pattern
![space]("/Pasted image 20260801140506.png")
Now in Discover interface we have additional Index Pattern
![space]("/Pasted image 20260801140640.png")

Now we get all events and can filter through them using Opensearch Dashboard Query language(DQL)

![space]("/Pasted image 20260801143133.png")
