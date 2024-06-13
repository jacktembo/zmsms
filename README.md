
# ZMSMS - Zambia SMS Gateway API Python Client

ZMSMS is a Python client library for the Zambia SMS Gateway API. This library allows you to send SMS messages, check your account balance, and list available sender IDs using the Zambia SMS Gateway service.

## Installation

To install ZMSMS, simply clone the repository:

```sh
git clone https://github.com/jacktembo/zmsms.git
Usage
## Initialization
To use the ZMSMS client, you need to initialize it with your username and password:

from zmsms import SMSClient

username = 'your_username'
password = 'your_password'
client = SMSClient(username, password)

## Sending SMS
You can send an SMS message to one or more phone numbers using the send_sms method:

message = 'Hello, this is a test message.'
sender_id = 'YourSenderID'
phone_numbers = ['+260971234567', '+260976543210']

response = client.send_sms(message, sender_id, phone_numbers)
print(response)


## Checking Balance
You can check the balance of your account using the check_balance method:

response = client.check_balance()
print(response)


## Listing Sender IDs
You can list the available sender IDs using the list_sender_ids method:

response = client.list_sender_ids()
print(response)


# API Reference
send_sms(message: str, sender_id: str, phone_numbers: list) -> dict
Send an SMS message to one or more phone numbers.

Parameters:

message (str): The message to be sent.
sender_id (str): The sender ID to be used.
phone_numbers (list): A list of phone numbers to send the message to.
Returns:

dict: A dictionary containing the response from the API.
check_balance() -> dict
Check the balance of the account.

Returns:

dict: A dictionary containing the response from the API.
list_sender_ids() -> dict
List the available sender IDs.

Returns:

dict: A dictionary containing the response from the API.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
If you would like to contribute to this project, please open an issue or submit a pull request.

Contact
For any inquiries or issues, please contact jacktembo.
