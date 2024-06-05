import os
import pandas as pd

schools = {
    "Chilliwack": [
        {
            "school_name": "A D Rundle Middle School",
            "address": "45660 Hocking Ave, Chilliwack, BC",
            "phone": "604-792-4257",
            "website": "https://adrundle.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Bernard Elementary",
            "address": "45465 Bernard Ave, Chilliwack, BC",
            "phone": "604-795-7840",
            "website": "https://bernard.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Cheam Elementary",
            "address": "9895 Banford Rd, Chilliwack, BC",
            "phone": "604-792-1416",
            "website": "https://cheam.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Chilliwack Central Elementary Community",
            "address": "9435 Young Rd, Chilliwack, BC",
            "phone": "604-792-8537",
            "website": "https://central.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Chilliwack Middle School",
            "address": "46354 Yale Rd, Chilliwack, BC",
            "phone": "604-795-5781",
            "website": "https://cms.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Chilliwack Secondary",
            "address": "46363 Yale Rd, Chilliwack, BC",
            "phone": "604-795-7295",
            "website": "https://css.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Cultus Lake Community School",
            "address": "71 Sunnyside Blvd, Cultus Lake, BC",
            "phone": "604-858-6266",
            "website": "https://cultuslake.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "East Chilliwack Elementary",
            "address": "49190 Chilliwack Central Rd, Chilliwack, BC",
            "phone": "604-794-7533",
            "website": "https://eastchilliwack.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Evans Elementary",
            "address": "7600 Evans Rd, Chilliwack, BC",
            "phone": "604-858-3057",
            "website": "https://evans.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "G.W. Graham Secondary",
            "address": "45955 Thomas Rd, Chilliwack, BC",
            "phone": "604-847-0772",
            "website": "https://gwgraham.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Greendale Elementary",
            "address": "6621 Sumas Prairie Rd, Chilliwack, BC",
            "phone": "604-823-6738",
            "website": "https://greendale.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Imagine High Integrated Arts/Technology",
            "address": "45669 Yale Rd, Chilliwack, BC",
            "phone": "604-792-9277",
            "website": "https://imaginehigh.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kw'íyeqel Secondary",
            "address": "8855 Elm Dr, Chilliwack, BC",
            "phone": "604-792-9277",
            "website": "https://kwiyekel.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Leary Integrated Arts & Technology",
            "address": "9320 Walden St, Chilliwack, BC",
            "phone": "604-792-1281",
            "website": "https://fgleary.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Little Mountain Elementary",
            "address": "9900 Carleton St, Chilliwack, BC",
            "phone": "604-792-0681",
            "website": "https://littlemountain.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "McCammon Elementary",
            "address": "9601 Hamilton St, Chilliwack, BC",
            "phone": "604-795-7000",
            "website": "https://mccammon.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mount Slesse Middle School",
            "address": "5871 Tyson Rd, Chilliwack, BC",
            "phone": "604-824-7481",
            "website": "https://msms.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Promontory Heights Community Elementary",
            "address": "46200 Stoneview Dr, Chilliwack, BC",
            "phone": "604-824-4885",
            "website": "https://promontory.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Robertson Elementary",
            "address": "46106 Southlands Cres, Chilliwack, BC",
            "phone": "604-795-5312",
            "website": "https://robertson.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Rosedale Traditional Community",
            "address": "50850 Yale Rd, Rosedale, BC",
            "phone": "604-794-7651",
            "website": "https://rosedale.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Sardis Elementary",
            "address": "45775 Manuel Rd, Chilliwack, BC",
            "phone": "604-858-7145",
            "website": "https://sardis.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Sardis Secondary",
            "address": "45460 Stevenson Rd, Chilliwack, BC",
            "phone": "604-858-9424",
            "website": "https://sardissecondary.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Stitó:s Lá:lém Totí:lt",
            "address": "5337 Tyson Road, Chilliwack, BC",
            "phone": "604-824-7450",
            "website": "https://stito-s.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Strathcona Elementary",
            "address": "46375 Strathcona Rd, Chilliwack, BC",
            "phone": "604-792-9301",
            "website": "https://strathcona.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Tyson Elementary",
            "address": "45170 S Sumas Rd, Chilliwack, BC",
            "phone": "604-858-3057",
            "website": "https://tyson.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Unsworth Elementary",
            "address": "5685 Unsworth Rd, Chilliwack, BC",
            "phone": "604-858-4510",
            "website": "https://unsworth.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Vedder Elementary",
            "address": "45850 Promontory Rd, Chilliwack, BC",
            "phone": "604-858-4759",
            "website": "https://vedder.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Vedder Middle School",
            "address": "45560 South Sumas Rd, Chilliwack, BC",
            "phone": "604-858-7141",
            "website": "https://veddermiddle.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Watson Elementary",
            "address": "45305 Watson Rd, Chilliwack, BC",
            "phone": "604-858-9477",
            "website": "https://watson.sd33.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Yarrow Community School",
            "address": "4605 Wilson Rd, Chilliwack, BC",
            "phone": "604-823-4408",
            "website": "https://yarrow.sd33.bc.ca",
            "students": "TODO"
        }
    ],
    "Abbotsford": [
        {
            "school_name": "Abbotsford School of Integrated Arts (ASIA) - North Poplar",
            "address": "32749 Cherry Ave, Mission, BC V2V 2T8",
            "phone": "604-826-2015",
            "website": "https://northpoplar.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Aberdeen Elementary",
            "address": "2975 Bradner Rd, Abbotsford, BC V4X 1K8",
            "phone": "604-856-7636",
            "website": "https://aberdeen.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Alexander Elementary",
            "address": "2250 Lobban Rd, Abbotsford, BC V2S 3W1",
            "phone": "604-853-3918",
            "website": "https://alexander.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Auguston Traditional Elementary",
            "address": "36367 Stephen Leacock Dr, Abbotsford, BC V3G 2Z6",
            "phone": "604-557-0422",
            "website": "https://auguston.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Barrowtown Elementary",
            "address": "5137 Tolmie Rd, Abbotsford, BC V3G 2V4",
            "phone": "604-854-5990",
            "website": "https://barrowtown.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "BlueJay Elementary",
            "address": "30995 Southern Dr, Abbotsford, BC V2T 5H9",
            "phone": "604-852-0685",
            "website": "https://bluejay.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Bradner Elementary",
            "address": "5291 Bradner Rd, Abbotsford, BC V4X 2P1",
            "phone": "604-856-3304",
            "website": "https://bradner.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dave Kandal Elementary",
            "address": "3351 Crestview Ave, Abbotsford, BC V2T 6T5",
            "phone": "604-853-7491",
            "website": "https://davekandal.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dormick Park Elementary",
            "address": "32161 Dormick Ave, Abbotsford, BC V2T 1J6",
            "phone": "604-859-3700",
            "website": "https://dormickpark.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dr. Roberta Bondar Elementary",
            "address": "32736 Huntingdon Rd, Abbotsford, BC V2T 5Z1",
            "phone": "604-859-3101",
            "website": "https://bondar.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dr. Thomas A. Swift Elementary",
            "address": "34800 Dewdney Trunk Rd, Mission, BC V2V 6Y3",
            "phone": "604-826-2481",
            "website": "https://swift.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "École Centennial Park Elementary",
            "address": "2527 Gladwin Rd, Abbotsford, BC V2T 3N8",
            "phone": "604-853-9148",
            "website": "https://centennialpark.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "École Clearbrook Elementary",
            "address": "3614 Clearbrook Rd, Abbotsford, BC V2T 6N3",
            "phone": "604-859-3134",
            "website": "https://clearbrook.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Godson Elementary",
            "address": "33130 Bevan Ave, Abbotsford, BC V2S 1T6",
            "phone": "604-853-2756",
            "website": "https://godson.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Harry Sayers Elementary",
            "address": "31321 Blueridge Dr, Abbotsford, BC V2T 6W2",
            "phone": "604-852-9665",
            "website": "https://harrysayers.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Irene Kelleher Totí:ltawtxw",
            "address": "34671 Blueridge Dr, Abbotsford, BC V2T 5W2",
            "phone": "604-859-3051",
            "website": "https://irenekelleher.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Jackson Elementary",
            "address": "33130 Bevan Ave, Abbotsford, BC V2S 1T6",
            "phone": "604-853-2756",
            "website": "https://jackson.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "John Maclure Community School",
            "address": "2990 Oriole Cres, Abbotsford, BC V2T 4E1",
            "phone": "604-859-3114",
            "website": "https://johnmaclure.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "King Traditional Elementary",
            "address": "28776 King Rd, Abbotsford, BC V4X 1C1",
            "phone": "604-857-0903",
            "website": "https://kingtraditional.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Margaret Stenersen Elementary",
            "address": "3060 Old Clayburn Rd, Abbotsford, BC V2S 4G5",
            "phone": "604-852-9665",
            "website": "https://stenersen.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mathxwí Elementary",
            "address": "2548 Bourquin Crescent W, Abbotsford, BC V2S 6Z7",
            "phone": "604-853-2994",
            "website": "https://mathxwi.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "McMillan Elementary",
            "address": "34830 Oakhill Dr, Abbotsford, BC V2S 7R4",
            "phone": "604-859-0126",
            "website": "https://mcmillan.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mountain Elementary",
            "address": "2299 Mountain Dr, Abbotsford, BC V3G 1E6",
            "phone": "604-852-8525",
            "website": "https://mountain.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mt. Lehman Elementary",
            "address": "28776 King Rd, Abbotsford, BC V4X 1C1",
            "phone": "604-856-3304",
            "website": "https://mtlehman.abbyschools.ca",
            "students": "TODO"
        },
        {
            "school_name": "Prince Charles Elementary",
            "address": "35410 McKee Rd, Abbotsford, BC V3G 3B1",
            "phone": "604-852-9323",
            "website": "https://princecharles.abbyschools.ca",
            "students": "TODO"
        }
    ],
    "Langley": [
        {
            "school_name": "Alex Hope Elementary",
            "address": "21150 85 Ave, Langley, BC V1M 2M4",
            "phone": "604-888-7109",
            "website": "https://alexhope.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Alice Brown Elementary",
            "address": "20011 44 Ave, Langley, BC V3A 6L8",
            "phone": "604-534-0744",
            "website": "https://alicebrown.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Belmont Elementary",
            "address": "20390 40 Ave, Langley, BC V3A 2X1",
            "phone": "604-533-3641",
            "website": "https://belmont.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Blacklock Fine Arts Elementary",
            "address": "5100 206 St, Langley, BC V3A 2E5",
            "phone": "604-530-3188",
            "website": "https://blacklock.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Coghlan Fundamental Elementary",
            "address": "4452 256 St, Langley, BC V4W 1J3",
            "phone": "604-856-8539",
            "website": "https://coghlan.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Dorothy Peacock Elementary",
            "address": "20292 91A Ave, Langley, BC V1M 2G2",
            "phone": "604-888-3397",
            "website": "https://dorothypeacock.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Douglas Park Community Elementary",
            "address": "5409 206 St, Langley, BC V3A 2C5",
            "phone": "604-533-4491",
            "website": "https://douglaspark.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Glenwood Elementary",
            "address": "20785 24 Ave, Langley, BC V2Z 2B4",
            "phone": "604-530-3188",
            "website": "https://glenwood.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "James Hill Elementary",
            "address": "22144 Old Yale Rd, Langley, BC V2Z 1B5",
            "phone": "604-530-0231",
            "website": "https://jameshill.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Langley Fundamental Elementary",
            "address": "21789 50 Ave, Langley, BC V3A 3T2",
            "phone": "604-530-9973",
            "website": "https://lfes.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Langley Fine Arts School",
            "address": "9096 Trattle St, Fort Langley, BC V1M 2S6",
            "phone": "604-888-3113",
            "website": "https://lfas.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Noel Booth Elementary",
            "address": "20202 35 Ave, Langley, BC V2Z 1A2",
            "phone": "604-530-9747",
            "website": "https://noelbooth.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "North Otter Elementary",
            "address": "5370 248 St, Langley, BC V4W 1A5",
            "phone": "604-856-3355",
            "website": "https://northotter.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Peterson Road Elementary",
            "address": "23422 47 Ave, Langley, BC V2Z 2S1",
            "phone": "604-534-7921",
            "website": "https://peterson.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "R.C. Garnett Demonstration Elementary",
            "address": "7096 201 St, Langley, BC V2Y 2Y1",
            "phone": "604-532-7814",
            "website": "https://rcgarnett.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Simonds Elementary",
            "address": "20190 48 Ave, Langley, BC V3A 3L4",
            "phone": "604-533-3643",
            "website": "https://simonds.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Topham Elementary",
            "address": "21555 91 Ave, Langley, BC V1M 2E4",
            "phone": "604-888-3041",
            "website": "https://topham.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Uplands Elementary",
            "address": "4471 207A St, Langley, BC V3A 5V8",
            "phone": "604-533-1285",
            "website": "https://uplands.sd35.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Walnut Grove Secondary",
            "address": "8919 Walnut Grove Dr, Langley, BC V1M 2N7",
            "phone": "604-882-0220",
            "website": "https://walnutgrove.sd35.bc.ca",
            "students": "TODO"
        }
    ],
    "Fraser-Cascade": [
        {
            "school_name": "Agassiz Centre for Education",
            "address": "PO Box 69, Agassiz, BC",
            "phone": "604-796-2225",
            "website": "https://sd78.bc.ca/school/agassiz-centre-for-education",
            "students": "TODO"
        },
        {
            "school_name": "Agassiz Elementary-Secondary School",
            "address": "PO Box 1100, Agassiz, BC",
            "phone": "604-796-2238",
            "website": "https://sd78.bc.ca/school/agassiz-elementary-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Boston Bar Elementary-Secondary School",
            "address": "PO Box 160, Boston Bar, BC",
            "phone": "604-867-9222",
            "website": "https://sd78.bc.ca/school/boston-bar-elementary-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Coquihalla Elementary School",
            "address": "PO Box 969, Hope, BC",
            "phone": "604-869-9904",
            "website": "https://sd78.bc.ca/school/coquihalla-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Harrison Hot Springs Elementary School",
            "address": "PO Box 310, Harrison Hot Springs, BC",
            "phone": "604-796-2838",
            "website": "https://sd78.bc.ca/school/harrison-hot-springs-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Hope Secondary School",
            "address": "PO Box 249, Hope, BC",
            "phone": "604-869-9971",
            "website": "https://sd78.bc.ca/school/hope-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Kent Elementary School",
            "address": "7285 McCullough Rd, Agassiz, BC",
            "phone": "604-796-2161",
            "website": "https://sd78.bc.ca/school/kent-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Silver Creek Elementary School",
            "address": "PO Box 670, Hope, BC",
            "phone": "604-869-5212",
            "website": "https://sd78.bc.ca/school/silver-creek-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Two Rivers Education Centre",
            "address": "PO Box 108, Hope, BC",
            "phone": "604-869-2411",
            "website": "https://sd78.bc.ca/school/two-rivers-education-centre",
            "students": "TODO"
        }
    ],
    "Maple Ridge – Pitt Meadows": [
        {
            "school_name": "Albion Elementary",
            "address": "10031 240th St, Maple Ridge, BC",
            "phone": "604-467-0033",
            "website": "https://albion.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Alexander Robinson Elementary",
            "address": "11849 238b St, Maple Ridge, BC",
            "phone": "604-466-5760",
            "website": "https://alexanderrobinson.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Alouette Elementary",
            "address": "22155 Isaac Cres, Maple Ridge, BC",
            "phone": "604-463-8730",
            "website": "https://alouette.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Blue Mountain Elementary",
            "address": "12453 248 St, Maple Ridge, BC",
            "phone": "604-463-6414",
            "website": "https://bluemountain.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Davie Jones Elementary",
            "address": "12030 Blakely Rd, Pitt Meadows, BC",
            "phone": "604-465-4920",
            "website": "https://daviejones.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Edith McDermott Elementary",
            "address": "12178 Bonson Rd, Pitt Meadows, BC",
            "phone": "604-465-5441",
            "website": "https://edithmcdermott.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Eric Langton Elementary",
            "address": "12138 Edge St, Maple Ridge, BC",
            "phone": "604-463-3810",
            "website": "https://ericlangton.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Fairview Elementary",
            "address": "12209 206 St, Maple Ridge, BC",
            "phone": "604-465-9331",
            "website": "https://fairview.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Golden Ears Elementary",
            "address": "23124 118 Ave, Maple Ridge, BC",
            "phone": "604-463-9513",
            "website": "https://goldenears.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Hammond Elementary",
            "address": "11520 203 St, Maple Ridge, BC",
            "phone": "604-465-5828",
            "website": "https://hammond.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Harry Hooge Elementary",
            "address": "12280 230 St, Maple Ridge, BC",
            "phone": "604-463-3920",
            "website": "https://harryhooge.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Highland Park Elementary",
            "address": "18961 Advent Rd, Pitt Meadows, BC",
            "phone": "604-465-6737",
            "website": "https://highlandpark.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kanaka Creek Elementary",
            "address": "11120 234a St, Maple Ridge, BC",
            "phone": "604-463-9804",
            "website": "https://kanakacreek.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Laity View Elementary",
            "address": "21023 123 Ave, Maple Ridge, BC",
            "phone": "604-463-9823",
            "website": "https://laityview.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Maple Ridge Elementary",
            "address": "20820 River Rd, Maple Ridge, BC",
            "phone": "604-463-5003",
            "website": "https://mapleridge.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Pitt Meadows Elementary",
            "address": "11941 Harris Rd, Pitt Meadows, BC",
            "phone": "604-465-5828",
            "website": "https://pittmeadows.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Westview Secondary",
            "address": "20905 Wicklund Ave, Maple Ridge, BC",
            "phone": "604-467-3481",
            "website": "https://westview.sd42.ca",
            "students": "TODO"
        },
        {
            "school_name": "Yennadon Elementary",
            "address": "23347 128 Ave, Maple Ridge, BC",
            "phone": "604-467-5551",
            "website": "https://yennadon.sd42.ca",
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