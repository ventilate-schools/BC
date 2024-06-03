import os
import pandas as pd

# vancouver_schools has a GPT4 sourced set of schools.

# There's 169 school districts in BC and this is just one below for vancouver.
# vancouver is hard coded a few times in here, which isn't optimal.

# GPT Prompt I used:
# All vancouver public school district (BC) schools in a python dict like so ```vancouver_schools = [
#    {"school_name": "School Name", "address": "400 Street St+Town+CT 12345", "students": 1234,
#    "website": "URL, "phone": "123 456 7890"}]``` please

# After you generate the markdown from this script, also run `python3 make_grade_subtotals_and_totals.py`

vancouver_schools = [
    {'school_name': '¿uuqinak’uuh Grandview Elementary', 'address': '2055 Woodland Drive Vancouver,  V5N 3N9',
     'google_map': 'https://www.google.com/maps/place/2055+Woodland+Drive+Vancouver,++V5N+3N9+++',
     'phone': '604-713-4663', 'website': 'https://www.vsb.bc.ca/grandview'},
    {'school_name': 'Bayview Elementary', 'address': '3505 West 7th Ave Vancouver,  V6R 0E9',
     'google_map': 'https://www.google.com/maps/place/3505+West+7th+Ave+Vancouver,++V6R+0E9', 'phone': '604-713-5433',
     'website': 'https://www.vsb.bc.ca/bayview'},
    {'school_name': 'Beaconsfield Elementary', 'address': '3663 Penticton Street Vancouver,  V5M 3C9',
     'google_map': 'https://www.google.com/maps/place/3663+Penticton+Street+Vancouver,++V5M+3C9+++',
     'phone': '604-713-4605', 'website': 'https://www.vsb.bc.ca/lord-beaconsfield'},
    {'school_name': 'Britannia Elementary', 'address': '1110 Cotton Drive Vancouver,  V5L 3T5',
     'google_map': 'https://www.google.com/maps/place/1110+Cotton+Drive+Vancouver,++V5L+3T5+++',
     'phone': '604-713-4497', 'website': 'https://www.vsb.bc.ca/britannia-elementary'},
    {'school_name': 'Britannia Secondary', 'address': '1001 Cotton Drive Vancouver,  V5L 3T4',
     'google_map': 'https://www.google.com/maps/place/1001+Cotton+Drive+Vancouver,++V5L+3T4+++',
     'phone': '604-713-8266', 'website': 'https://www.vsb.bc.ca/britannia-secondary'},
    {'school_name': 'Brock Elementary', 'address': '4860 Main Street Vancouver,  V5V 3R8',
     'google_map': 'https://www.google.com/maps/place/4860+Main+Street+Vancouver,++V5V+3R8+++', 'phone': '604-713-5245',
     'website': 'https://www.vsb.bc.ca/general-brock'},
    {'school_name': 'Bruce Elementary', 'address': '3633 Tanner Street Vancouver,  V5R 5P7',
     'google_map': 'https://www.google.com/maps/place/3633+Tanner+Street+Vancouver,++V5R+5P7+++',
     'phone': '604-713-4778', 'website': 'https://www.vsb.bc.ca/graham-d-bruce'},
    {'school_name': 'Byng Secondary', 'address': '3939 West 16th Avenue Vancouver,  V6R 3C9',
     'google_map': 'https://www.google.com/maps/place/3939+West+16th+Avenue+Vancouver,++V6R+3C9+++',
     'phone': '604-713-8171', 'website': 'https://www.vsb.bc.ca/lord-byng'},
    {'school_name': 'Carleton Elementary', 'address': '2330 East 37 Avenue Vancouver,  V5R 2T3',
     'google_map': 'https://www.google.com/maps/place/2330+East+37+Avenue+Vancouver,++V5R+2T3+++',
     'phone': '604-713-4675', 'website': 'https://www.vsb.bc.ca/sir-guy-carleton'},
    {'school_name': 'Carnarvon Elementary', 'address': '3400 Balaclava Street Vancouver,  V6L 2S6',
     'google_map': 'https://www.google.com/maps/place/3400+Balaclava+Street+Vancouver,++V6L+2S6+++',
     'phone': '604-713-5396', 'website': 'https://www.vsb.bc.ca/carnarvon'},
    {'school_name': 'Carr Elementary', 'address': '4070 Oak Street Vancouver,  V6H 2M8',
     'google_map': 'https://www.google.com/maps/place/4070+Oak+Street+Vancouver,++V6H+2M8+++', 'phone': '604-713-4941',
     'website': 'https://www.vsb.bc.ca/emily-carr'},
    {'school_name': 'Cavell Elementary', 'address': '500 West 20th Avenue Vancouver,  V5Z 1X7',
     'google_map': 'https://www.google.com/maps/place/500+West+20th+Avenue+Vancouver,++V5Z+1X7+++',
     'phone': '604-713-4932', 'website': 'https://www.vsb.bc.ca/edith-cavell'},
    {'school_name': 'Champlain Heights Annex', 'address': '7835 Champlain Crescent Vancouver,  V5S 4J6',
     'google_map': 'https://www.google.com/maps/place/7835+Champlain+Crescent+Vancouver,++V5S+4J6+++',
     'phone': '604-713-4880', 'website': 'https://www.vsb.bc.ca/champlain-heights-annex'},
    {'school_name': 'Champlain Heights Elementary', 'address': '6955 Frontenac Street Vancouver,  V5S 3T4',
     'google_map': 'https://www.google.com/maps/place/6955+Frontenac+Street+Vancouver,++V5S+3T4+++',
     'phone': '604-713-4760', 'website': 'https://www.vsb.bc.ca/champlain-heights'},
    {'school_name': 'Churchill Secondary', 'address': '7055 Heather Street Vancouver,  V6P 3P7',
     'google_map': 'https://www.google.com/maps/place/7055+Heather+Street+Vancouver,++V6P+3P7++',
     'phone': '604-713-8189', 'website': 'https://www.vsb.bc.ca/sir-winston-churchill'},
    {'school_name': 'Collingwood Elementary', 'address': '3417 Euclid Avenue Vancouver,  V5R 6H2',
     'google_map': 'https://www.google.com/maps/place/3417+Euclid+Avenue+Vancouver,++V5R+6H2+++',
     'phone': '604-713-5340', 'website': 'https://www.vsb.bc.ca/collingwood-neighbourhood-bruce-annex'},
    {'school_name': 'Cook Elementary', 'address': '3340 East 54th Avenue Vancouver,  V5S 1Z3',
     'google_map': 'https://www.google.com/maps/place/3340+East+54th+Avenue+Vancouver,++V5S+1Z3+++',
     'phone': '604-713-4828', 'website': 'https://www.vsb.bc.ca/captain-james-cook'},
    {'school_name': 'Cunningham Elementary', 'address': '2330 East 37th Street Vancouver,  V5R 2T3',
     'google_map': 'https://www.google.com/maps/place/2330+East+37th+Street+Vancouver,++V5R+2T3+++',
     'phone': '604-713-4675', 'website': 'https://www.vsb.bc.ca/george-t-cunningham'},
    {'school_name': 'David Thompson Secondary', 'address': '1755 East 55th Avenue Vancouver,  V5P 1Z7',
     'google_map': 'https://www.google.com/maps/place/1755+East+55th+Avenue+Vancouver,++V5P+1Z7+++',
     'phone': '604-713-8278', 'website': 'https://www.vsb.bc.ca/david-thompson'},
    {'school_name': 'Dickens Annex', 'address': '3877 Glen Drive Vancouver,  V5V 4S9',
     'google_map': 'https://www.google.com/maps/place/3877+Glen+Drive+Vancouver,++V5V+4S9+++', 'phone': '604-713-5392',
     'website': 'https://www.vsb.bc.ca/charles-dickens-annex'},
    {'school_name': 'Dickens Elementary', 'address': '1010 E. 17th Ave. Vancouver,  V5V 0A6',
     'google_map': 'https://www.google.com/maps/place/1010+E.+17th+Ave.+Vancouver,++V5V+0A6', 'phone': '604-713-4978',
     'website': 'https://www.vsb.bc.ca/charles-dickens'},
    {'school_name': 'Douglas Annex', 'address': '7668 Borden Street Vancouver,  V5P 3E1',
     'google_map': 'https://www.google.com/maps/place/7668+Borden+Street+Vancouver,++V5P+3E1+++',
     'phone': '604-713-4885', 'website': 'https://www.vsb.bc.ca/sir-james-douglas-annex'},
    {'school_name': 'Douglas Elementary', 'address': '2150 Brigadoon Avenue Vancouver,  V5P 3Z7',
     'google_map': 'https://www.google.com/maps/place/2150+Brigadoon+Avenue+Vancouver,++V5P+3Z7',
     'phone': '604-713-4817', 'website': 'https://www.vsb.bc.ca/sir-james-douglas'},
    {'school_name': 'Elsie Roy Elementary', 'address': '150 Drake Street Vancouver,  V6Z 2X1',
     'google_map': 'https://www.google.com/maps/place/150+Drake+Street+Vancouver,++V6Z+2X1+++', 'phone': '604-713-5890',
     'website': 'https://www.vsb.bc.ca/elsie-roy'},
    {'school_name': 'False Creek Elementary', 'address': '900 School Green Vancouver,  V6H 3N7',
     'google_map': 'https://www.google.com/maps/place/900+School+Green+Vancouver,++V6H+3N7+++', 'phone': '604-713-4959',
     'website': 'https://www.vsb.bc.ca/false-creek'},
    {'school_name': 'Fleming Elementary', 'address': '6363 Lanark Street Vancouver,  V5P 2Y8',
     'google_map': 'https://www.google.com/maps/place/6363+Lanark+Street+Vancouver,++V5P+2Y8+++',
     'phone': '604-713-4793', 'website': 'https://www.vsb.bc.ca/sir-sandford-fleming'},
    {'school_name': 'Franklin Elementary', 'address': '250 South Skeena Street Vancouver,  V5K 4H6',
     'google_map': 'https://www.google.com/maps/place/250+South+Skeena+Street+Vancouver,++V5K+4H6+++',
     'phone': '604-713-4709', 'website': 'https://www.vsb.bc.ca/sir-john-franklin'},
    {'school_name': 'Fraser Elementary', 'address': '100 West 15th Avenue Vancouver,  V5Y 3B7',
     'google_map': 'https://www.google.com/maps/place/100+West+15th+Avenue+Vancouver,++V5Y+3B7+++',
     'phone': '604-713-4946', 'website': 'https://www.vsb.bc.ca/simon-fraser'},
    {'school_name': 'Gathering Place Education Ctr', 'address': '609 Helmcken Street Vancouver,  V6B 5R1',
     'google_map': 'https://www.google.com/maps/place/609+Helmcken+Street+Vancouver,++V6B+5R1+++',
     'phone': '604-257-3849', 'website': 'https://www.vsb.bc.ca/page/5243'},
    {'school_name': 'Gladstone Secondary', 'address': '4105 Gladstone Street Vancouver,  V5N 4Z2',
     'google_map': 'https://www.google.com/maps/place/4105+Gladstone+Street+Vancouver,++V5N+4Z2+++',
     'phone': '604-713-8288', 'website': 'https://www.vsb.bc.ca/gladstone'},
    {'school_name': 'Gordon Elementary', 'address': '2268 Bayswater Street Vancouver,  V6K 4P5',
     'google_map': 'https://www.google.com/maps/place/2268+Bayswater+Street+Vancouver,++V6K+4P5',
     'phone': '604-713-5403', 'website': 'https://www.vsb.bc.ca/general-gordon'},
    {'school_name': 'Grenfell Elementary', 'address': '3323 Wellington Avenue Vancouver,  V5R 4Y3',
     'google_map': 'https://www.google.com/maps/place/3323+Wellington+Avenue+Vancouver,++V5R+4Y3+++',
     'phone': '604-713-4844', 'website': 'https://www.vsb.bc.ca/sir-wilfred-grenfell'},
    {'school_name': 'Hamber Secondary', 'address': '5025 Willow Street Vancouver,  V5Z 3S1',
     'google_map': 'https://www.google.com/maps/place/5025+Willow+Street+Vancouver,++V5Z+3S1+++',
     'phone': '604-713-8927', 'website': 'https://www.vsb.bc.ca/eric-hamber'},
    {'school_name': 'Hastings Elementary', 'address': '2625 Franklin Street Vancouver,  V5K 3W7',
     'google_map': 'https://www.google.com/maps/place/2625+Franklin+Street+Vancouver,++V5K+3W7+++',
     'phone': '604-713-5507', 'website': 'https://www.vsb.bc.ca/hastings'},
    {'school_name': 'Henderson Elementary', 'address': '451 East 53rd Avenue Vancouver,  V5X 1J3',
     'google_map': 'https://www.google.com/maps/place/451+East+53rd+Avenue+Vancouver,++V5X+1J3+++',
     'phone': '604-713-4837', 'website': 'https://www.vsb.bc.ca/john-henderson'},
    {'school_name': 'Hudson Elementary', 'address': '1551 Cypress Street Vancouver,  V6J 3L3',
     'google_map': 'https://www.google.com/maps/place/1551+Cypress+Street+Vancouver,++V6J+3L3+++',
     'phone': '604-713-5441', 'website': 'https://www.vsb.bc.ca/henry-hudson'},
    {'school_name': 'Jamieson Elementary', 'address': '6350 Tisdall Street Vancouver,  V5Z 3N4',
     'google_map': 'https://www.google.com/maps/place/6350+Tisdall+Street+Vancouver,++V5Z+3N4', 'phone': '604-713-5367',
     'website': 'https://www.vsb.bc.ca/dr-annie-b-jamieson'},
    {'school_name': 'John Oliver Secondary', 'address': '530 East 41st Avenue Vancouver,  V5W 1P3',
     'google_map': 'https://www.google.com/maps/place/530+East+41st+Avenue+Vancouver,++V5W+1P3+++',
     'phone': '604-713-8938', 'website': 'https://www.vsb.bc.ca/john-oliver'},
    {'school_name': 'Jules Quesnel Elementary', 'address': '3050 Crown Street Vancouver,  V6R 4K9',
     'google_map': 'https://www.google.com/maps/place/3050+Crown+Street+Vancouver,++V6R+4K9+++',
     'phone': '604-713-4577', 'website': 'https://www.vsb.bc.ca/jules-quesnel'},
    {'school_name': 'Kerrisdale Annex', 'address': '3250 West 43 Avenue Vancouver,  V6N 1L3',
     'google_map': 'https://www.google.com/maps/place/3250+West+43+Avenue+Vancouver,++V6N+1L3+++',
     'phone': '604-713-5488', 'website': 'https://www.vsb.bc.ca/kerrisdale-annex'},
    {'school_name': 'Kerrisdale Elementary', 'address': '5555 Carnarvon Street Vancouver,  V6N 1J2',
     'google_map': 'https://www.google.com/maps/place/5555+Carnarvon+Street+Vancouver,++V6N+1J2',
     'phone': '604-713-5446', 'website': 'https://www.vsb.bc.ca/kerrisdale'},
    {'school_name': 'Killarney Secondary', 'address': '6454 Killarney Street Vancouver,  V5S 2X7',
     'google_map': 'https://www.google.com/maps/place/6454+Killarney+Street+Vancouver,++V5S+2X7+++',
     'phone': '604-713-8950', 'website': 'https://www.vsb.bc.ca/killarney'},
    {'school_name': 'King George Secondary', 'address': '1755 Barclay Street Vancouver,  V6G 1K6',
     'google_map': 'https://www.google.com/maps/place/1755+Barclay+Street+Vancouver,++V6G+1K6', 'phone': '604-713-8999',
     'website': 'https://www.vsb.bc.ca/king-george'},
    {'school_name': 'Kingsford-Smith Elementary', 'address': '6901 Elliott Street Vancouver,  V5S 2N1',
     'google_map': 'https://www.google.com/maps/place/6901+Elliott+Street+Vancouver,++V5S+2N1+++',
     'phone': '604-713-4746', 'website': 'https://www.vsb.bc.ca/sir-charles-kingsford-smith'},
    {'school_name': 'Kitchener Elementary', 'address': '3455 West King Edward Avenue Vancouver,  V6S 0C7',
     'google_map': 'https://www.google.com/maps/place/3455+West+King+Edward+Avenue+Vancouver,++V6S+0C7+++',
     'phone': '604-713-5454', 'website': 'https://www.vsb.bc.ca/lord-kitchener'},
    {'school_name': 'Kitsilano Secondary', 'address': '2706 Trafalgar Street Vancouver,  V6K 2J6',
     'google_map': 'https://www.google.com/maps/place/2706+Trafalgar+Street+Vancouver,++V6K+2J6+++',
     'phone': '604-713-8961', 'website': 'https://www.vsb.bc.ca/kitsilano'},
    {'school_name': 'Laurier Elementary', 'address': '7350 Laurel Street Vancouver,  V6P 3T9',
     'google_map': 'https://www.google.com/maps/place/7350+Laurel+Street+Vancouver,++V6P+3T9+++',
     'phone': '604-713-4925', 'website': 'https://www.vsb.bc.ca/sir-wilfrid-laurier'},
    {'school_name': "L'Ecole Bilingue Elementary", 'address': '1166 West 14th Avenue Vancouver,  V6H 1P6',
     'google_map': 'https://www.google.com/maps/place/1166+West+14th+Avenue+Vancouver,++V6H+1P6+++',
     'phone': '604-713-4585', 'website': 'https://www.vsb.bc.ca/lecole-bilingue'},
    {'school_name': 'Livingstone Elementary', 'address': '315 East 23rd Avenue Vancouver,  V5V 1X6',
     'google_map': 'https://www.google.com/maps/place/315+East+23rd+Avenue+Vancouver,++V5V+1X6+++',
     'phone': '604-713-4985', 'website': 'https://www.vsb.bc.ca/david-livingstone'},
    {'school_name': 'Lloyd George Elementary', 'address': '1338 W 67th Avenue Vancouver,  V6P 2T4',
     'google_map': 'https://www.google.com/maps/place/1338+W+67th+Avenue+Vancouver,++V6P+2T4', 'phone': '604-713-4895',
     'website': 'https://www.vsb.bc.ca/david-lloyd-george'},
    {'school_name': 'Lord Elementary', 'address': '555 Lillooet Street Vancouver,  V5K 4G4',
     'google_map': 'https://www.google.com/maps/place/555+Lillooet+Street+Vancouver,++V5K+4G4+++',
     'phone': '604-713-4620', 'website': 'https://www.vsb.bc.ca/dr-ar-lord'},
    {'school_name': 'MacCorkindale Elementary', 'address': '6100 Battison Street Vancouver,  V5S 3M8',
     'google_map': 'https://www.google.com/maps/place/6100+Battison+Street+Vancouver,++V5S+3M8+++',
     'phone': '604-713-4775', 'website': 'https://www.vsb.bc.ca/dr-hn-maccorkindale'},
    {'school_name': 'Mackenzie Elementary', 'address': '960 East 39th Avenue Vancouver,  V5W 1K8',
     'google_map': 'https://www.google.com/maps/place/960+East+39th+Avenue+Vancouver,++V5W+1K8+++',
     'phone': '604-713-4799', 'website': 'https://www.vsb.bc.ca/sir-alexander-mackenzie'},
    {'school_name': 'Magee Secondary', 'address': '6360 Maple Street Vancouver,  V6M 4M2',
     'google_map': 'https://www.google.com/maps/place/6360+Maple+Street+Vancouver,++V6M+4M2+++',
     'phone': '604-713-8200', 'website': 'https://www.vsb.bc.ca/magee'},
    {'school_name': 'Maple Grove Elementary', 'address': '1924 West 45th Ave Vancouver,  V6M 0C7',
     'google_map': 'https://www.google.com/maps/place/1924+West+45th+Ave+Vancouver,++V6M+0C7', 'phone': '604-713-5356',
     'website': 'https://www.vsb.bc.ca/maple-grove'},
    {'school_name': 'Maquinna Elementary', 'address': '2684 East 2nd Avenue Vancouver,  V5M 1C9',
     'google_map': 'https://www.google.com/maps/place/2684+East+2nd+Avenue+Vancouver,++V5M+1C9',
     'phone': '604-713-4705', 'website': 'https://www.vsb.bc.ca/chief-maquinna'},
    {'school_name': 'McBride Annex', 'address': '4750 St. Catherines Street Vancouver,  V5V 4M7',
     'google_map': 'https://www.google.com/maps/place/4750+St.+Catherines+Street+Vancouver,++V5V+4M7+++',
     'phone': '604-713-5374', 'website': 'https://www.vsb.bc.ca/mcbride-annex'},
    {'school_name': 'McBride Elementary', 'address': '1300 East 29th Avenue Vancouver,  V5V 2T3',
     'google_map': 'https://www.google.com/maps/place/1300+East+29th+Avenue+Vancouver,++V5V+2T3+++',
     'phone': '604-713-4971', 'website': 'https://www.vsb.bc.ca/sir-richard-mcbride'},
    {'school_name': 'McKechnie Elementary', 'address': '7455 Maple Street Vancouver,  V6P 5P8',
     'google_map': 'https://www.google.com/maps/place/7455+Maple+Street+Vancouver,++V6P+5P8+++',
     'phone': '604-713-4952', 'website': 'https://www.vsb.bc.ca/dr-re-mckechnie'},
    {'school_name': 'Moberly Elementary', 'address': '1000 East 59th Avenue Vancouver,  V5X 1Y7',
     'google_map': 'https://www.google.com/maps/place/1000+East+59th+Avenue+Vancouver,++V5X+1Y7+++',
     'phone': '604-713-4784', 'website': 'https://www.vsb.bc.ca/walter-moberly'},
    {'school_name': 'Mount Pleasant Elementary', 'address': '2300 Guelph Street Vancouver,  V5T 3P1',
     'google_map': 'https://www.google.com/maps/place/2300+Guelph+Street+Vancouver,++V5T+3P1+++',
     'phone': '604-713-4617', 'website': 'https://www.vsb.bc.ca/mount-pleasant'},
    {'school_name': 'Nelson Elementary', 'address': '1355 Garden Drive Vancouver,  V5L 0C4',
     'google_map': 'https://www.google.com/maps/place/1355+Garden+Drive+Vancouver,++V5L+0C4+++',
     'phone': '604-713-4595', 'website': 'https://www.vsb.bc.ca/lord-nelson'},
    {'school_name': 'Nightingale Elementary', 'address': '2740 Guelph Street Vancouver,  V5T 3P7',
     'google_map': 'https://www.google.com/maps/place/2740+Guelph+Street+Vancouver,++V5T+3P7+++',
     'phone': '604-713-5290', 'website': 'https://www.vsb.bc.ca/florence-nightingale'},
    {'school_name': 'Nootka Elementary', 'address': '3375 Nootka Street Vancouver,  V5M 3N2',
     'google_map': 'https://www.google.com/maps/place/3375+Nootka+Street+Vancouver,++V5M+3N2+++',
     'phone': '604-713-4767', 'website': 'https://www.vsb.bc.ca/nootka'},
    {'school_name': 'Norma Rose Point School', 'address': '5488 Ortona Avenue Vancouver,  V6T 1S2',
     'google_map': 'https://www.google.com/maps/place/5488+Ortona+Avenue+Vancouver,++V6T+1S2+++',
     'phone': '604-713-5950', 'website': 'https://www.vsb.bc.ca/norma-rose-point-school'},
    {'school_name': 'Norquay Elementary', 'address': '4710 Slocan Street Vancouver,  V5R 2A1',
     'google_map': 'https://www.google.com/maps/place/4710+Slocan+Street+Vancouver,++V5R+2A1+++',
     'phone': '604-713-4666', 'website': 'https://www.vsb.bc.ca/john-norquay'},
    {'school_name': 'Oppenheimer Elementary', 'address': '2421 Scarboro Street Vancouver,  V5P 2L5',
     'google_map': 'https://www.google.com/maps/place/2421+Scarboro+Street+Vancouver,++V5P+2L5+++',
     'phone': '604-713-4570', 'website': 'https://www.vsb.bc.ca/david-oppenheimer'},
    {'school_name': 'Osler Elementary', 'address': '5970 Selkirk Street Vancouver,  V6M 2Y8',
     'google_map': 'https://www.google.com/maps/place/5970+Selkirk+Street+Vancouver,++V6M+2Y8+++',
     'phone': '604-713-4920', 'website': 'https://www.vsb.bc.ca/sir-william-osler'},
    {'school_name': 'Prince of Wales Secondary', 'address': '2250 Eddington Drive Vancouver,  V6L 2E7',
     'google_map': 'https://www.google.com/maps/place/2250+Eddington+Drive+Vancouver,++V6L+2E7+++',
     'phone': '604-713-8974', 'website': 'https://www.vsb.bc.ca/prince-wales'},
    {'school_name': 'Queen Alexandra Elementary', 'address': '1300 East Broadway Vancouver,  V5N 1V6',
     'google_map': 'https://www.google.com/maps/place/1300+East+Broadway+Vancouver,++V5N+1V6+++',
     'phone': '604-713-4599', 'website': 'https://www.vsb.bc.ca/queen-alexandra'},
    {'school_name': 'Queen Elizabeth Elementary', 'address': '4102 West 16th Avenue Vancouver,  V6R 3E3',
     'google_map': 'https://www.google.com/maps/place/4102+West+16th+Avenue+Vancouver,++V6R+3E3+++',
     'phone': '604-713-5408', 'website': 'https://www.vsb.bc.ca/queen-elizabeth'},
    {'school_name': 'Queen Mary Elementary', 'address': '2000 Trimble Street Vancouver,  V6R 3Z4',
     'google_map': 'https://www.google.com/maps/place/2000+Trimble+Street+Vancouver,++V6R+3Z4+++',
     'phone': '604-713-5464', 'website': 'https://www.vsb.bc.ca/queen-mary'},
    {'school_name': 'Queen Victoria Annex', 'address': '1850 East 3rd Avenue Vancouver,  V5N 1H2',
     'google_map': 'https://www.google.com/maps/place/1850+East+3rd+Avenue+Vancouver,++V5N+1H2+++',
     'phone': '604-713-4694', 'website': 'https://www.vsb.bc.ca/queen-victoria-annex'},
    {'school_name': 'Quilchena Elementary', 'address': '5300 Maple Street Vancouver,  V6N 3T6',
     'google_map': 'https://www.google.com/maps/place/5300+Maple+Street+Vancouver,++V6N+3T6+++',
     'phone': '604-713-5420', 'website': 'https://www.vsb.bc.ca/quilchena'},
    {'school_name': 'Renfrew Elementary', 'address': '3315 East 22nd Avenue Vancouver,  V5N 2Z2',
     'google_map': 'https://www.google.com/maps/place/3315+East+22nd+Avenue+Vancouver,++V5N+2Z2+++',
     'phone': '604-713-4851', 'website': 'https://www.vsb.bc.ca/renfrew'},
    {'school_name': 'Roberts Annex', 'address': '1150 Nelson Street Vancouver,  V6E 1J2',
     'google_map': 'https://www.google.com/maps/place/1150+Nelson+Street+Vancouver,++V6E+1J2+++',
     'phone': '604-713-5495', 'website': 'https://www.vsb.bc.ca/roberts-annex'},
    {'school_name': 'Roberts Elementary', 'address': '1100 Bidwell Street Vancouver,  V6G 2K4',
     'google_map': 'https://www.google.com/maps/place/1100+Bidwell+Street+Vancouver,++V6G+2K4+++',
     'phone': '604-713-5055', 'website': 'https://www.vsb.bc.ca/lord-roberts'},
    {'school_name': 'Secord Elementary', 'address': '2500 Lakewood Drive Vancouver,  V5N 4V1',
     'google_map': 'https://www.google.com/maps/place/2500+Lakewood+Drive+Vancouver,++V5N+4V1+++',
     'phone': '604-713-4996', 'website': 'https://www.vsb.bc.ca/laura-secord'},
    {'school_name': 'Selkirk Annex', 'address': '4444 Dumfries Street Vancouver,  V5N 3T2',
     'google_map': 'https://www.google.com/maps/place/4444+Dumfries+Street+Vancouver,++V5N+3T2+++',
     'phone': '604-713-4735', 'website': 'https://www.vsb.bc.ca/selkirk-annex'},
    {'school_name': 'Selkirk Elementary', 'address': '1750 East 22nd Avenue Vancouver,  V5N 2P7',
     'google_map': 'https://www.google.com/maps/place/1750+East+22nd+Avenue+Vancouver,++V5N+2P7+++',
     'phone': '604-713-4650', 'website': 'https://www.vsb.bc.ca/lord-selkirk'},
    {'school_name': 'Sexsmith Elementary', 'address': '7410 Columbia Street Vancouver,  V5X 3C1',
     'google_map': 'https://www.google.com/maps/place/7410+Columbia+Street+Vancouver,++V5X+3C1+++',
     'phone': '604-713-4901', 'website': 'https://www.vsb.bc.ca/jw-sexsmith'},
    {'school_name': 'Seymour Elementary', 'address': '1130 Keefer Street Vancouver,  V6A 1Z3',
     'google_map': 'https://www.google.com/maps/place/1130+Keefer+Street+Vancouver,++V6A+1Z3+++',
     'phone': '604-713-4641', 'website': 'https://www.vsb.bc.ca/admiral-seymour'},
    {'school_name': 'Shaughnessy Elementary', 'address': '4250 Marguerite Street Vancouver,  V6J 4G3',
     'google_map': 'https://www.google.com/maps/place/4250+Marguerite+Street+Vancouver,++V6J+4G3+++',
     'phone': '604-713-5500', 'website': 'https://www.vsb.bc.ca/shaughnessy'},
    {'school_name': 'South Hill Education Centre', 'address': '6010 Fraser Street Vancouver,  V5W 2Z7',
     'google_map': 'https://www.google.com/maps/place/6010+Fraser+Street+Vancouver,++V5W+2Z7+++',
     'phone': '604-713-5770', 'website': 'https://www.vsb.bc.ca/page/5245'},
    {'school_name': 'Southlands Elementary', 'address': '5351 Camosun Street Vancouver,  V6N 2C4',
     'google_map': 'https://www.google.com/maps/place/5351+Camosun+Street+Vancouver,++V6N+2C4+++',
     'phone': '604-713-5414', 'website': 'https://www.vsb.bc.ca/southlands'},
    {'school_name': 'staywate꞉n̓ Point Grey Secondary', 'address': '5350 East Boulevard Vancouver,  V6M 3V2',
     'google_map': 'https://www.google.com/maps/place/5350+East+Boulevard+Vancouver,++V6M+3V2+++',
     'phone': '604-713-8220', 'website': 'https://www.vsb.bc.ca/point-grey'},
    {'school_name': 'Strathcona Elementary', 'address': '592 East Pender Street Vancouver,  V6A 1V5',
     'google_map': 'https://www.google.com/maps/place/592+East+Pender+Street+Vancouver,++V6A+1V5+++',
     'phone': '604-713-4630', 'website': 'https://www.vsb.bc.ca/lord-strathcona'},
    {'school_name': 'šxʷəxʷaʔəs Thunderbird Elementary', 'address': '2325 Cassiar Street Vancouver,  V5M 3X3',
     'google_map': 'https://www.google.com/maps/place/2325+Cassiar+Street+Vancouver,++V5M+3X3+++',
     'phone': '604-713-4611', 'website': 'https://www.vsb.bc.ca/thunderbird'},
    {'school_name': 'šxʷwəq̓ʷəθət Crosstown Elementary', 'address': '55 Expo Boulevard Vancouver,  V6B 0P8',
     'google_map': 'https://www.google.com/maps/place/55+Expo+Boulevard+Vancouver,++V6B+0P8', 'phone': '604-713-5460',
     'website': 'https://www.vsb.bc.ca/crosstown'},
    {'school_name': 'Tecumseh Annex', 'address': '1551 East 37th Avenue Vancouver,  V5P 1E4',
     'google_map': 'https://www.google.com/maps/place/1551+East+37th+Avenue+Vancouver,++V5P+1E4+++',
     'phone': '604-713-4890', 'website': 'https://www.vsb.bc.ca/tecumseh-annex'},
    {'school_name': 'Tecumseh Elementary', 'address': '1850 East 41st Avenue Vancouver,  V5P 1K9',
     'google_map': 'https://www.google.com/maps/place/1850+East+41st+Avenue+Vancouver,++V5P+1K9+++',
     'phone': '604-713-5390', 'website': 'https://www.vsb.bc.ca/tecumseh'},
    {'school_name': 'Templeton Secondary', 'address': '727 Templeton Drive Vancouver,  V5L 4N8',
     'google_map': 'https://www.google.com/maps/place/727+Templeton+Drive+Vancouver,++V5L+4N8+++',
     'phone': '604-713-8984', 'website': 'https://www.vsb.bc.ca/templeton'},
    {'school_name': 'Tennyson Elementary', 'address': '2650 Maple Street Vancouver,  V6J 2B2',
     'google_map': 'https://www.google.com/maps/place/2650+Maple+Street+Vancouver,++V6J+2B2+++',
     'phone': '604-713-5426', 'website': 'https://www.vsb.bc.ca/lord-tennyson'},
    {'school_name': 'Tillicum Annex', 'address': '2450 Cambridge Street Vancouver,  V5K 1L2',
     'google_map': 'https://www.google.com/maps/place/2450+Cambridge+Street+Vancouver,++V5K+1L2+++',
     'phone': '604-713-4716', 'website': 'https://www.vsb.bc.ca/tillicum-annex'},
    {'school_name': 'Trafalgar Elementary', 'address': '4170 Trafalgar Street Vancouver,  V6L 2M5',
     'google_map': 'https://www.google.com/maps/place/4170+Trafalgar+Street+Vancouver,++V6L+2M5+++',
     'phone': '604-713-5475', 'website': 'https://www.vsb.bc.ca/trafalgar'},
    {'school_name': 'Trudeau Elementary', 'address': '449 East 62nd Avenue Vancouver,  V5X 2G2',
     'google_map': 'https://www.google.com/maps/place/449+East+62nd+Avenue+Vancouver,++V5X+2G2+++',
     'phone': '604-713-4865', 'website': 'https://www.vsb.bc.ca/pierre-elliott-trudeau'},
    {'school_name': 'Tupper Secondary', 'address': '419 East 24th Avenue Vancouver,  V5V 2A2',
     'google_map': 'https://www.google.com/maps/place/419+East+24th+Avenue+Vancouver,++V5V+2A2+++',
     'phone': '604-713-8233', 'website': 'https://www.vsb.bc.ca/sir-charles-tupper'},
    {'school_name': 'Tyee Elementary', 'address': '3525 Dumfries Street Vancouver,  V5N 3S5',
     'google_map': 'https://www.google.com/maps/place/3525+Dumfries+Street+Vancouver,++V5N+3S5+++',
     'phone': '604-713-4723', 'website': 'https://www.vsb.bc.ca/tyee'},
    {'school_name': 'University Hill Elementary', 'address': '5395 Chancellor Boulevard Vancouver,  V6T 1E2',
     'google_map': 'https://www.google.com/maps/place/5395+Chancellor+Boulevard+Vancouver,++V6T+1E2+++',
     'phone': '604-713-5350', 'website': 'https://www.vsb.bc.ca/university-hill-elementary'},
    {'school_name': 'University Hill Secondary', 'address': '3228 Ross Drive Vancouver,  V6S 0C6',
     'google_map': 'https://www.google.com/maps/place/3228+Ross+Drive+Vancouver,++V6S+0C6+++', 'phone': '604-713-8258',
     'website': 'https://www.vsb.bc.ca/university-hill'},
    {'school_name': 'Van Horne Elementary', 'address': '5855 Ontario Street Vancouver,  V5W 2L8',
     'google_map': 'https://www.google.com/maps/place/5855+Ontario+Street+Vancouver,++V5W+2L8+++',
     'phone': '604-713-4965', 'website': 'https://www.vsb.bc.ca/sir-william-van-horne'},
    {'school_name': 'Vancouver Learn Network Elem', 'address': '530 E 41st Ave Vancouver,  V5W 1P3',
     'google_map': 'https://www.google.com/maps/place/530+E+41st+Ave+Vancouver,++V5W+1P3', 'phone': '604-713-5520',
     'website': 'http://govsb.ca/vlne'},
    {'school_name': 'Vancouver Technical Secondary', 'address': '2600 East Broadway Vancouver,  V5M 1Y5',
     'google_map': 'https://www.google.com/maps/place/2600+East+Broadway+Vancouver,++V5M+1Y5+++',
     'phone': '604-713-8215', 'website': 'https://www.vsb.bc.ca/vancouver-technical'},
    {'school_name': 'Waverley Elementary', 'address': '6111 Elliott Street Vancouver,  V5S 2M1',
     'google_map': 'https://www.google.com/maps/place/6111+Elliott+Street+Vancouver,++V5S+2M1+++',
     'phone': '604-713-4752', 'website': 'https://www.vsb.bc.ca/waverley'},
    {'school_name': 'Weir Elementary', 'address': '2900 East 44th Avenue Vancouver,  V5R 3A8',
     'google_map': 'https://www.google.com/maps/place/2900+East+44th+Avenue+Vancouver,++V5R+3A8+++',
     'phone': '604-713-4771', 'website': 'https://www.vsb.bc.ca/dr-george-m-weir'},
    {'school_name': 'wək̓ʷan̓əs tə syaqʷəm Elementary', 'address': '3150 Kitchener Street Vancouver,  V5K 0G1',
     'google_map': 'https://www.google.com/maps/place/3150+Kitchener+Street+Vancouver,++V5K+0G1',
     'phone': '604-713-4686', 'website': 'https://www.vsb.bc.ca/sir-matthew-begbie'},
    {'school_name': 'Windermere Secondary', 'address': '3155 East 27th Avenue Vancouver,  V5R 1P3',
     'google_map': 'https://www.google.com/maps/place/3155+East+27th+Avenue+Vancouver,++V5R+1P3+++',
     'phone': '604-713-8180', 'website': 'https://www.vsb.bc.ca/windermere'},
    {'school_name': 'Wolfe Elementary', 'address': '4251 Ontario St Vancouver,  V5V 3G8',
     'google_map': 'https://www.google.com/maps/place/4251+Ontario+St+Vancouver,++V5V+3G8', 'phone': '604-713-4912',
     'website': 'https://www.vsb.bc.ca/general-wolfe'},
    {'school_name': 'χpey̓ Elementary', 'address': '1950 East Hastings Street Vancouver,  V5L 1T7',
     'google_map': 'https://www.google.com/maps/place/1950+East+Hastings+Street+Vancouver,++V5L+1T7+++',
     'phone': '604-713-4696', 'website': 'https://www.vsb.bc.ca/xpey'}
]



