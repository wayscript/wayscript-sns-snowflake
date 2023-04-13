# AWS S3 Event -> Write to Snowflake Database
This lair is used to monitor whenever a file is added to an s3 bucket. Once that file is added to the bucket, a file within that bucket is pulled and compared to the current snowflake database.
Then if differences exist, the new values are added to the snowflake DB

## Setup 
Setup for this service will require several things:
1. AWS account with the ability to create SNS Topics, SNS subscriptions, IAM Users
2. A snowflake database
3. Data being placed in an S3 bucket with consistent naming
4. A Wayscript Account
5. Alter SNS Policies


* Amazon SNS Topic
First you will need to create an AWS SNS Topic that will monitor your bucket for changes. For additional information on SNS, view these docs:
https://aws.amazon.com/sns/features/

* SNS Subscription
You will need to subscribe your S3 bucket to the sns subscription to recieve alerts that a new file has changed. This alert will be used to trigger the webhook built by wayscript.

* IAM User
An IAM user's credentials will be used in this code to grab the contents of an s3 bucket's file. This file's name can be changed in app.py 

* WayScript Account
A wayscript account will be used to be the datapipe line to transfer data from the S3 bucket to the snowflake database, while also processing it to find the relevent data in the set.

* Snowflake Data
The snowflake database will be used as the receipt of the final data from the S3 bucket. This is optional and any other datbase can be used in this instance. The credentials for the database will be very similar regardless of the chosen database.


To run this code for yourself you will need to input some credential values from your services into your wayscript's secrets manager.
These values include the credentials to make each of the clients within this code. This includes: Snowflake and your AWS IAM user.


# Additional Information

## AWS SNS OVERVIEW
* What is AWS SNS?
SNS stands for simple notification service. This AWS service allows you to create a variety of notifications (SMS, HTTP, ETC.) whenever certain AWS actions occur.
We can create these notifications by first creating an AWS SNS Topic. 

* What are SNS Topics?
A SNS topic allows you to group multiple endpoints to broadcast a message to. ( i.e. EVENT -> SMS message, HTTP POST, and an email.)

* What are IAM Users?
An IAM User allows AWS users to selectively choose what permissions they want to assign to security credential keys. These keys limit control of your AWS account to allow you to create many different keys for different actions. This prevents an AWS account takeover from one leak of credentials and gives admins better control over their aws resources

