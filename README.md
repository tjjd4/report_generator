# report_generator
generate a pdf by using `reportlab`

## installation
### using `pipenv`
```bash
git clone https://github.com/seantjjd4/report_generator.git

pip install pipenv    # optional if you haven't install virtual enviroment
pipenv install
```

### using `pip`
```bash
git clone https://github.com/seantjjd4/report_generator.git

pipenv run pip freeze > requirements.txt  # create requirements.txt from pipfile and pipfile.lock

pip install -r requirements.txt
```

## Usage
this program read data from `scoresheet` and `quesionnaire`, then generate a pdf report in specific pattern.

```bash
python main.py
```
The result pdf will be generate in `build` folder.
