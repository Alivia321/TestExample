from secondary import square_job
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("arg1", type=int, help="Integer to square")
    parser.add_argument("--delay", type=float, default=0, help="Optional delay in seconds")
    args = parser.parse_args()

    print("Running main.py", flush=True)
    square_job(args.arg1, args.delay)
