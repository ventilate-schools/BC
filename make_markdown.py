import os
import pandas as pd

schools = {
    "Nanaimo-Ladysmith": [
        {
            "school_name": "Nanaimo District Secondary School",
            "address": "355 Wakesiah Ave, Nanaimo, BC V9R 3K5",
            "phone": "250-753-6331",
            "website": "https://nd.schools.sd68.bc.ca/",
            "students": "TODO"
        },
        {
            "school_name": "Dover Bay Secondary School",
            "address": "6135 McGirr Rd, Nanaimo, BC V9V 1M1",
            "phone": "250-756-4573",
            "website": "https://doverb.schools.sd68.bc.ca/",
            "students": "TODO"
        },
        {
            "school_name": "Ladysmith Secondary School",
            "address": "410 Mackie Rd, Ladysmith, BC V9G 1E6",
            "phone": "250-245-3258",
            "website": "https://ladsec.sd68.bc.ca/",
            "students": "TODO"
        }
    ],
    "Qualicum": [
        {
            "school_name": "Kwalikum Secondary School",
            "address": "266 Village Way, Qualicum Beach, BC V9K 1L4",
            "phone": "250-752-5651",
            "website": "https://kss.sd69.bc.ca/",
            "students": "TODO"
        }
    ],
    "Pacific Rim": [
        {
            "school_name": "Ucluelet Secondary School",
            "address": "1586 Peninsula Rd, Ucluelet, BC V0R 3A0",
            "phone": "250-726-7708",
            "website": "https://uclueletsecondary.ca/",
            "students": "TODO"
        },
        {
            "school_name": "Wickaninnish Community School",
            "address": "800 Pearce St, Tofino, BC V0R 2Z0",
            "phone": "250-725-3835",
            "website": "https://wickaninnishcommunityschool.com/",
            "students": "TODO"
        }
    ],
    "Powell River": [
        {
            "school_name": "Brooks Secondary School",
            "address": "5800 Willingdon Ave, Powell River, BC V8A 4R3",
            "phone": "604-483-3171",
            "website": "https://brooks.sd47.bc.ca/",
            "students": "TODO"
        }
    ],
    "Greater Victoria": [
        {
            "school_name": "Esquimalt High School",
            "address": "847 Colville Rd, Victoria, BC V9A 4N9",
            "phone": "250-382-9231",
            "website": "https://esquimalt.public.sd61.bc.ca/",
            "students": "TODO"
        },
        {
            "school_name": "Lambrick Park Secondary School",
            "address": "4139 Torquay Dr, Victoria, BC V8N 3V4",
            "phone": "250-477-0181",
            "website": "https://lambrickpark.sd61.bc.ca/",
            "students": "TODO"
        },
        {
            "school_name": "Mount Douglas Secondary School",
            "address": "3370 Cedar Hill Rd, Victoria, BC V8P 3Z4",
            "phone": "250-477-6962",
            "website": "https://mountdouglas.sd61.bc.ca/",
            "students": "TODO"
        }
    ],
    "Cowichan Valley": [
        {
            "school_name": "Cowichan Secondary School",
            "address": "2618 Beverley St, Duncan, BC V9L 2X8",
            "phone": "250-746-4175",
            "website": "https://cowichan.sd79.bc.ca/",
            "students": "TODO"
        },
        {
            "school_name": "Chemainus Secondary School",
            "address": "3305 Chemainus Rd, Chemainus, BC V0R 1K5",
            "phone": "250-246-4711",
            "website": "https://chemainus.sd79.bc.ca/",
            "students": "TODO"
        }
    ],
    "Vancouver Island West": [
        {
            "school_name": "Zeballos Elementary Secondary School",
            "address": "157 Maquinna Ave, Zeballos, BC V0P 2A0",
            "phone": "250-761-4224",
            "website": "https://zess.sd84.bc.ca/",
            "students": "TODO"
        }
    ],
    "Vancouver Island North": [
        {
            "school_name": "Port Hardy Secondary School",
            "address": "9350 Granville St, Port Hardy, BC V0N 2P0",
            "phone": "250-949-7443",
            "website": "https://phss.sd85.bc.ca/",
            "students": "TODO"
        },
        {
            "school_name": "North Island Secondary School",
            "address": "7962 Guthrie Rd, Port McNeill, BC V0N 2R0",
            "phone": "250-956-3394",
            "website": "https://niss.sd85.bc.ca/",
            "students": "TODO"
        }
    ],
    "Saanich": [
        {
            "school_name": "Claremont Secondary School",
            "address": "4980 Wesley Rd, Victoria, BC V8Y 1Y9",
            "phone": "250-658-6672",
            "website": "https://claremont.sd63.bc.ca/",
            "students": "TODO"
        },
        {
            "school_name": "Stelly's Secondary School",
            "address": "1627 Stelly's Cross Rd, Saanichton, BC V8M 1S8",
            "phone": "250-652-4401",
            "website": "https://stellys.sd63.bc.ca/",
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