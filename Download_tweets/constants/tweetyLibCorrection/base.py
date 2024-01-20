import time
import logging
import os
import datetime as date
from ..utils import find_objects, parse_wait_time


class BaseGeneratorClass(dict):

    def setup_logging(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        timestamp = date.date.today().strftime("%Y-%m-%d")
        file_handler = logging.FileHandler(f"logs/twitter_service_{timestamp}.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def _get_cursor(self, response):
        cursor = find_objects(response, "cursorType", "Bottom")

        if not cursor:
            return False

        newCursor = cursor.get('value', self.cursor)

        if newCursor == self.cursor:
            return False

        self.cursor = newCursor
        return True

    def _get_cursor_top(self, response):
        cursor = find_objects(response, "cursorType", "Top")

        if not cursor:
            return False

        newCursor = cursor.get('value', self.cursor)

        if newCursor == self.cursor_top:
            return False

        self.cursor_top = newCursor
        return True

    @staticmethod
    def _get_entries(response):
        entry = find_objects(response, "type", "TimelineAddEntries")

        if not entry:
            return []

        return entry['entries']

    def generator(self):
        for page in range(1, int(self.pages) + 1):
            results = self.get_next_page()
            yield self, results

            if not self.is_next_page or len(results) == 0:
                break

            if page != self.pages:
                time.sleep(parse_wait_time(self.wait_time))

        return self

    def __repr__(self):
        class_name = self.__class__.__name__
        return "{}(user_id={}, count={})".format(
            class_name, self.user_id, self.__len__()
        )