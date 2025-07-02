from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key-123'  # Required for session management

# ---------------------- Dummy Photographer Data ----------------------
photographers = [
    {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"], "image": "amit.jpg"},
    {"id": "p2", "name": "Sana Clickz", "skills": ["Fashion", "Event"], "image": "sana.jpg"}
]

availability_data = {
    "p1": ["2025-06-20", "2025-06-23"],
    "p2": ["2025-06-19", "2025-06-22"]
}

# List of all available services
services = [
    "wedding",
    "fashion",
    "nature",
    "events",
    "portrait",
    "product",
    "food",
    "architecture",
    "sports",
    "wildlife",
    "aerial",
    "newborn",
    "pet",
    "street",
    "documentary"
]

# ---------------------- Routes ----------------------

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# New route for contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/show-photographers')
def show_photographers():
    return render_template('photographers.html', 
                         photographers=photographers, 
                         availability_data=availability_data)

# Temporary storage (replace with a database later)
bookings = []

# Route to render the booking form
@app.route('/book')
def book():
    return render_template('book.html')

# Route to handle booking submissions
@app.route('/add_booking', methods=['POST'])
def add_booking():
    data = request.form
    
    # Extract form data
    booking_details = {
        'name': data.get('name'),
        'email': data.get('email'),
        'phone': data.get('phone'),
        'event_type': data.get('event-type'),
        'event_date': data.get('event-date'),
        'event_time': data.get('event-time'),
        'duration': data.get('event-duration'),
        'photographer': data.get('photographer'),
        'package': data.get('package'),
        'total_price': data.get('total')  # Calculated in frontend
    }
    
    bookings.append(booking_details)  # Store in list (replace with database)
    
    # Redirect to a confirmation page or back to home
    return redirect(url_for('booking_confirmation', booking_id=len(bookings)))

# Route to show booking confirmation
@app.route('/booking-confirmation/<int:booking_id>')
def booking_confirmation(booking_id):
    booking = bookings[booking_id - 1]  # Get the booking (simplified)
    return render_template('confirmation.html', booking=booking)

# Route to display user's bookings
@app.route('/my-bookings')
def my_bookings():
    return render_template('my_bookings.html', bookings=bookings)

# API endpoint to get photographer data (optional)
@app.route('/api/photographers')
def get_photographers():
    photographers = [
        {'id': 'john-doe', 'name': 'John Doe', 'specialty': 'Wedding'},
        {'id': 'sarah-johnson', 'name': 'Sarah Johnson', 'specialty': 'Portrait'},
        # Add more photographers...
    ]
    return jsonify(photographers)

# API endpoint to get package pricing (optional)
@app.route('/api/packages')
def get_packages():
    packages = {
        'wedding': {'base_price': 2000, 'hourly_rate': 150},
        'portrait': {'base_price': 250, 'hourly_rate': 100},
        # Add more packages...
    }
    return jsonify(packages)
# Service pages - one route per service
@app.route('/wedding')
def wedding():
    return render_template('wedding.html')

@app.route('/fashion')
def fashion():
    return render_template('fashion.html')

@app.route('/nature')
def nature():
    return render_template('nature.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/portrait')
def portrait():
    return render_template('portrait.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/sports')
def sports():
    return render_template('sports.html')

@app.route('/wildlife')
def wildlife():
    return render_template('wildlife.html')

@app.route('/aerial')
def aerial():
    return render_template('aerial.html')

@app.route('/newborn')
def newborn():
    return render_template('newborn.html')

@app.route('/pet')
def pet():
    return render_template('pet.html')

@app.route('/street')
def street():
    return render_template('street.html')

@app.route('/graduation')
def graduation():
    return render_template('graduation.html')
3.
# ---------------------- Run App ----------------------
if __name__ == '__main__':
    app.run(debug=True)