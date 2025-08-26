# Flask Age Prediction App 🧑‍💻

A simple **Flask web application** that predicts whether a person is an **Adult ✅** or a **Minor ❌** based on their age input.  
The app also has **Home, About, and Contact** pages for navigation.  

---

## 🔹 Features
- Age prediction (Adult vs Minor)
- Flask routing with multiple pages
- User input validation
- Hosted on **AWS EC2** using **MobaXterm**

---

## 🛠️ Tech Stack
- Python 3
- Flask
- Gunicorn
- AWS EC2
- MobaXterm (SSH client)

---

## ⚙️ Setup Instructions (Run Locally)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/Flask-Age-Prediction-App.git
cd Flask-Age-Prediction-App

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
python app.py


The app will start at:
👉 http://127.0.0.1:5000

☁️ Hosting on AWS (EC2) with MobaXterm
1️⃣ Launch an EC2 instance

Go to AWS Management Console

Choose Ubuntu / Amazon Linux AMI

Select t2.micro (Free Tier)

Allow HTTP (port 80) & Custom TCP (port 5000) in Security Group inbound rules

Download the .pem key

2️⃣ Connect to EC2 with MobaXterm

Open MobaXterm → Session → SSH

Enter Public IPv4 address of EC2

Use your .pem key for authentication

3️⃣ Install dependencies on EC2
sudo apt update
sudo apt install python3-pip -y
pip3 install -r requirements.txt

4️⃣ Clone and run the project
git clone https://github.com/yourusername/Flask-Age-Prediction-App.git
cd Flask-Age-Prediction-App
python3 app.py


or run with Gunicorn:

gunicorn -w 4 -b 0.0.0.0:5000 app:app

5️⃣ Access from browser

👉 Open http://<EC2-Public-IP>:5000
