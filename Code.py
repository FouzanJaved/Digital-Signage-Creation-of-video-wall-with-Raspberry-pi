# Video wall Raspberry pi codes

# 1 First visit piwall uk website and in installation there are two files pwomxplayer and pwlibs. 

omxplayer /home/pi/Desktop/hugo.mp4
# This will run the video on screen.

pwomxplayer --tile--code=42 /home/pi/Desktop/hugo.mp4
# This will run the tile of video 42 shows total 4 video screens and this will show 2 means top right. 

# 4. On raspberry pi run this         
pwomxplayer --tile-code=$n udp://239.0.1.23:1234?buffer_size=1200000B" 
#(where $n=41 is the top left, 42 is the top right, 43 is the bottom left and 44 is the bottom right for a 4 screen PiWall).

# 5. On server side run this on ubuntu  
ffmpeg -re -i /home/fouzan/Desktop/1.mp4 -vcodec copy -f avi -an udp://239.0.1.23:1234

# Must remember that wifi should be on in this case and both on same network and complete video will be shown on raspberry pi.

# Network configurations for ethernet and ethernet switch:-



# For ubuntu Server:- ----------------------------

sudo ifconfig eth0 192.168.0.??? netmask 255.255.255.0 up
# If this is not working then you have to write " ifconfig -a "
# and in start ethernet name will be change mine is eno1
# So we have to write sudo ifconfig eno1 192.168.0.100 netmask 255.255.255.0 up

sudo route add -net 224.0.0.0 netmask 240.0.0.0 eno1



# In assigning raspberry pi static ip it was giving issue. So in file dhcp.conf I have put “auto eth0”.
# This helps in running the video on wire LAN on the raspberry pi.
# But this is testing the wire network on raspberry pi and ubuntu. 



Making configuration file :-


# 1 Write.   
sudo nano /home/pi/.pitile

# For first pi write
[tile]
id=pi1

# This .pitile will be changed for each pi forexample if we attach second pi to screen we will have to write
[tile]
id=pi2

# And .piwall file remain same for each pi. And we have to write .pitile and .piwall file for each pi.

# First write the piwall file written below and then do this.
# To access these we have to write 
pwomxplayer --config=4bez /home/pi/Desktop/hugo.mp4

2 Write.   
sudo nano /home/pi/.piwall
# wall definition for 2x2 screens with bezel compensation

[4bez_wall]
width=1067
height=613
x=0
y=0

 

# corresponding tile definitions

[4bez_1]
wall=4bez_wall
width=522
height=293
x=0
y=0
 

[4bez_2]

wall=4bez_wall
width=522
height=293
x=545
y=0

 

[4bez_3]

wall=4bez_wall
width=522
height=293
x=0
y=320

 

[4bez_4]

wall=4bez_wall
width=522
height=293
x=545
y=320

 
# config

[4bez]

pi1=4bez_1
pi2=4bez_2
pi3=4bez_3
pi4=4bez_4


#Master ubuntu looping video forever command
ffmpeg -stream_loop -1 -re -i /home/fouzan/Desktop/tcl.mp4 -vcodec copy -f avi -an udp://239.0.1.23:1234


# To access video wall from server.
# In client pi we will write:-

pwomxplayer --config=4bez udp://239.0.1.23:1234?buffer_size=1200000B
