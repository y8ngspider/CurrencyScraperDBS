# CurrencyScraperDBS

A Python automation tool that scrapes live USD/SGD exchange rates from 
DBS Bank every 60 seconds and sends email alerts when the rate crosses 
a threshold. Built during my SWE internship at HelloTech (Singapore, 2022).

## Stack
- **Selenium + headless Chrome** for scraping a dynamically rendered page
- **Regex parsing** to extract rates from the DOM
- **SMTP email alerts** with credentials stored in environment variables
- Runs on Linux/macOS

## How it works
1. Launches headless Chrome via Selenium WebDriver
2. Loads the DBS FX page, waits for JS to render the rate
3. Parses the rate with regex
4. If rate > threshold (default 1.33 SGD/USD), sends email via SMTP
5. Loops every 60 seconds

## Setup
For Mac:
<div>In order to send emails, sender needs to:
<p>1. Create an environment variable with the following steps:
<div>Open Terminal and run:

touch ~/.zshrc; open ~/.zshrc

A text editor should open a .zshrc file. Insert the following in the file:

export email="example@examplemail.com"
export password="my_strong_password"

Save and close the text editor. Close Terminal (important).</div></p>

<p>2. Now, you can fetch the values of the email and password variables from your Python script with:

my_email = os.getenv('email')
my_password = os.getenv('password')</p>
</body>
