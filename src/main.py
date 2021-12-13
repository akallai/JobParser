import yaml
import os
import pathlib

def main():
    #Load Config file
    with open(os.path.join(pathlib.Path(__file__).parent.parent, "config.yaml")) as stream:
        try:
            config=yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == '__main__':
    main()
    parser = 