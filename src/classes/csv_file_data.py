from abc import ABC


@ABC
class CSVFileData:
    @staticmethod
    def from_csv():
        raise NotImplementedError