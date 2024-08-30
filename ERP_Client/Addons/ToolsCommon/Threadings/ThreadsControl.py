import concurrent.futures
import threading
import os, sys

from Addons.WareHouse.Tools import WarehouseServerData as whserv

current_file_path = os.path.abspath(__file__)
addons_path = os.path.dirname(current_file_path)
sys.path.append(addons_path)

executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
# executor.shutdown()
# def threadsControl(func, args: () | None, kwargs: {} | None) -> None:
def threadsControl(func, args: tuple = None, kwargs: dict = None):
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    if args is None:
        # thread = executor.submit(func)
        try:
            result = executor.submit(func).result()
            check_tasks()
            return result
        except:
            # print("Function execution failed")
            # raise
            return None
    else:
        thread = executor.submit(func, args)
        try:
            result = thread.result()
            check_tasks()
            return result
        except:
            # print("Function execution failed")
            # raise
            return None
    # return result
    # print(thread)

def check_tasks():
    if executor._work_queue.qsize() > 0:
        return
        # print("There are still tasks running.")
    else:
        executor.shutdown()
        # print("No tasks are running.")
        

    