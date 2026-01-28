Against Facts and Dimensions

Kimball style data modeling

performance of analytic queries on row-oriented transactional databases. If you're using Snowflake, BigQuery, Pandas, or DuckDB, you're using a column-oriented database engine that's built to run analytic queries efficiently. So, the performance reason no longer exists.

Facts and dimensions only exist relative to the queries that you want to make. You're implying that you want to compute aggregate functions over the rows of a fact table while grouping by dimensions. You're biasing yourself toward asking some questions and not asking others.


Consultants love to create a template they can re-use from one client to the next. It's worth noting that the pioneer of dimensional analysis is the Kimball Group, a small consultancy. The advantage, for the consultant, is you can sell the same thing an unlimited number of times. Dimensional analysis applies to any domain, so it's a portable template for building a data warehouse.

evolving requirements


You want to analyze sales by product line, geographical region, sales staff, etc. The further your interests stray from retail sales, the more you have to wonder how well this style of analysis applies.

The alternative is modeling based on domain concepts and the relationships between them in the terms used by practicioners and experts in that domain.

Do you want to learn the consultant's language, or do you want to work in the terminology native to your domain?


slowly changing dimensions

Bias as a Feature: In some contexts, bias is not inherently bad—it reflects business priorities. By choosing dimensions, you're implicitly codifying what's important to measure, which can clarify organizational goals.

Tool Compatibility - many tools are designed around star-schema data warehouses.


Bridge Between Domains

Dimensions are a natural fit for time and geography and offer an efficient means of dealing with multiple levels of granularity. 
Handling different levels of granularity - city, state, region, country etc. day, week, month, year.
