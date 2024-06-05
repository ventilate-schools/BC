import os
import pandas as pd

schools = {
    "Southeast Kootenay": [
        {
            "school_name": "Amy Woodland Elementary",
            "address": "911 6th St S, Cranbrook, BC",
            "phone": "250-426-7258",
            "website": "https://amywoodland.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Elkford Elementary Secondary",
            "address": "Po Box 910, Elkford, BC",
            "phone": "250-865-4674",
            "website": "https://ees.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Fernie Secondary",
            "address": "Po Box 370, Fernie, BC",
            "phone": "250-423-4471",
            "website": "https://fses.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Frank J Mitchell Elementary",
            "address": "Po Box 345, Sparwood, BC",
            "phone": "250-425-7818",
            "website": "https://fjmes.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Gordon Terrace Elementary",
            "address": "1200 5th Ave S, Cranbrook, BC",
            "phone": "250-426-8248",
            "website": "https://gter.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Highlands Elementary",
            "address": "3300 7th St S, Cranbrook, BC",
            "phone": "250-489-4391",
            "website": "https://highlands.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Isabella Dicken Elementary",
            "address": "Po Box 1559, Fernie, BC",
            "phone": "250-423-4651",
            "website": "https://ides.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Jaffray Elem-Jr Secondary",
            "address": "Po Box 378, Jaffray, BC",
            "phone": "250-429-3211",
            "website": "https://jes.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kootenay Orchards Elementary",
            "address": "1301 - 20th Ave S, Cranbrook, BC",
            "phone": "250-426-5308",
            "website": "https://koes.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Laurie Middle School",
            "address": "1808 2nd St S, Cranbrook, BC",
            "phone": "250-426-5291",
            "website": "https://laurie.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mount Baker Secondary",
            "address": "1410 Baker St, Cranbrook, BC",
            "phone": "250-426-5241",
            "website": "https://mbss.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Parkland Middle School",
            "address": "1115 2nd Ave S, Cranbrook, BC",
            "phone": "250-426-3327",
            "website": "https://parkland.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Pinewood Elementary",
            "address": "40 Pinewood Ave W, Cranbrook, BC",
            "phone": "250-426-6201",
            "website": "https://pinewood.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Rocky Mountain Elementary",
            "address": "Po Box 460, Elkford, BC",
            "phone": "250-865-4625",
            "website": "https://rmes.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Sparwood Secondary",
            "address": "Po Box 67, Sparwood, BC",
            "phone": "250-425-6666",
            "website": "https://sses.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Steeples Elementary",
            "address": "700 24th Ave N, Cranbrook, BC",
            "phone": "250-426-3352",
            "website": "https://steeples.sd5.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "T M Roberts Elementary",
            "address": "10 Wattsville Rd, Cranbrook, BC",
            "phone": "250-489-4575",
            "website": "https://tmres.sd5.bc.ca",
            "students": "TODO"
        }
    ],
    "Rocky Mountain": [
        {
            "school_name": "Alexander Park Elementary",
            "address": "Po Box 464, Golden, BC",
            "phone": "250-344-5513",
            "website": "https://apes.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "David Thompson Secondary",
            "address": "1535 14th St Unit 1 Rr 4, Invermere, BC",
            "phone": "250-342-9213",
            "website": "https://dtss.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Edgewater Elementary",
            "address": "Po Box 69, Edgewater, BC",
            "phone": "250-347-9543",
            "website": "https://ees.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Eileen Madson Primary School",
            "address": "2001 15th Ave, Invermere, BC",
            "phone": "250-342-9315",
            "website": "https://emps.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Golden Alternate School",
            "address": "Po Box 1350, Golden, BC",
            "phone": "250-344-2160",
            "website": "https://gas.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Golden Secondary",
            "address": "Po Box 1350, Golden, BC",
            "phone": "250-344-2201",
            "website": "https://gss.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "J Alfred Laird Elementary",
            "address": "1202 13th Avenue, Invermere, BC",
            "phone": "250-342-6232",
            "website": "https://jales.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kimberley Alternate School",
            "address": "405 Halpin St, Kimberley, BC",
            "phone": "250-427-8011",
            "website": "https://kas.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Lady Grey Elementary",
            "address": "Po Box 899, Golden, BC",
            "phone": "250-344-6317",
            "website": "https://lges.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Lindsay Park Elementary",
            "address": "602 Salmo St, Kimberley, BC",
            "phone": "250-427-2255",
            "website": "https://lpes.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Martin Morigeau Elementary",
            "address": "4891 Beatty Avenue, Canal Flats, BC",
            "phone": "250-349-5665",
            "website": "https://mmes.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Marysville Elementary",
            "address": "546 309 Ave, Kimberley, BC",
            "phone": "250-427-2241",
            "website": "https://mes.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "McKim Middle School",
            "address": "689 Rotary Dr, Kimberley, BC",
            "phone": "250-427-2283",
            "website": "https://mms.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nicholson Elementary",
            "address": "Po Box 331, Golden, BC",
            "phone": "250-344-2370",
            "website": "https://nes.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Open Doors Alternate Education",
            "address": "Po Box 430, Invermere, BC",
            "phone": "250-342-6814",
            "website": "https://odas.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Selkirk Secondary School",
            "address": "405 Halpin St, Kimberley, BC",
            "phone": "250-427-4827",
            "website": "https://sss.sd6.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Windermere Elementary",
            "address": "4747 Government St, Windermere, BC",
            "phone": "250-342-6640",
            "website": "https://wes.sd6.bc.ca",
            "students": "TODO"
        }
    ],
    "Kootenay Lake": [
        {
            "school_name": "Adam Robertson Elementary",
            "address": "421 9 Ave N, Creston, BC",
            "phone": "250-428-2051",
            "website": "https://ares.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Blewett Elementary",
            "address": "2665 Blewett Rd, Nelson, BC",
            "phone": "250-352-5314",
            "website": "https://blewett.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Brent Kennedy Elementary",
            "address": "Po Box 40, Crescent Valley, BC",
            "phone": "250-359-7292",
            "website": "https://bkes.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Canyon-Lister Elementary",
            "address": "4575 Canyon-Lister Road, Canyon, BC",
            "phone": "250-428-4161",
            "website": "https://canyon.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Crawford Bay Elementary-Secondary",
            "address": "Po Box 100, Crawford Bay, BC",
            "phone": "250-227-9218",
            "website": "https://cbess.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Erickson Elementary",
            "address": "Po Box 180, Erickson, BC",
            "phone": "250-428-2325",
            "website": "https://erickson.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Hume Elementary",
            "address": "310 Nelson Ave, Nelson, BC",
            "phone": "250-352-3186",
            "website": "https://hume.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "J.V. Humphries Elementary-Secondary",
            "address": "Po Box 577, Kaslo, BC",
            "phone": "250-353-2227",
            "website": "https://jvh.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Jewett Elementary",
            "address": "Po Box 39, Meadow Creek, BC",
            "phone": "250-366-4223",
            "website": "https://jewett.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kootenay River Secondary",
            "address": "223 18th Ave S, Creston, BC",
            "phone": "250-428-2274",
            "website": "https://krs.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "L.V. Rogers Secondary",
            "address": "1004 Cottonwood Street, Nelson, BC",
            "phone": "250-352-5538",
            "website": "https://lvr.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Mount Sentinel Secondary",
            "address": "Po Box 99, South Slocan, BC",
            "phone": "250-359-7219",
            "website": "https://mtsentinel.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Redfish Elementary",
            "address": "265 Bryan Rd, Nelson, BC",
            "phone": "250-229-4211",
            "website": "https://redfish.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Rosemont Elementary",
            "address": "1605 Crease Street, Nelson, BC",
            "phone": "250-352-3027",
            "website": "https://rosemont.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Salmo Elementary",
            "address": "Po Drawer 220, Salmo, BC",
            "phone": "250-357-2214",
            "website": "https://ses.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Salmo Secondary",
            "address": "Po Box 310, Salmo, BC",
            "phone": "250-357-2235",
            "website": "https://salsec.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "South Nelson Elementary",
            "address": "814 Latimer St, Nelson, BC",
            "phone": "250-352-3252",
            "website": "https://southnelson.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Trafalgar Middle School",
            "address": "1201 Josephine St, Nelson, BC",
            "phone": "250-352-5538",
            "website": "https://trafalgar.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "W.E. Graham Community School",
            "address": "Po Box 10, Slocan, BC",
            "phone": "250-355-2212",
            "website": "https://weg.sd8.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Winlaw Elementary",
            "address": "Po Box 10, Winlaw, BC",
            "phone": "250-226-7217",
            "website": "https://winlaw.sd8.bc.ca",
            "students": "TODO"
        }
    ],
    "Arrow Lakes": [
        {
            "school_name": "Burton Elementary School",
            "address": "219 Burton School Rd, Burton, BC",
            "phone": "250-265-3638 ext. 3998",
            "website": "https://bes.sd10.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Edgewood Elementary School",
            "address": "Po Box 129, Edgewood, BC",
            "phone": "250-269-7212",
            "website": "https://ees.sd10.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Lucerne Elementary Secondary School",
            "address": "Po Box 130, New Denver, BC",
            "phone": "250-358-7222",
            "website": "https://less.sd10.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nakusp Elementary School",
            "address": "Po Box 250, Nakusp, BC",
            "phone": "250-265-3638",
            "website": "https://nes.sd10.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Nakusp Secondary School",
            "address": "Po Box 249, Nakusp, BC",
            "phone": "250-265-3668",
            "website": "https://nss.sd10.bc.ca",
            "students": "TODO"
        }
    ],
    "Kootenay-Columbia": [
        {
            "school_name": "Fruitvale Elementary",
            "address": "1867 Columbia Gardens Rd, Fruitvale, BC",
            "phone": "250-368-5528",
            "website": "https://fes.sd20.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Glenmerry Elementary",
            "address": "3660 Carnation Dr, Trail, BC",
            "phone": "250-364-1353",
            "website": "https://ges.sd20.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "James L Webster Elementary",
            "address": "395 Schofield Hwy, Trail, BC",
            "phone": "250-368-3242",
            "website": "https://wes.sd20.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Kinnaird Elementary",
            "address": "2273 10th Ave, Castlegar, BC",
            "phone": "250-365-7227",
            "website": "https://kesd20.com",
            "students": "TODO"
        },
        {
            "school_name": "Robson Community School",
            "address": "2925 - Robson School Rd, Robson, BC",
            "phone": "250-365-5924",
            "website": "https://rcs.sd20.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Twin Rivers Elementary",
            "address": "743 - 7th Ave, Castlegar, BC",
            "phone": "250-365-5744",
            "website": "https://tr.sd20.bc.ca",
            "students": "TODO"
        },
        {
            "school_name": "Rossland Summit School",
            "address": "2875 St Paul St, Rossland, BC",
            "phone": "250-362-7388",
            "website": "https://rosslandsummit.org",
            "students": "TODO"
        },
        {
            "school_name": "J. Lloyd Crowe Secondary",
            "address": "1300 Frances Moran Rd, Trail, BC",
            "phone": "250-364-3395",
            "website": "https://jlcrowe.org",
            "students": "TODO"
        },
        {
            "school_name": "Stanley Humphries Secondary",
            "address": "720 - 7th Ave, Castlegar, BC",
            "phone": "250-365-7735",
            "website": "https://shsscastlegar.com",
            "students": "TODO"
        },
        {
            "school_name": "Kootenay-Columbia Learning Centre",
            "address": "2001 Third Ave, Trail, BC",
            "phone": "250-364-1275",
            "website": "https://kclc.sd20.bc.ca",
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