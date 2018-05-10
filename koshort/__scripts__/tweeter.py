from koshort.stream import TwitterStreamer

def main():
    app = TwitterStreamer(async=False)
    app.options.verbose = True
    app.show_options()
    app.create_listener()
    app.stream(async=False)


if __name__ == '__main__':
    main()