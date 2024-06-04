import os
import pandas as pd

# mission_schools has a GPT4 sourced set of schools.

# There's 169 school districts in BC and this is just one below for Missiom.
# mission is hard coded a few times in here, which isn't optimal.

# GPT Prompt I used:
# All mission public school district (BC) schools in a python dict like so ```mission_schools = [
#    {"school_name": "School Name", "address": "400 Street St+Town+CT 12345", "students": 1234,
#    "website": "URL, "phone": "123 456 7890"}]``` please

# After you generate the markdown from this script, also run `python3 make_grade_subtotals_and_totals.py`

schools = [
    {
        "school_name": "Bankhead Elementary",
        "address": "1280 Wilson Ave, Kelowna, BC V1Y 6Y6",
        "website": "https://bke.sd23.bc.ca/",
        "student_count": 308
    },
    {
        "school_name": "Belgo Elementary",
        "address": "125 Adventure Rd, Kelowna, BC V1X 1N3",
        "website": "https://bge.sd23.bc.ca/",
        "student_count": 333
    },
    {
        "school_name": "Black Mountain Elementary",
        "address": "1650 Gallagher Rd, Kelowna, BC V1P 1G7",
        "website": "https://bme.sd23.bc.ca/",
        "student_count": 399
    },
    {
        "school_name": "Chute Lake Elementary",
        "address": "5240 Lark St, Kelowna, BC V1W 4K8",
        "website": "https://www.cle.sd23.bc.ca/",
        "student_count": 440
    },
    {
        "school_name": "Davidson Road Elementary",
        "address": "2115 Davidson Rd, Lake Country, BC V4V 1R3",
        "website": "https://www.dre.sd23.bc.ca/",
        "student_count": 404
    },
    {
        "school_name": "Dorothea Walker Elementary",
        "address": "4346 Gordon Dr, Kelowna, BC V1W 1S5",
        "website": "https://www.dwe.sd23.bc.ca/",
        "student_count": 378
    },
    {
        "school_name": "Ellison Elementary",
        "address": "3735 Parkdale Rd, Kelowna, BC V1X 6K9",
        "website": "https://ees.sd23.bc.ca/",
        "student_count": 373
    },
    {
        "school_name": "Glenmore Elementary",
        "address": "960 Glenmore Dr, Kelowna, BC V1Y 4P1",
        "website": "https://www.gme.sd23.bc.ca/",
        "student_count": 545
    },
    {
        "school_name": "Hudson Road Elementary",
        "address": "1221 Hudson Rd, West Kelowna, BC V1Z 1J4",
        "website": "https://www.hre.sd23.bc.ca/",
        "student_count": 277
    },
    {
        "school_name": "North Glenmore Elementary",
        "address": "125 Snowsell St, Kelowna, BC V1V 2E2",
        "website": "https://www.nge.sd23.bc.ca/",
        "student_count": 556
    },
    {
        "school_name": "Pearson Road Elementary",
        "address": "700 Pearson Rd, Kelowna, BC V1X 5H8",
        "website": "https://www.pre.sd23.bc.ca/",
        "student_count": 407
    },
    {
        "school_name": "Quigley Elementary",
        "address": "705 Kitch Rd, Kelowna, BC V1X 5V8",
        "website": "https://www.qge.sd23.bc.ca/",
        "student_count": 323
    },
    {
        "school_name": "Raymer Elementary",
        "address": "657 Raymer Ave, Kelowna, BC V1Y 4Z6",
        "website": "https://www.ray.sd23.bc.ca/",
        "student_count": 233
    },
    {
        "school_name": "Rose Valley Elementary",
        "address": "1680 Westlake Rd, West Kelowna, BC V1Z 3G6",
        "website": "https://www.rve.sd23.bc.ca/",
        "student_count": 381
    },
    {
        "school_name": "Rutland Elementary",
        "address": "620 Webster Rd, Kelowna, BC V1X 4V5",
        "website": "https://www.rle.sd23.bc.ca/",
        "student_count": 459
    },
    {
        "school_name": "Shannon Lake Elementary",
        "address": "3044 Sandstone Dr, West Kelowna, BC V4T 1T2",
        "website": "https://www.sle.sd23.bc.ca/",
        "student_count": 485
    },
    {
        "school_name": "South Kelowna Elementary",
        "address": "4176 Spiers Rd, Kelowna, BC V1W 4B5",
        "website": "https://www.ske.sd23.bc.ca/",
        "student_count": 263
    },
    {
        "school_name": "Watson Road Elementary",
        "address": "475 Yates Rd, Kelowna, BC V1V 1R3",
        "website": "https://www.wat.sd23.bc.ca/",
        "student_count": 542
    },
    {
        "school_name": "Anne McClymont Elementary",
        "address": "4489 Lakeshore Rd, Kelowna, BC V1W 1W9",
        "website": "https://www.ame.sd23.bc.ca/",
        "student_count": 475
    },
    {
        "school_name": "Constable Neil Bruce Middle",
        "address": "2010 Daimler Dr, West Kelowna, BC V1Z 3Y4",
        "website": "https://www.cnb.sd23.bc.ca/",
        "student_count": 679
    },
    {
        "school_name": "Dr. Knox Middle",
        "address": "121 Drysdale Blvd, Kelowna, BC V1V 2X9",
        "website": "https://www.drk.sd23.bc.ca/",
        "student_count": 810
    },
    {
        "school_name": "École Glenrosa Middle",
        "address": "2974 Glen Abbey Pl, West Kelowna, BC V4T 2N1",
        "website": "https://www.gms.sd23.bc.ca/",
        "student_count": 467
    },
    {
        "school_name": "KLO Middle",
        "address": "3130 Gordon Dr, Kelowna, BC V1W 3M4",
        "website": "https://www.klo.sd23.bc.ca/",
        "student_count": 709
    },
    {
        "school_name": "Okanagan Mission Secondary",
        "address": "4544 Gordon Dr, Kelowna, BC V1W 1T4",
        "website": "https://www.okm.sd23.bc.ca/",
        "student_count": 1132
    },
    {
        "school_name": "Rutland Middle",
        "address": "715 Rutland Rd N, Kelowna, BC V1X 3B6",
        "website": "https://www.rms.sd23.bc.ca/",
        "student_count": 598
    },
    {
        "school_name": "Springvalley Middle",
        "address": "350 Ziprick Rd, Kelowna, BC V1X 4H3",
        "website": "https://www.sms.sd23.bc.ca/",
        "student_count": 580
    },
    {
        "school_name": "George Elliot Secondary",
        "address": "10241 Bottom Wood Lake Rd, Lake Country, BC V4V 1Y7",
        "website": "https://www.ges.sd23.bc.ca/",
        "student_count": 805
    },
    {
        "school_name": "Kelowna Secondary",
        "address": "1079 Raymer Ave, Kelowna, BC V1Y 4Z7",
        "website": "https://www.kss.sd23.bc.ca/",
        "student_count": 1777
    },
    {
        "school_name": "Mount Boucherie Secondary",
        "address": "2751 Cameron Rd, West Kelowna, BC V1Z 2T6",
        "website": "https://www.mbs.sd23.bc.ca/",
        "student_count": 1541
    },
    {
        "school_name": "Rutland Senior Secondary",
        "address": "705 Rutland Rd N, Kelowna, BC V1X 3B6",
        "website": "https://www.rss.sd23.bc.ca/",
        "student_count": 1203
    }
]

