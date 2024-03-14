"""Print Duo Trust Monitor Events which surfaced within the past two weeks."""

from __future__ import print_function, absolute_import
import datetime
import json
import argparse

from duo_client import Admin


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


def main():
    """
    Main program code
    """
    args = get_arguments()

    # Instantiate the Admin client object.
    admin_client = Admin(ikey=args.ikey, skey=args.skey, host=args.host)

    # Query for Duo Trust Monitor events that were surfaced within the last two weeks (from today).
    # now = datetime.datetime.now(datetime.timezone.utc)
    now = datetime.datetime.fromtimestamp(1706715579)
    mintime_ms = int((now - datetime.timedelta(weeks=16)).timestamp() * 1000)
    maxtime_ms = int(now.timestamp() * 1000)

    events = 0
    # Loop over the returned iterator to navigate through each event, printing it to stdout.
    print(
        f"{mintime_ms=} ({human_time(mintime_ms)}), {maxtime_ms=}, ({human_time(maxtime_ms)})"
    )

    mintime_increase_factor = 60  # 1 minute
    try:
        for event in admin_client.get_trust_monitor_events_iterator(mintime_ms, maxtime_ms):
            events += 1
            print(json.dumps(event, sort_keys=True, indent=2))
    except StopIteration:
        print("All events were returned for the time period requested.")
    except RuntimeError as runtime_error:
        print(f"Runtime error occurred: {runtime_error}")
        if "mintime must be within the past 180 days" in str(runtime_error):
            print(f"Increasing mintime by {mintime_increase_factor}")
            mintime_ms += mintime_increase_factor
    print(f"Total events: {events}")


if __name__ == "__main__":
    main()
