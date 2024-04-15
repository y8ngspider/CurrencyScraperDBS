CurrencyScraperDBS.py
Scrapes SGD/USD Exchange Rate from DBS website every 60 seconds and sends email to user if rate > 1.33 SGD/USD


For Mac:
In order to send emails, sender needs to:
1. Create an environment variable with the following steps:
Open Terminal and run:

touch ~/.zshrc; open ~/.zshrc

A text editor should open a .zshrc file. Insert the following in the file:

export email="example@examplemail.com"
export password="my_strong_password"

Save and close the text editor. Close Terminal (important). 

2. Now, you can fetch the values of the email and password variables from your Python script with:

my_email = os.getenv('email')
my_password = os.getenv('password')
