import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


def fill(vars, tipoTuroria, Eid):
    try:
        # Configurar Edge para evitar iniciar sesión
        options = Options()
        options.add_argument("--user-data-dir=C:\\Users\\thom1\\AppData\\Local\\Microsoft\\Edge\\User Data\\Estudio")  # Ruta al directorio de datos de usuario
        # Nombre del perfil (puedes cambiar "Default" por el nombre de otro perfil)
        driver = webdriver.Edge(options=options)
        wait = WebDriverWait(driver, 180)

        # Abrir el formulario
        driver.get(vars["form"])
        time.sleep(0.5)

        # 1. Click en checkbox "registrar dirección de correo"
        check1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="checkbox" and ancestor::div[contains(., "Correo electrónico")]]')))
        check1.click()
        time.sleep(0.2)

        # 2. Ingresar número de identificación
        numberTF = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
        numberTF.send_keys(str(Eid))
        time.sleep(0.2)

        # 3. Seleccionar nombre desde el desplegable
        select_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="listbox"]')))
        select_box.click()
        time.sleep(1)

        # Esperar que aparezca la opción
        option_xpath = '//span[@class="vRMGwf oJeWuf" and contains(text(), "Thomas Monnier Granda")]'
        option = wait.until(EC.presence_of_element_located((By.XPATH, option_xpath)))
        time.sleep(0.5)

        # Usar ActionChains como fallback robusto
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(option, 0, -100).pause(0.2).click().perform()
        time.sleep(1)

        # 5. Seleccionar actividad
        if tipoTuroria == 'Tutoria abierta':
            Xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span'
        elif tipoTuroria == 'Tutoria con cita':
            Xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span'
        elif tipoTuroria== 'taller':
            Xpath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
        else:
            raise Exception("seleccionar actividad")


        actividad = driver.find_element(By.XPATH, Xpath)
        actividad.click()
        time.sleep(5)

        # 6. Enviar formulario 
        submit_button = driver.find_element(By.XPATH, '//span[contains(text(),"Enviar")]')
        submit_button.click()
        #print("✓ Formulario enviado")

        time.sleep(3)
        driver.quit()
        return True

    except Exception as e:
        print(f"❌ Algo salió mal: {e}")
        driver.quit()
        raise e