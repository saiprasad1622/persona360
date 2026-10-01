-- ==========================================
-- Persona360 SQL Analytics
-- ==========================================

-- 1. Customer revenue
SELECT
    customer_id,
    customer_name,
    plan,
    total_revenue,
    total_orders,
    avg_order_value
FROM customer_360
ORDER BY total_revenue DESC;


-- 2. Revenue by persona
SELECT
    persona,
    COUNT(*) AS customer_count,
    SUM(total_revenue) AS total_revenue
FROM customer_360
GROUP BY persona
ORDER BY total_revenue DESC;


-- 3. Customers with high churn risk
SELECT
    customer_id,
    customer_name,
    total_revenue,
    support_tickets,
    open_tickets,
    engagement_score,
    churn_risk
FROM customer_360
WHERE churn_risk = 'High'
ORDER BY total_revenue DESC;


-- 4. Marketing click rate
SELECT
    customer_id,
    campaign_contacts,
    campaign_clicks,
    campaign_opens,

    ROUND(
        100.0 * campaign_clicks
        / NULLIF(campaign_contacts, 0),
        2
    ) AS click_rate_pct

FROM customer_360;


-- 5. Revenue by customer type
SELECT
    customer_type,
    COUNT(*) AS customers,
    SUM(total_revenue) AS revenue
FROM customer_360
GROUP BY customer_type;


-- 6. Average support resolution time
SELECT
    customer_id,
    customer_name,
    support_tickets,
    avg_resolution_hours
FROM customer_360
ORDER BY avg_resolution_hours DESC;


-- 7. Customer 360 profile
SELECT *
FROM customer_360
WHERE customer_id = 'C001';