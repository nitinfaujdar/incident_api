Assignment:
You have to create a REST API for an incident management system.
Development Environment: Ubuntu (Version 18 & above), Development Language Python
3.8 and above, Database MySQL (Preferred)/ PostgreSQL & React.JS/ or any language for the
front end. If you do not have expertise in the front end, then you can demonstrate the same
using Postman.
The Front for the incident management system can be in any language you are comfortable
in and need to create the following
1. Front-End development: you need to create the following using ReactJs or any
language.
a. Registration Page for the user (See file registration.png)
b. Login Page- (Login.png)
c. Forgot Password (forgot password.png)
d. Create/view/edit- Incident- Use your own UI based on the inputs given below
in the backend section.
2. Back-End Development – this would need to be done using Python/Django Rest
Framework and should allow a user to log in and create incidents. You need to use
MySQL (preferred)
The Key functionalities to be demonstrated for the entire solution:
a. System should allow you to create multiple users.
b. Each User should be unique and should have the following details (see user
data.jpg file). You need to use any library wherein the moment one enters
the pin code, it should auto-select the City and Country,
i. User Name
ii. User Email ID
iii. User Phone Number
iv. User Address, Pin code
v. City and Country.
c. System should allow any user to create multiple incidents.
d. Each user can create multiple incidents.
e. Each Incident to have the following
i. Fields to identify Enterprise or Government
ii. Details of the person reporting the incident
iii. Ensure that if the person entering the details exists, auto-fill previous
information
iv. Auto-generate Incident ID and ensure that the format for the Incident
ID should be the following format- RMG + Random 5-digit number+
Current year (2022) e.g. RMG345712022
v. You need to ensure that each incident number should be unique. So
implement methods to check the uniqueness of the Incident.
vi. The incidents should have the following detailsa.Reporter name (Name of the user who logs in and creates the
incident)
b. Incident details (text field) Should be editable
c.Incident Reported date and time
d. Priority (Dropdown with values High, Medium, Low)
Should be editable
e.Incident status (Open, In progress, Closed) Should be editable
f. Limitations
i. A User should be allowed to view and edit the incidents created by
them only.
ii. No user should be able to view other users’ incidents.
iii. Any Incident which has the state = closed, should not be editable.
iv. There should be a provision to search the incident using the Incident
ID.
 
