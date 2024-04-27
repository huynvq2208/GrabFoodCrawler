from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

import time

def write_array_to_txt(filename, data):
    mode = 'a' if os.path.exists(filename) else 'w'
    with open(filename, mode) as file:
        if mode == 'a':
            file.write("\n")  # Append a new line before adding new data
        for item in data:
            file.write(str(item) + "\n")

def crawlRestaurantID():
    url = "https://food.grab.com/vn/vi/restaurants"

    locations = [
        {'lat': 10.775792941739054, 'lng': 106.70034207953456}, #Completed
        {'lat': 10.789004779264353, 'lng': 106.69080445456665}, #Completed
        {'lat': 10.793240709980772, 'lng': 106.69735821766018}, #Completed
        {'lat': 10.787964910309297, 'lng': 106.70537623880841}, #Completed
        {'lat': 10.776929328495026, 'lng': 106.69553669224612}, #Completed
        {'lat': 10.762311272449718, 'lng': 106.68930782626306}, #Completed
        {'lat': 10.763083190209734, 'lng': 106.6932285236395}, #Completed
        {'lat': 10.767300758646464, 'lng': 106.68697778623493}, #Completed
        {'lat': 10.758321735067135, 'lng': 106.68720358798714}, #Completed
        {'lat': 10.793431673580576, 'lng': 106.73083740755067}, #Completed
        {'lat': 10.80018050202991, 'lng': 106.77295352364543}, #Completed
        {'lat': 10.77433613863534, 'lng': 106.72398180014959}, #Completed
        {'lat': 10.832802636708943, 'lng': 106.77647011046932}, #Completed
        {'lat': 10.850199656360813, 'lng': 106.77660035459591}, #Completed
        {'lat': 10.775666691336946, 'lng': 106.76176608276059}, #Completed
        {'lat': 10.80812215718134, 'lng': 106.73066874040899}, #Completed
        {'lat': 10.814036367579142, 'lng': 106.73326197714385}, #Completed
        {'lat': 10.802557952757837, 'lng': 106.74367372496155}, #Completed
        {'lat': 10.806535636122428, 'lng': 106.74531206046126}, #Completed
        {'lat': 10.804987078590973, 'lng': 106.75625490555718}, #Completed
        {'lat': 10.794116587379566, 'lng': 106.74701222035223}, #Completed
        {'lat': 10.869539017814205, 'lng': 106.80812260866037}, #Completed
        {'lat': 10.792376429901985, 'lng': 106.78934067980884}, #Completed
        {'lat': 10.766520517298705, 'lng': 106.68163600375993}, #Completed
        {'lat': 10.76786932309829, 'lng': 106.67997755520558}, #Completed
        {'lat': 10.767335143305758, 'lng': 106.67600815374766}, #Completed
        {'lat': 10.77035324673569, 'lng': 106.68196225595918}, #Completed
        {'lat': 10.774933761880254, 'lng': 106.68662494349095},
        {'lat': 10.77598867671969, 'lng': 106.68534308704346},
        {'lat': 10.782335625510987, 'lng': 106.68969711655107},
        {'lat': 10.784435443091581, 'lng': 106.69144603232196},
        {'lat': 10.782774679562282, 'lng': 106.69579888892186},
        {'lat': 10.784393010966205, 'lng': 106.68429260030636},
        {'lat': 10.78918301730011, 'lng': 106.68103165063124},
        {'lat': 10.786157726342672, 'lng': 106.68097102628023},
        {'lat': 10.787679084659977, 'lng': 106.67814542858903},
        {'lat': 10.78748205506551, 'lng': 106.67561756347419},
        {'lat': 10.789733907372765, 'lng': 106.67810119766808},
        {'lat': 10.785379411455295, 'lng': 106.67126151619625},
        {'lat': 10.787946923695479, 'lng': 106.66834454469348},
        {'lat': 10.783916624679302, 'lng': 106.67840753009938},
        {'lat': 10.790805306503177, 'lng': 106.68256789850311},
        {'lat': 10.753874738846191, 'lng': 106.68817526619554},
        {'lat': 10.753020265523137, 'lng': 106.69543841471578},
        {'lat': 10.759301337484194, 'lng': 106.69524005141587},
        {'lat': 10.75315518254646, 'lng': 106.7020759561098},
        {'lat': 10.763078912126634, 'lng': 106.69853593417538},
        {'lat': 10.75610835075751, 'lng': 106.70116043322051},
        {'lat': 10.76337871760287, 'lng': 106.70367751880266},
        {'lat': 10.756688000503049, 'lng': 106.70613916839463},
        {'lat': 10.756755923960574, 'lng': 106.70205074105294},
        {'lat': 10.755499010635324, 'lng': 106.71673254012632},
        {'lat': 10.759131782309984, 'lng': 106.71858921819108},
        {'lat': 10.760434664483281, 'lng': 106.70721511468675},
        {'lat': 10.761032455619306, 'lng': 106.7034081443427},
        {'lat': 10.765147107094467, 'lng': 106.70701981768258},
        {'lat': 10.768263564843327, 'lng': 106.7056527479454},
        {'lat': 10.760765901765355, 'lng': 106.70437790672602},
        {'lat': 10.75033276601958, 'lng': 106.65593671032616},
        {'lat': 10.755881969219578, 'lng': 106.65412050843291},
        {'lat': 10.75001158713842, 'lng': 106.66127634313628},
        {'lat': 10.7553645236856, 'lng': 106.66463631619727},
        {'lat': 10.75065394453831, 'lng': 106.66485426039583},
        {'lat': 10.75668038048203, 'lng': 106.66556593492092},
        {'lat': 10.758012032072466, 'lng': 106.65954846081958},
        {'lat': 10.753418287102612, 'lng': 106.6697768084321},
        {'lat': 10.758489476299639, 'lng': 106.67195023102182},
        {'lat': 10.75319990864138, 'lng': 106.67903855159452},
        {'lat': 10.758926225446183, 'lng': 106.67768016263459},
        {'lat': 10.762492986461947, 'lng': 106.67896445765123},
        {'lat': 10.754534441341168, 'lng': 106.68410163771784},
        {'lat': 10.755002188871503, 'lng': 106.66725184305818},
        {'lat': 10.757582597731894, 'lng': 106.65278502944106},
        {'lat': 10.761646081168047, 'lng': 106.66848575580043},
        {'lat': 10.762295566102178, 'lng': 106.68262405656057},
        {'lat': 10.739338424529647, 'lng': 106.63621758485694},
        {'lat': 10.743048886839976, 'lng': 106.631654154045},
        {'lat': 10.743744593448211, 'lng': 106.64565916584718},
        {'lat': 10.749232889373147, 'lng': 106.63975817772827},
        {'lat': 10.749967231258704, 'lng': 106.64947513816405},
        {'lat': 10.754605138723475, 'lng': 106.63283435166878},
        {'lat': 10.755571360471064, 'lng': 106.6268546837083},
        {'lat': 10.747107152790505, 'lng': 106.63149679436182},
        {'lat': 10.735219623272089, 'lng': 106.62665361022339},
        {'lat': 10.745681327234538, 'lng': 106.62551126972899},
        {'lat': 10.75113249309539, 'lng': 106.62861190836503},
        {'lat': 10.755541452208613, 'lng': 106.62836712110594},
        {'lat': 10.749649465173722, 'lng': 106.64925563300373},
        {'lat': 10.754098527247509, 'lng': 106.63473158957481},
        {'lat': 10.747044128102765, 'lng': 106.63142696171597},
        {'lat': 10.70474803413083, 'lng': 106.73218667422857},
        {'lat': 10.70657177178163, 'lng': 106.7436638393621},
        {'lat': 10.71059139985845, 'lng': 106.7440426236762},
        {'lat': 10.714052703518494, 'lng': 106.7368836001398},
        {'lat': 10.713085031210102, 'lng': 106.73150486287965},
        {'lat': 10.706795085851523, 'lng': 106.72915640013225},
        {'lat': 10.717848926687923, 'lng': 106.7286639803692},
        {'lat': 10.719784237759802, 'lng': 106.73650481567097},
        {'lat': 10.718891018802701, 'lng': 106.74343656861892},
        {'lat': 10.723782082506654, 'lng': 106.74336508019361},
        {'lat': 10.723782082493601, 'lng': 106.72480521110668},
        {'lat': 10.719546656784752, 'lng': 106.73106168299613},
        {'lat': 10.726045995270473, 'lng': 106.7247226610882},
        {'lat': 10.731107279206514, 'lng': 106.72442829944946},
        {'lat': 10.729082775797478, 'lng': 106.71887222351836},
        {'lat': 10.730365229096932, 'lng': 106.70333169034345},
        {'lat': 10.733687759947225, 'lng': 106.69989170529941},
        {'lat': 10.745342415322908, 'lng': 106.70166133259107},
        {'lat': 10.748838233216313, 'lng': 106.69899626762603},
        {'lat': 10.737346682566075, 'lng': 106.71859162734255},
        {'lat': 10.740743178991611, 'lng': 106.72912354893732},
        {'lat': 10.758559244464017, 'lng': 106.74540399696231},
        {'lat': 10.766146212453249, 'lng': 106.73920399390856},
        {'lat': 10.754925980921104, 'lng': 106.72729346172633},
        {'lat': 10.735957497351896, 'lng': 106.7267496015825},
        {'lat': 10.73102566868833, 'lng': 106.70650802939204},
        {'lat': 10.74477022778948, 'lng': 106.70992299182653},
        {'lat': 10.745056122820426, 'lng': 106.71004698091618},
        {'lat': 10.7708628116785, 'lng': 106.7389381912914},
        {'lat': 10.751119258303955, 'lng': 106.73406497886498},
        {'lat': 10.741638346852474, 'lng': 106.70195790905964},
        {'lat': 10.737420123117996, 'lng': 106.71208704986618},
        {'lat': 10.749221011921716, 'lng': 106.71084950934686},
        {'lat': 10.752403596975155, 'lng': 106.72024025863604},
        {'lat': 10.737405590252235, 'lng': 106.75191026443946}

    ]




    firefox_options = webdriver.FirefoxOptions()


    for process,location in enumerate(locations):
        restaurant_ids = []
        network_url = "data:application/json,{\"location\":{\"lat\": "+ str(location['lat']) + ",\"lng\":" + str(location['lng']) + "},\"accuracy\":100.0}"

        firefox_options.set_preference("geo.prompt.testing",True)
        firefox_options.set_preference("geo.prompt.testing.allow",True)
        firefox_options.set_preference("geo.provider.network.url", network_url)

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=firefox_options)

        driver.get(url)
        time.sleep(10)

        # location input
        driver.find_element(By.CSS_SELECTOR,'.info___2rXBX').click()

        time.sleep(5)

        # click location button to update location
        driver.find_element(By.CSS_SELECTOR,'.location-icon___xyg1b').click()


        time.sleep(10)

        i = 1
        while True:
            xpath = '/html/body/div[1]/div[2]/div[3]/div[5]/div/div/div[4]/div/div/div/div[' + str(i) +']/a'
            last_height = driver.execute_script("return document.body.scrollHeight")
            try:
                element = driver.find_element(By.XPATH,xpath)
                href = element.get_attribute('href')
                id = str(href).split('/')[-1]
                if id not in restaurant_ids:
                    restaurant_ids.append(id)
            except NoSuchElementException:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height == new_height
            except StaleElementReferenceException:
                print("Stale element encountered. Retrying...")
                i -= 1
            i += 1
        time.sleep(5)
        driver.close()
        write_array_to_txt("restaurants.txt",restaurant_ids)
        print("Process: " + str(process+1) + "/" + str(len(locations)))

crawlRestaurantID()

