
# workflow_flows.py
from prefect import flow, task, get_run_logger

# -----------------------------
# Task Definitions
# -----------------------------

@task
def extract():
    """Extract data from source."""
    logger = get_run_logger()
    logger.info("Extracting data...")
    return "Data Extracted"

@task
def transform(data: str):
    """Transform the extracted data."""
    logger = get_run_logger()
    logger.info(f"Transforming data: {data}")
    return f"{data} -> Transformed"  # Use ASCII arrow

@task
def load(data: str):
    """Load the transformed data."""
    logger = get_run_logger()
    logger.info(f"Loading data: {data}")
    return data

# -----------------------------
# Flow Definitions
# -----------------------------

@flow
def etl_flow(job_name: str = "Daily ETL"):
    """
    Main ETL flow:
    1. Extract data
    2. Transform data
    3. Load data
    """
    logger = get_run_logger()
    logger.info(f"Starting ETL Flow for job: {job_name}")
    raw = extract()
    processed = transform(raw)
    load(f"{job_name}: {processed}")
    logger.info("ETL Flow completed")

@flow
def post_etl_flow():
    """Flow for post-ETL tasks."""
    logger = get_run_logger()
    logger.info("Post ETL tasks executed")
    return "Post ETL tasks executed"

@flow
def notification_flow():
    """Flow for sending notifications."""
       logger = get_run_logger()
    logger.info("Notification sent")
