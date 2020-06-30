"""
Simple Desktop app to use openpecha-toolkit CLI
"""

import argparse

from gooey import Gooey, GooeyParser

running = True

@Gooey(optional_cols=2, program_name="OpenPecha Toolkit")
def main():
    settings_msg = 'toolkit for download, update, apply-layers and export text'
    parser = GooeyParser(description=settings_msg)
    parser.add_argument('--verbose', help='be verbose', dest='verbose',
                        action='store_true', default=False)
    subs = parser.add_subparsers(help='commands', dest='command')

    download_parser = subs.add_parser(
        'Download', help='')
    download_parser.add_argument('Pecha ID or Number',
                             help='Pecha ID like P0000001 or Number like 1',
                             type=str)
    download_parser.add_argument('--batch',
                             help='path to text file containg list of names of echa in separate line. Poti batch download')
    download_parser.add_argument('--by-layers',
                             help='filter pecha by layer, specify layers names in comma separated, eg: title,yigchung,..')
    download_parser.add_argument('--output', default='./pecha',
                             help='directory to store all the pecha')

    # ########################################################
    layer_parser = subs.add_parser(
        'Apply Layer', help='')
    layer_parser.add_argument('--name',
                              type=str)
    layer_parser.add_argument('--list',
                              type=str)

    # ########################################################
    update_parser = subs.add_parser(
        'Update', help=' update the base text with your edits')
    update_parser.add_argument('File',
                               widget='FileSaver', type=argparse.FileType())

    # ########################################################
    export_parser = subs.add_parser(
        'Export', help='Export pecha in desirable format')
    export_parser.add_argument('Pehca ID')
    parser.parse_args()

    display_message()


if __name__ == '__main__':
    main()
