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
        "school_name": "Charles Hays Secondary School",
        "address": "Prince Rupert",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Conrad Elementary School",
        "address": "Prince Rupert",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Hartley Bay Elem-Jr Secondary School",
        "address": "Hartley Bay",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Pacific Coast School",
        "address": "Prince Rupert",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Lax Kxeen Elementary School",
        "address": "Prince Rupert",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Pineridge Elementary School",
        "address": "Prince Rupert",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Port Edward Elementary School",
        "address": "Port Edward",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Prince Rupert Middle School",
        "address": "Prince Rupert",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    },
    {
        "school_name": "Roosevelt Park Elementary School",
        "address": "Prince Rupert",
        "phone": "TODO",
        "website": "TODO",
        "student_count": "TODO"
    }
]

districts = [
    ("Prince Rupert", schools)
]


# Combine all school lists into one DataFrame
all_schools = (schools)
schools_data = pd.DataFrame(all_schools)

# Adjust the address column to replace "+" with ", "
schools_data['address'] = schools_data['address'].str.replace('+', ', ', regex=False)

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

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
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All British Columbia Districts]](../..) > [[All In Prince Rupert]](..)\n\n")

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
