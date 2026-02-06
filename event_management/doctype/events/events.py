import frappe
from frappe.model.document import Document

class Event(Document):

    def validate(self):
        if self.capacity is not None and self.capacity < 0:
            frappe.throw("Capacity cannot be negative")

        if self.ticket_price is not None and self.ticket_price < 0:
            frappe.throw("Ticket price cannot be negative")
