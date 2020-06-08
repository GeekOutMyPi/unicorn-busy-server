# Status Light Indicator
Raspberry Pi with Pimoroni Unicorn Hat that changes color to indicate your status. This is a simple status light indicator where I can change the color of the light from a browser window on my desktop. Place the Pi outside of your office to indicate to others if you are available, busy, or other. I have included green, red, yellow, blue, pink colors in this code. You can make a chart / key to indicate the status for each color. For example, blue could indicate a phone call and pink could indicate a video conference.

NOTE: This is a SOLDERING project! I do not recommend this project for someone without prior soldering experience.

![ProjectGIF](https://github.com/carolinedunn/unicorn-busy-server/blob/master/photos/ezgif.com-video-to-gif.gif)

# Materials
Materials:
- Raspberry Pi Zero with Headers - https://amzn.to/2NncxP4
  - or Raspberry Pi 3B, 3B+ (3A, or 4) - https://amzn.to/2O9SxiO
- MicroSD card - https://amzn.to/2Nq5AN9
- Motion Sensor - https://amzn.to/32OPMaA
- Keyboard/Mouse/Monitor
- Pimoroni Unicorn pHat - https://amzn.to/2Sz6mZe

Optional: Diffuser for Unicorn pHat. I printed one out using clear filament - https://www.thingiverse.com/thing:4335393

## Tools
- Solder Iron
- Solder
- Solder Holder

# Prerequisites
1. Soldering Skills
2. Raspbian OS Setup on a microSD card - https://youtu.be/2Jfv9NO6J2Q
or Raspbian Lite on a Raspberry Pi Zero W
3. Raspberry Pi setup with internet connectivity.
4. Other computer(s) that will update the status must be connected on the same network as your RPi.
5. Reserved IP address for your RPi. You will need to know the internal IP address for your Pi later in this tutorial.

# Hardware Assembly
- Assemble / Solder Unicorn pHat according to instructions - https://learn.pimoroni.com/tutorial/sandyj/soldering-phats
- If you are using a Raspberry Pi Zero W (without headers), you will need to solder on 40 GPIO pins / headers.
- Attach the unicorn pHat to your Raspberry Pi via GPIO headers.
- Power up your Pi.
- Open a Terminal on your Mac desktop and SSH into your Pi.
OR
- Windows https://www.chiark.greenend.org.uk/~sgtatham/putty/ and SSH into your Pi.
OR
- Connect a monitor, mouse, and keyboard to your RPi. 

## If you are using Raspberry Pi OS Lite (previously known as Raspbian Lite) run the following commands in the terminal
```
sudo apt-get update
sudo apt-get install python-pip
sudo apt-get install git
```
## Software Install command line 
```
git clone https://github.com/carolinedunn/unicorn-busy-server
cd unicorn-busy-server
chmod +x ./install.sh
sudo ./install.sh
sudo python3 server.py
```
## Test the service
- Go to your desktop / laptop computer and copy the file https://github.com/carolinedunn/unicorn-busy-server/blob/master/HTML/status.html to your local hard drive.
- Use Atom or any software editing tool to replace 0.0.0.0 with the IP address of your Raspberry Pi.
- Open your updated HTML file with your internet browser. I tested this on Chrome.
- Press the buttons to change the colors. If this works, move onto the next section to run on boot.

## Run on Boot
```
sudo cp busylight.service /etc/systemd/system/busylight.service
```

Testing the service:
```
sudo systemctl start busylight.service
sudo systemctl stop busylight.service
sudo systemctl status busylight.service
```

Enable/disable for startup:
```
sudo systemctl enable busylight.service
sudo systemctl disable busylight.service
```

# Original Project
Microsoft Teams Status light - https://www.eliostruyf.com/diy-building-busy-light-show-microsoft-teams-presence/

![Available Status Teams](https://github.com/carolinedunn/unicorn-busy-server/blob/master/photos/teams-available-status.jpg)
![Busy Status Teams](https://github.com/carolinedunn/unicorn-busy-server/blob/master/photos/teams-busy-status.jpg)
