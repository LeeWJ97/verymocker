import os


def get_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    return project_root


project_root = get_project_root()
print("root dir:", project_root)


matched_paths = []
raw_url = "https://reqres.in"  # example
raw_host = "reqres.in"