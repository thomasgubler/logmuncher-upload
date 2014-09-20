#!/usr/bin/env python
import requests
import time
import argparse
__author__ = "Thomas Gubler"
__license__ = "BSD"
__email__ = "thomasgubler@gmail.com"


class Uploader():
    """Uploads logs to logmuncher"""

    def __init__(self, args):
        """Constructor"""
        self.email = args.email
        self.verbose = args.verbose

    def upload(self, filenames):
        """upload each file to logmuncher"""

        print("I am going to upload the following files", filenames)

        for f in filenames:
            print("uploading", f)
            self.filenames = args.filenames
            payload = {
                'email': self.email,
                'title': f
            }
            files = {'file': open(f, 'rb')}
            r = requests.post("http://dash.oznet.ch/upload",
                              data=payload, files=files)

            if r.status_code == requests.codes.ok:
                print("uploaded", f)
            else:
                print("error while uploading", f, "status code:", r.status_code)
                print("Dumping response:\n", r.raw)

            if self.verbose:
                print(r.text)

            time.sleep(1)


if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Logmuncher upload tool')
    parser.add_argument(dest='email', default='', action='store',
                        help='Email')
    parser.add_argument(dest='filenames', default='', action='store',
                        help='Filenames of logfiles', nargs='+')
    parser.add_argument('-v', '--verbose', dest='verbose', default=False,
                        action='store_true', help='print more output')

    args = parser.parse_args()

    u = Uploader(args)
    u.upload(args.filenames)
