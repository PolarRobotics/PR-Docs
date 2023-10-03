# Router Setup
To begin using the data acquisition script, we need to setup our NETGEAR router in order to SSH into the Raspberry Pi.

1. Make sure the NETGEAR router is plugged in and the "2.4GHz" light is on. Using a laptop, connect to the NETGEAR router using WiFi:
	![[data-aq-wifi.png]]
	*(Example of WiFi list on Garuda Linux, this may differ with your system)*

2. Using a web browser, type "192.168.1.1" into your URL bar:

	![[data-aq-url-bar.png]]
	
3. If prompted for username and password, enter the following:
```
Username: admin
Password: password
```

4. Click "LAN Setup" on the left and you will find yourself here:
	![[data-aq-lan-setup.png]]
	
5. Under address reservation, click "Add". You will find a list of the currently connected devices to the router. Find your device from the list and copy the corresponding information:

	![[data-aq-address-reservation.png]]
	
6. Return to the "LAN Setup" menu and click "Apply". 
	![[data-aq-lan-setup-apply.png]]
	
7. We have now successfully reserved the IP address for your computer, and it will always maintain the same local IPv4 address, making it much easier to connect with. Repeat this process if the Raspberry Pi you want to connect to is not listed under "Address Reservation."
# Raspberry Pi SSH
In order to run our data acquisition script, we will use a handy Pi Zero as it is tiny and can fit into the robot while it is driving, and a laptop does not have this "being small" functionality.

1. Plug in the Raspberry Pi Zero and ensure the green light is on. At the time of writing, the only Pi Zero available is 'zerozero'. This may differ in the future, there should be a label on your Pi telling you the name of it. It will follow the naming scheme of 'zerozero', 'zeroone', 'zerotwo', etc. 
	![[data-aq-pi-front.png]]![[data-aq-pi-label.png]]
	
2. Download and install PuTTy, the most common SSH client: https://putty.org/

3. Open PuTTy. Refer to the "Address Reservation" list from Router Setup for the IP address of the Pi you want to connect to, and enter it into the "Host Name (or IP Address)" box.

	![[data-aq-putty.png]]
	*Pro Tip: you can save IP addresses and load them so you don't have to refer to the Address Reservation later!*

4. Click "Open". You will be sent to this screen: ![[data-aq-ssh-login.png]]
5. Enter the username after "login as: ". The username is the same name as the label and the one listed in Address Reservation. In our case, it will be 'zerozero'.![[data-aq-ssh-password.png]]
6. When prompted for the password, it should be on the back of your Pi. In our case, it will be 'rhysisfine69'. You will then be sent to the Linux terminal for the Pi Zero!
	 ![[data-aq-ssh-terminal.png]]
# Serial Monitor Script
Now we are going to acquire the script and get it into our home directory. 

1.  Using FileZilla or any other file transfer means, copy the most recent "SerialMonitor.py" script into the Pi's home directory.
	![[data-aq-list.png]]
2. Run the script using the following command:
```bash
python ./SerialMonitor.py
```

3. 