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
pip install -r requirements.txt<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py runserver<br>
<br><br>

Click on the link for API page<br>
<br>
Category API<br>
Category List **{host}/api/category/**<br>
Category Create **{host}/api/category/**<br>
Category Update **{host}/api/category/update/{id}/**<br>
Category Delete **{host}/api/category/delete/{id}/**<br>
<br><br><br>

Product API<br>
Product List **{host}/api/product/**<br>
Product Create **{host}/api/product/**<br>
Product Update **{host}/api/product/update/{id}/**<br>
Product Delete **{host}/api/product/delete/{id}/**<br>

