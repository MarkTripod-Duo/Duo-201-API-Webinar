# Postman JSON Configuration Files

[Postman](https://www.postman.com/) is an application for prototyping and testing of APIs. It is available for download
on all major workstation operating systems.

---

The JSON files contained here describe dedicated Postman Collections and Environments for use with each of the Duo APIs.

To use any of the JSON configuration files:

1. Download the desired JSON configuration file
1. Open the Postman application
1. Expand the **File** menu item
1. Select **Import...**
1. Click on the **Upload Files** button
1. Navigate to the downloaded JSON file, select it and then click the **Open** button

The new Collection or Environment should now be visible within Postman.

   ---

### The Postman Environments

The Postman Environments are intended to represent discreet Duo API integrations as they are configured
within a Duo account. The Postman Environments contain variables for the API Integration key `ikey`,
API Secret key `skey`, and the API Hostname `apihost`. 

> [!IMPORTANT]
> The `current value` setting for all three variables must be set before any of the examples contained here can be used.


   ---

### Duo API Authorization

The various Duo API endpoints require each incoming request to be set with a properly formatted
HTTP Authorization header created using the `ikey`, `skey`, and `apihost` values. For this reason, there is a pre-request
script included with the Postman Collection templates in this repository. Any request that is executed
from within the Collections will automatically have the proper headers calculated and included with the requests before
they are sent to the Duo APIs.


   ---

### Troubleshooting

The pre-request script also contains a fair amount of code to provide logging of operations that it is performing. Should
an unexpected result or failure occur, the Postman Console will contain all of the log information. It is recommended that
investigations begin there for determine the cause of any failures.