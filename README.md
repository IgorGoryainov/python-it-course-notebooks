# python-it-course-notebooks

Jupyter notebooks from an introductory Python and data science course. Covers core Python, OOP, NumPy/Pandas, linear regression, and probability simulations.

## Notebooks

| Notebook | Topic |
|---|---|
| `hw-01-bank-accounts.ipynb` | Binary search algorithm — maximize account disbursements across managers |
| `hw-02-python-basics.ipynb` | Variables, types, conditionals, string operations |
| `hw-03-loops-and-arrays.ipynb` | Loops, lists, functions, Monte Carlo simulations |
| `hw-04-list-operations.ipynb` | List manipulation, consecutive runs, matrix transpose |
| `hw-05-oop-geometry.ipynb` | OOP — Point class, Euclidean distance, nearest-neighbor counting |
| `hw-06-numpy-and-pandas.ipynb` | NumPy arrays, matrix operations, BMW car dataset analysis |
| `hw-07-linear-regression.ipynb` | Linear regression from scratch using the normal equation |
| `hw-08-queue-simulation.ipynb` | Monte Carlo queue simulation (change-making problem) |

## Stack

- Python 3.10+
- Jupyter Notebook / JupyterLab
- numpy, pandas (for hw-06 through hw-08)
- matplotlib (for hw-03)

## Setup

```bash
pip install -r requirements.txt
jupyter lab
```

## Data

`hw-07-linear-regression.ipynb` loads `data/data.csv`. Download it first:

```bash
python3 -c "
import urllib.request, os
os.makedirs('data', exist_ok=True)
url = 'https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv'
urllib.request.urlretrieve(url, 'data/data.csv')
print('Downloaded data/data.csv')
"
```

## Tests

The core algorithms from the notebooks are extracted into `src/` as plain Python modules. Run the tests with:

```bash
pytest tests/ -v
```
