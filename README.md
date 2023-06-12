# Usage

1. Clone this repository (branch=pubsub-dev) and its sub-modules

    `git clone --recurse-submodules --branch pubsub-dev git@github.com:jadurani/rshake-tools.git`

2. Create and activate a virtual python environment

    `python3 -m venv .venv`

    `source .venv/bin/activate`

3. Install dependencies

    `pip install -r requirements.txt`

4. Run main function

    `python main.py`


## Troubleshooting

ERROR: Could not find a version that satisfies the requirement pkg_resources==0.0.0 (from versions: none)
ERROR: No matching distribution found for pkg_resources==0.0.0
WARNING: You are using pip version 21.2.4; however, version 23.1.2 is available.
You should consider upgrading via the '/Users/jadurani/code/citizen-science/rshake-tools/.venv/bin/python3 -m pip install --upgrade pip' command.

`./.venv/bin/python3 -m pip install --upgrade pip`


ERROR: Could not find a version that satisfies the requirement pkg_resources==0.0.0 (from versions: none)
ERROR: No matching distribution found for pkg_resources==0.0.0

comment out `pkg_resources==0.0.0`

In main.py. replace `rs.local` to the IP address of your raspishake unit (for me it's `192.168.1.60`)