from datetime import datetime, timedelta

from datetime import datetime, timedelta


class DateAndTime:

    @staticmethod
    def get_future_datetime(days=15):
        future = datetime.now() + timedelta(days=days)
        future = future.replace(hour=10, minute=0, second=0, microsecond=0)
        return future

    @staticmethod
    def get_current_datetime():
        return datetime.now()

    @staticmethod
    def get_past_datetime(days=1, hour=10, minute=0):
        past = datetime.now() - timedelta(days=days)
        past = past.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0
        )
        return past