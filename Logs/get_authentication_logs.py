"""
Example for extracting authentication logs from Duo Admin API
"""

import duo_client
import argparse
import datetime
import json
from pprint import pprint as pp


def human_time(seconds: int) -> str:
    """Convert Unix timestamp to human readable string"""
    return datetime.datetime.fromtimestamp(seconds / 1000).strftime(
        "%m/%d/%Y, %H:%M:%S"
    )


def get_arguments() -> argparse.Namespace:
    """Collect command line arguments."""
    parser = argparse.ArgumentParser()
    duo_credentials = parser.add_argument_group()
    duo_credentials.add_argument(
        "--ikey", "-i", nargs="?", required=True, help="Duo Auth API Integration key"
    )
    duo_credentials.add_argument(
        "--skey", "-s", nargs="?", required=True, help="Duo Auth API Secret key"
    )
    duo_credentials.add_argument(
        "--host", nargs="?", required=True, help="Duo Auth API hostname"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_arguments()

    client = duo_client.Admin(
        ikey=args.ikey,
        skey=args.skey,
        host=args.host,
    )

    now = datetime.datetime.now()
    mintime_ms = int((now - datetime.timedelta(weeks=16)).timestamp() * 1000)
    maxtime_ms = int(now.timestamp() * 1000)

    print(
        f"{mintime_ms=} ({human_time(mintime_ms)}), {maxtime_ms=}, ({human_time(maxtime_ms)})"
    )

    try:
        logs = client.get_authentication_log(api_version=2, mintime=mintime_ms, maxtime=maxtime_ms)
        if 'authlogs' in logs:
            for log in logs['authlogs']:
                # print(json.dumps(log))
                pp(log, depth=2)
    except RuntimeError as e_str:
        print(f"An error occurred while attempting to extract authentication logs: {e_str}")
        exit()
