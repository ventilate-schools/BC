import os
import pandas as pd

schools = {
    "Surrey": [
        {
            "school_name": "Johnston Heights Secondary",
            "address": "15350 99 Ave, Surrey, BC V3R 0R9",
            "phone": "604-581-5500",
            "website": "https://www.surreyschools.ca/schools/johnstonheights",
            "students": 1400
        },
        {
            "school_name": "Semiahmoo Secondary",
            "address": "1785 148 St, Surrey, BC V4A 4M6",
            "phone": "604-536-2131",
            "website": "https://www.surreyschools.ca/schools/semiahmoo",
            "students": 1600
        },
        {
            "school_name": "All Hallows Catholic School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Ash Manor School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Blenheim High School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Broadwater School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Christ's College, Guildford",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Collingwood College",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "de Stafford School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Epsom and Ewell High School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Fullbrook School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "George Abbot School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Glebelands School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Glyn School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Heathside School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Hinchley Wood School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Howard of Effingham School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Kings International College",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Oakwood School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Oxted School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Reigate School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Rodborough Technology College",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Rosebery School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Royal Alexandra and Albert School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Rydens Enterprise School and Sixth Form College",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Salesian School, Chertsey",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "St Andrew's Catholic School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "St Bede's School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "St John the Baptist Catholic Comprehensive School, Woking",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "St Paul's Catholic College",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "St Peter's Catholic School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Sunbury Manor School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Thamesmead School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Ashcombe School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Beacon School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Bishop David Brown School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Bishop Wand Church of England School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Magna Carta School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Matthew Arnold School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Priory Voluntary Aided School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Warwick School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "The Winston Churchill School A Specialist Sports College",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Therfield School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Thomas Knyvett College",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Warlingham School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Weydon School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Woolmer Hill School",
            "address": "TODO",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        }
    ],
    "Delta": [
        {
            "school_name": "Beach Grove Elementary",
            "address": "5955 17a Ave, Delta, BC",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Brooke Elementary",
            "address": "8718 Delwood Dr, Delta, BC",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Burnsview Secondary",
            "address": "7658 112 St, Delta, BC",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Delta Secondary",
            "address": "4615 51 St, Delta, BC",
            "phone": "604-946-4194",
            "website": "https://de.deltasd.bc.ca/",
            "students": 1200
        },
        {
            "school_name": "Delview Secondary",
            "address": "9111 116 St, Delta, BC",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "North Delta Secondary",
            "address": "11447 82 Ave, Delta, BC",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Sands Secondary",
            "address": "10840 82 Ave, Delta, BC",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        },
        {
            "school_name": "Seaquam Secondary",
            "address": "11584 Lyon Rd, Delta, BC",
            "phone": "604-591-6166",
            "website": "https://se.deltasd.bc.ca/",
            "students": 1300
        },
        {
            "school_name": "South Delta Secondary",
            "address": "750 53 St, Delta, BC",
            "phone": "TODO",
            "website": "TODO",
            "students": "TODO"
        }
    ],
    "Richmond": [
        {
            "school_name": "Christ's School",
            "address": "Queen's Road, Richmond, TW10 6HW",
            "phone": "020 8940 6982",
            "website": "www.christs.richmond.sch.uk",
            "students": "TODO"
        },
        {
            "school_name": "Grey Court School",
            "address": "Ham Street, Ham, Richmond, TW10 7HN",
            "phone": "020 8948 1173",
            "website": "www.greycourt.richmond.sch.uk",
            "students": "TODO"
        },
        {
            "school_name": "Hampton High",
            "address": "Hanworth Road, Hampton, TW12 3HB",
            "phone": "020 8979 3399",
            "website": "www.hamptonhigh.org.uk",
            "students": "TODO"
        },
        {
            "school_name": "Orleans Park School",
            "address": "Richmond Road, Twickenham, TW1 3BB",
            "phone": "020 8891 0187",
            "website": "https://www.orleanspark.school/",
            "students": "TODO"
        },
        {
            "school_name": "Richmond Park Academy",
            "address": "Park Avenue, London, SW14 8RG",
            "phone": "020 8876 8891",
            "website": "www.richmondparkacademy.org",
            "students": "TODO"
        },
        {
            "school_name": "St Richard Reynolds Catholic High School",
            "address": "Clifden Road, Twickenham, TW1 4LT",
            "phone": "020 8325 4630",
            "website": "www.strichardreynolds.org.uk",
            "students": "TODO"
        },
        {
            "school_name": "Teddington School",
            "address": "Broom Road, Teddington, TW11 9PJ",
            "phone": "020 8943 0033",
            "website": "www.teddingtonschool.org",
            "students": "TODO"
        },
        {
            "school_name": "The Richmond upon Thames School",
            "address": "Egerton Road, Twickenham, TW2 7SJ",
            "phone": "020 8891 2985",
            "website": "www.richmonduponthamesschool.org.uk",
            "students": "TODO"
        },
        {
            "school_name": "Turing House School",
            "address": "2 Queen's Road, Teddington, TW11 0LR",
            "phone": "020 8069 6100",
            "website": "www.turinghouseschool.org.uk",
            "students": "TODO"
        },
        {
            "school_name": "Twickenham School",
            "address": "Percy Road, Twickenham, TW2 6JW",
            "phone": "020 8894 4503",
            "website": "www.twickenhamschool.org.uk",
            "students": "TODO"
        },
        {
            "school_name": "Waldegrave School",
            "address": "Fifth Cross Road, Twickenham, TW2 5LH",
            "phone": "020 8894 3244",
            "website": "www.waldegrave.richmond.sch.uk",
            "students": "TODO"
        }
    ],
    "Burnaby": [
        {
            "school_name": "Burnaby North Secondary",
            "address": "751 Hammarskjold Dr, Burnaby, BC V5B 4A1",
            "phone": "604-296-6875",
            "website": "https://north.burnabyschools.ca/",
            "students": 1800
        },
        {
            "school_name": "Burnaby South Secondary",
            "address": "5455 Rumble St, Burnaby, BC V5J 2B7",
            "phone": "604-296-6880",
            "website": "https://south.burnabyschools.ca/",
            "students": 1700
        }
    ],
"Coquitlam": [
        {
            "school_name": "Centennial Secondary",
            "address": "570 Poirier St, Coquitlam, BC V3J 6A8",
            "phone": "604-936-7205",
            "website": "https://www.sd43.bc.ca/school/centennial/",
            "students": 1500
        },
        {
            "school_name": "Gleneagle Secondary",
            "address": "1195 Lansdowne Dr, Coquitlam, BC V3B 7Y8",
            "phone": "604-464-5793",
            "website": "https://www.sd43.bc.ca/school/gleneagle/",
            "students": 1400
        }
    ],
    "New Westminster": [
        {
            "school_name": "New Westminster Secondary",
            "address": "820 Sixth St, New Westminster, BC V3M 3S9",
            "phone": "604-517-6220",
            "website": "https://nwss.ca/",
            "students": 2000
        }
    ],
"Sunshine Coast": [
        {
            "school_name": "Chatelech Secondary",
            "address": "5904 Cowrie St, Sechelt, BC V0N 3A0",
            "phone": "604-885-3216",
            "website": "https://chatelech.sd46.bc.ca/",
            "students": 600
        },
        {
            "school_name": "Elphinstone Secondary",
            "address": "840 Gibsons Way, Gibsons, BC V0N 1V7",
            "phone": "604-886-2204",
            "website": "https://elphinstone.sd46.bc.ca/",
            "students": 500
        }
    ],
    "Sea To Sky": [
        {
            "school_name": "Howe Sound Secondary",
            "address": "38430 Buckley Ave, Squamish, BC V8B 0A1",
            "phone": "604-892-5261",
            "website": "https://www.sd48howesound.org/",
            "students": 800
        },
        {
            "school_name": "Whistler Secondary",
            "address": "8000 Alpine Way, Whistler, BC V8E 0G5",
            "phone": "604-932-5535",
            "website": "https://www.sd48whistler.org/",
            "students": 400
        }
    ],
    "Conseil Scolaire Francophone": [
        {
            "school_name": "École des Pionniers-de-Maillardville",
            "address": "3550 Wellington St, Port Coquitlam, BC V3B 3Y5",
            "phone": "604-552-7915",
            "website": "https://pionniers.csf.bc.ca/",
            "students": "TODO"
        },
        {
            "school_name": "École Gabrielle-Roy",
            "address": "6887 132 St, Surrey, BC V3W 4L9",
            "phone": "604-597-5912",
            "website": "https://gabrielle-roy.csf.bc.ca/",
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