import os
import pandas as pd

schools = {
    "Kamloops-Thompson": [
        {
            "school_name": "Aberdeen Elementary",
            "address": "2191 Van Horne Drive, Kamloops, V1S 1L9",
            "phone": "250-372-5844",
            "website": "https://aberdeen.sd73.bc.ca",
            "students": 400
        },
        {
            "school_name": "AE Perry Elementary",
            "address": "1380 Sherbrooke Ave, Kamloops, V2B 1W9",
            "phone": "250-376-6224",
            "website": "https://aeperry.sd73.bc.ca",
            "students": 300
        },
        {
            "school_name": "Arthur Hatton Elementary",
            "address": "315 Chestnut Ave, Kamloops, V2B 1L4",
            "phone": "250-376-7217",
            "website": "https://arthurhatton.sd73.bc.ca",
            "students": 250
        },
        {
            "school_name": "Arthur Stevenson Elementary",
            "address": "2890 Bank Road, Kamloops, V2B 6Y7",
            "phone": "250-579-9284",
            "website": "https://arthurstevenson.sd73.bc.ca",
            "students": 300
        },
        {
            "school_name": "Barriere Elementary",
            "address": "4475 Airfield Road, Barriere, V0E 1E0",
            "phone": "250-672-9916",
            "website": "https://barriere.sd73.bc.ca",
            "students": 200
        },
        {
            "school_name": "Barriere Secondary",
            "address": "4811 Barriere Town Rd., Barriere, V0E 1E0",
            "phone": "250-672-9943",
            "website": "https://barrieresecondary.sd73.bc.ca",
            "students": 200
        },
        {
            "school_name": "Beattie Elementary",
            "address": "492 McGlll Road, Kamloops, V2C 1M3",
            "phone": "250-374-0608",
            "website": "https://beattie.sd73.bc.ca",
            "students": 300
        },
        {
            "school_name": "Bert Edwards Science and Technology School",
            "address": "711 Windsor Avenue, Kamloops, V2B 2B7",
            "phone": "250-376-2205",
            "website": "https://bert.sd73.bc.ca",
            "students": 250
        },
        {
            "school_name": "Blue River Elementary",
            "address": "5913 3rd Ave, Blue River, V0E 1J0",
            "phone": "250-673-8253",
            "website": "https://blueriver.sd73.bc.ca",
            "students": 10
        }
    ],
    "Gold Trail": [
        {
            "school_name": "Cache Creek Elementary",
            "address": "1260 Cariboo Highway, PO Box 128, Cache Creek, BC V0K 1H0",
            "phone": "250-457-6248",
            "website": "https://www.sd74.bc.ca/school/cces",
            "students": "TODO"
        },
        {
            "school_name": "Cayoosh Elementary",
            "address": "351 6th Avenue, Lillooet, BC V0K 1V0",
            "phone": "250-256-4212",
            "website": "https://www.sd74.bc.ca/school/cayoosh",
            "students": "TODO"
        },
        {
            "school_name": "George M. Murray Elementary",
            "address": "281 Hollywood Crescent, PO Box 968, Lillooet, BC V0K 1V0",
            "phone": "250-256-7543",
            "website": "https://www.sd74.bc.ca/school/gmme",
            "students": "TODO"
        },
        {
            "school_name": "Gold Bridge Community School",
            "address": "Haylmore Avenue, General Delivery, Gold Bridge, BC V0K 1P0",
            "phone": "250-238-2255",
            "website": "https://www.sd74.bc.ca/school/gbcs",
            "students": "TODO"
        },
        {
            "school_name": "David Stoddart School",
            "address": "1203 Cariboo Avenue, Box 129, Clinton, BC V0K 1K0",
            "phone": "250-459-2219",
            "website": "https://www.sd74.bc.ca/school/davidstoddart",
            "students": "TODO"
        },
        {
            "school_name": "Desert Sands Community School",
            "address": "435 Ranch Road, PO Box 669, Ashcroft, BC V0K 1A0",
            "phone": "250-453-9144",
            "website": "https://www.sd74.bc.ca/school/desertsands",
            "students": "TODO"
        },
        {
            "school_name": "Kumsheen ShchEma-meet School",
            "address": "PO Box 60, Lytton, BC V0K 1Z0",
            "phone": "250-455-2328",
            "website": "https://www.sd74.bc.ca/school/kumsheen",
            "students": "TODO"
        },
        {
            "school_name": "Lillooet Secondary School",
            "address": "920 Columbia, PO Box 760, Lillooet, BC V0K 1V0",
            "phone": "250-256-4274",
            "website": "https://www.sd74.bc.ca/school/lillooetsecondary",
            "students": "TODO"
        }
    ],
    "North Okanagan-Shuswap": [
        {
            "school_name": "A L Fortune Secondary",
            "address": "500 Bass Ave, Enderby, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/al-fortune-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Armstrong Elementary",
            "address": "3010 Pleasant Valley Rd, Armstrong, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/armstrong-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Bastion Elementary",
            "address": "2251 12 Ave NE, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/bastion-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Carlin Elementary Middle",
            "address": "4005 Myers Frontage Rd, Tappen, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/carlin-elementary-middle",
            "students": "TODO"
        },
        {
            "school_name": "Eagle River Secondary",
            "address": "PO Box 9, Sicamous, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/eagle-river-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Falkland Elementary Junior School",
            "address": "PO Box 10, Falkland, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/falkland-elementary-junior",
            "students": "TODO"
        },
        {
            "school_name": "Grindrod Elementary",
            "address": "PO Box 249, Grindrod, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/grindrod-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Highland Park Elementary",
            "address": "PO Box 647, Armstrong, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/highland-park-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Hillcrest Elementary",
            "address": "1180 20 St SE, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/hillcrest-elementary",
            "students": "TODO"
        },
        {
            "school_name": "J.L. Jackson Secondary",
            "address": "551 14 St NE, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/jl-jackson-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Len Wood Middle School",
            "address": "3700 Patten Dr, Armstrong, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/len-wood-middle",
            "students": "TODO"
        },
        {
            "school_name": "M.V. Beattie Elementary",
            "address": "PO Box 249, Enderby, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/mv-beattie-elementary",
            "students": "TODO"
        },
        {
            "school_name": "North Canoe Elementary",
            "address": "PO Box 78, Canoe, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/north-canoe-elementary",
            "students": "TODO"
        },
        {
            "school_name": "North Shuswap Elementary",
            "address": "5295 Squilax-Anglemont Rd, Celista, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/north-shuswap-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Parkview Elementary School",
            "address": "PO Box 444, Sicamous, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/parkview-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Pleasant Valley Secondary",
            "address": "2365 Pleasant Valley Rd, Armstrong, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/pleasant-valley-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Ranchero Elementary Junior",
            "address": "6285 Ranchero Dr E, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/ranchero-elementary-junior",
            "students": "TODO"
        },
        {
            "school_name": "Salmon Arm Secondary",
            "address": "PO Box 1000 Stn Main, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/salmon-arm-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Salmon Arm Storefront",
            "address": "PO Box 129, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/salmon-arm-storefront",
            "students": "TODO"
        },
        {
            "school_name": "Salmon Arm West Elementary",
            "address": "4750 10 Ave SW, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/salmon-arm-west-elementary",
            "students": "TODO"
        },
        {
            "school_name": "Shuswap Middle School",
            "address": "PO Box 1090 Stn Main, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/shuswap-middle",
            "students": "TODO"
        },
        {
            "school_name": "Silver Creek Elementary Secondary",
            "address": "935 Salmon River Rd, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/silver-creek-elementary-secondary",
            "students": "TODO"
        },
        {
            "school_name": "Sorrento Elementary",
            "address": "PO Box 220, Sorrento, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/sorrento-elementary",
            "students": "TODO"
        },
        {
            "school_name": "South Broadview Elementary",
            "address": "3200 6 Ave NE, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/south-broadview-elementary",
            "students": "TODO"
        },
        {
            "school_name": "South Canoe",
            "address": "5970 10 Ave SE, Salmon Arm, BC",
            "phone": "TODO",
            "website": "https://sd83.bc.ca/south-canoe",
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