import csv
import os
from datetime import datetime


BASE_DIR = 'results/'
FILE_NAME = 'status_summary'
DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def __init__(self):
        self.status_summary = dict()

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item.get('status')
        self.status_summary[status] = self.status_summary.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        self.status_summary['total'] = sum(self.status_summary.values())
        self.write_to_csv(
            filename=FILE_NAME,
            dict_to_save=self.status_summary,
            header=('Статус', 'Количество')
        )

    def write_to_csv(self, filename: str, dict_to_save: dict, header: tuple):
        """Записывает файл filename_datetime_format.csv в BASE_DIR"""
        file = (
            filename
            + '_'
            + str(datetime.now().strftime(DATE_FORMAT))
            + '.csv'
        )
        full_file_name = os.path.join(BASE_DIR, file)
        with open(full_file_name, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for row in dict_to_save.items():
                writer.writerow(row)
