# Log Extraction

The various reporting logs that are available in the Duo Administration Panel can be accessed and exported via the 
Duo Admin API.

---

### Script Descriptions

* [get_authentication_logs.py](get_authentication_logs.py) : This script provides a basic example of how the user authentication logs can be extracted using the Duo Admin API. The method to access the other log types is very similar and can be quickly replicated using this as a base example.
* [trust_monitor_events.py](trust_monitor_events.py) : This script shows an example of how to collect the available Duo Trust Monitor events that have been triggered.

---

### Usages

```bash
usage: python3 get_authentication_logs.py [-h] --ikey [IKEY] --skey [SKEY] --host [HOST]

options:
  -h, --help                show this help message and exit

  --ikey [IKEY], -i [IKEY]  Duo Auth API Integration key
  --skey [SKEY], -s [SKEY]  Duo Auth API Secret key
  --host [HOST]             Duo Auth API hostname
```

---

```bash
usage: python3 trust_monitor_events.py [-h] --ikey [IKEY] --skey [SKEY] --host [HOST]

options:
  -h, --help                show this help message and exit

  --ikey [IKEY], -i [IKEY]  Duo Auth API Integration key
  --skey [SKEY], -s [SKEY]  Duo Auth API Secret key
  --host [HOST]             Duo Auth API hostname
```

