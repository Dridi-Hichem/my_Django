import csv
import datetime
import pathlib
import random

from django.utils import timezone

from polls.models import Choice, Question


def run():
    print(" Polls Loader ".center(20, "="))

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print(" Data deleted successfully ".center(33, "="))

    with pathlib.Path.open("scripts/dj4e_batch.csv") as fh:
        reader = csv.reader(fh)
        next(reader)  # Advance past the header

        for row in reader:
            question, question_created = Question.objects.get_or_create(
                question_text=row[0]
            )
            if question_created:
                pub_date = (
                    timezone.now()
                    - datetime.timedelta(days=random.randint(0,365))
                )
                question.pub_date = pub_date
            question.save()

            choice_set = [
                Choice(choice_text=choice_text, question=question)
                for choice_text in row[1:]
            ]
            Choice.objects.bulk_create(choice_set)

    print(" Done ".center(12, "="))
