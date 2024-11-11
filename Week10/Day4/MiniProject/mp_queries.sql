-- Active: 1730390108417@@127.0.0.1@3306
/*
tables:
    'olist_customers_dataset',
    'olist_geolocation_dataset',
    'olist_order_items_dataset',
    'olist_order_payments_dataset',
    'olist_order_reviews_dataset',
    'olist_orders_dataset',
    'olist_products_dataset',
    'olist_sellers_dataset',
    'product_category_name_translation'
*/

-- Customers
select * from olist_customers_dataset;
-- Geo Data
select * from olist_geolocation_dataset;
-- Order Items
select * from olist_order_items_dataset;
-- Payments
select * from olist_order_payments_dataset;
-- Reviews
select * from olist_order_reviews_dataset;
-- Orders
select * from olist_orders_dataset;
-- Products
select * from olist_products_dataset;
-- Sellers
select * from olist_sellers_dataset;
-- Product Category
select * from product_category_name_translation;


-- Query 1: Count and Percentage of Orders Purchased in Jan 2018 with 5 Review Score
create index olist_orders_dataset_date_order_purchase_timestamp_idx on olist_orders_dataset (order_purchase_timestamp);
CREATE INDEX olist_orders_dataset_order_id_idx on olist_orders_dataset (order_id);
CREATE INDEX olist_order_reviews_dataset_order_id_idx on olist_order_reviews_dataset (order_id);

PRAGMA index_list('olist_order_reviews_dataset');

-- Result Query
with cnt_all as (
    select count(*) as ord_cnt from olist_orders_dataset
)
select count(*) as "Period Order Count"
    , cnt_all.ord_cnt as "Total Order Count" 
    , round(count(*) * 100.0 / cnt_all.ord_cnt, 2) as "Order Percentage"
from olist_orders_dataset od
    , cnt_all
where strftime('%Y', od.order_purchase_timestamp) = '2018'
    and strftime('%m', od.order_purchase_timestamp) = '01'
    and EXISTS (
        select 1 
        from olist_order_reviews_dataset
        where od.order_id = order_id
            and review_score = 5
    )
;

-- Query 2: Customer Purchase Trend Year-on-Year

-- Result Query
with orders_by_year as (
    select 
        strftime('%Y', order_purchase_timestamp) as purchase_year
        , count(distinct customer_id) as num_customers
        , count(*) as num_orders
        , round(count(*) * 1.0 / count(distinct customer_id), 2) as orders_per_customer
    from olist_orders_dataset
    group by strftime('%Y', order_purchase_timestamp)
),
lag_year as (
    select 
        purchase_year
        , lag(num_customers) over (order by purchase_year) as num_customers_prev
        , lag(num_orders) over (order by purchase_year) as num_orders_prev
    from orders_by_year
)
select 
    purchase_year as "Year"
    , num_customers as "Total Customers"
    , num_orders as "Total Orders"
    , orders_per_customer as "Orders per Customer"
    , num_customers_prev as "Total Customers Prev Year"
    , num_orders_prev as "Total Orders Prev Year"
    , round(coalesce((num_customers - num_customers_prev) * 100.0 / num_customers_prev, 0), 2) as "Customer Growth %"
    , round(coalesce((num_orders - num_orders_prev) * 100.0 / num_orders_prev, 0), 2) as "Order Growth %"
from orders_by_year
join lag_year USING (purchase_year)
;

-- Query 3: Average Order Values of Customers

select * from olist_order_payments_dataset;
select * from olist_orders_dataset;
select * from olist_order_items_dataset;

create index olist_orders_dataset_customer_id_idx on olist_orders_dataset (customer_id);
create index olist_order_payments_dataset_order_id_idx on olist_order_payments_dataset (order_id);
create index olist_order_items_dataset_order_id_idx on olist_order_items_dataset (order_id);

select customer_id 
    , count(*)
from olist_orders_dataset
group by customer_id
having count(*) > 1
; -- No customer with more than 1 order


create temp table tt_ord_val as 
select 
    order_id 
    , sum(price) as order_value
    , sum(freight_value) as freight_value
from olist_order_items_dataset
GROUP BY order_id;

create index tt_ord_val_order_id_idx on tt_ord_val (order_id);

-- Result Query:
select avg(order_value) as "Avg Order Value"
from tt_ord_val

-- Query 4: Top 5 Cities with Highest Revenue from 2016 to 2018
select * from olist_geolocation_dataset;
select * from olist_customers_dataset;

create index olist_customers_dataset_customer_id_idx on olist_customers_dataset (customer_id);

-- Result Query: 
-- I assume that we should subtract freight value from order value
with city_orders as (
    select 
        cd.customer_state
        , cd.customer_city as city_name
        , count(DISTINCT od.customer_id) as num_customers
        , count(DISTINCT od.order_id) as num_orders
        , sum(ov.order_value) as order_value
        , sum(ov.freight_value) as freight_value
        , sum(ov.order_value - ov.freight_value) as revenue
    from olist_orders_dataset od 
    join olist_customers_dataset cd using (customer_id)
    join tt_ord_val ov using (order_id)
    group by customer_city, customer_state
)
select *
from city_orders
order by revenue DESC
limit 5
;

