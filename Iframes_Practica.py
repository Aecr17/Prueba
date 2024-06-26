#Librerias importadas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Instanciamos el driver de Chrome
driver = webdriver.Chrome()

# Navegar a una URL
driver.get("https://practice-automation.com/iframes/")

# Maximizar ventana
driver.maximize_window()

# se localiza el iframe
iframe_Disney = driver.find_element(By.ID,"frame2")
driver.switch_to.frame(iframe_Disney)

tiempo_espera = WebDriverWait

# Espera explicita de 4 segundos
#driver.implicitly_wait(4)

exit_click = tiempo_espera(driver,10).until(
         EC.visibility_of_element_located((By.CLASS_NAME, "ab-close-button"))
)


#INTERACTUA CON EL BOTON DE SALIDA
exit_click = driver.find_element(By.CLASS_NAME, "ab-close-button")
exit_click.click()
#Otra forma de interactuar con la ventana de espera 
# button_ok = driver.find_element(By.CLASS_NAME, "ab-message-button")
# button_ok.click()

#Se agrega time sleep para observar la interaccion con el botton login
#driver.implicitly_wait(3)

#Interaccion con el boton de Login dentro del iframe
boton_dentro_del_iframe = driver.find_element(By.XPATH,'//*[@id="fitt-analytics"]/div[2]/div/div/div/div/nav/ul/li[1]/div/div/button')
boton_dentro_del_iframe.click()

#Interactua con un nuevo iframe de inicio de sesión
iframe_sesion = driver.find_element(By.ID,"oneid-iframe")
driver.switch_to.frame(iframe_sesion)
driver.implicitly_wait(3)

#Interactua ingresando el mail en el iframe
email_text = driver.find_element(By.XPATH, '//*[@id="InputIdentityFlowValue"]')
email_text.send_keys("Prueba@gmail.com")

#Cerrar caja de inicio de sesión
close_btn = driver.find_element(By.ID,"close")
close_btn.click()

#Sale del iframe
driver.switch_to.default_content()
#Scrolea
driver.execute_script("window.scrollBy(0, 700);")

#Interactua con el segundo iframe de la pagina
iframe_Selenium = driver.find_element(By.ID,"frame1")
driver.switch_to.frame(iframe_Selenium)

#Colocar una nueva espera EXPLICITA

About_btn = tiempo_espera(driver,10).until(
    EC.visibility_of_element_located((By.ID, "navbarDropdown"))
)

#Interactuar con el boton About
About_btn = driver.find_element(By.ID, "navbarDropdown")
About_btn.click()

#Se elige una opcion del menu desplegable
About_btn.send_keys(Keys.TAB)
item = driver.find_element(By.XPATH, '//*[@id="main_navbar"]/ul/li[1]/div/a[5]')
item.click()


#Se agrega un scroll en la pagina web
driver.execute_script("window.scrollBy(0, 500);")


driver.quit()