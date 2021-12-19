import yaml
import os
import pathlib
from parsers.stepstone import StepstoneParser

def main():
    #Load Config file
    with open(os.path.join(pathlib.Path(__file__).parent.parent, "config.yaml")) as stream:
        try:
            config=yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    parser=StepstoneParser("Data Engineering", "Berlin", 30, debugmode=True)
    parser.parse()
    print(parser.encodedURL)
    print(parser.page_jobs)


if __name__ == '__main__':
    main()