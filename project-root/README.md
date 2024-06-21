# Project Overview
- Develop a web application for digitalizing the hospitality process for group accommodation.
- Allow users to upload two CSV files to efficiently allocate rooms in hostels.
- Ensure group members with the same ID stay together and adhere to hostel capacities and gender-specific accommodations.

# Technical Details
- CSV File 1 (Group Information)
- Contains group ID, number of members, and gender information.
- Various scenarios under the same registration ID: groups of different sizes and gender compositions.

- CSV File 2 (Hostel Information)
- Contains hostel name, room number, capacity, and gender accommodation.

# Frontend Requirements
- User-friendly interface to upload two CSV files.
- Algorithm for room allocation based on criteria:
  - Keep members of the same group together.
  - Separate boys and girls into respective hostels.
  - Ensure room capacity is not exceeded.

# Output
- Display of allocated rooms with group members.
- Downloadable CSV file with allocation details.

# Enhancements
- Include a feature to handle special requests or preferences from groups.
- Implement a feature to optimize room allocation based on proximity or specific requirements.
- Add a feature to generate reports or statistics on room occupancy and utilization.

# Programming Languages
- Frontend: HTML, CSS, JavaScript
- Backend: Python

# APIs
- Flask API for handling backend logic and routing
- Pandas API for reading and processing CSV files

# Packages and Libraries
- Flask (latest version) for creating web application and APIs
- Pandas (latest version) for data manipulation and analysis
- Bootstrap (latest version) for frontend design and layout
- jQuery (latest version) for frontend interactions and AJAX requests

# Rationale
- Python chosen for backend due to its ease of handling data processing tasks efficiently.
- Flask selected for API development as it provides a lightweight framework for building web applications.
- Pandas used for CSV file processing as it offers robust data manipulation capabilities.
- Bootstrap and jQuery chosen for frontend development to ensure a responsive and visually appealing interface.

# Frontend Design
- Create a simple interface with file upload buttons for CSV files.
- Display allocation results in a clear and organized format.
- Implement user-friendly feedback for successful uploads and allocations.

# Backend Logic
- Develop algorithms to allocate rooms based on the specified criteria.
- Ensure data integrity by handling edge cases like gender-specific accommodations and room capacity constraints.
- Generate downloadable CSV files with allocation details for users to access.

# Enhancements
- Implement a form for users to input special requests or preferences.
- Utilize geolocation APIs to optimize room allocation based on proximity.
- Integrate data visualization libraries for generating reports on room occupancy and utilization.