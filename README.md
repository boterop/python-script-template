## Use

To run this script you need to create a `.env` file with the variables found in `.env.example`.

Then run `pip3 install -r requirements.txt` to install the dependencies.

Then run `python3 main.py` to run the code

## Test

To unit test the code run `python3 -m unittest -v`

To get the coverage report use

```sh
coverage run -m unittest discover
coverage report -m
```
