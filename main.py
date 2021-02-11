from sys import argv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

"""
Pour utiliser le logiciel changer les identifiants.
Cherchez ensuite le driver pour votre navigateur (Firefox ou Chrome) et mettez le dans le meme dossier que ce script
Enlevez le # de la ligne 21 ou de la ligne 22 en fonction de votre navigateur
Pour lancer le programme faites (faites ESPACE + M si vous souhaitez que le navigateur se ferme apres): python3 main.py
Chrome: https://chromedriver.chromium.org/
Firefox: https://github.com/mozilla/geckodriver/releases
"""

# Identifiants
user = ''
password = ''

#navigateur = webdriver.Chrome() # Chrome
#navigateur = webdriver.Firefox(executable_path="./geckodriver") # Firefox

argument = False

if len(argv) > 1:
    if argv[1] == 'm':
        argument = True

attendre = WebDriverWait(navigateur, 10)

navigateur.get("https://monbureaunumerique.fr")

attendre.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.fo-connect__link'))).click()

attendre.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/div/form/div[1]/div/label'))).click()

navigateur.find_element_by_xpath('//*[@id="button-submit"]').click()

attendre.until(EC.presence_of_element_located((By.ID, 'username'))).send_keys(user)

navigateur.find_element_by_id('password').send_keys(password)

navigateur.find_element_by_id('bouton_valider').click()

attendre.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/button'))).click()

navigateur.find_element_by_xpath('/html/body/div[1]/div[2]/div/ul/li[1]/a').click()

if argument:
    attendre.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/ul[2]/li[6]/a'))).click()

    tableau = attendre.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/main/div/div/div/div[2]/table/tbody[2]')))

    donnees = tableau.text.split('\n')

    navigateur.close()

    z = []
    moyennes = []
    texteAvant = True
    a = 1
    e = 0

    for x in range(len(donnees)):
        try:
            if len(donnees[x]) < 5:
                z = donnees[x].split(',')
                donnees[x] = float(z[0] + '.' + z[1])
        except:
            pass

    while a < len(donnees):
        try:
            float(donnees[a-1])
        except ValueError:
            texteAvant = True
        else:
            texteAvant = False


        if texteAvant:
            try:
                moyennes.append(float(donnees[a]))
            except ValueError:
                pass
        a += 1

    for notes in moyennes:
        e += notes    

    print(f"Moyenne generale = {e/len(moyennes)}")