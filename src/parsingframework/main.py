import yaml
import os
import pathlib
import logging

from parsers import StepstoneParser

def main():
    #Load Config file
    # with open(os.path.join(pathlib.Path(__file__).parent.parent, "config.yaml")) as stream:
    #     try:
    #         config=yaml.safe_load(stream)
    #     except yaml.YAMLError as exc:
    #         print(exc)
    logging.basicConfig(filename="logs.txt")
    parser=StepstoneParser("Schauspieler", "Rheine", 30)

    
    parser.parse()
    parser.to_json("output.json")


if __name__ == '__main__':
    main()