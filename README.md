# Drug Prediction app
<p>Created an webapp using streamlit and connected with the django rest framework to compute on the user input and then fetch the output to frontend</p>

<h3>Installation Process</h3>
clone this repo

then run
```
pip install -r reuirements.txt
```

then go to the <mark>webapp.py</mark> directory and run
```
streamlit run webapp.py
```
this will start the webapp in 8501 port
then to start backend

go to drugpredapi folder where the django  project files are present and simply run

For Linux
```
python3 manage.py runserver
```

For Windows
```
python manage.py runserver
```
