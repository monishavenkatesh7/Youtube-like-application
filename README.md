# How to Deploy Streamlit app on EC2 instance

## 1. Login with your AWS console and launch an EC2 instance

## 2. Run the following commands

### Note: Do the port mapping to this port:- 8501

```bash
sudo apt update
```

```bash
sudo apt-get update
```

```bash
sudo apt upgrade -y
```

```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```

```bash
git clone https://github.com/monishavenkatesh7/ML-Capstone-project.git
```

```bash
cd ML-Capstone-project
```

```bash
sudo apt install python3-pip
```

```bash
pip3 install -r requirements.txt
```
Note: If the above one doesnt work
```bash
pip install -r requirements.txt --break-system-packages
```

#Temporary running
```bash
python3 -m streamlit run app.py
```

#Permanent running
```bash
nohup python3 -m streamlit run app.py
```

Note: Streamlit runs on this port: 8501

#For reloading the git
```bash
git pull origin main
```

#For Terminating the permanently running application
```bash
sudo pkill -f streamlit
```

