# Duo Auth API Examples

The scripts in this folder are dedicated to providing examples of how to accomplish specific tasks
using the Duo Auth API. 


---

### Script Descriptions

* [email_enroll_urls.py](email_enroll_urls.py) : This script demonstrates how the Duo Auth API can be used to enroll users and capture the activation URL that can be sent to the user separately to complete enrollment in Duo. This is an easy way for companies to automate the onboarding of new users while also maintaining control over how the activation information is delivered.


---

### Usage

```bash
usage: python3 email_enroll_urls [-h] --ikey [IKEY] --skey [SKEY] --host [HOST] [--file [FILE] | --user [USER]]

Example script to enroll users in Duo using the Duo Auth API.

options:
  -h, --help                show this help message and exit

Required Duo API Credentials:
  All three Duo Auth API integration key (ikey), secret key (skey), and api-hostname (host) arguments required to access the API.

  --ikey [IKEY], -i [IKEY]  Duo Auth API Integration key
  --skey [SKEY], -s [SKEY]  Duo Auth API Secret key
  --host [HOST]             Duo Auth API hostname

Other options:
  Select how the users should be input into the script to enroll

  --file [FILE], -f [FILE]  The name of the file containing the list of users to enroll.
  --user [USER], -u [USER]  The name of a single user to enroll.
```