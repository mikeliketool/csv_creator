# csv_creator

### Generating an input file
1. Download your e-statement from your bank
2. Pull the latest [Tabular code](https://github.com/tabulapdf/tabula-java)
3. Run this command: java -jar ~/git/tabula-java/target/tabula-1.0.6-SNAPSHOT-jar-with-dependencies.jar -p all eStatement_2021-11-25.pdf >> raw-2021-11-25.csv

### Create a file contaning your unique payment identifiers
This will be a json file at the root of the repo called payment_identifiers.json
It should have the following format:
```json
{
  "IDENTIFIER1": "IDENTIFIER1",
  "IDENTIFIER2": "IDENTIFIER2"
}
```

### Running a make command to process the tabular output
make filepath=~/folder/path.csv process_file


### Run Tests
```bash
$ cd git/csv_creator
$ pipenv shell
$ pytest .
```
