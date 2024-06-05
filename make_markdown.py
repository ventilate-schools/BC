import os
import pandas as pd

schools = {
    "Okanagan-Similkameen (SD53)": [
        {
            "school_name": "Cawston Primary School",
            "address": "517 School Rd, Cawston, BC V0X 1C1",
            "phone": "250-499-5617",
            "website": "https://cps.sd53.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Oliver Elementary School",
            "address": "Box 989, 809 School Avenue, Oliver, BC V0H 1T0",
            "phone": "250-498-3468",
            "website": "https://oes.sd53.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Okanagan Falls Elementary School",
            "address": "Box 6, 1141 Cedar St, Okanagan Falls, BC V0H 1R0",
            "phone": "250-497-5414",
            "website": "https://okf.sd53.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Tuc-el-Nuit Elementary School",
            "address": "6648 Park Drive, Oliver, BC V0H 1T4",
            "phone": "250-498-3415",
            "website": "https://ten.sd53.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Osoyoos Elementary School",
            "address": "Box 580, 8507 68 Ave, Osoyoos, BC V0H 1V0",
            "phone": "250-485-4444",
            "website": "https://ose.sd53.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Similkameen Elementary Secondary School",
            "address": "830 2nd Ave, Keremeos, BC V0X 1N2",
            "phone": "250-499-2727",
            "website": "https://sess.sd53.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Osoyoos Secondary School",
            "address": "5800 - 115th St, Osoyoos, BC V0H 1V4",
            "phone": "250-485-4433",
            "website": "https://oss.sd53.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Southern Okanagan Secondary School",
            "address": "Box 990, 6140 Gala Street, Oliver, BC V0H 1T0",
            "phone": "250-498-4931",
            "website": "https://soss.sd53.bc.ca",
            "students": "TODO"
        }
    ],
    "Nicola-Similkameen (SD58)": [
        {
            "school_name": "École Élémentaire Collettville",
            "address": "1275 Birch Ave, Merritt, BC V1K 1R1",
            "phone": "250-378-2213",
            "website": "https://cves.sd58.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Diamond Vale Elementary",
            "address": "1281 Coldwater Ave, Merritt, BC V1K 1R5",
            "phone": "250-378-2514",
            "website": "https://dves.sd58.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Merritt Bench Elementary School",
            "address": "3411 Voght St, Merritt, BC V1K 1C6",
            "phone": "250-378-5121",
            "website": "https://mbes.sd58.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Merritt Central Elementary School",
            "address": "2350 Jackson Ave, Merritt, BC V1K 1S7",
            "phone": "250-378-9931",
            "website": "https://mces.sd58.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nicola Canford Elementary",
            "address": "1930 Nicola Ave, Merritt, BC V1K 1B8",
            "phone": "250-378-2539",
            "website": "https://nces.sd58.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Merritt Secondary School",
            "address": "2345 Voght St, Merritt, BC V1K 1R2",
            "phone": "250-378-5131",
            "website": "https://mss.sd58.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kengard Learning Centre",
            "address": "2975 Clapperton Ave, Merritt, BC V1K 1G2",
            "phone": "250-378-5534",
            "website": "https://www.klc.scides.org",
            "students": "TODO"
        },
        {
            "school_name": "John Allison Elementary School",
            "address": "278 Mayne Ave, Princeton, BC V0X 1W0",
            "phone": "250-295-3188",
            "website": "https://jaes.sd58.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Vermilion Forks Elementary School",
            "address": "1506 Tomkinson Rd, Princeton, BC V0X 1W0",
            "phone": "250-295-6642",
            "website": "https://vves.sd58.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Princeton Secondary School",
            "address": "201 Old Hedley Rd, Princeton, BC V0X 1W0",
            "phone": "250-295-3218",
            "website": "https://pss.sd58.bc.ca",
            "students": "TODO"
        }
    ],
    "Okanagan-Skaha (SD67)": [
        {
            "school_name": "Carmi Elementary School",
            "address": "400 Carmi Ave, Penticton, BC V2A 3G5",
            "phone": "(250) 770-7697",
            "website": "https://carmi.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Columbia Elementary School",
            "address": "1437 Allison St, Penticton, BC V2A 3X5",
            "phone": "(250) 770-7676",
            "website": "https://columbia.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Giant's Head Elementary School",
            "address": "10503 Prairie Valley Rd, Summerland, BC V0H 1Z0",
            "phone": "(250) 770-7671",
            "website": "https://gh.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kaleden Elementary School",
            "address": "152 Linden Avenue, Kaleden, BC V0H 1K0",
            "phone": "(250) 770-7692",
            "website": "https://kaleden.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Naramata Elementary School",
            "address": "3660 8th Street, Naramata, BC V0H 1N0",
            "phone": "(250) 770-7688",
            "website": "https://naramata.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Parkway Elementary School",
            "address": "225 Kinney Ave, Penticton, BC V2A 3P2",
            "phone": "(250) 770-7686",
            "website": "https://parkway.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Queen's Park Elementary School",
            "address": "330 Power Street, Penticton, BC V2A 5X2",
            "phone": "(250) 770-7680",
            "website": "https://queenspark.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Trout Creek Elementary School",
            "address": "5811 Nixon Road, Summerland, BC V0H 1Z0",
            "phone": "(250) 770-7665",
            "website": "https://troutcreek.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Uplands Elementary School",
            "address": "145 Middle Bench Road South, Penticton, BC V2A 8S7",
            "phone": "(250) 770-7678",
            "website": "https://uplands.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "West Bench Elementary School",
            "address": "1604 West Bench Drive, Penticton, BC V2A 8Z3",
            "phone": "(250) 770-7698",
            "website": "https://westbench.sd67.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Wiltse Elementary School",
            "address": "640 Wiltse Blvd, Penticton, BC V2A 8J2",
            "phone": "(250) 770-7694",
            "website": "https://wiltse.sd67.bc.ca",
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