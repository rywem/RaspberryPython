import subprocess
import datetime

def take_picture():
    # Generate a filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"/home/rypi/Pictures/pic_{timestamp}.jpg"
    
    # Run raspistill to capture the image
    try:
        subprocess.run(["raspistill", "-o", filename], check=True)
        print(f"Picture saved as {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to take picture: {e}")

if __name__ == "__main__":
    take_picture()
