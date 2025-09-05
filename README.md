



# Python Automation Projects

An automation suite built with Python that delivers **real-time stock market notifications** and **daily weather/rain alerts** directly to your phone using **Twilio SMS integration**.

This project is designed to demonstrate how different APIs can be combined for **useful, real-world automation**.

---

## 🚀 Features

* 📈 **Stock Market Alerts**

  * Tracks stock price changes using **Alpha Vantage API**
  * Fetches relevant company news using **News API**
  * Sends concise stock movement + news updates via Twilio

* 🌦 **Daily Weather Notifications**

  * Uses **OpenWeather API** to check local forecast
  * Alerts you if rain is expected in your location
  * Sends reminders every day at a fixed time

* 📲 **Notification Delivery (SMS/WhatsApp)**

  * Powered by **Twilio API**
  * Supports both SMS and WhatsApp messages
  * Configurable to notify multiple numbers

---

## 🛠️ Tech Stack

* **Language:** Python 3

* **APIs Used:**

  * [Alpha Vantage API](https://www.alphavantage.co/) – Stock market data
  * [News API](https://newsapi.org/) – Latest news headlines
  * [OpenWeather API](https://openweathermap.org/api) – Weather forecast
  * [Twilio API](https://www.twilio.com/) – SMS/WhatsApp notifications

* **Libraries:**

  * `requests` – API calls
  * `python-dotenv` – Secure environment variable management
  * `twilio` – Sending messages

---

## ⚙️ Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/j-harishankar/Python-Automation-Projects.git
   cd Python-Automation-Projects
   ```



2. **Configure Environment Variables** 
   Create a `.env` file in the project root:

   ```env
   ACCOUNT_SID=your_twilio_account_sid
   AUTH_TOKEN=your_twilio_auth_token
   STOCK_API=your_alpha_vantage_api_key
   NEWS_API=your_news_api_key
   API_KEY=your_openweather_api_key
   MY_EMAIL=your_email_if_used
   MY_PASSWORD=your_email_password_if_used
   ```

3. **Run the scripts** 

   * For stock alerts:

     ```bash
     python stock-news-hard-start/main.py
     ```
   * For weather alerts:

     ```bash
     python rain_finder/main.py
     ```

---

## 📊 Example Notifications

* **Stock Alert**

  > 🚨 TSLA stock moved +5% today.
  > Headline: "Tesla beats earnings expectations..."

* **Weather Alert**

  > 🌧️ Rain expected today in your area. Don’t forget your umbrella!

---

## 📌 Future Improvements

* Add email notifications as fallback
* Support for multiple stock tickers and locations
* Dockerize the project for easy deployment

---

## 🤝 Contribution

Pull requests are welcome! Please open an issue first to discuss major changes.



---

✅ This format makes your repo look professional and **recruiter-ready**: short description, features, tech stack, setup, usage, and future improvements.

Do you want me to also **add shields/badges** (Python version, APIs used, Twilio, etc.) at the top so it looks even more eye-catching on GitHub?
## ☁️ Deployment

This project is **hosted on [PythonAnywhere](https://www.pythonanywhere.com/)** to run daily automation tasks.

* **Daily Stock & News Alerts** → scheduled using PythonAnywhere’s **daily task scheduler**.
* **Daily Weather Alerts** → runs automatically at a fixed time every day.
* No need to keep the system running locally — all notifications are triggered from the cloud.

---

We can also add a little **architecture flow** in text:

1. PythonAnywhere runs the script daily →
2. Script calls **Alpha Vantage / News API / OpenWeather API** →
3. Generates alert →
4. Uses **Twilio API** to send notification →
5. Delivered to your phone (SMS/WhatsApp).


