from selenium import webdriver
from time import sleep

Token = 'LOL I AINT PUTTING A TOKEN HERE'
thetoken = Token
driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://discord.com/login")
js = '''
let token = 
function login(token) {
  setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"` 
  }, 50);
  setTimeout(() => {
    location.reload();
  }, 2500);
}
login(token);
'''
js1 = js.replace("let token =", f"let token = '{thetoken}';") # See how I use this function?
sleep(2)
driver.execute_script(js1)