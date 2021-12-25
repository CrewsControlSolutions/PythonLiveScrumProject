# PythonLiveScrumProject

<h2>Introduction</h2>
Written from scratch in Python using the Django web framework, this app holds competitor information for a Bitcoin price prediction competition. A competitor's entry, consisting of a 90-day price prediction and their contact info, is stored in a database and can easily be retrieved, updated, and/or deleted. The Model-View-Template (MVT) pattern in Django is used.
<br><br>
The web app utilizes best practices in code organization and UI/UX. To prevent unnecessary code reuse and to maintain consistent formatting, a base HTML file is extended to all other HTML files. The <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/HomePage.png">Home</a> page is an example of the user-friendly aesthetics used throughout the app.

<h2>CRUD Functionality</h2>
When interacting with the web app, Create, Read, Update, and Delete (CRUD) operations are performed on the database table containing the competitors.
<ul>
 <li><h3>Create</h3></li>
 The <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/JoinCompetitionPage.png">Join Competition</a> page allows the user to enter the competition by providing their name, Bitcoin price forecast, and LinkedIn profile. The web page displayed to the user is a specific Django <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/BitcoinAnalytics/templates/BitcoinAnalytics/bitcoin_analytics_add_competitor.html">template</a> rendered by a view and linked to the <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/BitcoinAnalytics/models.py">model</a> containing the attributes to be stored in the database. When the user selects "Submit," their information is saved as a single row of the sqlite3 database file. 
  <li><h3>Read</h3></li>
 The <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/CompetitionBoardPage.png">Competition Board</a> page displays the names and price predictions of all competitors. If an individual competitor is selected, all of their <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/CompetitorDetailsPage.png">details</a> are displayed on a subsequent page. The retrieval of competitor information is made possible by the "show_competition" and "selection" functions in the <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/BitcoinAnalytics/views.py">Views</a> file. The "selection" function is passed the primary key of the selected competitor from the table. Lastly, the web page paths are saved in the <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/BitcoinAnalytics/urls.py">URL patterns</a> file.
   <li><h3>Update and Delete</h3></li>
 The user has the ability to update or delete any competitor. Each of these operations requires a specific function found in the <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/BitcoinAnalytics/views.py">Views</a> file. If the user selects the "Delete" button, a <a href="https://github.com/CrewsControlSolutions/PythonLiveScrumProject/blob/main/DeleteConfirmationPage.png">Confirmation</a> page is displayed.
</ul>

<h2>Agile Software Development</h2>
This app was created during a two week Sprint using the PyCharm IDE and Microsoft Azure for DevOps. Multiple Stories were created to incrementally build the web app. To simulate real-world Agile development, a Branch was created for each of the Stories. Once a Branch was completed, changes were committed/pushed to GitHub and a Pull Request in Microsoft Azure was created. Following an instructor's review, the changes were merged into the Master Branch and the Story was closed. Daily Scrum meetings were held to monitor progress, culminating in a Sprint Retrospective at the end of the two-week period. 
