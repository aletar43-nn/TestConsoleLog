import argparse
import json

# from tabulate import tabulate


class Logs:
    def __init__(self, file_names: list):
        self.files_list = file_names
        self.data: list[dict] = []
        self._read_logs()

    def _read_file_logs(self, file_name):
        with open(file_name, 'r') as f:
            for row in f:
                self.data.append(json.loads(row))

    def _read_logs(self):
        for file_name in self.files_list:
            self._read_file_logs(file_name)


class Report:
    def __init__(
        self,
        report_type: str,
        logs: Logs
    ):
        self.report_type = report_type
        self.logs = logs
        self.report_functions = {
            'average': self.average
        }

    def average(self):
        pass

    def write_report(self):
        r_type = self.report_type
        r_func = self.report_functions.get(r_type)

        if r_func is None:
            print(f'Неподходящий тип отчета "{r_type}"')
            exit


def main():
    parser = argparse.ArgumentParser(description='Logs writer')
    parser.add_argument('--files', dest='files', nargs='+', required=True)
    parser.add_argument('--report', dest='report_type', required=True)

    c_args = parser.parse_args()

    logs = Logs(c_args.files)
    report = Report(c_args.report_type, logs)

    report.write_report()


if __name__ == '__main__':
    main()
