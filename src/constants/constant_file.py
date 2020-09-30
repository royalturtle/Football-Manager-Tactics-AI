_project_path = "G:\\PHIL\\Coding\\PyCharm\\Project\\auto-football-tactics v2\\"

_dir_match = _project_path + "matches\\"
_dir_data = _project_path + "data\\"
_file_fd = _dir_data + "(v2.1) players stat (FD).csv"
_file_gk = _dir_data + "(v2.1) players stat (FD).csv"


class ConstantFile:
    @staticmethod
    def project_path():
        return _project_path

    @staticmethod
    def dir_match():
        return _dir_match

    @staticmethod
    def file_fd():
        return _file_fd

    @staticmethod
    def file_gk():
        return _file_gk
