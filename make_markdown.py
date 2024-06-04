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
        "school_name":  "Argyle Secondary",
        "grade_range": "8-12",
        "address": "1131 Frederick Rd, North Vancouver, BC",
        "website": "http://www.sd44.ca/school/argyle/Pages/default.aspx",
        "student_count": "1445"
    },
    {
        "school_name":  "Blueridge Elementary",
        "grade_range": "K-7",
        "address": "2650 Bronte Dr, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/blueridge/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Boundary Elementary",
        "grade_range": "K-7",
        "address": "750 26th St E, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/boundary/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Braemar Elementary",
        "grade_range": "K-7",
        "address": "3600 Mahon Ave, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/braemar/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Brooksbank Elementary",
        "grade_range": "K-7",
        "address": "980 13th St E, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/brooksbank/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Canyon Heights Elementary",
        "grade_range": "K-7",
        "address": "4501 Highland Blvd, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/canyonheights/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Capilano Elementary",
        "grade_range": "K-7",
        "address": "1230 20th St W, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/capilano/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Carisbrooke Elementary",
        "grade_range": "K-7",
        "address": "510 Carisbrooke Rd E, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/carisbrooke/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Carson Graham Secondary",
        "grade_range": "8-12",
        "address": "2145 Jones Ave, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/carsongraham/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Cleveland Elementary",
        "grade_range": "K-7",
        "address": "1255 Eldon Rd, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/cleveland/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Cove Cliff Elementary",
        "grade_range": "K-7",
        "address": "1818 Banbury Rd, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/covecliff/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Dorothy Lynas Elementary",
        "grade_range": "K-7",
        "address": "4000 Inlet Cres, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/dorothylynas/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Eastview Elementary",
        "grade_range": "K-7",
        "address": "1801 Mountain Hwy, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/eastview/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Handsworth Secondary",
        "grade_range": "8-12",
        "address": "1033 Handsworth Rd, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/handsworth/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Highlands Elementary",
        "grade_range": "K-7",
        "address": "3150 Colwood Dr, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/highlands/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Larson Elementary",
        "grade_range": "K-7",
        "address": "2605 Larson Rd, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/larson/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Lynn Valley Elementary",
        "grade_range": "K-7",
        "address": "3207 Institute Road, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/lynnvalley/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Lynnmour Elementary School",
        "grade_range": "K-7",
        "address": "800 Forsman Ave, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/lynnmour/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Montroyal Elementary",
        "grade_range": "K-7",
        "address": "5310 Sonora Dr, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/montroyal/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Mountainside Secondary",
        "grade_range": "9-12",
        "address": "3365 Mahon Ave, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/mountainside/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Norgate Community Elementary",
        "grade_range": "K-7",
        "address": "1295 Sowden St, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/norgate/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Queen Mary Community Elementary",
        "grade_range": "K-7",
        "address": "230 Keith Rd W, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/queenmary/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Queensbury Elementary",
        "grade_range": "K-7",
        "address": "2020 Moody Ave, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/queensbury/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Ridgeway Elementary",
        "grade_range": "K-7",
        "address": "420 8th St E, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/ridgeway/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Ross Road Elementary",
        "grade_range": "K-7",
        "address": "2875 Bushnell Pl, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/rossroad/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Seycove Secondary Community",
        "grade_range": "8-12",
        "address": "1204 Caledonia Ave, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/seycove/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Seymour Heights Elementary",
        "grade_range": "K-7",
        "address": "2640 Carnation St, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/seymourheights/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Sherwood Park Elementary",
        "grade_range": "K-7",
        "address": "4085 Dollar Rd, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/sherwoodpark/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Sutherland Secondary",
        "grade_range": "8-12",
        "address": "1860 Sutherland Ave, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/sutherland/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Upper Lynn Elementary",
        "grade_range": "K-7",
        "address": "1540 Coleman St, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/upperlynn/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Westview Elementary",
        "grade_range": "K-7",
        "address": "641 17th St W, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/westview/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Windsor Secondary",
        "grade_range": "8-12",
        "address": "931 Broadview Dr, North Vancouver, BC",
        "website": "https://www.sd44.ca/school/windsor/Pages/default.aspx",
        "student_count": "TODO"
    },
    {
        "school_name":  "Bodwell High School",
        "grade_range": "8-12",
        "address": "955 Harbourside Dr, North Vancouver, BC",
        "website": "https://bodwell.edu",
        "student_count": "TODO"
    },
    {
        "school_name":  "Brockton Preparatory School",
        "grade_range": "K-12",
        "address": "3467 Duval Rd, North Vancouver, BC",
        "website": "https://www.brocktonschool.com",
        "student_count": "TODO"
    },
    {
        "school_name":  "Cousteau L'école Francaise Internationale",
        "grade_range": "K-9",
        "address": "3657 Fromme Rd, North Vancouver, BC",
        "website": "https://www.cousteauschool.org",
        "student_count": "TODO"
    },
    {
        "school_name":  "Holy Trinity School",
        "grade_range": "K-7",
        "address": "128 27th St W, North Vancouver, BC",
        "website": "https://www.holytrinityschool.ca",
        "student_count": "TODO"
    },
    {
        "school_name":  "Kenneth Gordon",
        "grade_range": "K-12",
        "address": "420 Seymour River Pl, North Vancouver, BC",
        "website": "https://kgms.ca",
        "student_count": "TODO"
    },
    {
        "school_name":  "Lions Gate Christian Academy",
        "grade_range": "K-12",
        "address": "919 Tollcross Rd, North Vancouver, BC",
        "website": "https://www.lgca.ca",
        "student_count": "TODO"
    },
    {
        "school_name":  "North Star Montessori Elementary School",
        "grade_range": "K-6",
        "address": "1325 Keith Rd E, North Vancouver, BC",
        "website": "https://northstarmontessori.ca",
        "student_count": "TODO"
    },
    {
        "school_name":  "Saplings Nature School",
        "grade_range": "K-5",
        "address": "1390 W22nd Street, North Vancouver, BC",
        "website": "https://saplingsoutdoorschool.com",
        "student_count": "TODO"
    },
    {
        "school_name":  "St Alcuin College for the Liberal Arts",
        "grade_range": "K-12",
        "address": "200-1046 St. Georges Ave, North Vancouver, BC",
        "website": "https://www.stalcuincollege.com",
        "student_count": "TODO"
    },
    {
        "school_name":  "St Edmund's",
        "grade_range": "K-7",
        "address": "535 Mahon Ave, North Vancouver, BC",
        "website": "https://stedmunds.ca",
        "student_count": "TODO"
    },
    {
        "school_name":  "St Pius X Elementary School",
        "grade_range": "K-7",
        "address": "1150 Mt. Seymour Road, North Vancouver, BC",
        "website": "https://www.saintpius.ca",
        "student_count": "TODO"
    },
    {
        "school_name":  "St Thomas Aquinas",
        "grade_range": "8-12",
        "address": "541 Keith Rd W, North Vancouver, BC",
        "website": "https://www.aquinas.org",
        "student_count": "TODO"
    },
    {
        "school_name":  "Vancouver Waldorf School",
        "grade_range": "K-12",
        "address": "2725 St. Christopher's Rd, North Vancouver, BC",
        "website": "https://vancouverwaldorfschool.ca",
        "student_count": "TODO"
    }
]

districts = [
    ("North Vancouver", schools)
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
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All British Columbia Districts]](../..) > [[All In North Vancouver]](..)\n\n")

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
