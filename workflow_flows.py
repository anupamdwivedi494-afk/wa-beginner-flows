
from prefect import flow, task

# -----------------------------
# Task Definitions
# -----------------------------

@task
def extract():
    """Extract data from source."""
    return "Data Extracted"

@task
def transform(data: str):
    """Transform the extracted data."""
    return f"{data} -> Transformed"  # Use ASCII arrow for compatibility

@task
def load(data: str):
    """Load the transformed data."""
    return f"{data}"  # Logs will not appear in Prefect Cloud for push-based deployments

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
    raw = extract()
    processed = transform(raw)
    load(f"{job_name}: {processed}")

@flow
def post_etl_flow():
    """Flow for post-ETL tasks."""
    return "Post ETL tasks executed"  # Logs not visible in Cloud UI

@flow
def notification_flow():
    """Flow for sending notifications."""
   
