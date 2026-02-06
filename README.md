# Event Management Web Application

*(Built using Frappe Framework)*

---

## Project Overview

This project is a **Frappe-based Event Management Web Application** developed as part of a Developer Hiring Test.

The application enables event planners to:

* Create and manage events
* Register and manage attendees
* Track ticket sales and event capacity
* Import event data using CSV files
* View basic ticket and revenue reports

For simplicity, the system is designed for **single-role usage (Event Planner)** and does not implement complex user roles or permissions.

---

## Technology Stack

* **Framework:** Frappe Framework
* **Backend:** Python (Frappe ORM & Controllers)
* **Database:** MariaDB (via Frappe)
* **Frontend:** Frappe Desk UI / Web Forms
* **Version Control:** Git & GitHub

---

## DocTypes Implemented

### 1️⃣ Event

Stores all core event information.

**Fields:**

* Event Title
* Description
* Event Date
* Location
* Capacity
* Ticket Price
* Tickets Sold
* Remaining Capacity

---

### 2️⃣ Attendee

Stores attendee details and links them to specific events.

**Fields:**

* Attendee Name
* Email
* Phone Number
* Event (Link to Event)

---

### 3️⃣ Ticket Sale

Handles ticket transactions and revenue calculation.

**Fields:**

* Event (Link to Event)
* Attendee
* Ticket Quantity
* Total Price

---

## Event Management

* Create events with:

* Title, Description, Date, Location, Capacity
* Update and delete events
* Search and filter events by:

  * Event Title
  * Event Date

---

### Attendee Management

* Register attendees for specific events
* Update attendee details
* View attendees mapped to each event
* Prevent registrations when event capacity is exceeded

---

### Ticket Sales Management

* Track:

  * Tickets sold
  * Tickets available
* Automatically calculate:

  * Total ticket price
  * Remaining event capacity
* Prevent ticket sales when capacity is exceeded

---

### 🔹 CSV Import (Data Import)

* Import Event records using CSV files
* Supported CSV fields:

  * Event Title
  * Description
  * Event Date
  * Location
  * Capacity
* Implemented using **Frappe Data Import Tool**

---

### 🔹 Reports

* Event-wise:

  * Total tickets sold
  * Revenue per event
* Implemented using **Frappe Report Builder**

---

## 🧪 How to Run & Test the Application

### ▶️ Start the Server

```bash
bench start
```

Open in browser:

```
http://127.0.0.1:8000/app/
```

---

### ▶️ Test Event & Ticket Flow

1. Create an Event with:

   * Capacity
   * Ticket Price
2. Create a Ticket Sale for the event
3. Verify:

   * Tickets Sold increases
   * Remaining Capacity decreases
   * Total Price is auto-calculated
4. Try selling tickets beyond capacity → system blocks the action

---

### Test CSV Import

1. Go to **Data Import**
2. Select **Event**
3. Download the CSV template
4. Upload a filled CSV file
5. Verify imported events in the Event list

---


## Screenshots (For Submission)

Event FormCreation
![event](https://github.com/HariHara-sn/event-management-frappe/blob/main/Images/event_1.png?raw=true)

![event_form](https://github.com/HariHara-sn/event-management-frappe/blob/main/Images/event_data.png?raw=true)
* Attendee List
![attendee](https://github.com/HariHara-sn/event-management-frappe/blob/main/Images/event_2.png?raw=true)
* Ticket Sale Entry
![ticket](https://github.com/HariHara-sn/event-management-frappe/blob/main/Images/ticke_2.png?raw=true)
* Ticket Tracking
![ticket_tracking](https://github.com/HariHara-sn/event-management-frappe/blob/main/Images/ticket_tracking.png?raw=true)
* Reports View data is from csv file
![report](https://github.com/HariHara-sn/event-management-frappe/blob/main/Images/image%20copy%202.png?raw=true)

---

## 👤 Author

**HARI HARA SUDHAN S - B.TECH IT**

Event Management Web Application using Frappe Framework