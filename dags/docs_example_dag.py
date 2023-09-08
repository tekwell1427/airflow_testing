doc_md_DAG = """
### The Activity DAG

This DAG will help me decide what to do today. It uses the [BoredAPI](https://www.boredapi.com/) to do so.

Before I get to do the activity I will have to:

- Clean up the kitchen.
- Check on my pipelines.
- Water the plants.

Here are some happy plants:

<img src="https://www.publicdomainpictures.net/pictures/80000/velka/succulent-roses-echeveria.jpg" alt="plants" width="300"/>
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from pendulum import datetime
import requests

def query_api():
    #response = requests.get("https://www.boredapi.com/api/activity")
    #return response.json()["activity"]
    return "hello world"

with DAG(
    dag_id="docs_example_dag",
    start_date=datetime(2022,11,1),
    schedule="@daily",
    catchup=False,
    doc_md=doc_md_DAG
):

    tell_me_what_to_do = PythonOperator(
        task_id="tell_me_what_to_do",
        python_callable=query_api,
    )