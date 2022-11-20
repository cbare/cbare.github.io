---
layout: post
title:  "Snowflake Cheat Sheet"
date:   2022-10-25 11:47:00 +1200
categories: programming data sql
---

Snowflake is awesome. Here's a catalog of resources.


database: contains schemas
schema: namespace within a DB
table: data in rows and columns
view: a virtual table based on a query

stored procedure:
function: 

storage integration: links to a service account with permissions on external storage.
stage: location from which to read files, for example a bucket.
task: schedule execution of SQL statement or stored proc
pipe: copy data from a stage into a table
stream: change data capture


https://learn.snowflake.com/


https://docs.snowflake.com/en/sql-reference/functions/task_history.html


Open question:

Is the old-school fact-dimension style of data warehouse obsolete in column-oriented DBs?
