from selenium import webdriver   #biblioteca para realizar automacao 
from selenium.webdriver.common.by import By   #biblioteca para realizar automacao
from selenium.webdriver.chrome.service import Service  #biblioteca para realizar automacao
from webdriver_manager.chrome import ChromeDriverManager  #biblioteca para realizar automacao
import progressbar #biblioteca para realizar barra de progresso
import time #biblioteca para utilizar o sleep
import image2console  #biblioteca para imprimir as imagens
import cv2

#Declarando váriaveis para automacao
num_perguntas = 0
questao_atual = 0
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get("https://personality-app-b8bb1.web.app/")

#Declarando variaveis para respostas 
tigre = 0
leao = 0
coruja = 0
panda = 0
tubarao = 0

print("**\n"
         "Bem-vindo ao Teste de Personalidade!\n"
          "**\n")

#Declarando vetores vazios para buscar respostas e as perguntas 
perguntas = []
alternativas_a = []
alternativas_b = []
alternativas_c = []
alternativas_d = []
alternativas_e = []

def pegar_perguntas():
    global num_perguntas
    pega_titulo_pergunta = driver.find_element(by=By.CSS_SELECTOR, value=".title-question").text  
    pega_alternativa_a = driver.find_element(by=By.XPATH, value="/html/body/app-root/div/div[2]/div[2]/span" ).text
    pega_alternativa_b = driver.find_element(by=By.XPATH, value="/html/body/app-root/div/div[2]/div[3]/span" ).text
    pega_alternativa_c = driver.find_element(by=By.XPATH, value="/html/body/app-root/div/div[2]/div[4]/span" ).text
    pega_alternativa_d = driver.find_element(by=By.XPATH, value="/html/body/app-root/div/div[2]/div[5]/span" ).text
    pega_alternativa_e = driver.find_element(by=By.XPATH, value="/html/body/app-root/div/div[2]/div[6]/span" ).text
    #time.sleep(1)
    clica_caixa = driver.find_element("xpath", "/html/body/app-root/div/div[2]/div[2]/input").click()
    #time.sleep(1)
    clica_proximo = driver.find_element("xpath", "/html/body/app-root/div/button[2]").click()
    #time.sleep(1)
    perguntas.append(pega_titulo_pergunta)
    alternativas_a.append(pega_alternativa_a)
    alternativas_b.append(pega_alternativa_b)
    alternativas_c.append(pega_alternativa_c)
    alternativas_d.append(pega_alternativa_d)
    alternativas_e.append(pega_alternativa_e)
    num_perguntas +=1

#laço de repeticao para responder até as perguntas finais 
while (num_perguntas < 20):
    pegar_perguntas()

def pergunta_01():
    global tigre, leao, coruja, panda, tubarao, id
    print(perguntas[0])
    print(alternativas_a[0])
    print(alternativas_b[0])
    print(alternativas_c[0])
    print(alternativas_d[0])
    print(alternativas_e[0])
    alternativa_selecionada = input(str.lower("Qual sua resposta?: "))
    id=1

    match alternativa_selecionada:
        case "a":
            tigre = tigre + 1
            return tigre
        case "b":
            leao = leao + 1
            return leao
        case "c":
            panda = panda + 1
            return panda
        case "d":
            coruja = coruja + 1
            return coruja
        case "e":
            tubarao = tubarao + 1
            return tubarao
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            pergunta_01()
        
def pergunta_02():
    global tigre, leao, coruja, panda, tubarao, id
    id=2
    print(perguntas[1])
    print(alternativas_a[1])
    print(alternativas_b[1])
    print(alternativas_c[1])
    print(alternativas_d[1])
    print(alternativas_e[1])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            coruja = coruja + 1
            return coruja
        case "b":
            leao = leao + 1
            return leao
        case "c":
            panda = panda + 1
            return panda
        case "d":
            tigre = tigre + 1
            return tigre
        case "e":
            tubarao = tubarao + 1
            return tubarao
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            pergunta_02()
                      
def pergunta_03():
    global tigre, leao, coruja, panda, tubarao, id
    id=3
    print(perguntas[2])
    print(alternativas_a[2])
    print(alternativas_b[2])
    print(alternativas_c[2])
    print(alternativas_d[2])
    print(alternativas_e[2])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            panda = panda + 1
            return panda
        case "b":
            tigre= tigre + 1
            return tigre
        case "c":
            tubarao = tubarao + 1
            return tubarao
        case "d":
            coruja = coruja + 1
            return coruja
        case "e":
            leao = leao + 1
            return leao
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_03()

