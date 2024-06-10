def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default=None)
    parser.add_argument('--d', type=str, default=None)
    parser.add_argument('--gpu', type=int, default=0)
    parser.add_argument('--seed', type=int, default=3407)
    parser.add_argument('--load', action='store_true', default=False)
    parser.add_argument('--eval', action='store_true', default=False)
    args, overrides = parser.parse_known_args()
    # everything about configuration
    if len(overrides) > 0:
        print('>>> Override with Caution!!! >>>')
        opt = Config(args.cfg, args.d, overrides)
    else:
        opt = Config(args.cfg, args.d)
