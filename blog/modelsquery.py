# #***(1)Returns all customers from customer table
# customers = Customer.objects.all()
# print(customer.query) show the sql query which is used for retrive data
# #(2)Returns first customer in table
# firstCustomer = Customer.objects.first()

# #(3)Returns last customer in table
# lastCustomer = Customer.objects.last()

# #(4)Returns single customer by name
# customerByName = Customer.objects.get(name='Peter Piper')

# #***(5)Returns single customer by name
# customerById = Customer.objects.get(id=4)

# #***(6)Returns all orders related to customer (firstCustomer variable set above)
# firstCustomer.order_set.all()

# #(7)***Returns orders customer name: (Query parent model values)
# order = Order.objects.first() 
# parentName = order.customer.name

# #(8)***Returns products from products table with value of "Out Door" in category attribute
# products = Product.objects.filter(category="Out Door")

# #(9)***Order/Sort Objects by id
# leastToGreatest = Product.objects.all().order_by('id') 
# greatestToLeast = Product.objects.all().order_by('-id') 


# #(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
# productsFiltered = Product.objects.filter(tags__name="Sports")

# '''
# (11)Bonus
# Q: If the customer has more than 1 ball, how would you reflect it in the database?
# A: Because there are many different products and this value changes constantly you would most 
# likly not want to store the value in the database but rather just make this a function we can run
# each time we load the customers profile
# '''

# #Returns the total count for number of time a "Ball" was ordered by the first customer
# ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

# #Returns total count for each product orderd
# allOrders = {}

# for order in firstCustomer.order_set.all():
# 	if order.product.name in allOrders:
# 		allOrders[order.product.name] += 1
# 	else:
# 		allOrders[order.product.name] = 1

# #Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


# #RELATED SET EXAMPLE
# class ParentModel(models.Model):
# 	name = models.CharField(max_length=200, null=True)

# class ChildModel(models.Model):
# 	parent = models.ForeignKey(Customer)
# 	name = models.CharField(max_length=200, null=True)

# parent = ParentModel.objects.first()
# #Returns all child models related to parent
# parent.childmodel_set.all()

# Post.objects.filter(title__startswith = 'Blog') | Post.objects.none()

# we can easily perform or opretation using Q object 
# from django.db.models import Q
# Post.objects.filter(Q(title__startswith = 'Blog') | Q(title__icontains = 'python')| ~Q(title__icontains = 'ODOO')) ~ USE FOR ADD NEGOTIATION
# Post.objects.filter(title__startswith = 'Blog') & Post.objects.filter(title__icontains = '1')
# Post.objects.filter(Q(title__startswith = 'Blog') & Q(title__icontains = 'python'))

# union allow us to combine result of two queryset
# Post.objects.all().values_list('title','content').union(Profile.objects.all().values_list('user','image'))
# q = Post.objects.all().values_list('title','content') value_list return only field that is defined in that 
# q2 = Profile.objects.all().values_list('user','image')
# q.union(q2) returns union of the q and q2 query set 
 
# to perform not opretation we have to use the exclude 

# Post.objects.all().exclude(title__icontains = 'blog')
# gt
# gte
# lt
# lte
# Post.objects.filter(Q(title__icontains = 'blog'))

# we can also retrive only single field with using orm
#  Post.objects.filter(Q(title__icontains = 'blog'))

# allows to retrive only single field
# Post.objects.filter(id=1).only('content')
# Post.objects.filter(id=1).only('content','date_posted')

# we can also execute raw query in django 
# execute sql using raw method
# execute the sql querys
# profile.objects.raw(query)

# there are 3 type of models
# abstrect model
# multitable model
# proxy model

# abstrect model (abstrect base class)
# when ne need the same data for number of models
# abc = the model will not be created 
# fields are added to the child class 
# 

# from django.db import models

# class CommonInfo(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()

#     class Meta:
#         abstract = True

# class Student(CommonInfo):
#     home_group = models.CharField(max_length=5)

# meta inheritance

# When an abstract base class is created, Django makes any Meta inner class you declared in the base class available as an attribute. If a 
# child class does not declare its own Meta class, it will inherit the parent’s Meta. If the child wants to extend the parent’s Meta class, 
# it can subclass it. For example:

# multitable inheritance
#  every model is model by it self
# one to one link is automatically created

# from django.db import models
# class Book(models.Model):
#     title = models.CharField(_(""), max_length=50)
#     author = models.models.CharField(_(""), max_length=50)

# class Authordetails(Book):
#     isbn = models.IntegerField()

# Proxy model 
# Change the bheviour of model
# proxy model oprate on orignal model 

# from django.db import models
# class Book(models.Model):
#     title = models.CharField(_(""), max_length=50)
#     author = models.models.CharField(_(""), max_length=50)

# class Authordetails(Book):
#     class Meta:
#       proxy=True
#