# Combine all school lists into one DataFrame
all_schools = (vancouver_schools)
schools_data = pd.DataFrame(all_schools)

# Adjust the address column to replace "+" with ", "
schools_data['address'] = schools_data['address'].str.replace('+', ', ', regex=False)

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Adding district names to the DataFrame
districts = [
    ("Vancouver", vancouver_schools)
]

# Assign district names to each row in the DataFrame
schools_data['district_name'] = ""
for district_name, schools_list in districts:
    for school in schools_list:
        schools_data.loc[schools_data['school_name'] == school['school_name'], 'district_name'] = district_name


# Function to generate markdown files
def generate_markdown_by_index(row):
    # Simplify the school name for the directory and file
    district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    path = os.path.join(output_dir, district_name_simple)
    os.makedirs(path, exist_ok=True)

    # Filename for the markdown
    file_path = os.path.join(path, f"{school_name_simple}.md")

    # Markdown content with front-matter and details
    with open(file_path, 'w') as file:
        file.write(f"---\nlayout: page\ntitle: {row['school_name']}\n---\n")  # School Name
        file.write(
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All British Columbia Districts]](../..) > [[All In Vancouver]](..)\n\n")

        file.write(f"# {row['school_name']} ({row['district_name']})\n\n")  # School Name and area as header

        # Loop through keys per school
        for key, value in row.items():
            if key not in ['district_name', 'school_name']:
                if str(value).startswith("http"):
                    value = "<" + value + ">"
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")

        file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        file.write(f"**School's policy on Ventilation**: TODO\n\n")
        file.write(f"**School's Ventilation Work Completion**: TODO\n\n")
        file.write(f"**School's Air-Purification**: TODO\n\n")
        file.write(f"**School's CO2 monitoring to actively drive ventilation and filtration**: TODO\n\n")
        file.write(f"**School's Wikidata URL**: TODO")
        file.write(f"\n\n\n[Edit this page](https://github.com/ventilate-schools/BC/edit/main/{file_path}).")
        file.write(f" See also [rules for contribution](../../../contribution-rules/)")


