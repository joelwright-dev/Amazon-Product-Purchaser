# Amazon Product Purchaser
Python bot using Selenium which buys an item when it's available.

## How To Install
1. Go to your Start menu (lower left Windows icon), type "Microsoft Store", select the link to open the store.
2. Once the store is open, select Search from the upper-right menu and enter "Python". Select the most recent version.
3. Once Python has completed the downloading and installation process, open Windows PowerShell using the Start menu (lower left Windows icon). Once PowerShell is open, enter Python --version to confirm that Python3 has installed on your machine.
4. The Microsoft Store installation of Python includes pip, the standard package manager. Pip allows you to install and manage additional packages that are not part of the Python standard library. To confirm that you also have pip available to install and manage packages, enter pip --version.
5. Install Selenium
```
pip install selenium
```
6. Install Gecko Driver auto installer
```
pip install geckodriver-autoinstaller
```
7. Download main.py and open CMD and navigate to the desktop - Replace (username) with your Windows user account.
```
cd c:\Users\(username)\Desktop
```
8. Edit the Python file using NotePad or VS Code and enter your details in to the Python file, replacing the following lines with your account information:
```
# ACCOUNT INFO
ACCOUNT_EMAIL = 'email@email.com'
ACCOUNT_PASSWORD = 'password123'
```
9. Enter the URL to your desired product by replacing the URL in the following line:
```
AMAZON_PRODUCT_LINK = "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945/ref=sr_1_2?crid=1ZDXB7YRF1RXT&keywords=playstation+5&qid=1648454510&rnid=5367991051&s=videogames&sprefix=playstatio%2Caps%2C303&sr=1-2"
```
10. Run the python file
```
python main.py
```
