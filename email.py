import streamlit as st
from datetime import date, timedelta

# Title of the app
st.title("Leave Request Email Generator")

# Input: Recipient Email
recipient_email = st.text_input("Recipient Email:")

# Input: Your Name
your_name = st.text_input("Your Name:")

# Input: Number of Leave Days
leave_days = st.number_input("Number of Leave Days:", min_value=1, max_value=365, step=1)

# Input: Start Date of Leave
start_date = st.date_input("Start Date of Leave:", value=date.today())

# Input: Reason for Leave
reason = st.text_area("Reason for Leave:")

# Generate Leave Request Email
if st.button("Generate Leave Request Email"):
    end_date = start_date + timedelta(days=leave_days-1)
    email_subject = f"Leave Request for {leave_days} Days"
    email_body = f"""
    Dear {recipient_email},

    I hope this email finds you well. I am writing to formally request leave for {leave_days} days starting from {start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}. The reason for my leave is as follows:

    {reason}

    I assure you that I will complete all my pending tasks before my leave starts and ensure a smooth handover of my responsibilities. I will also be available on phone and email for any urgent matters.

    I kindly request you to approve my leave request.

    Thank you for your understanding and consideration.

    Best regards,
    {your_name}
    """

    st.write("### Generated Leave Request Email:")
    st.write(f"**To:** {recipient_email}")
    st.write(f"**Subject:** {email_subject}")
    st.write("**Body:**")
    st.write(email_body)
