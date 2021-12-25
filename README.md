# PythonLiveScrumProject

<h2>Introduction</h2>
Written from scratch in Python using the Django web framework, this app holds competitor information for a Bitcoin price prediction competition. A competitor's entry, consisting of a price prediction and their contact info, is stored in a database and can easily be retrieved, updated, and/or deleted. The Model-View-Template (MVT) pattern in Django is used.
<br><br>
The web app utilizes best practices in code organization and UI/UX. To prevent unnecessary code reuse and to maintain consistent formatting, a base HTML file is extended to all other HTML files. The Home page is an example of the user-friendly aesthetics used throughout the app.

<h2>CRUD Functionality</h2>
When interacting with the web app, Create, Read, Update, and Delete (CRUD) operations are performed on the database table containing the competitors.
<ul>
 <li><h3>Create</h3></li>
 The Join Competition page allows the user to enter the competition by providing their name, Bitcoin price prediction, and LinkedIn profile. The web page displayed to the user is a Django template rendered by a view and linked to the model containing the attributes to be stored in the database. When the user selects "Submit," their information is saved as a single row in the sqlite3 database file. 
  <li><h3>Read</h3></li>
 The Competition Board page displays the names and price predictions of all competitors. If an individual competitor is selected, all of their details are displayed on a subsequent web page. The retrieval of competitor information is made possible by the "show_competition" and "selection" functions in the Views file. The "selection" function is passed a primary key of the selected competitor from the table. It is also worth mentioning that the web page paths are saved in the URL patterns file.
   <li><h3>Update and Delete</h3></li>
 The user has the ability to update or delete any competitor. Each of these operations requires a specific function found in the Views file. If the user selects the "Delete" button, a Confirmation page is displayed.
</ul>

<h2>Agile Software Development</h2>
This app was created during a two week Sprint using the PyCharm IDE and Microsoft Azure for DevOps. Multiple Stories were created to incrementally build the web app. To simulate real-world Agile development, a Branch was created for each of the Stories. Once a Branch was complete, changes were committed/pushed to GitHub and a Pull Request in Microsoft Azure was created. Following an instructor's review, the changes were merged into the Master Branch and the Story was closed. Daily Scrum meetings were held to monitor progress, culminating in a Spring Retrospective at the end of the two-week period. 