# Generate markdown files for each school
schools_data.apply(generate_markdown_by_index, axis=1)


def create_area_and_root_index():
    # Create a dictionary to keep track of schools in each district
    districts_dict = {}

    for index, row in schools_data.iterrows():
        district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
        school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the district already exists in the dictionary
        if district_name_simple not in districts_dict:
            districts_dict[district_name_simple] = []

        # Append the school name to the district's list
        districts_dict[district_name_simple].append(school_name_simple)

    # Write an index markdown file for each district and gather data for root index
    root_index_content = "---\ntitle: Schools in British Columbia and their ventilation status\n---\n"

    root_index_content += (
        "\n# Navigation\n\n[[All countries/states/provinces]](..)\n\n# Purpose of site\n\nGiven **COVID-19 is Airborne** and the world is pushing to better ventilate "
        "schools for long term student and teacher health, we're tracking the "
        "progress for that in British Columbia. This is ahead of government effort to do the same. If government starts to "
        "track this work, this effort will continue because that effort might be weak."
        "We're guided by 33 profs and PhDs who are pushing for a policy change in a "
        "March 2024 article on **Science.org**: [Mandating indoor air quality for public buildings](https://drive.google.com/file/d/16l_IH47cQtC7fFuafvHca7ORNVGITxx8/view). "
        "Not only active ventilation (which should "
        "be mechanical heat recovery type in this age), but air filtration/purification "
        "too and CO2 monitoring to drive ventilation levels, as CO2 inside is a proxy indicator "
        "for COVID risk. As it happens the WHO also have a [2023 airborne risk assessment guide](https://iris.who.int/handle/10665/376346)\n\n"
        "Know that other diseases are airborne too: Measles "
        "(studies [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810934/pdf/10982072.pdf) "
        "[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880795/pdf/nihms532643.pdf) "
        "[3](https://pubmed.ncbi.nlm.nih.gov/31257413/) "
        "[4](https://www.sciencedirect.com/science/article/pii/S0196655316305363)), "
        "Influenza, RSV and TB. The same "
        "ventilation and air filtration measures reduce transmission of those too.\n\n When we say "
        "student and teacher health, we're wanting absences to go down too. If we lower "
        "transmission in schools, we reduce multi-generation transmission too, as kids bring "
        "infections home to parents. With lowered transmission, we also reduce long COVID, "
        "where the worst sufferers have disappeared from education and the workplace.\n\n")

    root_index_content += (
        "\n## Leaderboard\n\n1. to be announced\n2. to be announced\n3. to be announced\n4. to be announced\n5. to be announced\n\n")

    root_index_content += ("{% include_relative grade.html %}\n\n")

    root_index_content += ("# British Columbia School Districts:\n\n")

    for district, schools in districts_dict.items():
        district_index_file_path = os.path.join(output_dir, district, "index.md")
        os.makedirs(os.path.join(output_dir, district), exist_ok=True)

        with open(district_index_file_path, 'w') as district_index_file:
            district_index_file.write(f"---\nlayout: page\ntitle: Schools in {district.replace('_', ' ')}\n---\n")
            district_index_file.write(
                f"# Navigation\n\n[[All countries/states/provinces]](../..) > [[All B.C. districts]](..)\n\n")
            district_index_file.write(f"# Schools in {district.replace('_', ' ')}\n\n")
            district_index_file.write("{% include_relative grade.html %}\n\n")
            district_index_file.write(f"**Schools:**\n\n")
            for school in schools:
                school_file_path = school
                district_index_file.write(f"- [{school.replace('_', ' ')}]({school_file_path}.md)\n")

        # Add to root index content with cleaner URLs
        root_index_content += f"- [{district.replace('_', ' ')}]({district}/): {len(schools)} schools\n"

    root_index_content += ("\n\n# Site ownership\n\nThis site is edited by volunteers who're "
                           "interested in accelerating the work to complete the adequate ventilation of British Columbia schools. "
                           "This effort was not commissioned by education authorities or government.\n\n"
                           "[Edit this page](https://github.com/ventilate-schools/BC/edit/main/index.md). See also [rules for contribution](./contribution_rules/)")

    # Write the root index file
    root_index_path = os.path.join(output_dir, "index.md")
    with open(root_index_path, 'w') as root_index_file:
        root_index_file.write(root_index_content)


# Call the function to create index markdown files and root index
create_area_and_root_index()

# Print confirmation
print("Index markdown files with front matter and links have been created in each area directory and root directory.")
