from datetime import datetime
from django.utils.deprecation import MiddlewareMixin


class TrackUserVisitsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_date = datetime.now().date().isoformat()
        user_history_path = '/user_history/'
        # Initialize session variables if not present
        if 'total_visits' not in request.session:
            request.session['total_visits'] = 0
            request.session['daily_visits'] = {}

        # Update total visits
        if request.path == user_history_path:
            request.session['total_visits'] += 1

        # Update daily visits
        if current_date in request.session['daily_visits'] and request.path == user_history_path:
            request.session['daily_visits'][current_date] += 1
        else:
            request.session['daily_visits'][current_date] = 1

        # Save session
        request.session.modified = True
