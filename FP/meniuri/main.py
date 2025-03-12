from ui.console import Console

if __name__ == '__main__':
    try:
        service = 1
        console = Console(service)
        console.run()
    except Exception as e:
        print(e)
