# from django.conf import settings
# from django_cron import CronJobBase, Schedule

# import requests

# from models import Actor, Director, Genre, Movie

# class updateAPIData(CronJobBase):
#     RUN_EVERY_MINS = 1440
#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

#     def do(self):
#         url = "https://api.themoviedb.org/3/movie/121?language=en-US"
#         headers = {
#             "accept": "application/json",
#             "Authorization": f"Bearer {settings.TMDB_API_KEY}"
#         }

#         response = requests.get(url, headers=headers)