school_phone_numbers = {
    "Bankhead Elementary": "250-870-5114",
    "Belgo Elementary": "250-870-5115",
    "Black Mountain Elementary": "250-870-5143",
    "Chute Lake Elementary": "250-870-5139",
    "Davidson Road Elementary": "250-870-5117",
    "Dorothea Walker Elementary": "250-870-5138",
    "Ellison Elementary": "250-870-5140",
    "Glenmore Elementary": "250-870-5137",
    "Hudson Road Elementary": "250-870-5128",
    "North Glenmore Elementary": "250-870-5129",
    "Pearson Road Elementary": "250-870-5118",
    "Quigley Elementary": "250-870-5131",
    "Raymer Elementary": "250-870-5125",
    "Rose Valley Elementary": "250-870-5136",
    "Rutland Elementary": "250-870-5123",
    "Shannon Lake Elementary": "250-870-5132",
    "South Kelowna Elementary": "250-870-5127",
    "Watson Road Elementary": "250-870-5135",
    "Anne McClymont Elementary": "250-870-5121",
    "Constable Neil Bruce Middle": "250-870-5177",
    "Dr. Knox Middle": "250-870-5130",
    "École Glenrosa Middle": "250-870-5176",
    "KLO Middle": "250-870-5106",
    "Okanagan Mission Secondary": "250-870-5000",
    "Rutland Middle": "250-870-5141",
    "Springvalley Middle": "250-870-5107",
    "George Elliot Secondary": "250-870-5102",
    "Kelowna Secondary": "250-870-5105",
    "Mount Boucherie Secondary": "250-870-5101",
    "Rutland Senior Secondary": "250-870-5119"
}

# Merging phone numbers into the schools list
for school in schools:
    school_name = school["school_name"]
    if school_name in school_phone_numbers:
        school["phone_number"] = school_phone_numbers[school_name]


# Combine all school lists into one DataFrame
all_schools = (schools)
schools_data = pd.DataFrame(all_schools)

# Adjust the address column to replace "+" with ", "
schools_data['address'] = schools_data['address'].str.replace('+', ', ', regex=False)

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Adding district names to the DataFrame
districts = [
    ("Central Okanagan", schools)
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
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All British Columbia Districts]](../..) > [[All In Central Okanagan]](..)\n\n")

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
