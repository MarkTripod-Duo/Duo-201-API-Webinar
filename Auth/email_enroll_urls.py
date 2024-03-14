"""
Script to use Duo Auth API to enroll a list of users and collect the enrollment URLs for each.
The enrollment URLs can then be sent separately to each user via the customer internal message
delivery system.

"""

import duo_client
import argparse


def get_arguments() -> argparse.Namespace:
    """Collect command line arguments."""
    parser = argparse.ArgumentParser(
            prog='email_enroll_urls',
            description='Example script to enroll users in Duo using the Duo Auth API.',
            formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=45)
    )
    duo_credentials = parser.add_argument_group(
            title="Required Duo API Credentials",
            description="All three Duo Auth API integration key (ikey), secret key (skey), and api-hostname (host) "
                        "arguments required to access the API. ")
    duo_credentials.add_argument("--ikey", "-i", nargs="?", required=True,
                                 help="Duo Auth API Integration key")
    duo_credentials.add_argument("--skey", "-s", nargs="?", required=True,
                                 help="Duo Auth API Secret key")
    duo_credentials.add_argument("--host", nargs="?", required=True,
                                 help="Duo Auth API hostname")
    users_input_group = parser.add_argument_group(
            title="Other options",
            description="Select how the users should be input into the script to enroll"
    )

    exclusive_grp = users_input_group.add_mutually_exclusive_group()
    exclusive_grp.add_argument(
        "--file",
        "-f",
        nargs="?",
        help="The name of the file containing the list of users to enroll.",
    )
    exclusive_grp.add_argument(
        "--user", "-u", nargs="?", help="The name of a single user to enroll."
    )
    return parser.parse_args()


def parse_users_file(file_name: str) -> list:
    """Open file_name and return the read list of users"""
    users = []
    try:
        with open(args.file) as fn:
            for line in fn.readlines():
                user = line.strip()
                if users != "":
                    users.append(user)
        return users
    except FileNotFoundError as e_str:
        print(f"The provided file name cannot be found: {e_str}")
        exit()
    except OSError as os_str:
        print(f"The provided file could not be opened: {os_str}")
        exit()


def enroll_users(ikey: str, skey: str, host: str, users: list) -> list[tuple[str, str, str]]:
    """Enroll users in Duo using the Auth API and return the enrollment links"""
    client = duo_client.Auth(ikey=ikey, skey=skey, host=host)
    try:
        client.check()
    except RuntimeError as e_str:
        print(f"Validation of Duo Auth API credentials failed. Please verify the information and try again. [{e_str}]")
        exit()
    enrollment_results = []
    for user in users:
        try:
            resp = client.enroll(user)
            if isinstance(resp, dict) and 'user_id' in resp:
                enrollment_results.append((resp['username'], resp['user_id'], resp['activation_url']))
        except RuntimeError as user_str:
            print(f"Enrollment for {user} failed: {user_str}")
            continue
    return enrollment_results


def output_users(enrollment_results: list[tuple[str, str, str]]):
    """Output the results of the enrollment actions"""
    columns = ["Username", "user_id", "activation_url"]
    print(f"{columns[0]:^25} | {columns[1]:^25} | {columns[2]}")
    for entry in enrollment_results:
        print(f"{entry[0]:<25}   {entry[1]:<25} | {entry[2]}")


if __name__ == "__main__":
    """Main program entry point"""
    # Collect command-line arguments
    args: argparse.Namespace = get_arguments()

    users: list = []

    # If a file name was provided, parse it and add users to the list
    if args.file:
        print(f"... Reading user file: {args.file}")
        users = parse_users_file(args.file)
    if args.user:
        print(f"... Processing user: {args.user}")
        users = [args.user]

    print("... Enrolling users ...")
    email_links: list[tuple[str, str, str]] = enroll_users(args.ikey, args.skey, args.host, users)
    print("... Outputting results ...")
    output_users(email_links)
    print("\n=== Done ===\n")