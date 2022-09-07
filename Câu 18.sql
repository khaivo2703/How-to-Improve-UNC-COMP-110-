with a as (
select year(b.transaction_date) as year,
	case
		when c.product like N'%trà khô%' then 1
		when c.product like N'%trà túi lọc%' then 2
		when c.product like N'%trà hòa tan%' then 3
		when c.product like N'%trà chai%' then 4
	end as product_type,
	case
		when c.product like N'%trà khô%' then N'Trà Khô'
		when c.product like N'%trà túi lọc%' then N'Trà túi lọc'
		when c.product like N'%trà hòa tan%' then N'Trà hòa tan'
		when c.product like N'%trà chai%' then N'Trà chai'
	end as product_type_name,
	sum(b.line_amount) as sales_amount
from pos_sales_line as b
	join product_sku as c on b.product_sku_id = c.id
where c.product_subcategory_id = 27
group by year(b.transaction_date), c.product),
	d as (
select year(b.transaction_date) as year, sum(b.line_amount) as sales_amount_ht
from pos_sales_line as b
	join product_sku as c on b.product_sku_id = c.id
where c.product_subcategory_id = 27
group by year(b.transaction_date)),
	e as (
select year, product_type, product_type_name, sum(sales_amount) as sales_amount
from a
group by year, product_type, product_type_name)

select e.year, e.product_type, e.product_type_name, d.sales_amount_ht, e.sales_amount, e.sales_amount/d.sales_amount_ht as ratio
from e
	join d on e.year = d.year
where e.product_type_name like N'%trà hòa tan%'
order by year
