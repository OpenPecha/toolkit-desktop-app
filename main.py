"""
Simple Desktop app to use openpecha-toolkit CLI
"""

import argparse

from gooey import Gooey, GooeyParser

running = True


@Gooey(
    program_name="OpenPecha Toolkit",
    program_description="toolkit for download, update, apply-layers and export text",
    default_size=(600, 720),
    navigation="TABBED",
    progress_regex=r"^Progress (\d+)$",
)
def main():
    parser = GooeyParser()
    subs = parser.add_subparsers(help="commands", dest="command")

    download_parser = subs.add_parser("download", prog="Download Pecha")
    download_parser.add_argument(
        "pecha_id",
        metavar="Pecha ID/Number",
        help="Pecha ID like P0000001 or Number like 1",
    )
    download_parser.add_argument(
        "--batch",
        help="path to text file containg list of names of echa in separate line. Poti batch download",
        widget="FileChooser",
    )
    download_parser.add_argument(
        "--by-layers",
        help="filter pecha by layer, specify layers names in comma separated, eg: title,yigchung,..",
    )
    download_parser.add_argument(
        "--output",
        metavar="Save at",
        default="./pecha",
        widget="DirChooser",
        gooey_options=dict(full_width=True,),
        help="directory to store all the pecha",
    )

    layer_parser = subs.add_parser("apply_layer",)
    layer_parser.add_argument(
        "pecha_id",
        metavar="Pecha ID/Number",
        help="Pecha ID like P0000001 or Number like 1",
    )
    layer_parser.add_argument("--list", type=str)

    update_parser = subs.add_parser(
        "update", prog="Update Pecha", help=" update the base text with your edits"
    )
    update_parser.add_argument("File", widget="FileChooser")

    export_parser = subs.add_parser("Export", help="Export pecha in desirable format")
    export_parser.add_argument("Pehca ID")

    args = parser.parse_args()
    run(args)


def run(args):
    if args.command == "download":
        print(f"downloading pecha {args.pecha_id}....")
        print(args)
        pass
    elif args.command == "apply_layer":
        # apply layers
        pass
    elif args.command == "update":
        # update the pecha
        pass
    else:
        # export pecha
        pass


if __name__ == "__main__":
    main()
