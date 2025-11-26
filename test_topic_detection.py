from nyspccu.topic_detection import is_on_topic, contains_pii

def test_basic_on_topic_keyword():
    q = "How do I enable MFA on my account?"
    on_topic, details = is_on_topic(q)
    assert on_topic is True
    assert details["intent"] or details["keyword"]

def test_basic_off_topic():
    q = "What is the weather today?"
    on_topic, details = is_on_topic(q)
    assert on_topic is False
    assert details["negative"] is True

def test_pii_detection_email():
    text = "Contact me at alice@example.com"
    pii = contains_pii(text)
    assert "email" in pii
