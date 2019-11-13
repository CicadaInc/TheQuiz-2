try:
    from game_main import GameMain
except ImportError as error:
    import traceback

    traceback.print_exc()
    print("Error occurred when trying to import Engine.")
    print("Likely submodule was not initialized")
    print("Run update_engine.bat")
    input("Press enter to continue")
else:

    if __name__ == '__main__':
        main = GameMain()
        main.start()
