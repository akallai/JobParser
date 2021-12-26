import yaml
import os
import pathlib
import logging

from parsers import StepstoneParser

def main():
    #Load Config file
    with open(os.path.join(pathlib.Path(__file__).parent.parent, "config.yaml")) as stream:
        try:
            config=yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    config_databases = config["database"]
    config_jobs = config["jobs"]
    config_city = config["location"]["city"]
    config_radius = config["location"]["radius"]
    config_max_threads = config["threads"]["max"]
    config_max_pages = config["max_pages"]

    if "Stepstone" in config_databases:
        for job in config_jobs:
            parser = StepstoneParser(job, config_city, config_radius, config_max_threads, config_max_pages)
            parser.parse()
            parser.to_json("output.json")
    """
    logging.basicConfig(filename="logs.txt")
    parser=StepstoneParser("Schauspieler", "Rheine", 30)

    
    parser.parse()
    parser.to_json("output.json")"""


if __name__ == '__main__':
    main()