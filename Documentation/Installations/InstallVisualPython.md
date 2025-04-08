Install Visual Python


pip3 install vpython --break-system-packages

### Option 1: System-wide install
```
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install vpython --break-system-packages
```
### Option 2: Virtual Environment
```
sudo apt install python3-venv -y
python3 -m venv vpython-env
source vpython-env/bin/activate
pip install vpython
```
