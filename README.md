# Demo of Flask API

See <https://flask.palletsprojects.com/en/stable/tutorial/views/>

To use,
```bash
make container
make up
```

In a browser, visit <http://localhost:5000> to see a static HTML page

To access the API, use
```bash
curl -s http://localhost:5000/api/v1/list
```
