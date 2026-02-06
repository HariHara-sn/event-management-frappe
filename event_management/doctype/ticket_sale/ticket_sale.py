import frappe
from frappe.model.document import Document

class TicketSale(Document):

    def validate(self):
        if not self.event or not self.quantity:
            return

        event = frappe.get_doc("Events", self.event)

        # Capacity check
        sold = event.tickets_sold or 0
        capacity = event.capacity or 0

        if sold + self.quantity > capacity:
            frappe.throw(
                f"Event capacity exceeded. Available seats: {capacity - sold}"
            )

        # Revenue calculation
        ticket_price = event.ticket_price or 0
        self.total_price = ticket_price * self.quantity


    def on_submit(self):
        event = frappe.get_doc("Events", self.event)

        # Update sold tickets
        event.tickets_sold = (event.tickets_sold or 0) + self.quantity

        # Remaining capacity
        event.remaining_capacity = event.capacity - event.tickets_sold
        event.save()
