RegApiPython
============

RegRu API 2.0 python wrapper

Библиотека-оболочка для RegRU.API v.2.0. 

## Установка

    pip install RegApi

## Как использовать

```python
from RegApi import RegRuApiDomain
```

```python
params = {
    'username' : 'test',
    'password' : 'test',
    'show_renew_data' : 1,
    'show_update_data' : 1,
    'currency' : 'RUR',
    'output_content_type': 'plain',
    'show_input_params': 0,
}
```

```python
RegRuApiDomain().get_api(params, 'get_suggest')
```
