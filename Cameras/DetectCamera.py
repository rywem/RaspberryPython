import os

def check_camera_devices():
    devices = []
    for i in range(0, 10): #check for /dev/video0-9
        dev = f"/dev/video{i}"
        if os.path.exists(dev):
           devices.append(dev)
           
    if devices:
        print("Found video devices: ", devices)
    else:
        print("no devices found")
        
if __name__ == "__main__":
    check_camera_devices()