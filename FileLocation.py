from abc import ABC, abstractmethod


class FileLocation(ABC):

    def authorize_user(self):
        pass

    @abstractmethod
    def set_connection_to_database(self):
        pass

    @abstractmethod
    def read_directory_with_regrex(self):
        pass

    @abstractmethod
    def check_if_latest_file_is_already_present_in_directory(self):
        pass

    @abstractmethod
    def list_all_columns_from_table(self):
        pass

    @abstractmethod
    def select_columns_from_table(self):
        pass

    @abstractmethod
    def push_file_to_gcp_bucket(self):
        pass


