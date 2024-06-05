import os
import pandas as pd

schools = {
    "Cariboo-Chilcotin": [
        {
            "school_name": "100 Mile House Elementary",
            "address": "Po Box 460, 100 Mile House, BC",
            "phone": "250-395-2258",
            "website": "https://100mile.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "150 Mile Elementary",
            "address": "Po Box 259, 150 Mile House, BC",
            "phone": "250-296-3356",
            "website": "https://150mile.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Alexis Creek Elementary/Secondary",
            "address": "Po Box 199, Alexis Creek, BC",
            "phone": "250-481-2228",
            "website": "https://alexis.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Anahim Lake Elem-Jr Secondary",
            "address": "Po Box 3350, Anahim Lake, BC",
            "phone": "250-742-3333",
            "website": "https://anahim.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Big Lake Elementary",
            "address": "Box 70, Big Lake, BC",
            "phone": "250-243-2345",
            "website": "https://biglake.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Cataline Elementary",
            "address": "1175 Blair St, Williams Lake, BC",
            "phone": "250-392-5255",
            "website": "https://cataline.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Chilcotin Road Elementary",
            "address": "709 Lyne Rd, Williams Lake, BC",
            "phone": "250-398-5778",
            "website": "https://chilcotinroad.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Columneetza Junior Secondary",
            "address": "1045 Western Ave, Williams Lake, BC",
            "phone": "250-392-4331",
            "website": "https://columneetza.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dog Creek Elem-Secondary",
            "address": "General Delivery, Dog Creek, BC",
            "phone": "250-440-5644",
            "website": "https://dogcreek.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Forest Grove Elementary",
            "address": "Po Box 99, Forest Grove, BC",
            "phone": "250-397-2962",
            "website": "https://forestgrove.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Horse Lake Elementary",
            "address": "6548 Ryall Rd, Lone Butte, BC",
            "phone": "250-395-4572",
            "website": "https://horselake.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Horsefly Elem-Jr Secondary",
            "address": "Po Box 39, Horsefly, BC",
            "phone": "250-620-3438",
            "website": "https://horsefly.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Lac La Hache Elementary",
            "address": "Po Box 128, Lac La Hache, BC",
            "phone": "250-396-7230",
            "website": "https://laclahache.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Lake City Secondary",
            "address": "640 Carson Drive, Williams Lake, BC",
            "phone": "250-392-5288",
            "website": "https://lakecitysecondary.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Likely Elem-Jr Secondary",
            "address": "Po Box 57, Likely, BC",
            "phone": "250-790-2337",
            "website": "https://likely.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Marie Sharpe Elementary",
            "address": "260 Cameron St, Williams Lake, BC",
            "phone": "250-392-4104",
            "website": "https://mariesharpe.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mile 108 Elementary",
            "address": "Po Box 27, 108 Mile Ranch, BC",
            "phone": "250-791-5221",
            "website": "https://mile108.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mountview Elementary",
            "address": "1222 Dog Creek Rd, Williams Lake, BC",
            "phone": "250-392-7344",
            "website": "https://mountview.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Naghtaneqed Elem-Jr Secondary",
            "address": "Po Box 100, Nemaiah Valley, BC",
            "phone": "250-468-5788",
            "website": "https://naghtaneqed.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nesika Elementary",
            "address": "1180 Moon Ave, Williams Lake, BC",
            "phone": "250-398-7192",
            "website": "https://nesika.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "PSO Outback Storefront",
            "address": "Po Box 910, 100 Mile House, BC",
            "phone": "250-395-2461",
            "website": "https://psooutback.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Peter Skene Ogden Secondary",
            "address": "Po Box 910, 100 Mile House, BC",
            "phone": "250-395-2461",
            "website": "https://peterskene.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Skyline Alternate School",
            "address": "320 Second Ave N, Williams Lake, BC",
            "phone": "250-398-5571",
            "website": "https://skyline.sd27.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Tatla Lake Elem-Jr Secondary",
            "address": "Po Box 56, Tatla Lake, BC",
            "phone": "250-476-1131",
            "website": "https://tatlalake.sd27.bc.ca",
            "students": "TODO"
        }
    ],
    "Quesnel": [
        {
            "school_name": "Barlow Creek Elementary",
            "address": "816 Barkerville Hwy, Quesnel, BC",
            "phone": "250-992-5134",
            "website": "https://barlowcreek.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Bouchie Lake Elementary",
            "address": "2074 Blackwater Rd, Quesnel, BC",
            "phone": "250-249-5880",
            "website": "https://bouchielake.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Carson Elementary",
            "address": "1255 Graham Ave, Quesnel, BC",
            "phone": "250-992-6821",
            "website": "https://carson.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dragon Lake Elementary",
            "address": "2671 Hydraulic Rd, Quesnel, BC",
            "phone": "250-747-2097",
            "website": "https://dragonlake.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "École Red Bluff Lhtako Elementary",
            "address": "1533 Maple Dr, Quesnel, BC",
            "phone": "250-747-2634",
            "website": "https://redbluff.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kersley Elementary",
            "address": "2899 Arnoldus Rd, Quesnel, BC",
            "phone": "250-747-2624",
            "website": "https://kersley.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Lakeview Elementary",
            "address": "1525 Beryl St, Quesnel, BC",
            "phone": "250-747-2009",
            "website": "https://lakeview.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nazko Valley Elementary",
            "address": "9560 Nazko Rd, Quesnel, BC",
            "phone": "250-249-5600",
            "website": "https://nazko.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Parkland Elementary",
            "address": "5016 Bjornson Rd, Quesnel, BC",
            "phone": "250-747-2003",
            "website": "https://parkland.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Riverview Elementary",
            "address": "346 Hartley St, Quesnel, BC",
            "phone": "250-992-7217",
            "website": "https://riverview.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Voyageur Elementary",
            "address": "1337 Lark Ave, Quesnel, BC",
            "phone": "250-992-2613",
            "website": "https://voyageur.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Wells Elementary",
            "address": "Po Box 190, Wells, BC",
            "phone": "250-994-3216",
            "website": "https://wells.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Quesnel Junior School",
            "address": "950 Mountain Ash Rd, Quesnel, BC",
            "phone": "250-747-2103",
            "website": "https://qjs.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Correlieu Secondary",
            "address": "850 Anderson Dr, Quesnel, BC",
            "phone": "250-992-7007",
            "website": "https://css.sd28.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "McNaughton Centre",
            "address": "241 Kinchant St, Quesnel, BC",
            "phone": "250-992-5614",
            "website": "https://mcnaughton.sd28.bc.ca",
            "students": "TODO"
        }
    ],
    "Central Coast": [
        {
            "school_name": "Bella Coola Elementary School",
            "address": "Box 158, Bella Coola, BC",
            "phone": "250-799-5312",
            "website": "https://www.sd49.bc.ca/schools/bella-coola-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Nusatsum Elementary School",
            "address": "Box 129, Hagensborg, BC",
            "phone": "250-982-2696",
            "website": "https://www.sd49.bc.ca/schools/nusatsum-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Sir Alexander Mackenzie Secondary School",
            "address": "Box 800, Hagensborg, BC",
            "phone": "250-982-2355",
            "website": "https://www.sd49.bc.ca/schools/sir-alexander-mackenzie-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Shearwater Elementary School",
            "address": "Box 80, Denny Island, BC",
            "phone": "250-957-2427",
            "website": "https://www.sd49.bc.ca/schools/shearwater-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Wuikinuxv Elementary School",
            "address": "Box 59, Rivers Inlet, BC",
            "phone": "250-396-7081",
            "website": "https://www.sd49.bc.ca/schools/wuikinuxv-elementary",
            "students": "TODO"
        }
    ],
    "Bulkley Valley": [
        {
            "school_name": "Muheim Elementary",
            "address": "3659 3rd Ave, Smithers, BC",
            "phone": "250-847-2688",
            "website": "https://mme.sd54.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Walnut Park Elementary",
            "address": "4092 Mountainview Drive, Smithers, BC",
            "phone": "250-847-4464",
            "website": "https://wps.sd54.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Telkwa Elementary",
            "address": "PO Box 190, Telkwa, BC",
            "phone": "250-846-5999",
            "website": "https://tes.sd54.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Silverthorne Elementary",
            "address": "PO Box 430, Houston, BC",
            "phone": "250-845-2228",
            "website": "https://ses.sd54.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Twain Sullivan Elementary",
            "address": "PO Box 260, Houston, BC",
            "phone": "250-845-2244",
            "website": "https://tses.sd54.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Smithers Secondary",
            "address": "PO Box 848, Smithers, BC",
            "phone": "250-847-2231",
            "website": "https://sss.sd54.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Houston Secondary",
            "address": "PO Box 158, Houston, BC",
            "phone": "250-845-7217",
            "website": "https://hss.sd54.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Bulkley Valley Learning Centre",
            "address": "PO Box 849, Smithers, BC",
            "phone": "250-877-3218",
            "website": "https://bvlc.sd54.bc.ca",
            "students": "TODO"
        }
    ],
    "Peace River North": [
        {
            "school_name": "Alwin Holland Elementary",
            "address": "10615 96th St, Fort St. John, BC",
            "phone": "250-785-6125",
            "website": "https://alwinholland.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Bert Ambrose Elementary",
            "address": "9616 115 St, Fort St. John, BC",
            "phone": "250-785-2321",
            "website": "https://bertambrose.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Baldonnel Elementary",
            "address": "PO Box 90, Baldonnel, BC",
            "phone": "250-789-3396",
            "website": "https://baldonnel.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Charlie Lake Elementary",
            "address": "PO Box 68, Charlie Lake, BC",
            "phone": "250-785-2025",
            "website": "https://charlielake.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Clearview Elementary-Jr Secondary",
            "address": "PO Box 340, Clearview, BC",
            "phone": "250-781-3333",
            "website": "https://clearview.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "CM Finch Elementary",
            "address": "10904 106 St, Fort St. John, BC",
            "phone": "250-785-8580",
            "website": "https://cmfinch.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dr. Kearney Middle School",
            "address": "10717 100 St, Fort St. John, BC",
            "phone": "250-785-8378",
            "website": "https://drkearney.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Ecole Central Elementary",
            "address": "10615 100th St, Fort St. John, BC",
            "phone": "250-785-4511",
            "website": "https://central.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Fort St. John Secondary",
            "address": "10215 99 Ave, Fort St. John, BC",
            "phone": "250-785-4429",
            "website": "https://fss.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Hudson's Hope Elementary-Secondary",
            "address": "PO Box 189, Hudson's Hope, BC",
            "phone": "250-783-9994",
            "website": "https://hudsonhope.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Robert Ogilvie Elementary",
            "address": "9907 86 St, Fort St. John, BC",
            "phone": "250-785-3704",
            "website": "https://roberttogilvie.prn.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Upper Pine Elementary-Jr Secondary",
            "address": "PO Box 70, Rose Prairie, BC",
            "phone": "250-827-3676",
            "website": "TODO",
            "students": "TODO"
        }
    ],
    "Peace River South": [
        {
            "school_name": "Canalta Elementary",
            "address": "1901 110 Ave, Dawson Creek, BC",
            "phone": "250-782-8403",
            "website": "https://canalta.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Chetwynd Secondary",
            "address": "5000-46 Street, Chetwynd, BC",
            "phone": "250-788-2267",
            "website": "https://chetwyndsecondary.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Crescent Park Elementary",
            "address": "9300 17 St, Dawson Creek, BC",
            "phone": "250-782-8412",
            "website": "https://crescentpark.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dawson Creek Secondary (Central Campus)",
            "address": "10701 10 St, Dawson Creek, BC",
            "phone": "250-784-7676",
            "website": "https://dcss.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Devereaux Elementary",
            "address": "11600 7th St, Dawson Creek, BC",
            "phone": "250-843-7300",
            "website": "https://devereaux.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Don Titus Montessori",
            "address": "Po Box 538, Chetwynd, BC",
            "phone": "250-788-2531",
            "website": "https://dontitus.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "École Frank Ross Elementary",
            "address": "1000 92 Ave, Dawson Creek, BC",
            "phone": "250-782-5206",
            "website": "https://frankross.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Little Prairie Elementary",
            "address": "Po Box 1600, Chetwynd, BC",
            "phone": "250-788-1924",
            "website": "https://littleprairie.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "McLeod Elementary Secondary",
            "address": "Po Box 157, Groundbirch, BC",
            "phone": "250-843-7374",
            "website": "https://mcleod.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Moberly Lake Elementary",
            "address": "6531 Lakeshore Drive, Moberly Lake, BC",
            "phone": "250-788-2574",
            "website": "https://moberlylake.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Parkland Elementary",
            "address": "11600 7 St, Dawson Creek, BC",
            "phone": "250-843-7777",
            "website": "https://parkland.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Peace View School",
            "address": "11600 7th St, Dawson Creek, BC",
            "phone": "250-789-2280",
            "website": "https://peaceview.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Pouce Coupe Elementary",
            "address": "Po Box 7, Pouce Coupe, BC",
            "phone": "250-786-5314",
            "website": "https://pouce.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "South Peace Elementary",
            "address": "11600 7th St, Dawson Creek, BC",
            "phone": "778-299-2037",
            "website": "https://southpeace.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Tremblay Elementary",
            "address": "11311 13a St, Dawson Creek, BC",
            "phone": "250-782-8147",
            "website": "https://tremblay.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Tumbler Ridge Elementary",
            "address": "Po Box 700, Tumbler Ridge, BC",
            "phone": "250-242-5281",
            "website": "https://tumbler.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Tumbler Ridge Secondary",
            "address": "180 Southgate, Tumbler Ridge, BC",
            "phone": "250-242-4227",
            "website": "https://trs.sd59.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Windrem Elementary",
            "address": "Po Box 210, Chetwynd, BC",
            "phone": "250-788-2214",
            "website": "https://windrem.sd59.bc.ca",
            "students": "TODO"
        }
    ],
    "Coast Mountains": [
        {
            "school_name": "Bear Valley (K-12)",
            "address": "Box 218 824 Main Street, Stewart, BC V0T 1W0",
            "phone": "250-636-2238",
            "website": "http://bearvalley.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Caledonia Secondary (10-12)",
            "address": "3605 Munroe Street, Terrace, BC V8G 3C4",
            "phone": "250-635-6531",
            "website": "http://caledonia.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Cassie Hall Elementary (K-6)",
            "address": "2620 Eby Street, Terrace, BC V8G 2X3",
            "phone": "250-635-5646",
            "website": "http://cassiehall.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Ecole Mountainview (K-6)",
            "address": "3505 Bailey Street, Terrace, BC V8G 5P5",
            "phone": "250-635-3115",
            "website": "http://mountainview.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Hazelton Secondary (8-12)",
            "address": "Box 300 2725 Highway 62, Hazelton, BC V0J 1Y0",
            "phone": "250-842-5214",
            "website": "http://hazeltonsec.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kildala Elementary (K-6)",
            "address": "803 Columbia Street, Kitimat, BC V8C 1V7",
            "phone": "250-632-6194",
            "website": "http://kildala.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kitimat City High",
            "address": "1426 Cormorant Street, Kitimat, BC V8C 1R8",
            "phone": "250-632-2811",
            "website": "http://kitimatcityhigh.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kitwanga Elementary (K-7)",
            "address": "Box 88 3650 School Road, Kitwanga, BC V0J 2A0",
            "phone": "250-849-5484",
            "website": "http://kitwanga.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Majagaleehl Gali Aks Elementary (K-7)",
            "address": "Box 240 3990 John Field Road, Hazelton, BC V0J 1Y0",
            "phone": "250-842-5313",
            "website": "http://majagaleehl.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mount Elizabeth Middle/Secondary (7-12)",
            "address": "1491 Kingfisher Avenue, Kitimat, BC V8C 1E9",
            "phone": "250-632-6174",
            "website": "http://mountelizabeth.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nechako Elementary (K-6)",
            "address": "61 Nightingale Street, Kitimat, BC V8C 1M9",
            "phone": "250-632-2912",
            "website": "http://nechako.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "New Hazelton Elementary (K-7)",
            "address": "Box 220 3275 Bowser Street, New Hazelton, BC V0J 2J0",
            "phone": "250-842-5777",
            "website": "http://newhazelton.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Northwest Trades & Employment Training Centre",
            "address": "3120 Highway 16, Terrace, BC",
            "phone": "250-635-7944",
            "website": "http://ncdes.ca",
            "students": "TODO"
        },
        {
            "school_name": "Parkside Secondary",
            "address": "3824 Eby Street, Terrace, BC",
            "phone": "250-635-5778",
            "website": "http://parkside.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Skeena Middle School (7-9)",
            "address": "3411 Munroe Street, Terrace, BC V8G 3C1",
            "phone": "250-635-9136",
            "website": "http://skeena.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Suwilaawks Community School (K-6)",
            "address": "3430 Sparks Street, Terrace, BC V8G 2V3",
            "phone": "250-635-5624",
            "website": "http://suwilaawks.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Thornhill Elementary (4-6)",
            "address": "3210 Highway 16 East, Thornhill, BC V8G 4R7",
            "phone": "250-635-5082",
            "website": "http://thornhill.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Thornhill Primary (K-3)",
            "address": "3480 Paquette Avenue, Thornhill, BC V8G 4E9",
            "phone": "250-635-5081",
            "website": "http://thornhill.cmsd.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Uplands Elementary (K-6)",
            "address": "4110 Thomas Street, Terrace, BC V8G 4L7",
            "phone": "250-635-2721",
            "website": "http://uplands.cmsd.bc.ca",
            "students": "TODO"
        }
    ],
    "Nechako Lakes": [
        {
            "school_name": "Babine Elementary-Secondary",
            "address": "Po Box 250, Granisle, BC",
            "phone": "250-697-2291",
            "website": "https://babine.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "David Hoy Elementary",
            "address": "Po Box 880, Fort St James, BC",
            "phone": "250-996-8246",
            "website": "https://davidhoy.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Decker Lake Elementary",
            "address": "6710 Decker Lake Frtg Rd, Burns Lake, BC",
            "phone": "250-698-7301",
            "website": "https://deckerlake.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Evelyn Dickson Elementary",
            "address": "Po Box 1970, Vanderhoof, BC",
            "phone": "250-567-5544",
            "website": "https://evelyndickson.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Fort St James Secondary",
            "address": "Po Box 220, Fort St James, BC",
            "phone": "250-996-7017",
            "website": "https://fsjss.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Francois Lake Elementary",
            "address": "860 Francois Lake Road, Burns Lake, BC",
            "phone": "250-695-6641",
            "website": "https://francoislake.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Fraser Lake Elementary-Secondary",
            "address": "Po Bag Service 1002, Fraser Lake, BC",
            "phone": "250-699-6233",
            "website": "https://fraserlake.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Grassy Plains School",
            "address": "34310 Keefes Landing Rd, Burns Lake, BC",
            "phone": "250-694-3683",
            "website": "https://grassyplains.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Lakes District Secondary",
            "address": "Box 3000, Burns Lake, BC",
            "phone": "250-692-7733",
            "website": "https://ldss.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mapes Elementary",
            "address": "14907 Mapes Rd, Vanderhoof, BC",
            "phone": "250-567-4393",
            "website": "https://mapes.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mouse Mountain Elementary",
            "address": "Postal Bag 3001, Fraser Lake, BC",
            "phone": "250-699-6747",
            "website": "https://mousemountain.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nechako Valley Secondary",
            "address": "Po Box 950, Vanderhoof, BC",
            "phone": "250-567-2291",
            "website": "https://nvss.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Sinkutview Elementary",
            "address": "3348 Sinkut View Rd, Vanderhoof, BC",
            "phone": "250-567-2267",
            "website": "https://sinkutview.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "W L Mcleod Elementary",
            "address": "Po Box 559, Vanderhoof, BC",
            "phone": "250-567-2261",
            "website": "https://wlmcleod.sd91.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "William Konkin Elementary",
            "address": "Box 7000, Burns Lake, BC",
            "phone": "250-692-3146",
            "website": "https://wke.sd91.bc.ca",
            "students": "TODO"
        }
    ],
    "Nisga’a": [
        {
            "school_name": "Nisga'a Elementary Secondary School",
            "address": "5000 Skateen Avenue, PO Box 239, New Aiyansh, BC V0J 1A0",
            "phone": "250-633-2225",
            "website": "https://ness.nisgaa.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Gitwinksihlkw Elementary School",
            "address": "PO Box 120, Gitwinksihlkw, BC V0J 3T0",
            "phone": "250-633-2657",
            "website": "https://ges.nisgaa.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Alvin A. McKay Elementary School",
            "address": "311 Church St., PO Box 220, Laxgalts’ap, BC V0J 1X0",
            "phone": "250-621-3277",
            "website": "https://aames.nisgaa.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nathan Barton Elementary School",
            "address": "1310 Volunteer St., Gingolx, BC V0V 1B0",
            "phone": "250-326-4206",
            "website": "https://nbes.nisgaa.bc.ca",
            "students": "TODO"
        }
    ]
}

# Combine all school lists into one DataFrame
schools_data = pd.DataFrame([school for district in schools.values() for school in district])

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Assign district names to each row in the DataFrame
for district_name, schools_list in schools.items():
    district_name = district_name.replace(" Dist.", "").replace(" District", "").replace(" Public School District", "").replace(" School District", "").replace(" School Dist", "").replace(" Public School", "").rstrip('.')

    for school in schools_list:
        school['address'] = school['address'].replace('+', ', ')
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
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All British Columbia Districts]](../..) > [[All In {row['district_name']}]](..)\n\n")

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