import pdb

from models.ticket import Ticket
import repositories.ticket_repository as ticket_repository

from models.bug import Bug
import repositories.bug_repository as bug_repository

from models.product import Product
import repositories.product_repository as product_repository

from models.user import User
import repositories.user_repository as user_repository

# ticket_repository.delete_all()
# bug_repository.delete_all()
# product_repository.delete_all()
# user_repository.delete_all()

user1 = User("Pippo Lo Russo", "Admin")
user_repository.save(user1)

user2 = User("Leila Simmons", "Developer")
user_repository.save(user2)

user3 = User("Kyle Montgomery", "Developer")
user_repository.save(user3)

user4 = User("Laura Benitez", "Developer")
user_repository.save(user4)

user5 = User("Johann Van Sanchez", "Tech Support")
user_repository.save(user5)

user6 = User("Mia Stockwell", "Tech Support")
user_repository.save(user6)

user7 = User("Luis Perez", "Tech Support")
user_repository.save(user7)

product1 = Product("GeniusPDF")
product_repository.save(product1)

product2 = Product("Diamond Scan")
product_repository.save(product2)

product3 = Product("docuMental")
product_repository.save(product3)

product4 = Product("OmniConverter")
product_repository.save(product4)


bug1 = Bug(
    "Not showing PDF preview",
    "PDF preview does not show in Icon View when program is in Desktop mode.",
    product3,
    "16 April 2022"
    )
bug_repository.save(bug1)

bug2 = Bug(
    "Indexing fails: too many files",
    "Indexing process hangs in folders with number of files between 665 and 667.",
    product3,
    "30 April 2022"
    )
bug_repository.save(bug2)

bug3 = Bug(
    "AudioNotes cannot access microphone",
    "The feature AudioNotes cannot access the microphone to record voice notes. Error: the application can't find a multimedia driver.",
    product3,
    "8 May 2022"
    )
bug_repository.save(bug3)

bug4 = Bug(
    "Check for Updates causes application to close",
    "Application shuts down whenever the user clicks the Check For Updates button on the Help ribbon.",
    product3,
    "19 May 2022"
    )
bug_repository.save(bug4)

bug5 = Bug(
    "Email Document does not connect to Gmail",
    "The Email Document feature cannot get to connect to Gmail: connection error 1248 from Google server.",
    product3,
    "11 June 2022"
    )
bug_repository.save(bug5)

bug6 = Bug(
    "Spanish proofreading unresponsive",
    "Spanish OCR proofreading tends to hang or flag random errors in unexpected contexts.",
    product2,
    "9 April 2022"
    )
bug_repository.save(bug6)

bug7 = Bug(
    "Contents not showing correctly in Scan dialog box",
    "The Scanner dialog box cuts off the advanced options that should be displayed on the side.",
    product2,
    "12 May 2022"
    )
bug_repository.save(bug7)

bug8 = Bug(
    "Scanning unresponsive with Canon TWAIN driver",
    "When a TWAIN driver is selected for a Canon device, scanning is poerformed but no graphic data are acquired.",
    product2,
    "10 June 2022"
    )
bug_repository.save(bug8)

bug9 = Bug(
    "Program does not lunch if BitDefender is running",
    "When BitDefender is running on system, the application will not start.",
    product2,
    "4 July 2022"
    )
bug_repository.save(bug9)

bug10 = Bug(
    "Script error when accessing Online Help",
    "When trying to open the Online Help a script error shows up. If user clicks 'run script' it returns a blank page.",
    product2,
    "15 July"
    )
bug_repository.save(bug10)


bug11 = Bug(
    "Cloud Share option permanently greyed out",
    "The Cloud Share option is constantly unaccessible on the 'Share' ribbon.",
    product1,
    "9 April 2022"
    )
bug_repository.save(bug11)

bug12 = Bug(
    "PDF to JPEG conversion produces unexpected result",
    "Graphic characters and fonts are generated instead of the expected graphic conversion to JPEG.",
    product1,
    "22 Aprile 2022"
    )
bug_repository.save(bug12)

