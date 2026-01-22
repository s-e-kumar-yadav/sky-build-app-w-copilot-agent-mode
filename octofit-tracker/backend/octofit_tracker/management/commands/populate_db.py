from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete all data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        running = Workout.objects.create(name='Running', description='Run 5km')
        pushups.suggested_for.set([tony, bruce])
        running.suggested_for.set([steve, clark])

        # Create Activities
        Activity.objects.create(user=tony, type='pushups', duration=10, date=timezone.now())
        Activity.objects.create(user=steve, type='running', duration=30, date=timezone.now())
        Activity.objects.create(user=bruce, type='pushups', duration=15, date=timezone.now())
        Activity.objects.create(user=clark, type='running', duration=25, date=timezone.now())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=98)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
