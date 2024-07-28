"""

Django command to wait for the database to be available

"""
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.core.management.base import BaseCommand

from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database"""

# entry point of me command when executed
    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('waiting for database...')  # shows in the console
        db_up = False
        while db_up is False:
            try:
                # check method is a built-in method from
                # Django’s BaseCommand class,
                # and it is used in this command to ensure the database
                # is up and running before proceeding.
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available...'))
