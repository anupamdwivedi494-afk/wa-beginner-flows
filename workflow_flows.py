
from prefect import flow, task, get_run_logger

@task
def extract():
    # Use Prefect logger so messages appear in Cloud logs for push work pools
    logger = get_run_logger()
    logger.info("Extracting data...")
    return "Data Extracted"

@task
def transform(data):
    logger = get_run_logger()
    logger.info(f"Transforming: {data}")
    return f"{data} → Transformed"

@task
def load(data):
    logger = get_run_logger()
    # Using logger ensures visibility in Prefect Cloud logs
    logger.info(f"Loading: {data}")
    return f"{data}"

@flow
def etl_flow(job_name: str = "Daily ETL"):   # FIXED: 'str' instead of 'ste'
    raw = extract()
    processed = transform(raw)
    load(f"{job_name}: {processed}")

@flow
def post_etl_flow():
    logger = get_run_logger()
    logger.info("Post ETL tasks executed")
    return "Post ETL tasks executed"

@flow
def notification_flow():
    logger = get_run_logger()
    logger.info("Notification    logger.info("Notification sent")
