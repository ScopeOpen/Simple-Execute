from selenium import webdriver
from time import sleep

driver=webdriver.Chrome() # Change the webdriver to whatever browser you are using for it.
driver.implicitly_wait(3) # Makes sure the webdriver loads in before anything else is ran
driver.get("") # THE SITE YOU WANT YOUR CODE TO RUN ON
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
js1 = js.replace("", f"") # Use this or as many as you need to execute code with previous declarations of anything. Because using f' won't work, (HEAD TO THE EXAMPLE SCRIPT TO VIEW A EXAMPLE)
# js2 = js1.replace("", f"")
# js3 = js2.replace("", f"")
# js4 = js3.replace("", f"") # EASILY ADD MORE 
sleep(2)
driver.execute_script(js1) # Change this to the last declaration of a replacement or other you would like to execute