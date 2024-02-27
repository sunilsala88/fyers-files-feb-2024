

# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel
import credentials as cd
client_id = cd.client_id
secret_key = cd.secret_key
redirect_uri =cd.redirect_uri
user_name=cd.user_name
totp_key=cd.totp_key
pin1 =cd.pin1
pin2 = cd.pin2
pin3 = cd.pin3
pin4 = cd.pin4


# Replace these values with your actual API credentials

response_type = "code"  
state = "sample_state"

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type
)

# Generate the auth code using the session model
response = session.generate_authcode()

# Print the auth code received in the response
print(response)


link=response


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyotp as tp

# driver = webdriver.Chrome()
# Set Chrome options for headless mode
options = Options()
options.add_argument('--headless=new')

# Initialize Chrome webdriver
driver = webdriver.Chrome(options=options)



driver.get(link)

time.sleep(1)
login_with_clien_id_x_path='//*[@id="login_client_id"]'
elem = driver.find_element(By.XPATH, login_with_clien_id_x_path)
elem.click()
time.sleep(1)
client_id_input_x_path='//*[@id="fy_client_id"]'
elem2 = driver.find_element(By.XPATH, client_id_input_x_path)
elem2.send_keys("XS45474")
elem2.send_keys(Keys.RETURN)
time.sleep(1)

t=tp.TOTP(totp_key).now()



driver.find_element(By.XPATH, '//*[@id="first"]').send_keys(t[0])
driver.find_element(By.XPATH, '//*[@id="second"]').send_keys(t[1])
driver.find_element(By.XPATH, '//*[@id="third"]').send_keys(t[2])
driver.find_element(By.XPATH, '//*[@id="fourth"]').send_keys(t[3])
driver.find_element(By.XPATH, '//*[@id="fifth"]').send_keys(t[4])
driver.find_element(By.XPATH, '//*[@id="sixth"]').send_keys(t[5])

driver.find_element(By.XPATH, '//*[@id="confirmOtpSubmit"]').click() 
time.sleep(1)

driver.find_element(By.ID,"verifyPinForm").find_element(By.ID,"first").send_keys(pin1)
driver.find_element(By.ID,"verifyPinForm").find_element(By.ID,"second").send_keys(pin2)
driver.find_element(By.ID,"verifyPinForm").find_element(By.ID,"third").send_keys(pin3)
driver.find_element(By.ID,"verifyPinForm").find_element(By.ID,"fourth").send_keys(pin4)

driver.find_element(By.XPATH,'//*[@id="verifyPinSubmit"]').click()
time.sleep(1)
newurl = driver.current_url
print(newurl)
auth_code = newurl[newurl.index('auth_code=')+10:newurl.index('&state')]
print(auth_code)
driver.close()


# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

response_type = "code" 
grant_type = "authorization_code"  


# Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key, 
    redirect_uri=redirect_uri, 
    response_type=response_type, 
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
print(response)

access_token=response['access_token']
with open('access.txt','w') as k:
    k.write(access_token)