from mendeley import Mendeley
import yaml
import os
import csv
# Get the DOI to look up
import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("doi", help="Searches the Mendeley catalogue for this DOI")
# args = parser.parse_args()

# config_file = 'config.yml'

config = {}

# if os.path.isfile(config_file):
#     with open('config.yml') as f:
#         config = yaml.load(f)
# else:
# config['clientId'] = os.environ.get('MENDELEY_CLIENT_ID')
config['clientId'] = 10787
# config['clientSecret'] = os.environ.get('MENDELEY_CLIENT_SECRET')
config['clientSecret'] = 'idravljCIiczdX8y'

mendeley = Mendeley(config['clientId'], config['clientSecret'])
# mendeley = Mendeley(10467, 'bdrMTaTJXLD1EHf7')
session = mendeley.start_client_credentials_flow().authenticate()

# doi = args.doi


with open('bangladesh 2016-2020 16501-17000.csv', encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    doi = []

    for row in reader:
        doi.append(row["DOI"])

        print(doi)

        j = 0
        mysrting = " "
        i = 0

        for i in range(len(doi)):
            if doi is mysrting:
                pass

            else:
                #try:

                    v = str(j)+".txt"
                    with open(v, mode='w') as file:
                        doc = session.catalog.by_identifier(
                            doi=doi[i], view='stats')
                        print(session.catalog)
                        # if doc  is None:
                        # pass

                        # else:

                        print('"%s" has %s readers.' %
                              (doc.title,  doc.reader_count))

                        file.write(doc.title)
                        file.write(",READERS:  ")
                        file.write(str(doc.reader_count))
                        file.write('\n')
                        file.write(str(doc.reader_count_by_academic_status))
                        file.write('\n')
                        file.write(str(doc.reader_count_by_country))
                        file.write('\n')
                        file.write(str(doc.reader_count_by_subdiscipline))
                        file.write('\n')
                        j = j+1
                #except:

            i = i+1
