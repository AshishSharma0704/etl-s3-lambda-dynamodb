# 🌦️ Serverless Weather ETL Pipeline on AWS

![AWS](https://img.shields.io/badge/AWS-Serverless-orange)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![DynamoDB](https://img.shields.io/badge/Database-DynamoDB-blue)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-success)
![CodePipeline](https://img.shields.io/badge/CD-CodePipeline-yellow)

## 📌 Project Overview

This project demonstrates a **serverless ETL (Extract, Transform, Load) pipeline** built on AWS. Weather data is uploaded to an Amazon S3 bucket, automatically triggering an AWS Lambda function that validates and transforms the data before loading it into Amazon DynamoDB. The project also includes a CI/CD pipeline using GitHub Actions, AWS CodeBuild, and AWS CodePipeline.

The solution is fully serverless, scalable, event-driven, and designed to demonstrate modern cloud-native data engineering practices.

---

# 🏗️ Architecture

> Add the architecture diagram below after uploading it to the repository.

```text
GitHub
    │
    ▼
GitHub Actions (CI)
    │
    ▼
AWS CodePipeline
    │
    ▼
AWS CodeBuild
    │
    ▼
Lambda Source Validation

──────────────────────────────────────

Weather JSON
      │
      ▼
 Amazon S3 (raw/)
      │
      ▼
 S3 Event Notification
      │
      ▼
 AWS Lambda
      │
 Extract
 Transform
 Validate
 Load
      │
      ▼
 Amazon DynamoDB
      │
      ▼
 Amazon CloudWatch Logs
```

---

# 🚀 Features

* Event-driven ETL using Amazon S3
* Serverless processing with AWS Lambda
* Automatic data validation
* Weather status classification
* DynamoDB storage
* CloudWatch logging and monitoring
* CI using GitHub Actions
* CD pipeline using AWS CodePipeline & CodeBuild
* Production-ready project structure

---

# 🛠️ AWS Services Used

| Service           | Purpose                              |
| ----------------- | ------------------------------------ |
| Amazon S3         | Stores raw weather JSON files        |
| AWS Lambda        | Extracts, transforms, and loads data |
| Amazon DynamoDB   | Stores cleaned weather records       |
| Amazon CloudWatch | Logs and monitoring                  |
| AWS IAM           | Access management                    |
| AWS CodeBuild     | Build validation                     |
| AWS CodePipeline  | CI/CD orchestration                  |
| GitHub Actions    | Continuous Integration               |

---

# 📂 Project Structure

```text
etl-s3-lambda-dynamodb/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── sample_data/
│   └── weather_data_100.json
│
├── screenshots/
│
├── lambda_function.py
├── requirements.txt
├── buildspec.yml
├── README.md
└── .gitignore
```

---

# ⚙️ Workflow

### Step 1 — Extract

* Weather JSON is uploaded to Amazon S3.
* S3 generates an ObjectCreated event.

### Step 2 — Transform

AWS Lambda automatically:

* Reads the JSON
* Validates each record
* Cleans the data
* Adds derived field:

```
weather_status
```

Classification:

| Temperature | Status |
| ----------- | ------ |
| <25°C       | COOL   |
| 25–34°C     | WARM   |
| ≥35°C       | HOT    |

### Step 3 — Load

The transformed records are inserted into Amazon DynamoDB.

---

# 📊 Sample Record

```json
{
  "record_id": "Delhi_20260629153000",
  "city": "Delhi",
  "temperature_c": 36.8,
  "humidity": 54,
  "wind_speed_kmh": 9.2,
  "weather_status": "HOT",
  "timestamp": "2026-06-29T10:30:00Z"
}
```

---

# 🔄 CI/CD Pipeline

## Continuous Integration

Every push to the `main` branch automatically triggers:

* GitHub Actions
* Python syntax validation

## Continuous Delivery

CodePipeline performs:

```
GitHub
    ↓
CodePipeline
    ↓
CodeBuild
    ↓
Build Validation
```

(Current implementation validates the Lambda source. Deployment to Lambda can be added as a future enhancement.)

---

# 📈 Monitoring

Amazon CloudWatch captures:

* Lambda execution logs
* Execution duration
* Invocation count
* Error metrics

Example ETL summary:

```text
Total Records : 100
Inserted Records : 100
Rejected Records : 0
```

---

# 🧪 Testing

### GitHub Actions

* Syntax validation
* Build verification

### Lambda

Triggered automatically when a JSON file is uploaded to Amazon S3.

### DynamoDB

Verify new records are inserted successfully.

---

# 📷 Screenshots

Include the following screenshots:

* S3 Bucket
* Lambda Function
* Lambda Trigger
* CloudWatch Logs
* DynamoDB Items
* GitHub Actions
* CodeBuild Success
* CodePipeline Success
* Architecture Diagram

---

# ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/etl-s3-lambda-dynamodb.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Upload the sample dataset to:

```
S3 Bucket
└── raw/
      weather_data_100.json
```

4. The pipeline automatically:

* Triggers Lambda
* Processes the data
* Loads records into DynamoDB
* Stores logs in CloudWatch

---

# 📌 Future Enhancements

* Automatic Lambda deployment through CodePipeline
* Infrastructure as Code using AWS CloudFormation or Terraform
* Data quality dashboards
* SNS email notifications
* EventBridge scheduling
* Dead Letter Queue (DLQ)
* AWS X-Ray tracing

---

# 📚 Technologies

* Python
* AWS Lambda
* Amazon S3
* Amazon DynamoDB
* Amazon CloudWatch
* GitHub Actions
* AWS CodeBuild
* AWS CodePipeline
* Git
* JSON

---

# 👨‍💻 Author

**Ashish Sharma**

Data Engineering | AWS | Python | Serverless ETL | Cloud Computing

---

## ⭐ If you found this project useful, consider giving it a star!