def pergunta_04():
    global tigre, leao, coruja, panda, tubarao, id
    id=4
    print(perguntas[3])
    print(alternativas_a[3])
    print(alternativas_b[3])
    print(alternativas_c[3])
    print(alternativas_d[3])
    print(alternativas_e[3])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            tubarao = tubarao + 1
            return tubarao
        case "b":
            leao= leao + 1
            return leao
        case "c":
            coruja= coruja + 1
            return coruja
        case "d":
            panda = panda + 1
            return panda
        case "e":
            tigre = tigre + 1
            return tigre
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_04()

def pergunta_05():
    global tigre, leao, coruja, panda, tubarao, id
    id=5
    print(perguntas[4])
    print(alternativas_a[4])
    print(alternativas_b[4])
    print(alternativas_c[4])
    print(alternativas_d[4])
    print(alternativas_e[4])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            coruja = coruja + 1
            return coruja
        case "b":
            leao= leao + 1
            return leao
        case "c":
            panda= panda + 1
            return panda
        case "d":
            tigre = tigre + 1
            return tigre
        case "e":
            tubarao = tubarao + 1
            return tubarao
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_05()

def pergunta_06():
    global tigre, leao, coruja, panda, tubarao, id
    id=6
    print(perguntas[5])
    print(alternativas_a[5])
    print(alternativas_b[5])
    print(alternativas_c[5])
    print(alternativas_d[5])
    print(alternativas_e[5])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            panda= panda + 1
            return panda
        case "b":
            tigre= tigre + 1
            return tigre
        case "c":
            leao= leao + 1
            return leao
        case "d":
            tubarao = tubarao + 1
            return tubarao
        case "e":
            coruja = coruja + 1
            return coruja
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_06()

def pergunta_07():
    global tigre, leao, coruja, panda, tubarao, id
    id=7
    print(perguntas[6])
    print(alternativas_a[6])
    print(alternativas_b[6])
    print(alternativas_c[6])
    print(alternativas_d[6])
    print(alternativas_e[6])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            leao = leao + 1
            return leao
        case "b":
            tubarao= tubarao + 1
            return tubarao
        case "c":
            coruja= coruja + 1
            return coruja
        case "d":
            tigre = tigre + 1
            return tigre
        case "e":
            panda= panda + 1
            return panda
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_07()

def pergunta_08():
    global tigre, leao, coruja, panda, tubarao, id
    id=8
    print(perguntas[7])
    print(alternativas_a[7])
    print(alternativas_b[7])
    print(alternativas_c[7])
    print(alternativas_d[7])
    print(alternativas_e[7])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            tubarao = tubarao + 1
            return tubarao
        case "b":
            coruja= coruja + 1
            return coruja
        case "c":
            tigre= tigre + 1
            return tigre
        case "d":
            panda = panda + 1
            return panda
        case "e":
            leao = leao + 1
            return leao
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_08()

def pergunta_09():
    global tigre, leao, coruja, panda, tubarao, id
    id=9
    print(perguntas[8])
    print(alternativas_a[8])
    print(alternativas_b[8])
    print(alternativas_c[8])
    print(alternativas_d[8])
    print(alternativas_e[8])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            coruja = coruja + 1
            return coruja
        case "b":
            leao= leao + 1
            return leao
        case "c":
            tubarao= tubarao + 1
            return tubarao
        case "d":
            tigre = tigre + 1
            return tigre
        case "e":
            panda = panda + 1
            return panda
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_09()

def pergunta_10():
    global tigre, leao, coruja, panda, tubarao, id
    id=10
    print(perguntas[9])
    print(alternativas_a[9])
    print(alternativas_b[9])
    print(alternativas_c[9])
    print(alternativas_d[9])
    print(alternativas_e[9])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            panda = panda + 1
            return panda
        case "b":
            leao= leao + 1
            return leao
        case "c":
            tubarao= tubarao + 1
            return tubarao
        case "d":
            coruja = coruja + 1
            return coruja
        case "e":
            tigre = tigre + 1
            return tigre
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_10()

def pergunta_11():
    global tigre, leao, coruja, panda, tubarao, id
    id=11
    print(perguntas[10])
    print(alternativas_a[10])
    print(alternativas_b[10])
    print(alternativas_c[10])
    print(alternativas_d[10])
    print(alternativas_e[10])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            panda = panda + 1
            return panda
        case "b":
             tubarao= tubarao + 1

             return tubarao
        case "c":
            tigre= tigre + 1
            return tigre
        case "d":
            leao = leao + 1
            return leao
        case "e":
            coruja = coruja + 1
            return coruja
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_11()
            
