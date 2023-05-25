"""ArgumentParser for `__main__`."""

import argparse
import datetime

import dateutil.parser


TIME_PARSER = argparse.ArgumentParser(add_help=False)
TIME_PARSER.add_argument(
    "-s",
    "--start",
    help="Observations recorded after this date (by default, 14 days ago).",
    type=dateutil.parser.parse,
    default=datetime.datetime.now() - datetime.timedelta(days=14),
)
TIME_PARSER.add_argument(
    "-e",
    "--end",
    help="Observations recorded before this date (by default, now).",
    type=dateutil.parser.parse,
    default=datetime.datetime.now(),
)
TIME_PARSER.add_argument(
    "-d",
    "--delta",
    help="A delta in days from to subtract from '--end' - overrides '--start' if also given.",
    type=dateutil.parser.parse,
    default=None,
)

ID_PARSER = argparse.ArgumentParser(add_help=False)
ID_PARSER.add_argument(
    "id", help="The ID (or slug if applicable) of the object to query for."
)

MAIN_PARSER = argparse.ArgumentParser(
    description=__doc__,
)
MAIN_PARSER.add_argument("--debug", help="Display debug output.", action="store_true",)
SUBPARSER = MAIN_PARSER.add_subparsers(dest="command", title="Commands")

AVY_OBS_PARSER = SUBPARSER.add_parser(
    "avy-obs", description="Query avalanche observations.", parents=[TIME_PARSER]
)
FIELD_REPORTS_PARSER = SUBPARSER.add_parser(
    "field-reports",
    description="Query field (or observation) report.",
    parents=[TIME_PARSER],
)
FIELD_REPORT_PARSER = SUBPARSER.add_parser(
    "field-report",
    description="Query for a single field (or observation) report.",
    parents=[ID_PARSER],
)
SNOWPACK_PARSER = SUBPARSER.add_parser(
    "snowpack-observation",
    description="Query for a single Snowpack Observation.",
    parents=[ID_PARSER],
)