-- Query 5: State Wise Revenue Table Between 2016 to 2018
-- Result Query
with state_orders as (
    select 
        cd.customer_state as state_name
        , count(DISTINCT od.customer_id) as num_customers
        , count(DISTINCT od.order_id) as num_orders
        , sum(ov.order_value) as order_value
        , sum(ov.freight_value) as freight_value
        , sum(ov.order_value - ov.freight_value) as revenue
    from olist_orders_dataset od 
    join olist_customers_dataset cd using (customer_id)
    join tt_ord_val ov using (order_id)
    group by customer_state
)
select *
from state_orders
order by revenue DESC
;

--  Query 6: Top Successful Sellers in Terms of Goods Sold, Revenue, and Customer Count
select * from olist_sellers_dataset;
select * from olist_orders_dataset;

select seller_city
    , seller_state
    , count(*) 
from olist_sellers_dataset
group by seller_city, seller_state
;

-- Result Query
with seller_metrics as (
    select 
        oi.seller_id
        , count(DISTINCT oi.order_id) as num_orders
        , count(DISTINCT od.customer_id) as num_customers
        , sum(oi.price) as order_value
        , sum(oi.freight_value) as freight_value
        , sum(oi.price - oi.freight_value) as revenue
        , count(oi.order_item_id) as items_sold
    from olist_order_items_dataset oi
    join olist_orders_dataset od using (order_id)
    group by seller_id
)
select *
from seller_metrics
order by revenue DESC
limit 10
;

-- Query 7: Delivery Success Rate Across States

select DISTINCT order_status from olist_orders_dataset;

-- Result Query
with delivery_metrics as (
    select 
        c.customer_state
        , count(*) as total_orders
        , count(case when o.order_status = 'delivered' then 1 end) as delivered_orders
        , count(case when o.order_status = 'canceled' then 1 end) as canceled_orders
        , count(case when o.order_status not in ('delivered', 'canceled') then 1 end) as other_status
    from olist_orders_dataset o
    join olist_customers_dataset c using (customer_id)
    group by customer_state
)
select 
    customer_state
    , total_orders
    , delivered_orders
    , canceled_orders
    , other_status
    , round(100.0 * delivered_orders / total_orders, 2) as delivery_success_rate
    , round(100.0 * canceled_orders / total_orders, 2) as cancellation_rate
from delivery_metrics
order by delivery_success_rate DESC
;

-- Query 8: Preferred Form of Payment for Different Categories
with payment_by_category as (
    select 
        p.product_category_name
        , op.payment_type
        , count(*) as num_transactions
        , sum(oi.price) as total_value
    from olist_order_payments_dataset op
    join olist_orders_dataset o using (order_id) 
    join olist_order_items_dataset oi using (order_id)
    join olist_products_dataset p using (product_id)
    group by p.product_category_name, op.payment_type
),
ranked_payments as (
    select 
        product_category_name
        , payment_type
        , num_transactions
        , total_value
        , row_number() over (partition by product_category_name order by num_transactions desc) as payment_rank
    from payment_by_category
)
select 
    product_category_name
    , payment_type as preferred_payment
    , num_transactions
    , round(total_value, 2) as total_value
from ranked_payments
where payment_rank = 1
order by num_transactions desc
limit 20
;

-- Query 9: Distance Between Cities

select * from olist_geolocation_dataset;
select count(*) from olist_geolocation_dataset;

create index olist_geolocation_dataset_geolocation_state_geolocation_city_idx on olist_geolocation_dataset (geolocation_state, geolocation_city);

PRAGMA index_list('olist_geolocation_dataset');

-- try to filter out same cities because there are cities with the same name but written slightly different
create temp table tt_city_coord as
with city_coord as (
    select geolocation_state as "state"
        , geolocation_city as city
        , avg(geolocation_lat) as lat
        , avg(geolocation_lng) as lng
    from olist_geolocation_dataset
    GROUP BY geolocation_state, geolocation_city
),
city_coord_unique as (
    select *
    from (
        select *
            , row_number() over (PARTITION BY length(city), round(lat, 1), round(lng, 1)) as rn
        from city_coord) sq
    where sq.rn = 1
)
select * from city_coord_unique;


select * from tt_city_coord;

-- Result Query
with city_distance as (
    select city_from.city as "city_from"
        , city_to.city as "city_to"
        -- calculating distance with formula: ((x1 - x2)^2 + (y1 - y2)^2)^(1/2)
        , power(power(city_from.lat - city_to.lat, 2) + power(city_from.lng - city_to.lng, 2), 0.5) as distance
    from tt_city_coord as city_from
    cross join tt_city_coord as city_to
)
select *
from city_distance cd
where distance > 0
;



with city_coord as (
    select geolocation_state as "state"
        , geolocation_city as city
        , avg(geolocation_lat) as lat
        , avg(geolocation_lng) as lng
    from olist_geolocation_dataset
    GROUP BY geolocation_state, geolocation_city
)
select *
    , row_number() over (PARTITION BY length(city), round(lat, 1), round(lng, 1))
    , length(city), round(lat, 2), round(lng, 2)
from city_coord