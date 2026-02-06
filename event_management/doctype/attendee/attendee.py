import frappe

def before_insert(doc):
    event = frappe.get_doc("Events", doc.event)

    attendee_count = frappe.db.count(
        "Attendee",
        {"event": doc.event}
    )

    if attendee_count >= event.capacity:
        frappe.throw("Event capacity exceeded.")
