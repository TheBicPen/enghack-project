
#assume debian w/ aptitude
sudo apt install python
sudo apt install python3
sudo apt install python-pip
# sudo apt install python3-pip

# pip install -r requirements.txt
# pip3 install -r requirements.txt
# pip install opencv-python
pip install python-opencv
pip install google-cloud
pip install google-cloud-vision
# pip install google-cloud-language
# pip3 install ffmpeg

sudo apt install python-opencv
sudo apt install python3-opencv

export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/credentials/creds.json"
echo "$(printenv | grep 'GOOGLE_APPLICATION_CREDENTIALS')"