bug13 = Bug(
    "A3 format compromises document layout",
    "Setting document size to A3, whatever the orientation, causes serious layout issues.",
    product1,
    "8 May 2022"
    )
bug_repository.save(bug13)

bug14 = Bug(
    "Network installation on Windows Server 2012",
    "Users are unable to deploy network installations on Windows Server 2012. Process does not even start.",
    product1,
    "23 June 2022"
    )
bug_repository.save(bug14)

bug15 = Bug(
    "Image captions cannot be edited",
    "Mouse-click on image_caption objects does not trigger edit mode in caption field.",
    product1,
    "24 June 2022"
    )
bug_repository.save(bug15)

bug16 = Bug(
    "Full screen view turnes the screen green",
    "When setting the view to Full Screen mode the screen becomes green. Switching Full Screen mode off does not help.",
    product4,
    "16 July 2022"
    )
bug_repository.save(bug16)

ticket1 = Ticket(
    bug11,
    product1,
    "9 April 2022",
    user4,
    "Under review"
    )
ticket_repository.save(ticket1)

ticket2 = Ticket(
    bug6,
    product2,
    "9 April 2022",
    user6,
    "Closed"
    )
ticket_repository.save(ticket2)

ticket3 = Ticket(
    bug1,
    product3,
    "16 April 2022",
    user2,
    "Under review"
    )
ticket_repository.save(ticket3)

ticket4 = Ticket(
    bug12,
    product1,
    "22 April 2022",
    user6,
    "Closed"
    )
ticket_repository.save(ticket4)

ticket5 = Ticket(
    bug2,
    product3,
    "30 April 2022",
    user1,
    "Under review"
    )
ticket_repository.save(ticket5)

ticket6 = Ticket(
    bug3,
    product3,
    "8 May 2022",
    user6,
    "Closed"
    )
ticket_repository.save(ticket6)

ticket7 = Ticket(
    bug13,
    product1,
    "8 May 2022",
    user4,
    "Under review"
    )
ticket_repository.save(ticket7)

ticket8 = Ticket(
    bug7,
    product2,
    "12 May 2022",
    user6,
    "Closed"
    )
ticket_repository.save(ticket8)

ticket9 = Ticket(
    bug4,
    product3,
    "19 May 2022",
    user4,
    "Under review"
    )
ticket_repository.save(ticket9)

ticket10 = Ticket(
    bug8,
    product2,
    "10 June 2022",
    user3,
    "Under review"
    )
ticket_repository.save(ticket10)

ticket11 = Ticket(
    bug5,
    product3,
    "11 June 2022",
    user4,
    "Under review"
    )
ticket_repository.save(ticket11)

ticket12 = Ticket(
    bug14,
    product1,
    "23 June 2022",
    user7,
    "Closed"
    )
ticket_repository.save(ticket12)

ticket13 = Ticket(
    bug15,
    product1,
    "24 June 2022",
    user2,
    "New"
    )
ticket_repository.save(ticket13)

ticket14 = Ticket(
    bug9,
    product2,
    "4 July 2022",
    user3,
    "New"
    )
ticket_repository.save(ticket14)

ticket15 = Ticket(
    bug3,
    product3,
    "6 July 2022",
    user4,
    "Under review"
    )
ticket_repository.save(ticket15)

ticket16 = Ticket(
    bug12,
    product1,
    "12 July 2022",
    user5,
    "Reassigned"
    )
ticket_repository.save(ticket16)

ticket17 = Ticket(
    bug10,
    product2,
    "15 July 2022",
    user5,
    "Reassigned"
    )
ticket_repository.save(ticket17)

ticket18 = Ticket(
    bug9,
    product2,
    "18 July 2022",
    user2,
    "New"
    )
ticket_repository.save(ticket18)

ticket19 = Ticket(
    bug16,
    product4,
    "18 July 2022",
    user4,
    "Under review"
    )
ticket_repository.save(ticket19)

ticket20 = Ticket(
    bug16,
    product4,
    "18 July 2022",
    user2,
    "New"
    )
ticket_repository.save(ticket20)


pdb.set_trace()