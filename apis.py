async def diagnose_symptoms(input_data, user_id=None, context=None, section=None, voice=False):
    """Simulate medical diagnosis API with simple text output."""
    if voice:
        return f"Diagnosis based on voice: {input_data}"
    elif section:
        return f"Section-specific diagnosis [{section}] for user input: {input_data}"
    else:
        return f"Diagnosis for user {user_id}: No issues detected based on {input_data}"

async def track_symptom(user_id, symptom, value, context):
    """Simulate a tracking API response."""
    return f"Symptom '{symptom}' with value '{value}' has been successfully tracked for user {user_id}."

async def get_symptom_trend(user_id, context):
    """Simulate fetching symptom trends."""
    return f"Here are the tracked trends for user {user_id}:\n- Fever: 3 days\n- Headache: 5 instances"

async def process_consultation(user_id, user_message, context):
    """Simulate a consultation process."""
    # Simulate response
    return f"Consultation ongoing for user {user_id}. Response: {user_message}"

async def start_consultation(user_id, context):
    """Start a consultation session and return the introduction."""
    return f"Consultation started for user {user_id}. What concerns do you have?"