def pergunta_12():
    global tigre, leao, coruja, panda, tubarao, id
    id=12
    print(perguntas[11])
    print(alternativas_a[11])
    print(alternativas_b[11])
    print(alternativas_c[11])
    print(alternativas_d[11])
    print(alternativas_e[11])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            tubarao = tubarao + 1
            return tubarao
        case "b":
            tigre = tigre + 1
            return tigre
        case "c":
            panda= panda + 1
            return panda
        case "d":
            coruja = coruja + 1
            return coruja
        case "e":
            leao = leao + 1
            return leao
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_12()

def pergunta_13():
    global tigre, leao, coruja, panda, tubarao, id
    id=13
    print(perguntas[12])
    print(alternativas_a[12])
    print(alternativas_b[12])
    print(alternativas_c[12])
    print(alternativas_d[12])
    print(alternativas_e[12])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            coruja = coruja + 1
            return coruja
        case "b":
            leao= leao + 1
            return leao
        case "c":
            tigre= tigre+ 1
            return tigre
        case "d":
            tubarao = tubarao + 1
            return tubarao
        case "e":
            panda = panda + 1
            return panda
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_13()

def pergunta_14():
    global tigre, leao, coruja, panda, tubarao, id
    id=14
    print(perguntas[13])
    print(alternativas_a[13])
    print(alternativas_b[13])
    print(alternativas_c[13])
    print(alternativas_d[13])
    print(alternativas_e[13])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            leao = leao + 1
            return leao
        case "b":
            tigre = tigre + 1
            return tigre
        case "c":
            panda= panda + 1
            return panda
        case "d":
            tubarao = tubarao + 1
            return tubarao
        case "e":
            coruja = coruja + 1
            return coruja
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_14()

def pergunta_15():
    global tigre, leao, coruja, panda, tubarao, id
    id=15
    print(perguntas[14])
    print(alternativas_a[14])
    print(alternativas_b[14])
    print(alternativas_c[14])
    print(alternativas_d[14])
    print(alternativas_e[14])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            panda = panda + 1
            return panda
        case "b":
            coruja = coruja + 1
            return coruja
        case "c":
            tubarao= tubarao + 1
            return tubarao
        case "d":
            leao = leao + 1
            return leao
        case "e":
            tigre = tigre + 1
            return tigre
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_15()
            
def pergunta_16():
    global tigre, leao, coruja, panda, tubarao, id
    id=16
    print(perguntas[15])
    print(alternativas_a[15])
    print(alternativas_b[15])
    print(alternativas_c[15])
    print(alternativas_d[15])
    print(alternativas_e[15])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            leao = leao + 1
            return leao
        case "b":
            panda= panda + 1
            return panda
        case "c":
            tigre= tigre + 1
            return tigre
        case "d":
            tubarao = tubarao + 1
            return tubarao
        case "e":
            coruja= coruja + 1
            return coruja
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_16()

def pergunta_17():
    global tigre, leao, coruja, panda, tubarao, id
    id=17
    print(perguntas[16])
    print(alternativas_a[16])
    print(alternativas_b[16])
    print(alternativas_c[16])
    print(alternativas_d[16])
    print(alternativas_e[16])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            coruja = coruja + 1
            return coruja
        case "b":
            tigre = tigre + 1
            return tigre
        case "c":
            tubarao= tubarao + 1
            return tubarao
        case "d":
            leao = leao + 1
            return leao
        case "e":
            panda = panda + 1
            return panda
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_17()

def pergunta_18():
    global tigre, leao, coruja, panda, tubarao, id
    id=18
    print(perguntas[17])
    print(alternativas_a[17])
    print(alternativas_b[17])
    print(alternativas_c[17])
    print(alternativas_d[17])
    print(alternativas_e[17])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            leao = leao + 1
            return leao
        case "b":
            tubarao = tubarao + 1
            return tubarao
        case "c":
            tigre = tigre + 1
            return tigre
        case "d":
            coruja = coruja + 1
            return coruja
        case "e":
            panda = panda + 1
            return panda
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_18()
          
def pergunta_19():
    global tigre, leao, coruja, panda, tubarao, id
    id=19
    print(perguntas[18])
    print(alternativas_a[18])
    print(alternativas_b[18])
    print(alternativas_c[18])
    print(alternativas_d[18])
    print(alternativas_e[18])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            tigre = tigre + 1
            return tigre
        case "b":
            leao = leao + 1
            return leao
        case "c":
            panda = panda + 1
            return panda
        case "d":
            coruja = coruja + 1
            return coruja
        case "e":
            tubarao = tubarao + 1
            return tubarao
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            time.sleep(1)
            return pergunta_19()
            
