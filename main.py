"""
Simple Desktop app to use openpecha-toolkit CLI
"""

from gooey import Gooey, GooeyParser


class cmd_names:
    DOWNLOAD = "download"
    APPLY_LAYER = "apply_layer"
    EDIT = "edit"
    UPDATE = "update"
    EXPORT = "export"


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

    download_parser = subs.add_parser(cmd_names.DOWNLOAD, prog="Download Pecha")
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

    layer_parser = subs.add_parser(cmd_names.APPLY_LAYER, prog="Apply Layer")
    layer_parser.add_argument(
        "pecha_id",
        metavar="Pecha ID/Number",
        help="Pecha ID like P0000001 or Number like 1",
    )
    layer_parser.add_argument("--layers", type=str)

    edit_parser = subs.add_parser(cmd_names.EDIT, prog="Edit text")
    edit_parser.add_argument(
        "pecha_id",
        metavar="Pecha ID/Number",
        help="Pecha ID like P0000001 or Number like 1",
    )
    edit_parser.add_argument("--volume", help="Volume number")
    edit_parser.add_argument("--text-id", help="ID of the text to be edited")

    update_parser = subs.add_parser(
        cmd_names.UPDATE,
        prog="Update Pecha",
        help=" update the base text with your edits",
    )
    update_parser.add_argument("Path to text", widget="FileChooser")

    export_parser = subs.add_parser(
        cmd_names.EXPORT, prog="Export Pecha", help="Export pecha in desirable format"
    )
    export_parser.add_argument(
        "pecha_id",
        metavar="Pecha ID/Number",
        help="Pecha ID like P0000001 or Number like 1",
    )
    export_parser.add_argument(
        "format",
        metavar="File format",
        widget="Dropdown",
        choices=[".txt", ".epub", ".docx", ".pdf", ".md"],
    )

    args = parser.parse_args()
    run(args)


def run(args):
    if args.command == cmd_names.DOWNLOAD:
        print(f"downloading pecha {args.pecha_id} ...")
        print(args)
        pass
    elif args.command == cmd_names.APPLY_LAYER:
        print(f"Applying layer for pecha {args.pecha_idi} ...")
        pass
    elif args.command == cmd_names.EDIT:
        print(f"Edit Volume")
        pass
    elif args.command == cmd_names.UPDATE:
        print("Updating pecha")
    else:
        print("Export pecha")


if __name__ == "__main__":
    main()
