import yaml
import os
import pathlib
from parsers import StepstoneParser
import logging

def main():
    #Load Config file
    # with open(os.path.join(pathlib.Path(__file__).parent.parent, "config.yaml")) as stream:
    #     try:
    #         config=yaml.safe_load(stream)
    #     except yaml.YAMLError as exc:
    #         print(exc)
    logging.basicConfig(filename="../output/logs.txt")
    parser=StepstoneParser("Data Engineering", "Berlin", 30)
    


if __name__ == '__main__':
    main()