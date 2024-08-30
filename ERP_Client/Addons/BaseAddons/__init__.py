# from .server_sql import server_data_format
# from .User import UserProfile
import os, sys

current_file_path = os.path.abspath(__file__)
addons_path = os.path.dirname(current_file_path)
sys.path.append(addons_path)