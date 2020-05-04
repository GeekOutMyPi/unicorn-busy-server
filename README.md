# Status Light Indicator
Raspberry Pi with Pimoroni Unicorn Hat that changes color to indicate your status. NOTE: This is a SOLDERING project! I do not recommend this project for someone without prior soldering experience.

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

# Tools
- Solder Iron
- Solder
- Solder Holder

# Prerequisites
1. Soldering Skills
2. Raspbian OS Setup on a microSD card - https://youtu.be/2Jfv9NO6J2Q
or Raspbian Lite on a Raspberry Pi Zero W

## Install

## Service

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

#Original Project - Microsoft Teams Status light - https://www.eliostruyf.com/diy-building-busy-light-show-microsoft-teams-presence/

![Available Status Teams](https://github.com/carolinedunn/unicorn-busy-server/blob/master/photos/teams-available-status.jpg)
![Busy Status Teams](https://github.com/carolinedunn/unicorn-busy-server/blob/master/photos/teams-busy-status.jpg)
