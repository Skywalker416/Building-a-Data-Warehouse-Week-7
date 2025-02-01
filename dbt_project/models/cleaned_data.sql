SELECT
    message_id,
    sender_id,
    DATE_TRUNC('day', date) AS message_date,
    text AS message_text
FROM medical_data
WHERE text IS NOT NULL;
