Signup Flow Automation 🚀

This project automates the entire signup flow  for the Authorized Partner Portal
 using Selenium WebDriver.

📌 Prerequisites

Before running the script, make sure you have the following installed:

Python 3.9+

Google Chrome or Mozilla Firefox browser

WebDriver (compatible with your browser version)

ChromeDriver
 (for Chrome)

GeckoDriver
 (for Firefox)

pip (Python package manager)

⚙️ Environment Setup

Clone this repository or download the script.

Create and activate a virtual environment (recommended):

python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


requirements.txt example:

selenium==4.24.0

▶️ How to Run the Script

Run the automation script with:

python signup_automation_script.py

🔐 OTP Entry

The script will pause and ask you to manually enter the 6-digit OTP received in your email:

Enter the 6-digit OTP received in your email:


Enter the code in the terminal and press Enter to continue.

🧪 Test Data Used

User Information

First Name: Bhupen

Last Name: Sen

Email: manorsen10@gmail.com

Phone: 9815684326

Password: Test@123

Agency Details

Agency Name: Test Agency

Role: Manager

Agency Email: testagency@example.com

Website: https://www.testagency.com

Address: Kathmandu, Nepal

Country: Nepal

Experience: 1 year

Number of Students: 50

Focus Area: Undergraduate admissions to Canada

Success Metrics: 90%

Registration Number: REG-12345

Preferred Country: UK

Certification: ICEF Certified Education Agent

File Upload: Sample PNG/JPG fil
