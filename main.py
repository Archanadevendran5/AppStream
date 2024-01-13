import time


def execution(value):
    st = time.time()
    if value == "f":
        import src.execution.Fleets
        src.execution.Fleets.fleets()
    elif value == "i":
        import src.execution.ImageBuilder
        src.execution.ImageBuilder.imageBuilder()
    elapsed_time = time.time() - st
    print('Total Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))


while True:
    inputValue = input("To run ImageBuilder type 'i' & for Fleets type 'f' : ")
    if inputValue == "f":
        execution('f')
        break
    elif inputValue == "i":
        execution('i')
        break
    else:
        print("Invalid input. Please enter 'f' or 'i'.")
