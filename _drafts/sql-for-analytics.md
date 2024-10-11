---
layout: post
title:  "SQL for analytics"
categories: Programming Tools
---

## outline

Analytics - data warehousing, data science, business intelligence.

### Basics

#### SQL is declarative

describe what you want rather than how to do it
benefit from decades of research and optimization
at some cost to expressivity

#### SQL statements

- DDL - create tables and other artifacts
  - create
  - alter
- DML - Data manipulation language
  - select
  - insert
  - update
  - delete
- TCL - transaction control
  - commit
  - rollback
- DCL - data control (permissions)
  - grant

The statements for manipulating data are also known by the fun acronym CRUD - create, read, update, and delete. Lots of web applications and APIs are just a thin layer over a database doing CRUD.

SQL statements take tables as input and produce tables as output. Often SQL queries are described in terms of set operations over rows.

#### Transaction processing vs. analytics

At this point, there's a split.

Databases were created in the context of processing transactions in banking and airline reservations. If you want to use databases to build these kinds of multiuser applications, you'll want to learn about transactions and indexes. These are less important in analytic use cases.

### Analytic queries

select/where - maps and filters
group by - split-apply-combine

CTEs subqueries
window functions

