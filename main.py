import argparse
from scripts.vid2vid import vid2vid

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--config", type=str, required=True)
        args = parser.parse_args()
        vid2vid(config_path=args.config)
    except Exception as e:
        print("An Error occured: ", e)
