# Django_Practical
Write API for Create, Update, Delete category/product with following feature.

1. Category  can be subcategory of other category & possibly N number of depth.check below example
    Category 1
		sub category  1
			sub category
				sub category
				.
				.
				N
			.
			.
			N
		Sub category  2
		Sub category  3
		.
		.
		N
	.
	.
	N
2. Implement simple CRUD API to create product(name, price) & assign multiple categories to it
Hint: You can use django rest framework for writing api



## Solution
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Click on the link for API page

Category API
Category List **{host}/api/category/**
Category Create **{host}/api/category/**
Category Update **{host}/api/category/update/{id}/**
Category Delete **{host}/api/category/delete/{id}/**


Product API
Product List **{host}/api/product/**
Product Create **{host}/api/product/**
Product Update **{host}/api/product/update/{id}/**
Product Delete **{host}/api/product/delete/{id}/**

