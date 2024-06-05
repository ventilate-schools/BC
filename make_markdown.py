import os
import pandas as pd

schools = {
    "Surrey": [
        {
            "school_name": "A.H.P. Matthew",
            "address": "13367-97 Avenue, Surrey, BC V3T 1A4",
            "phone": "604-588-3415",
            "website": "https://www.surreyschools.ca/schools/ahpmatthew",
            "students": "TODO"
        },
        {
            "school_name": "A.J. McLellan",
            "address": "16545-61 Avenue, Surrey, BC V3S 5V4",
            "phone": "604-574-7296",
            "website": "https://www.surreyschools.ca/schools/ajmclellan",
            "students": "TODO"
        },
        {
            "school_name": "Adams Road",
            "address": "18228 68 Avenue, Surrey, BC V3S 9H5",
            "phone": "604-595-1070",
            "website": "https://www.surreyschools.ca/schools/adamsroad",
            "students": "TODO"
        },
        {
            "school_name": "Bayridge",
            "address": "1730-142 Street, Surrey, BC V4A 6G7",
            "phone": "604-531-8082",
            "website": "https://www.surreyschools.ca/schools/bayridge",
            "students": "TODO"
        },
        {
            "school_name": "Bear Creek",
            "address": "13780-80 Avenue, Surrey, BC V3W 7X6",
            "phone": "604-594-7501",
            "website": "https://www.surreyschools.ca/schools/bearcreek",
            "students": "TODO"
        },
        {
            "school_name": "Beaver Creek",
            "address": "6505-123A Street, Surrey, BC V3W 5Y5",
            "phone": "604-572-6911",
            "website": "https://www.surreyschools.ca/schools/beavercreek",
            "students": "TODO"
        },
        {
            "school_name": "Berkshire Park",
            "address": "15372-94 Avenue, Surrey, BC V3R 1E3",
            "phone": "604-583-7305",
            "website": "https://www.surreyschools.ca/schools/berkshirepark",
            "students": "TODO"
        },
        {
            "school_name": "Betty Huff",
            "address": "13055 Huntley Avenue, Surrey, BC V3V 1V1",
            "phone": "604-585-3104",
            "website": "https://www.surreyschools.ca/schools/bettyhuff",
            "students": "TODO"
        },
        {
            "school_name": "Bonaccord",
            "address": "14986-98 Avenue, Surrey, BC V3R 1J1",
            "phone": "604-584-3533",
            "website": "https://www.surreyschools.ca/schools/bonaccord",
            "students": "TODO"
        },
        {
            "school_name": "Bothwell",
            "address": "17070-102 Avenue, Surrey, BC V4N 4N6",
            "phone": "604-589-0369",
            "website": "https://www.surreyschools.ca/schools/bothwell",
            "students": "TODO"
        },
        {
            "school_name": "Boundary Park",
            "address": "12332 N.Boundary Drive, Surrey, BC V3X 1Z6",
            "phone": "604-543-8158",
            "website": "https://www.surreyschools.ca/schools/boundarypark",
            "students": "TODO"
        },
        {
            "school_name": "Bridgeview",
            "address": "12834-115A Avenue, Surrey, BC V3R 2X4",
            "phone": "604-580-1047",
            "website": "https://www.surreyschools.ca/schools/bridgeview",
            "students": "TODO"
        },
        {
            "school_name": "Brookside",
            "address": "8555-142A Street, Surrey, BC V3W 0S6",
            "phone": "604-596-8561",
            "website": "https://www.surreyschools.ca/schools/brookside",
            "students": "TODO"
        },
        {
            "school_name": "Cambridge",
            "address": "6115 150 Street, Surrey, BC V3S 3H7",
            "phone": "604-595-4036",
            "website": "https://www.surreyschools.ca/schools/cambridge",
            "students": "TODO"
        },
        {
            "school_name": "Cedar Hills",
            "address": "12370-98 Avenue, Surrey, BC V3V 2K3",
            "phone": "604-581-0407",
            "website": "https://www.surreyschools.ca/schools/cedarhills",
            "students": "TODO"
        },
        {
            "school_name": "Chantrell Creek",
            "address": "2575-137 Street, Surrey, BC V4P 2K5",
            "phone": "604-535-6708",
            "website": "https://www.surreyschools.ca/schools/chantrellcreek",
            "students": "TODO"
        },
        {
            "school_name": "Chimney Hill",
            "address": "14755-74 Avenue, Surrey, BC V3S 8Y8",
            "phone": "604-592-2913",
            "website": "https://www.surreyschools.ca/schools/chimneyhill",
            "students": "TODO"
        },
        {
            "school_name": "Cindrich",
            "address": "13455-90 Avenue, Surrey, BC V3V 8A2",
            "phone": "604-590-3211",
            "website": "https://www.surreyschools.ca/schools/cindrich",
            "students": "TODO"
        },
        {
            "school_name": "City Central Learning Centre",
            "address": "13104-109 Avenue, Surrey, BC V3T 2N7",
            "phone": "604-581-0611",
            "website": "https://www.surreyschools.ca/schools/citycentrallc",
            "students": "TODO"
        },
        {
            "school_name": "Clayton Heights",
            "address": "7003-188 Street, Surrey, BC V4N 3G6",
            "phone": "604-576-4138",
            "website": "https://www.surreyschools.ca/schools/claytonheights",
            "students": "TODO"
        },
        {
            "school_name": "Cloverdale Learning Centre",
            "address": "#200, 5658 - 176 Street, Surrey, BC V3S 4C6",
            "phone": "604-574-3615",
            "website": "https://www.surreyschools.ca/schools/cloverdalelc",
            "students": "TODO"
        },
        {
            "school_name": "Cloverdale Traditional",
            "address": "17857-56 Avenue, Surrey, BC V3S 1E2",
            "phone": "604-576-8295",
            "website": "https://www.surreyschools.ca/schools/cloverdaletraditional",
            "students": "TODO"
        },
        {
            "school_name": "Coast Meridian",
            "address": "8222-168A Street, Surrey, BC V4N 4T8",
            "phone": "604-574-6036",
            "website": "https://www.surreyschools.ca/schools/coastmeridian",
            "students": "TODO"
        },
        {
            "school_name": "Colebrook",
            "address": "5404-125A Street, Surrey, BC V3X 1W6",
            "phone": "604-596-3221",
            "website": "https://www.surreyschools.ca/schools/colebrook",
            "students": "TODO"
        },
        {
            "school_name": "Cougar Creek",
            "address": "12236-70A Avenue, Surrey, BC V3W 4Z8",
            "phone": "604-591-9098",
            "website": "https://www.surreyschools.ca/schools/cougarcreek",
            "students": "TODO"
        },
        {
            "school_name": "Coyote Creek",
            "address": "8131-156 Street, Surrey, BC V3S 3R4",
            "phone": "604-597-0858",
            "website": "https://www.surreyschools.ca/schools/coyotecreek",
            "students": "TODO"
        },
        {
            "school_name": "Creekside",
            "address": "13838-91 Avenue, Surrey, BC V3V 7K4",
            "phone": "604-543-9132",
            "website": "https://www.surreyschools.ca/schools/creekside",
            "students": "TODO"
        },
        {
            "school_name": "École Crescent Park",
            "address": "2440-128 Street, Surrey, BC V4A 3W3",
            "phone": "604-535-9101",
            "website": "https://www.surreyschools.ca/schools/crescentpark",
            "students": "TODO"
        },
        {
            "school_name": "David Brankin",
            "address": "9160-128 Street, Surrey, BC V3V 5M8",
            "phone": "604-585-9547",
            "website": "https://www.surreyschools.ca/schools/davidbrankin",
            "students": "TODO"
        },
        {
            "school_name": "Dogwood",
            "address": "10752-157 Street, Surrey, BC V4N 1K6",
            "phone": "604-581-8111",
            "website": "https://www.surreyschools.ca/schools/dogwood",
            "students": "TODO"
        },
        {
            "school_name": "Don Christian",
            "address": "6256-184 Street, Surrey, BC V3S 8E6",
            "phone": "604-576-1381",
            "website": "https://www.surreyschools.ca/schools/donchristian",
            "students": "TODO"
        },
        {
            "school_name": "Douglas",
            "address": "17325 2nd Avenue, Surrey, BC V3Z 9P9",
            "phone": "604-535-0180",
            "website": "https://www.surreyschools.ca/schools/douglas",
            "students": "TODO"
        },
        {
            "school_name": "Dr. F.D. Sinclair",
            "address": "7480-128 Street, Surrey, BC V3W 4E5",
            "phone": "604-596-1537",
            "website": "https://www.surreyschools.ca/schools/drfdsinclair",
            "students": "TODO"
        },
        {
            "school_name": "Earl Marriott",
            "address": "15751-16 Avenue, Surrey, BC V4A 1S1",
            "phone": "604-531-8354",
            "website": "https://www.surreyschools.ca/schools/earlmarriott",
            "students": "TODO"
        },
        {
            "school_name": "East Kensington",
            "address": "2795-184 Street, Surrey, BC V3S 9V2",
            "phone": "604-541-1257",
            "website": "https://www.surreyschools.ca/schools/eastkensington",
            "students": "TODO"
        },
        {
            "school_name": "Edgewood",
            "address": "16666-23 Avenue, Surrey, BC V3Z 0M7",
            "phone": "778-537-0206",
            "website": "https://www.surreyschools.ca/schools/edgewood",
            "students": "TODO"
        },
        {
            "school_name": "Education Services School",
            "address": "14033-92nd Avenue, Surrey, BC V3V 0B7",
            "phone": "604-595-6436",
            "website": "https://www.surreyschools.ca/schools/edsc-school",
            "students": "TODO"
        },
        {
            "school_name": "École Elementaire K.B. Woodward",
            "address": "13130-106 Avenue, Surrey, BC V3T 2C3",
            "phone": "604-588-5918",
            "website": "https://www.surreyschools.ca/schools/kbwoodward",
            "students": "TODO"
        },
        {
            "school_name": "Elgin Park",
            "address": "13484-24 Avenue, Surrey, BC V4A 2G5",
            "phone": "604-538-6678",
            "website": "https://www.surreyschools.ca/schools/elginpark",
            "students": "TODO"
        },
        {
            "school_name": "Ellendale",
            "address": "14525-110A Avenue, Surrey, BC V3R 2B4",
            "phone": "604-584-4754",
            "website": "https://www.surreyschools.ca/schools/ellendale",
            "students": "TODO"
        },
        {
            "school_name": "Enver Creek",
            "address": "14505-84 Avenue, Surrey, BC V3S 8X2",
            "phone": "604-543-8149",
            "website": "https://www.surreyschools.ca/schools/envercreek",
            "students": "TODO"
        },
        {
            "school_name": "Erma Stephenson",
            "address": "10929-160 Street, Surrey, BC V4N 1P3",
            "phone": "604-583-5419",
            "website": "https://www.surreyschools.ca/schools/ermastephenson",
            "students": "TODO"
        },
        {
            "school_name": "Fleetwood Park",
            "address": "7940-156 Street, Surrey, BC V3S 3R3",
            "phone": "604-597-2301",
            "website": "https://www.surreyschools.ca/schools/fleetwoodpark",
            "students": "TODO"
        },
        {
            "school_name": "Forsyth Road",
            "address": "10730-139 Street, Surrey, BC V3T 4L9",
            "phone": "604-588-8394",
            "website": "https://www.surreyschools.ca/schools/forsythroad",
            "students": "TODO"
        },
        {
            "school_name": "Frank Hurt",
            "address": "13940-77 Avenue, Surrey, BC V3W 5Z4",
            "phone": "604-590-1311",
            "website": "https://www.surreyschools.ca/schools/frankhurt",
            "students": "TODO"
        },
        {
            "school_name": "Fraser Heights",
            "address": "16060-108 Avenue, Surrey, BC V4N 1M1",
            "phone": "604-582-9231",
            "website": "https://www.surreyschools.ca/schools/fraserheights",
            "students": "TODO"
        },
        {
            "school_name": "Fraser Wood",
            "address": "10650-164 Street, Surrey, BC V4N 1W8",
            "phone": "604-589-6442",
            "website": "https://www.surreyschools.ca/schools/fraserwood",
            "students": "TODO"
        },
        {
            "school_name": "George Greenaway",
            "address": "17285-61A Avenue, Surrey, BC V3S 1W3",
            "phone": "604-576-1136",
            "website": "https://www.surreyschools.ca/schools/georgegreenaway",
            "students": "TODO"
        },
        {
            "school_name": "Georges Vanier",
            "address": "6985-142 Street, Surrey, BC V3W 5N1",
            "phone": "604-596-1030",
            "website": "https://www.surreyschools.ca/schools/georgesvanier",
            "students": "TODO"
        },
        {
            "school_name": "Goldstone Park",
            "address": "6287 - 146 Street, Surrey, BC V3S 3A3",
            "phone": "604-595-2767",
            "website": "https://www.surreyschools.ca/schools/goldstonepark",
            "students": "TODO"
        },
        {
            "school_name": "Grandview Heights",
            "address": "16987-25th Avenue, Surrey, BC V3Z 0Z9",
            "phone": "604-542-3320",
            "website": "https://www.surreyschools.ca/schools/grandview",
            "students": "TODO"
        },
        {
            "school_name": "Green Timbers",
            "address": "8824-144 Street, Surrey, BC V3V 5Z7",
            "phone": "604-588-5961",
            "website": "https://www.surreyschools.ca/schools/greentimbers",
            "students": "TODO"
        },
        {
            "school_name": "Guildford Learning Centre",
            "address": "#300 10183-152A Street, Surrey, BC V3R 4H6",
            "phone": "604-951-9553",
            "website": "https://www.surreyschools.ca/schools/guildfordlc",
            "students": "TODO"
        },
        {
            "school_name": "Guildford Park",
            "address": "10707-146 Street, Surrey, BC V3R 1T5",
            "phone": "604-588-7601",
            "website": "https://www.surreyschools.ca/schools/guildfordpark",
            "students": "TODO"
        },
        {
            "school_name": "H.T. Thrift",
            "address": "1739-148 Street, Surrey, BC V4A 4M6",
            "phone": "604-536-8712",
            "website": "https://www.surreyschools.ca/schools/htthrift",
            "students": "TODO"
        },
        {
            "school_name": "Harold Bishop",
            "address": "15670-104 Avenue, Surrey, BC V4N 2J3",
            "phone": "604-581-6016",
            "website": "https://www.surreyschools.ca/schools/haroldbishop",
            "students": "TODO"
        },
        {
            "school_name": "Hazelgrove",
            "address": "7057 -191 Street, Surrey, BC V4N 6E5",
            "phone": "604-574-0044",
            "website": "https://www.surreyschools.ca/schools/hazelgrove",
            "students": "TODO"
        },
        {
            "school_name": "École Henry Bose",
            "address": "6550-134 Street, Surrey, BC V3W 4S3",
            "phone": "604-596-6324",
            "website": "https://www.surreyschools.ca/schools/henrybose",
            "students": "TODO"
        },
        {
            "school_name": "Hillcrest",
            "address": "18599-65 Avenue, Surrey, BC V3S 8T2",
            "phone": "604-575-1359",
            "website": "https://www.surreyschools.ca/schools/hillcrest",
            "students": "TODO"
        },
        {
            "school_name": "Hjorth Road",
            "address": "14781-104 Avenue, Surrey, BC V3R 5X4",
            "phone": "604-581-2327",
            "website": "https://www.surreyschools.ca/schools/hjorthroad",
            "students": "TODO"
        },
        {
            "school_name": "Holly",
            "address": "10719-150 Street, Surrey, BC V3R 4C8",
            "phone": "604-585-2566",
            "website": "https://www.surreyschools.ca/schools/holly",
            "students": "TODO"
        },
        {
            "school_name": "Hyland",
            "address": "6677-140 Street, Surrey, BC V3W 5J3",
            "phone": "604-543-9347",
            "website": "https://www.surreyschools.ca/schools/hyland",
            "students": "TODO"
        },
        {
            "school_name": "Invergarry Adult Education Centre",
            "address": "12772 88 Avenue, Surrey, BC V3W 3J9",
            "phone": "604-595-8218",
            "website": "https://www.surreyschools.ca/schools/invergarryadulted",
            "students": "TODO"
        },
        {
            "school_name": "J.T. Brown",
            "address": "12530-60 Avenue, Surrey, BC V3X 2K8",
            "phone": "604-596-3445",
            "website": "https://www.surreyschools.ca/schools/jtbrown",
            "students": "TODO"
        },
        {
            "school_name": "James Ardiel",
            "address": "13751-112 Avenue, Surrey, BC V3R 2G4",
            "phone": "604-588-3021",
            "website": "https://www.surreyschools.ca/schools/jamesardiel",
            "students": "TODO"
        },
        {
            "school_name": "Janice Churchill",
            "address": "8226-146 Street, Surrey, BC V3S 3A5",
            "phone": "604-543-7187",
            "website": "https://www.surreyschools.ca/schools/janicechurchill",
            "students": "TODO"
        },
        {
            "school_name": "Jessie Lee",
            "address": "2064-154 Street, Surrey, BC V4A 4S3",
            "phone": "604-531-8833",
            "website": "https://www.surreyschools.ca/schools/jessielee",
            "students": "TODO"
        },
        {
            "school_name": "Johnston Heights",
            "address": "15350-99 Avenue, Surrey, BC V3R 0R9",
            "phone": "604-581-5500",
            "website": "https://www.surreyschools.ca/schools/johnstonheights",
            "students": "TODO"
        },
        {
            "school_name": "Katzie",
            "address": "6887 – 194A Street, Surrey, BC V4N 1N2",
            "phone": "778-571-4080",
            "website": "https://www.surreyschools.ca/schools/katzie",
            "students": "TODO"
        },
        {
            "school_name": "Kennedy Trail",
            "address": "8305-122A Street, Surrey, BC V3W 9P8",
            "phone": "604-590-1198",
            "website": "https://www.surreyschools.ca/schools/kennedytrail",
            "students": "TODO"
        },
        {
            "school_name": "Kirkbride",
            "address": "12150-92 Avenue, Surrey, BC V3V 1G2",
            "phone": "604-588-5711",
            "website": "https://www.surreyschools.ca/schools/kirkbride",
            "students": "TODO"
        },
        {
            "school_name": "Kwantlen Park",
            "address": "10441-132 Street, Surrey, BC V3T 3V3",
            "phone": "604-588-6934",
            "website": "https://www.surreyschools.ca/schools/kwantlenpark",
            "students": "TODO"
        },
        {
            "school_name": "L.A. Matheson",
            "address": "9484-122 Street, Surrey, BC V3V 4M1",
            "phone": "604-588-3418",
            "website": "https://www.surreyschools.ca/schools/lamatheson",
            "students": "TODO"
        },
        {
            "school_name": "École Laronde",
            "address": "1880 Laronde Drive, Surrey, BC V4A 9S4",
            "phone": "604-536-1626",
            "website": "https://www.surreyschools.ca/schools/laronde",
            "students": "TODO"
        },
        {
            "school_name": "Latimer Road",
            "address": "19233-60 Avenue, Surrey, BC V3S 2T5",
            "phone": "604-576-9184",
            "website": "https://www.surreyschools.ca/schools/latimerroad",
            "students": "TODO"
        },
        {
            "school_name": "Lena Shaw",
            "address": "14250-100A Avenue, Surrey, BC V3T 1K8",
            "phone": "604-581-1363",
            "website": "https://www.surreyschools.ca/schools/lenashaw",
            "students": "TODO"
        },
        {
            "school_name": "Lord Tweedsmuir",
            "address": "6151-180 Street, Surrey, BC V3S 4L5",
            "phone": "604-574-7407",
            "website": "https://www.surreyschools.ca/schools/lordtweedsmuir",
            "students": "TODO"
        },
        {
            "school_name": "M.B. Sanford",
            "address": "7318-143 Street, Surrey, BC V3W 7T6",
            "phone": "604-596-7517",
            "website": "https://www.surreyschools.ca/schools/mbsanford",
            "students": "TODO"
        },
        {
            "school_name": "Maddaugh",
            "address": "19405-76th Avenue, Surrey, BC V4N 6C6",
            "phone": "604-283-0184",
            "website": "https://www.surreyschools.ca/schools/maddaugh",
            "students": "TODO"
        },
        {
            "school_name": "Maple Green",
            "address": "14898 Spenser Drive, Surrey, BC V3S 7K7",
            "phone": "604-594-8838",
            "website": "https://www.surreyschools.ca/schools/maplegreen",
            "students": "TODO"
        },
        {
            "school_name": "Martha Currie",
            "address": "5811-184 Street, Surrey, BC V3S 4N2",
            "phone": "604-576-8551",
            "website": "https://www.surreyschools.ca/schools/marthacurrie",
            "students": "TODO"
        },
        {
            "school_name": "Martha Jane Norris",
            "address": "12928-66A Ave, Surrey, BC V3W 8Z7",
            "phone": "604-594-7150",
            "website": "https://www.surreyschools.ca/schools/marthajanenorris",
            "students": "TODO"
        },
        {
            "school_name": "Mary Jane Shannon",
            "address": "10682-144 Street, Surrey, BC V3T 4W1",
            "phone": "604-588-5991",
            "website": "https://www.surreyschools.ca/schools/mjshannon",
            "students": "TODO"
        },
        {
            "school_name": "McLeod Road Traditional",
            "address": "6325-142 Street, Surrey, BC V3X 1B9",
            "phone": "604-595-1060",
            "website": "https://www.surreyschools.ca/schools/mcleodroad",
            "students": "TODO"
        },
        {
            "school_name": "Morgan",
            "address": "3366-156A Street, Surrey, BC V3S 9Y7",
            "phone": "604-531-8426",
            "website": "https://www.surreyschools.ca/schools/morgan",
            "students": "TODO"
        },
        {
            "school_name": "Mountainview Montessori",
            "address": "15225 98 Avenue, Surrey, BC V3R 1J2",
            "phone": "604-589-1193",
            "website": "https://www.surreyschools.ca/schools/mountainview",
            "students": "TODO"
        },
        {
            "school_name": "Newton",
            "address": "13359-81 Avenue, Surrey, BC V3W 3C5",
            "phone": "604-596-8621",
            "website": "https://www.surreyschools.ca/schools/newton",
            "students": "TODO"
        },
        {
            "school_name": "North Ridge",
            "address": "13460-62 Avenue, Surrey, BC V3X 2J2",
            "phone": "604-599-3900",
            "website": "https://www.surreyschools.ca/schools/northridge",
            "students": "TODO"
        },
        {
            "school_name": "North Surrey Learning Centre",
            "address": "9260 140 St, Surrey, BC V3V 5Z4",
            "phone": "604-583-4040",
            "website": "https://www.surreyschools.ca/schools/northsurreylc",
            "students": "TODO"
        },
        {
            "school_name": "North Surrey Secondary",
            "address": "15945-96 Avenue, Surrey, BC V4N 2R8",
            "phone": "604-581-4433",
            "website": "https://www.surreyschools.ca/schools/northsurrey",
            "students": "TODO"
        },
        {
            "school_name": "Ocean Cliff",
            "address": "12550-20 Avenue, Surrey, BC V4A 1Y6",
            "phone": "604-538-1770",
            "website": "https://www.surreyschools.ca/schools/oceancliff",
            "students": "TODO"
        },
        {
            "school_name": "Old Yale Road",
            "address": "10135-132 Street, Surrey, BC V3T 3T6",
            "phone": "604-588-5468",
            "website": "https://www.surreyschools.ca/schools/oldyaleroad",
            "students": "TODO"
        },
        {
            "school_name": "Pacific Heights",
            "address": "17148 26 Avenue, Surrey, BC V3S 0A4",
            "phone": "604-531-2828",
            "website": "https://www.surreyschools.ca/schools/pacificheights",
            "students": "TODO"
        },
        {
            "school_name": "Panorama Park",
            "address": "12878-62 Avenue, Surrey, BC V3X 2E8",
            "phone": "604-596-0963",
            "website": "https://www.surreyschools.ca/schools/panoramapark",
            "students": "TODO"
        },
        {
            "school_name": "École Panorama Ridge",
            "address": "13220 64 Avenue, Surrey, BC V3W 1X9",
            "phone": "604-595-8890",
            "website": "https://www.surreyschools.ca/schools/panoramaridge",
            "students": "TODO"
        },
        {
            "school_name": "École Peace Arch",
            "address": "15877 Roper Avenue, White Rock, BC V4B 2H5",
            "phone": "604-536-8711",
            "website": "https://www.surreyschools.ca/schools/peacearch",
            "students": "TODO"
        },
        {
            "school_name": "Port Kells",
            "address": "19076-88 Avenue, Surrey, BC V4N 3G5",
            "phone": "604-882-2021",
            "website": "https://www.surreyschools.ca/schools/portkells",
            "students": "TODO"
        },
        {
            "school_name": "Prince Charles",
            "address": "12405-100 Avenue, Surrey, BC V3V 2X2",
            "phone": "604-588-5481",
            "website": "https://www.surreyschools.ca/schools/princecharles",
            "students": "TODO"
        },
        {
            "school_name": "Princess Margaret",
            "address": "12870-72 Avenue, Surrey, BC V3W 2M9",
            "phone": "604-594-5458",
            "website": "https://www.surreyschools.ca/schools/princessmargaret",
            "students": "TODO"
        },
        {
            "school_name": "Queen Elizabeth",
            "address": "9457 King George Blvd., Surrey, BC V3V 5W4",
            "phone": "604-588-1258",
            "website": "https://www.surreyschools.ca/schools/queenelizabeth",
            "students": "TODO"
        },
        {
            "school_name": "Queen Elizabeth Continuing Education",
            "address": "9457 King George Blvd, Surrey, BC V3V 5W4",
            "phone": "604-581-1413",
            "website": "https://www.surreyschools.ca/schools/queenelizabethadulted",
            "students": "TODO"
        },
        {
            "school_name": "Ray Shepherd",
            "address": "1650-136 Street, Surrey, BC V4A 4E4",
            "phone": "604-531-1471",
            "website": "https://www.surreyschools.ca/schools/rayshepherd",
            "students": "TODO"
        },
        {
            "school_name": "Regent Road Elementary",
            "address": "18711 – 74th Avenue, Surrey, BC V4N 6C2",
            "phone": "604-595-6488",
            "website": "https://www.surreyschools.ca/schools/regentroad",
            "students": "TODO"
        },
        {
            "school_name": "Riverdale",
            "address": "14835-108A Avenue, Surrey, BC V3R 1W9",
            "phone": "604-588-5978",
            "website": "https://www.surreyschools.ca/schools/riverdale",
            "students": "TODO"
        },
        {
            "school_name": "Rosemary Heights",
            "address": "15516 36th Avenue, Surrey, BC V3S 0J5",
            "phone": "604-541-1613",
            "website": "https://www.surreyschools.ca/schools/rosemaryheights",
            "students": "TODO"
        },
        {
            "school_name": "Royal Heights",
            "address": "11665-97 Avenue, Surrey, BC V3V 2B9",
            "phone": "604-581-7622",
            "website": "https://www.surreyschools.ca/schools/royalheights",
            "students": "TODO"
        },
        {
            "school_name": "S. Surrey - W.R. Learning Centre",
            "address": "13-2320 King George Blvd, Surrey, BC V4A 5A5",
            "phone": "604-536-0550",
            "website": "https://www.surreyschools.ca/schools/whiterocklc",
            "students": "TODO"
        },
        {
            "school_name": "École Salish Secondary",
            "address": "7278 184 Street, Surrey, BC V4N 5V2",
            "phone": "604-235-9836",
            "website": "https://www.surreyschools.ca/schools/salish",
            "students": "TODO"
        },
        {
            "school_name": "Semiahmoo",
            "address": "1785-148 Street, Surrey, BC V4A 4M6",
            "phone": "604-536-2131",
            "website": "https://www.surreyschools.ca/schools/semiahmoo",
            "students": "TODO"
        },
        {
            "school_name": "Semiahmoo Trail",
            "address": "3040-145A Street, Surrey, BC V4P 1P8",
            "phone": "604-531-6063",
            "website": "https://www.surreyschools.ca/schools/semiahmootrail",
            "students": "TODO"
        },
        {
            "school_name": "Senator Reid",
            "address": "9341-126 Street, Surrey, BC V3V 5C4",
            "phone": "604-584-7441",
            "website": "https://www.surreyschools.ca/schools/senatorreid",
            "students": "TODO"
        },
        {
            "school_name": "Serpentine Heights",
            "address": "16126-93A Avenue, Surrey, BC V4N 3A2",
            "phone": "604-589-6322",
            "website": "https://www.surreyschools.ca/schools/serpentineheights",
            "students": "TODO"
        },
        {
            "school_name": "École Simon Cunningham",
            "address": "9380-140 Street, Surrey, BC V3V 5Z4",
            "phone": "604-588-4435",
            "website": "https://www.surreyschools.ca/schools/simoncunningham",
            "students": "TODO"
        },
        {
            "school_name": "South Meridian",
            "address": "16244-13 Avenue, Surrey, BC V4A 8E6",
            "phone": "604-538-7114",
            "website": "https://www.surreyschools.ca/schools/southmeridian",
            "students": "TODO"
        },
        {
            "school_name": "Strawberry Hill",
            "address": "7633-124 Street, Surrey, BC V3W 8N2",
            "phone": "604-596-5533",
            "website": "https://www.surreyschools.ca/schools/strawberryhill",
            "students": "TODO"
        },
        {
            "school_name": "Sullivan",
            "address": "6016-152 Street, Surrey, BC V3S 3K6",
            "phone": "604-597-1977",
            "website": "https://www.surreyschools.ca/schools/sullivan",
            "students": "TODO"
        },
        {
            "school_name": "Sullivan Heights",
            "address": "6248-144 Street, Surrey, BC V3X 1A1",
            "phone": "604-543-8749",
            "website": "https://www.surreyschools.ca/schools/sullivanheights",
            "students": "TODO"
        },
        {
            "school_name": "Sunnyside",
            "address": "2828 – 159 Street, Surrey, BC V3S 0E5",
            "phone": "604-531-4826",
            "website": "https://www.surreyschools.ca/schools/sunnyside",
            "students": "TODO"
        },
        {
            "school_name": "Sunrise Ridge",
            "address": "18690-60 Avenue, Surrey, BC V3S 8L8",
            "phone": "604-576-3000",
            "website": "https://www.surreyschools.ca/schools/sunriseridge",
            "students": "TODO"
        },
        {
            "school_name": "Surrey Centre",
            "address": "16670 Old McLellan Road, Surrey, BC V3S 1K3",
            "phone": "604-576-9191",
            "website": "https://www.surreyschools.ca/schools/surreycentre",
            "students": "TODO"
        },
        {
            "school_name": "Surrey Traditional",
            "address": "13875-113 Avenue, Surrey, BC V3R 2J6",
            "phone": "604-588-1248",
            "website": "https://www.surreyschools.ca/schools/surreytraditional",
            "students": "TODO"
        },
        {
            "school_name": "T.E. Scott",
            "address": "7079-148 Street, Surrey, BC V3S 3E5",
            "phone": "604-596-0357",
            "website": "https://www.surreyschools.ca/schools/tescott",
            "students": "TODO"
        },
        {
            "school_name": "Tamanawis",
            "address": "12600-66 Avenue, Surrey, BC V3W 2A8",
            "phone": "604-597-5234",
            "website": "https://www.surreyschools.ca/schools/tamanawis",
            "students": "TODO"
        },
        {
            "school_name": "W.E. Kinvig",
            "address": "13266-70B Avenue, Surrey, BC V3W 8N1",
            "phone": "604-594-1135",
            "website": "https://www.surreyschools.ca/schools/wekinvig",
            "students": "TODO"
        },
        {
            "school_name": "Walnut Road",
            "address": "16152-82 Avenue, Surrey, BC V4N 0N5",
            "phone": "604-572-6617",
            "website": "https://www.surreyschools.ca/schools/walnutroad",
            "students": "TODO"
        },
        {
            "school_name": "Westerman",
            "address": "7626-122 Street, Surrey, BC V3W 1H4",
            "phone": "604-572-4054",
            "website": "https://www.surreyschools.ca/schools/westerman",
            "students": "TODO"
        },
        {
            "school_name": "White Rock",
            "address": "1273 Fir Street, White Rock, BC V4B 5A6",
            "phone": "604-531-5731",
            "website": "https://www.surreyschools.ca/schools/whiterock",
            "students": "TODO"
        },
        {
            "school_name": "William F. Davidson",
            "address": "15550-99A Avenue, Surrey, BC V3R 9H5",
            "phone": "604-584-7688",
            "website": "https://www.surreyschools.ca/schools/williamfdavidson",
            "students": "TODO"
        },
        {
            "school_name": "William Watson",
            "address": "16450-80 Avenue, Surrey, BC V4N 0H3",
            "phone": "604-574-4141",
            "website": "https://www.surreyschools.ca/schools/williamwatson",
            "students": "TODO"
        },
        {
            "school_name": "Woodland Park",
            "address": "9025-158 Street, Surrey, BC V4N 2Y6",
            "phone": "604-589-5957",
            "website": "https://www.surreyschools.ca/schools/woodlandpark",
            "students": "TODO"
        },
        {
            "school_name": "Woodward Hill",
            "address": "6082-142 Street, Surrey, BC V3X 1C1",
            "phone": "604-594-2408",
            "website": "https://www.surreyschools.ca/schools/woodwardhill",
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