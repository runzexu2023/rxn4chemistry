# Python wrapper for the IBM RXN for Chemistry API

![logo](./docs_source/_static/logo.jpg)

A python wrapper to access the API of the IBM RXN for Chemistry [website](https://rxn.res.ibm.com/rxn/).

## Install

```console
pip install https://github.com/rxn4chemistry/rxn4chemistry.git
```

## Usage

Get your API key from [here](https://rxn.res.ibm.com/rxn/user/profile) and build the wrapper:

```python
api_key='API_KEY'
from rxn4chemistry import RXN4ChemistryWrapper

rxn4chemistry_wrapper = RXN4ChemistryWrapper(api_key=api_key)
# NOTE: you can create a project or set an esiting one using:
# rxn4chemistry_wrapper.set_project('PROJECT_ID')
rxn4chemistry_wrapper.create_project('test_wrapper')
print(rxn4chemistry_wrapper.project_id)
```

Run a reaction prediction is as simple as:

```python
response = rxn4chemistry_wrapper.predict_reaction(
    'BrBr.c1ccc2cc3ccccc3cc2c1'
)
results = rxn4chemistry_wrapper.get_predict_reaction_results(
    response['prediction_id']
)
print(results['payload']['attempts'][0]['smiles'])
```

## Examples

An example on how to predict retrosynthesis for COVID19 candidates [here](./examples/diamond_light_source_covid19_candidates_retrosynthesis.ipynb).

## Documentation

The documentation is hosted on GitHub pages.