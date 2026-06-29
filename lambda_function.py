import json
import boto3
from decimal import Decimal
from datetime import datetime

# AWS Clients
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

TABLE_NAME = "clean_records"
table = dynamodb.Table(TABLE_NAME)


def get_weather_status(temp):
    if temp >= 35:
        return "HOT"
    elif temp >= 25:
        return "WARM"
    else:
        return "COOL"


def lambda_handler(event, context):

    inserted = 0
    rejected = 0
    total = 0

    # Get uploaded file information
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    print(f"Reading file from S3: {bucket}/{key}")

    # Read file from S3
    response = s3.get_object(Bucket=bucket, Key=key)

    records = json.loads(response["Body"].read().decode("utf-8"))

    for record in records:

        total += 1

        try:

            city = record["city"].title()

            temperature = float(record["temperature"])
            humidity = int(record["humidity"])
            wind_speed = float(record["wind_speed"])

            latitude = Decimal(str(record["latitude"]))
            longitude = Decimal(str(record["longitude"]))

            timestamp = record["timestamp"]

            # Validation
            if temperature < -50 or temperature > 60:
                rejected += 1
                continue

            if humidity < 0 or humidity > 100:
                rejected += 1
                continue

            item = {

                "record_id": f"{city}_{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}",

                "city": city,

                "temperature_c": Decimal(str(temperature)),

                "humidity": humidity,

                "wind_speed_kmh": Decimal(str(wind_speed)),

                "latitude": latitude,

                "longitude": longitude,

                "weather_status": get_weather_status(temperature),

                "timestamp": timestamp

            }

            table.put_item(Item=item)

            inserted += 1

        except Exception as e:

            rejected += 1

            print(f"Rejected Record : {e}")

    print("========== ETL SUMMARY ==========")
    print(f"Total Records    : {total}")
    print(f"Inserted Records : {inserted}")
    print(f"Rejected Records : {rejected}")
    print("================================")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "total": total,
            "inserted": inserted,
            "rejected": rejected
        })
    }