def pergunta_20():
    global tigre, leao, coruja, panda, tubarao, id
    id=20
    print(perguntas[19])
    print(alternativas_a[19])
    print(alternativas_b[19])
    print(alternativas_c[19])
    print(alternativas_d[19])
    print(alternativas_e[19])
    alternativa_selecionada = input(str("Qual sua resposta?: "))
    match alternativa_selecionada:
        case "a":
            panda = panda + 1
            return panda
        case "b":
            coruja = coruja + 1
            return coruja
        case "c":
            tubarao = tubarao + 1
            return tubarao
        case "d":
            leao = leao + 1
            return leao
        case "e":
            tigre = tigre + 1
            return tigre
        case _:
            print("Resposta invalida... Voltando para a pergunta")
            return pergunta_20()
            time.sleep(1)

# Mostrar respostas na tela junto com as imagens correspondentes 
def imprimir_resultado(tigre, leao, coruja, panda, tubarao):
    if tubarao>tigre and tubarao>leao and tubarao>coruja and tubarao>panda:
        print (''' Sua personalidade é similar a um Tubarão: 
             Você é inteligente e sabe muito para a sua idade. Sua inteligência é vasta e a sensatez acompanha sua genialidade. 
               Acima de tudo, você tem uma perspectiva que sempre permite que você tenha uma visão mais ampla.''')
        url="IMAGES\tubarao.jpg"
        image=cv2.imread(url)
        width, height = 200,200
        imgResive =cv2.resize(image,(width,height))
        cv2.imshow("Road Resized",image)
        cv2.waitKey(0)
        
    elif tigre>tubarao and tigre>leao and tigre>coruja and tigre>panda:
        print ('''Sua personalidade é similar a um Tigre:
        Os Tigres costumam ser pessoas fogosas e humanitárias, que amam a vida, mas a sua personalidade forte gera, frequentemente, 
        conflitos, pois os Tigres são muito competitivos - arrogantes, por vezes - e necessitam de aprovação constante. Não suportam ser ignorados.''')
        url="IMAGES\Tiger.jpg"
        image=cv2.imread(url)
        width, height = 200,200
        imgResive =cv2.resize(image,(width,height))
        cv2.imshow("Road Resized",image)
        cv2.waitKey(0)

    elif leao>tubarao and leao>tigre and leao>coruja and leao>panda:
        print ('''Sua personalidade é similar a um Leão:
        Você é líder e uma pessoa que os outros admiram. Raramente segue os outros e gosta de definir seu próprio caminho. 
        Você é da realeza e se porta com um prestígio invejável.''')
        url="IMAGES\leao.jpg"
        image=cv2.imread(url)
        width, height = 200,200
        imgResive =cv2.resize(image,(width,height))
        cv2.imshow("Road Resized",image)
        cv2.waitKey(0)

    elif coruja>tubarao and coruja>tigre and coruja>leao and coruja>panda:
        print ('''Sua personalidade é similar a de uma Coruja: 
         Você é inteligente e sabe muito para a sua idade. Sua inteligência é vasta e a sensatez acompanha sua genialidade. 
         Acima de tudo, você tem uma perspectiva que sempre permite que você tenha uma visão mais ampla.''')
        url="IMAGES\Coruja.jpg"
        image=cv2.imread(url)
        width, height = 200,200
        imgResive =cv2.resize(image,(width,height))
        cv2.imshow("Road Resized",image)
        cv2.waitKey(0)
    else:
        print ('''Sua personalidade é similar a um Panda: 
        Você gosta de brincar e tem bastante energia. Você é uma gracinha e sempre movimenta as festas que você vai. 
        As pessoas gostam da sua atitude e sempre querem estar perto de você.''')
        url="IMAGES\pandaa.jpg"
        image=cv2.imread(url)
        width, height = 200,200
        imgResive =cv2.resize(image,(width,height))
        cv2.imshow("Road Resized",image)
        cv2.waitKey(0)

