from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="supply_chain_kpi_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["supply-chain", "etl", "kpi"]
) as dag:

    run_pipeline = BashOperator(
        task_id="run_supply_chain_pipeline",
        bash_command="python /opt/airflow/app/pipeline.py"
    )