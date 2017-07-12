# Reddit Text Analysis Tool

## Tech Stack

__Backend:__ Python<br>
__Libraries:__ Scikit-learn, NLTK<br>

## Installation

Clone git repository:

```
$ git clone https://github.com/obettaglio/reddit-text-analysis.git
```

Create a virtual environment in repository:

```
$ virtualenv env
```

Activate virtual environment:

```
$ source env/bin/activate
```

Install dependencies:

```
$ pip install -r requirements.txt
```

Run the file:

```
$ python data_matrix.py
```

Get the results!


## Customizations

If you'd like to find more data to run, download a file at `http://files.pushshift.io/reddit/comments`, add it to your `data/` directory, and change line 36 of `load_data.py` to open the new file.<br>

The maximum number of features to vectorize can be adjusted in line 14 of `data_matrix.py`.<br>

N-gram length can be adjusted in line 15 of `data_matrix.py`.<br>

The number of displayed influential phrases can be adjusted in line 53 of `data_matrix.py`.