#pendente
def pular_retroceder_pergunta(id):
    if id == 1:
        passar = input(str("Você deseja avançar? 1 - Avançar"))
        match int(passar):
            case 1:
                bar.update(5)
                pergunta_02()
            case _:
                pular_retroceder_pergunta(id)
    elif id != 1 and 20:
        passar_ou_retroceder = input(str("Você deseja avançar ou retroceder? 1 - Avançar / 2 - Retroceder"))
        match int(passar_ou_retroceder):
            case 1:
                if id == 2:
                    bar.update(10)
                    print (end=" ")
                    pergunta_03()
                elif id == 3:
                    bar.update(15)
                    print (end=" ")
                    pergunta_04()
                elif id == 4:
                    bar.update(20)
                    print (end=" ")
                    pergunta_05()
                elif id == 5:
                    bar.update(25)
                    print (end=" ")
                    pergunta_06()
                elif id == 6:
                    bar.update(30)
                    print (end=" ")
                    pergunta_07()
                elif id == 7:
                    bar.update(35)
                    print (end=" ")
                    pergunta_08()
                elif id == 8:
                    bar.update(40)
                    print (end=" ")
                    pergunta_09()
                elif id == 9:
                    bar.update(45)
                    print (end=" ")
                    pergunta_10()
                elif id == 10:
                    bar.update(50)
                    print (end=" ")
                    pergunta_11()
                elif id == 11:
                    bar.update(55)
                    print (end=" ")
                    pergunta_12()
                elif id == 12:
                    bar.update(60)
                    print (end=" ")
                    pergunta_13()
                elif id == 13:
                    bar.update(65)
                    print (end=" ")
                    pergunta_14()
                elif id == 14:
                    bar.update(70)
                    print (end=" ")
                    pergunta_15()
                elif id == 15:
                    bar.update(75)
                    print (end=" ")
                    pergunta_16()
                elif id == 16:
                    bar.update(80)
                    print (end=" ")
                    pergunta_17()
                elif id == 17:
                    bar.update(85)
                    print (end=" ")
                    pergunta_18()
                elif id == 18:
                    bar.update(90)
                    print (end=" ")
                    pergunta_19()
                elif id == 19:
                    bar.update(95)
                    print (end=" ")
                    pergunta_20()
                    #colocar outras perguntas
            case 2:
                if id == 2:
                    id = id-1
                    bar.update(5)
                    print (end=" ")
                    pergunta_01()
                elif id == 3:
                    id = id-1
                    bar.update(10)
                    print (end=" ")
                    pergunta_02()
                elif id == 4:
                    id = id-1
                    bar.update(15)
                    print (end=" ")
                    pergunta_03()
                elif id == 5:
                    id = id-1
                    bar.update(20)
                    print (end=" ")
                    pergunta_04()
                elif id == 6:
                    id = id-1
                    bar.update(25)
                    print (end=" ")
                    pergunta_05()
                elif id == 7:
                    id = id-1
                    bar.update(30)
                    print (end=" ")
                    pergunta_06()
                elif id == 8:
                    id = id-1
                    bar.update(35)
                    print (end=" ")
                    pergunta_07()
                elif id == 9:
                    id = id-1
                    bar.update(40)
                    print (end=" ")
                    pergunta_08()
                elif id == 10:
                    id = id-1
                    bar.update(45)
                    print (end=" ")
                    pergunta_09()
                elif id == 11:
                    id = id-1
                    bar.update(50)
                    print (end=" ")
                    pergunta_10()
                elif id == 12:
                    id = id-1
                    bar.update(55)
                    print (end=" ")
                    pergunta_11()
                elif id == 13:
                    id = id-1
                    bar.update(60)
                    print (end=" ")
                    pergunta_12()
                elif id == 14:
                    id = id-1
                    bar.update(65)
                    print (end=" ")
                    pergunta_13()
                elif id == 15:
                    id = id-1
                    bar.update(70)
                    print (end=" ")
                    pergunta_14()
                elif id == 16:
                    id = id-1
                    bar.update(75)
                    print (end=" ")
                    pergunta_15()
                elif id == 17:
                    id = id-1
                    bar.update(80)
                    print (end=" ")
                    pergunta_16()
                elif id == 18:
                    id = id-1
                    bar.update(85)
                    print (end=" ")
                    pergunta_17()
                elif id == 19:
                    id = id-1
                    bar.update(90)
                    print (end=" ")
                    pergunta_18()
                    #colocar outras perguntas
            case _:
                pular_retroceder_pergunta(id)

#Opção de finalizar o programa
def finalizar_programa(id):

    finalizar_ou_retroceder = input(str("Para finalizar Digite -1"))
    match int(finalizar_ou_retroceder):
            case 1:
                bar.update(100)
                print (end=" ")
                imprimir_resultado(tigre, leao, coruja, panda, tubarao)
            case _:
                pular_retroceder_pergunta(id)

with progressbar.ProgressBar(min_value=5, max_value=100) as bar: 
    pergunta_01()
    while id < 20:
        pular_retroceder_pergunta(id) 

finalizar_programa(id)