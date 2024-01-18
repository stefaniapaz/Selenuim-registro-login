from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.demoblaze.com/"
ruta_chromedriver = "/home/stefania/Documentos/Cursos/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=ruta_chromedriver)

driver.get(url)

# Registro de usuario
enlace_signup = driver.find_element_by_id("signin2")
driver.execute_script("arguments[0].scrollIntoView();", enlace_signup)
driver.execute_script("arguments[0].click();", enlace_signup)
driver.implicitly_wait(10)

campo_username = driver.find_element_by_id("sign-username")
campo_password = driver.find_element_by_id("sign-password")

nombre_usuario_registro = "TuNombreDeUsuario37"
contrasena_registro = "TuContraseña11"

campo_username.send_keys(nombre_usuario_registro)
campo_password.send_keys(contrasena_registro)

boton_signup = driver.find_element_by_xpath('//button[@onclick="register()"]')
boton_signup.click()
driver.implicitly_wait(20)

alerta_exito = WebDriverWait(driver, 10).until(EC.alert_is_present())
mensaje_alerta = alerta_exito.text
alerta_exito.accept()

driver.implicitly_wait(10)

# Inicio de sesión
formulario_login = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "login2")))
driver.execute_script("arguments[0].click();", formulario_login)

campo_username_login = driver.find_element_by_id("loginusername")
campo_password_login = driver.find_element_by_id("loginpassword")

# Utiliza las variables del registro para iniciar sesión
campo_username_login.send_keys(nombre_usuario_registro)
campo_password_login.send_keys(contrasena_registro)

boton_login = driver.find_element_by_xpath('//button[@onclick="logIn()"]')
boton_login.click()

driver.implicitly_wait(30)



# Cierra el navegador al finalizar
# driver.quit()


