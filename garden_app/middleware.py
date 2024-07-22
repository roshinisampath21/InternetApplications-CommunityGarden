from datetime import datetime
from django.utils.deprecation import MiddlewareMixin


class TrackUserVisitsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_date = datetime.now().date().isoformat()

        # Initialize session variables if not present
        if 'total_visits' not in request.session:
            request.session['total_visits'] = 0
            request.session['daily_visits'] = {}

        # Update total visits
        request.session['total_visits'] += 1

        # Update daily visit
        if current_date in request.session['daily_visits']:
            request.session['daily_visits'][current_date] += 1
        else:
            request.session['daily_visits'][current_date] = 1

        # Save session
        request.session.modified = True
