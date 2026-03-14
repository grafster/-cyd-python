mpremote cp ~/dev/ST77xx-pure-MP/st*.py :
esptool.py --baud 460800 write_flash 0x1000 ESP32_BOARD_NAME-DATE-VERSION.bin
apt install esptool thonny
sudo usermod -a -G dialout stwinnersh
