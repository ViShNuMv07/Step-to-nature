from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

CATEGORY_CHOICES=(
    ('ID','indoor'),
    ('OD','outdoor'),
    ('OF','office'),
    ('BL','balcony'),
    ('LR','living_room'),
    ('MD','medicinal'),
    ('HD','hedge'),
    ('HP','hanging_plant'),
    ('FB','flowering_bulb'),
    ('FS','flower_seed'),
    ('HS','herb_seed'),
    ('VS','vegitable_seed'),
    ('MG','microgreens'),
    ('CP','Cane_Pots'),
    ('CR','ceramic_Pots'),
    ('CO','coco_Pots'),
    ('CC','concrete_Pots'),
    ('GP','glass_Pots'),
    ('GB','grow_bag'),
    ('HG','hanging_Pots'),
    ('MP','metal_Pots'),
    ('RP','resin_pot'),
    ('SG','smart_garden'),
    ('TC','terracotta'),
    ('WP','wooden_Pots'),
    ('FL','fertiliser'),
    ('GK','grow_kit'),
    ('PC','pesticide'),
    ('PS','pot_stand'),
    ('PM','potting_media'),
    ('TE','tools&equipments'),
    ('AP','artificial_plants'),
    ('BC','birds_corner'),
    ('FG','fairy_garden'),
    ('GA','garden_art'),
    ('GL','garden_lights'),
    ('MT','miniature'),
    ('MF','moss_frames'),
    ('TK','terrarium_kit'),
    ('WF','water_fountain'),
)


class Product(models.Model):
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=3)
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name


# administrator
# username:surya@123
# password:surya@123

